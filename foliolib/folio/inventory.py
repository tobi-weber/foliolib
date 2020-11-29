# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os

from foliolib.folio import FolioService
from foliolib.folio.api.inventory import Inventory
from foliolib.folio.api.inventoryStorage import (AlternativeTitleType,
                                                 CallNumberType,
                                                 ClassificationType,
                                                 ContributorNameType,
                                                 ContributorType,
                                                 ElectronicAccessRelationship,
                                                 HoldingsNoteType,
                                                 HoldingsSources, HoldingsType,
                                                 IdentifierType, IllPolicy,
                                                 InstanceFormat,
                                                 InstanceNoteType,
                                                 InstanceRelationshipType,
                                                 InstanceStatus, InstanceType,
                                                 ItemDamagedStatuses,
                                                 ItemNoteType, LoanType,
                                                 Location, Locationunit,
                                                 MaterialType, ModeOfIssuance,
                                                 NatureOfContentTerm,
                                                 ServicePoint, StatisticalCode,
                                                 StatisticalCodeType)
from foliolib.folio.exceptions import UnknownFile
from foliolib.okapi.exceptions import OkapiRequestError

log = logging.getLogger("foliolib.folio.inventory")


class InventoryService(FolioService):
    def __init__(self, tenant: str) -> None:
        """
        Args:
            tenant (str): Tenant id
        """
        super().__init__(tenant)
        self._inventory = Inventory(tenant)

    def upload_modsFiles(self, filePathes: list):
        statusIds = []
        for path in filePathes:
            self._inventory.upload_mods(path)
            statusIds.append(self._inventory.headers()[
                             "Location"].split("/")[-1])
        return statusIds

    def get_uploadStatus(self, statusId):
        return self._inventory.get_status(statusId)

    def load_referenceData(self, path):

        methods = [
            ("material-types", MaterialType, "set_materialType"),
            ("loan-types", LoanType, "set_loanType"),
            ("location-units/institutions", Locationunit, "set_institution"),
            ("location-units/campuses", Locationunit, "set_campuse"),
            ("location-units/libraries", Locationunit, "set_library"),
            ("locations", Location, "set_location"),
            ("identifier-types", IdentifierType, "set_identifierType"),
            ("contributor-types", ContributorType,  "set_contributorType"),
            ("service-points", ServicePoint, "set_servicePoint"),
            ("instance-relationship-types", InstanceRelationshipType,
             "set_instanceRelationshipType"),
            ("contributor-name-types", ContributorNameType,
             "set_contributorNameType"),
            ("instance-types", InstanceType, "set_instanceType"),
            ("instance-formats", InstanceFormat, "set_instanceFormat"),
            ("classification-types", ClassificationType,  "set_classificationType"),
            ("instance-statuses", InstanceStatus, "set_instanceStatus"),
            ("statistical-code-types", StatisticalCodeType, "set_statisticalCodeType"),
            ("statistical-codes", StatisticalCode, "set_statisticalCode"),
            ("modes-of-issuance", ModeOfIssuance, "set_modesOfIssuance"),
            ("alternative-title-types", AlternativeTitleType,
             "set_alternativeTitleType"),
            ("electronic-access-relationships", ElectronicAccessRelationship,
             "set_electronicAccessRelationship"),
            ("ill-policies", IllPolicy, "set_illPolicy"),
            ("holdings-types", HoldingsType, "set_holdingsType"),
            ("call-number-types", CallNumberType, "set_callNumberType"),
            ("holdings-note-types", HoldingsNoteType,  "set_holdingsNoteType"),
            ("item-note-types", ItemNoteType, "set_itemNoteType"),

            ("holdings-sources", HoldingsSources, "set_holdingsSource"),
            ("instance-note-types", InstanceNoteType, "set_instanceNoteType"),
            ("item-damaged-statuses", ItemDamagedStatuses, "set_itemDamagedStatus"),
            ("nature-of-content-terms",  NatureOfContentTerm,
             "set_natureOfContentTerm"),
        ]

        for dname, klass, methodName in methods:
            obj = klass(self._tenant)
            method = getattr(obj, methodName)
            for fname in os.listdir(os.path.join(path, dname)):
                if os.path.splitext(fname)[1] == ".json":
                    fpath = os.path.join(path, dname, fname)
                    log.info("Load %s/%s -> %s.%s", dname,
                             fname, klass.__name__, methodName)
                    with open(fpath) as f:
                        try:
                            method(json.load(f))
                        except OkapiRequestError as e:
                            log.error(str(e))
