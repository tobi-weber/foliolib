# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os
import time

from foliolib.folio import FolioService
from foliolib.folio.api.configuration import Config
from foliolib.folio.api.dataImport import DataImport
from foliolib.folio.api.dataImportConverterStorage import \
    DataImportConverterStorage
from foliolib.folio.api.inventoryStorage import InstanceStatus
from foliolib.folio.exceptions import UnknownFile
from foliolib.okapi.exceptions import OkapiRequestUnprocessableEntity

log = logging.getLogger("foliolib.folio.dataImport")


class DataImportService(FolioService):
    """
    Requirements:

        - mod-data-import
    """

    def __init__(self, tenant: str) -> None:
        """
        Args:
            tenant (str): Tenant id
        """
        super().__init__(tenant)
        self._dataImport = DataImport(tenant)
        self._dataImportConverterStorage = DataImportConverterStorage(tenant)
        self._instanceStatus = InstanceStatus(tenant)
        self._config = Config(tenant)

    def importMarcFiles(self, filePathes: list, action="CREATE", marcType="MARC_BIBLIOGRAPHIC",
                        folioRecordType="INSTANCE", jobProfileId=None):
        """[summary]

        Args:
            filePathes (list): [description]

        Raises:
            UnknownFile: [description]

        Returns:
            [type]: [description]
        """

        if jobProfileId is None:
            jobProfile = self._create_jobProfile(action=action,
                                                 marcType=marcType,
                                                 folioRecordType=folioRecordType)
            jobProfileId = jobProfile["id"]
        else:
            jobProfile = self._dataImportConverterStorage.get_jobProfile(
                jobProfileId)

        fileDefinitions = []
        files = {}
        for filePath in filePathes:
            basename = os.path.basename(filePath)
            log.info("Create FileDefintion for %s", basename)
            files[basename] = filePath
            fileDefinitions.append({"name": basename})

        # Create UploadDefinition
        log.info("Create UploadDefintion")
        uploadDefinition = self._dataImport.set_uploadDefinition(
            {"fileDefinitions": fileDefinitions})

        
        # Upload files
        time.sleep(60)
        uploadDefinitionId = uploadDefinition["id"]
        log.info("Upload Files")
        for fileDefinition in uploadDefinition["fileDefinitions"]:
            fileId = fileDefinition["id"]
            name = fileDefinition["name"]
            log.info("Upload file %s", name)
            uploadDefinition = self._dataImport.upload_file(uploadDefinitionId, fileId,
                                                            files[name])

        # Processing files
        log.info("Processing files")
        processFile = {"uploadDefinition": uploadDefinition,
                       "jobProfileInfo": {"id": jobProfileId,
                                          "name": "foliolibImport",
                                          "dataType": "MARC"}}
        self._dataImport.set_processFile(
            uploadDefinitionId, processFile, defaultMapping=True)

        return uploadDefinition

    def delete_file(self, fileName: str):
        """[summary]

        Args:
            fileName (str): [description]
        """
        def get_fileIds(fileName: str):
            fileIds = []

            def searchFile(offset):
                uploadDefintions = self._dataImport.get_uploadDefinitions(
                    offset=offset, limit=10)
                totalRecords = uploadDefintions["totalRecords"]
                for uploadDefintion in uploadDefintions["uploadDefinitions"]:
                    for fileDefinition in uploadDefintion["fileDefinitions"]:
                        if fileDefinition["name"] == fileName:
                            fileIds.append({"uploadDefinitionId": uploadDefintion["id"],
                                            "fileId": fileDefinition["id"]})
                offset += 10
                if offset < totalRecords:
                    searchFile(offset)
                else:
                    return
            searchFile(0)
            return fileIds

        for f in get_fileIds(fileName):
            self._dataImport.delete_file(f["uploadDefinitionId"],
                                         f["fileId"])
            uploadDefinition = self._dataImport.get_uploadDefinition(
                f["uploadDefinitionId"])
            if len(uploadDefinition["fileDefinitions"]) == 0:
                self._dataImport.delete_uploadDefinition(
                    f["uploadDefinitionId"])

    def clean_profiles(self):
        # Delete jobProfile
        jobProfiles = self._dataImportConverterStorage.get_jobProfiles(
            query=f"name==foliolib*")
        if len(jobProfiles["jobProfiles"]) > 0:
            jobProfileId = jobProfiles["jobProfiles"][0]["id"]
            mappingAssociations = self._dataImportConverterStorage.get_profileAssociations(
                master="JOB_PROFILE", detail="ACTION_PROFILE",
                query="masterProfileId==" + jobProfileId)
            if len(mappingAssociations["profileAssociations"]) > 0:
                jobMappingAssociationId = mappingAssociations["profileAssociations"][0]["id"]
                self._dataImportConverterStorage.delete_profileAssociation(
                    jobMappingAssociationId,
                    master="JOB_PROFILE", detail="ACTION_PROFILE")
            self._dataImportConverterStorage.delete_jobProfile(jobProfileId)

        # Delete actionProfile
        actionProfiles = self._dataImportConverterStorage.get_actionProfiles(
            query=f"name==foliolib*")
        if len(actionProfiles["actionProfiles"]) > 0:
            actionProfileId = actionProfiles["actionProfiles"][0]["id"]
            mappingAssociations = self._dataImportConverterStorage.get_profileAssociations(
                master="ACTION_PROFILE", detail="MAPPING_PROFILE",
                query="masterProfileId==" + actionProfileId)
            if len(mappingAssociations["profileAssociations"]) > 0:
                actionMappingAssociationId = mappingAssociations["profileAssociations"][0]["id"]
                self._dataImportConverterStorage.delete_profileAssociation(
                    actionMappingAssociationId,
                    master="ACTION_PROFILE", detail="MAPPING_PROFILE")
            self._dataImportConverterStorage.delete_actionProfile(
                actionProfileId)

        # Delete mappingProfile
        mappingProfiles = self._dataImportConverterStorage.get_mappingProfiles(
            query=f"name==foliolib*")
        if len(mappingProfiles["mappingProfiles"]) > 0:
            mappingProfileId = mappingProfiles["mappingProfiles"][0]["id"]
            self._dataImportConverterStorage.delete_mappingProfile(
                mappingProfileId)

    def _create_jobProfile(self, marcType="MARC_BIBLIOGRAPHIC",
                           action="CREATE", folioRecordType="INSTANCE"):
        name = f"foliolib_{action}_{marcType}_{folioRecordType}_"
        jobProfiles = self._dataImportConverterStorage.get_jobProfiles(
            query=f"name==foliolib*Job")
        if len(jobProfiles["jobProfiles"]) > 0:
            log.error("Job profile already exists: %s", name)
            return jobProfiles["jobProfiles"][0]

        if action not in ["CREATE", "REPLACE", "MODIFY", "COMBINE"]:
            raise Exception(
                "action must be one of CREATE|REPLACE|MODIFY|COMBINE")

        actionProfile = self._dataImportConverterStorage.set_actionProfile({
            "profile": {"name": name+"Action",
                        "action": action,
                        "folioRecord": folioRecordType}})

        jobProfile = self._dataImportConverterStorage.set_jobProfile(
            {"profile": {"name": name+"Job",
                         "description": "foliolib jobProfile to import files",
                         "dataType": "MARC"},
                "addedRelations": [{"detailProfileId": actionProfile["id"],
                                    "detailProfileType": "ACTION_PROFILE",
                                    "masterProfileId": None,
                                    "masterProfileType": "JOB_PROFILE",
                                    "order": 0}]
             })

        return jobProfile
