# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.dataExport")


class DataExportJobProfile(FolioApi):
    """Data export Job Profile API

    APIs for creating job Profiles to manage export jobs
    """

    def get_jobProfiles(self, **kwargs):
        """Retrieve a list of jobProfile items.

        ``GET /data-export/job-profiles``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - status=SUCCESS

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataExportJobProfile_get_jobProfiles_return.schema 
        """
        return self.call("GET", "/data-export/job-profiles", query=kwargs)

    def set_jobProfile(self, jobProfile: dict):
        """Create a new jobProfile item.

        ``POST /data-export/job-profiles``

        Args:
            jobProfile (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created jobProfile item

        Schema:

            .. literalinclude:: ../files/DataExportJobProfile_set_jobProfile_request.schema
        """
        return self.call("POST", "/data-export/job-profiles", data=jobProfile)

    def get_jobProfile(self, jobProfilesId: str):
        """Retrieve jobProfile item with given {jobProfileId}

        ``GET /data-export/job-profiles/{jobProfilesId}``

        Args:
            jobProfilesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataExportJobProfile_get_jobProfile_return.schema 
        """
        return self.call("GET", f"/data-export/job-profiles/{jobProfilesId}")

    def delete_jobProfile(self, jobProfilesId: str):
        """Delete jobProfile item with given {jobProfileId}

        ``DELETE /data-export/job-profiles/{jobProfilesId}``

        Args:
            jobProfilesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/data-export/job-profiles/{jobProfilesId}")

    def modify_jobProfile(self, jobProfilesId: str, jobProfile: dict):
        """Update jobProfile item with given {jobProfileId}

        ``PUT /data-export/job-profiles/{jobProfilesId}``

        Args:
            jobProfilesId (str)
            jobProfile (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataExportJobProfile_modify_jobProfile_request.schema
        """
        return self.call("PUT", f"/data-export/job-profiles/{jobProfilesId}", data=jobProfile)


class DataExport(FolioApi):
    """Data export API

    API for exporting MARC records
    """

    def set_export(self, export: dict):
        """Starts the export process

        ``POST /data-export/export``

        Args:
            export (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataExport_set_export_request.schema
        """
        return self.call("POST", "/data-export/export", data=export)

    def set_quickExport(self, quickExport: dict):
        """Starts the export process

        ``POST /data-export/quick-export``

        Args:
            quickExport (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataExport_set_quickExport_request.schema
            .. literalinclude:: ../files/DataExport_set_quickExport_return.schema 
        """
        return self.call("POST", "/data-export/quick-export", data=quickExport)

    def get_jobExecutions(self, **kwargs):
        """Retrieve jobExecution item with given {jobExecutionId}

        ``GET /data-export/job-executions``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - status=SUCCESS
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataExport_get_jobExecutions_return.schema 
        """
        return self.call("GET", "/data-export/job-executions", query=kwargs)

    def delete_jobExecution(self, jobExecutionsId: str):
        """

        ``DELETE /data-export/job-executions/{jobExecutionsId}``

        Args:
            jobExecutionsId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/data-export/job-executions/{jobExecutionsId}")

    def get_download(self, jobExecutionId: str, exportFileId: str):
        """

        ``GET /data-export/job-executions/{jobExecutionId}/download/{exportFileId}``

        Args:
            jobExecutionId (str)
            exportFileId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataExport_get_download_return.schema 
        """
        return self.call("GET", f"/data-export/job-executions/{jobExecutionId}/download/{exportFileId}")

    def set_expireJob(self):
        """

        ``POST /data-export/expire-jobs``

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("POST", "/data-export/expire-jobs")

    def set_cleanUpFile(self):
        """

        ``POST /data-export/clean-up-files``

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("POST", "/data-export/clean-up-files")


class DataExportLogs(FolioApi):
    """Data export Error Logs API

    APIs for managing Error Logs
    """

    def get_logs(self, **kwargs):
        """Retrieve log item with given {logId}

        ``GET /data-export/logs``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - jobExecutionId=67dfac11-1caf-4470-9ad1-d533f6360bdd

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataExportLogs_get_logs_return.schema 
        """
        return self.call("GET", "/data-export/logs", query=kwargs)


class DataExportMappingProfiles(FolioApi):
    """Data export Mapping Profile API

    APIs for managing Mapping Profiles
    """

    def get_mappingProfiles(self, **kwargs):
        """Retrieve a list of mappingProfile items.

        ``GET /data-export/mapping-profiles``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - status=SUCCESS

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataExportMappingProfiles_get_mappingProfiles_return.schema 
        """
        return self.call("GET", "/data-export/mapping-profiles", query=kwargs)

    def set_mappingProfile(self, mappingProfile: dict):
        """Create a new mappingProfile item.

        ``POST /data-export/mapping-profiles``

        Args:
            mappingProfile (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created mappingProfile item

        Schema:

            .. literalinclude:: ../files/DataExportMappingProfiles_set_mappingProfile_request.schema
        """
        return self.call("POST", "/data-export/mapping-profiles", data=mappingProfile)

    def get_mappingProfile(self, mappingProfilesId: str):
        """Retrieve mappingProfile item with given {mappingProfileId}

        ``GET /data-export/mapping-profiles/{mappingProfilesId}``

        Args:
            mappingProfilesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataExportMappingProfiles_get_mappingProfile_return.schema 
        """
        return self.call("GET", f"/data-export/mapping-profiles/{mappingProfilesId}")

    def delete_mappingProfile(self, mappingProfilesId: str):
        """Delete mappingProfile item with given {mappingProfileId}

        ``DELETE /data-export/mapping-profiles/{mappingProfilesId}``

        Args:
            mappingProfilesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/data-export/mapping-profiles/{mappingProfilesId}")

    def modify_mappingProfile(self, mappingProfilesId: str, mappingProfile: dict):
        """Update mappingProfile item with given {mappingProfileId}

        ``PUT /data-export/mapping-profiles/{mappingProfilesId}``

        Args:
            mappingProfilesId (str)
            mappingProfile (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataExportMappingProfiles_modify_mappingProfile_request.schema
        """
        return self.call("PUT", f"/data-export/mapping-profiles/{mappingProfilesId}", data=mappingProfile)


class DataExportFileDefinition(FolioApi):
    """Data export File Definition API

    APIs for creating fileDefinition to upload files
    """

    def set_fileDefinition(self, fileDefinition: dict):
        """API to create file definition to use it for the file uploading

        ``POST /data-export/file-definitions``

        Args:
            fileDefinition (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestPayloadToLarge: Payload Too Large
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataExportFileDefinition_set_fileDefinition_request.schema
        """
        return self.call("POST", "/data-export/file-definitions", data=fileDefinition)

    def get_fileDefinition(self, fileDefinitionId: str):
        """Method to get file definition by id

        ``GET /data-export/file-definitions/{fileDefinitionId}``

        Args:
            fileDefinitionId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataExportFileDefinition_get_fileDefinition_return.schema 
        """
        return self.call("GET", f"/data-export/file-definitions/{fileDefinitionId}")

    def upload_upload(self, fileDefinitionId: str, filePath: str):
        """Method to upload file

        ``POST /data-export/file-definitions/{fileDefinitionId}/upload``

        Args:
            fileDefinitionId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataExportFileDefinition_upload_upload_return.schema 
        """
        import os
        headers = {}
        headers["Content-Type"] = "application/octet-stream"
        headers["Content-length"] = str(os.path.getsize(filePath))
        headers["Content-Disposition"] = "attachment; filename=%s" % os.path.basename(
            filePath)
        with open(filePath, 'rb') as f:
            data = f.read()
        
        return self.call("POST", f"/data-export/file-definitions/{fileDefinitionId}/upload", headers=headers, data=data)


class DataExportTransformationFields(FolioApi):
    """Data export transformation fields API

    API for getting transformation fields
    """

    def get_transformationFields(self):
        """Retrieve transformationField item with given {transformationFieldId}

        ``GET /data-export/transformation-fields``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataExportTransformationFields_get_transformationFields_return.schema 
        """
        return self.call("GET", "/data-export/transformation-fields")
