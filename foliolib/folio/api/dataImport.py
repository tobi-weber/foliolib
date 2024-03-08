# -*- coding: utf-8 -*-
# Generated at 2024-03-23

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.dataImport")


class DataImport(FolioApi):
    """Data import API

    API for uploading source records and processing them
    """

    def get_uploadDefinitions(self, **kwargs):
        """Get a list of definitions

        ``GET /data-import/uploadDefinitions``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example id=67dfac11-1caf-4470-9ad1-d533f6360bdd
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - id=67dfac11-1caf-4470-9ad1-d533f6360bdd
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImport_get_uploadDefinitions_return.schema 
        """
        return self.call("GET", "/data-import/uploadDefinitions", query=kwargs)

    def set_uploadDefinition(self, uploadDefinition: dict):
        """Create a new uploadDefinition item.

        ``POST /data-import/uploadDefinitions``

        Args:
            uploadDefinition (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created uploadDefinition item

        Schema:

            .. literalinclude:: ../files/DataImport_set_uploadDefinition_request.schema
        """
        return self.call("POST", "/data-import/uploadDefinitions", data=uploadDefinition)

    def get_uploadDefinition(self, uploadDefinitionId: str):
        """Retrieve uploadDefinition item with given {uploadDefinitionId}

        ``GET /data-import/uploadDefinitions/{uploadDefinitionId}``

        Args:
            uploadDefinitionId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImport_get_uploadDefinition_return.schema 
        """
        return self.call("GET", f"/data-import/uploadDefinitions/{uploadDefinitionId}")

    def delete_uploadDefinition(self, uploadDefinitionId: str):
        """Delete uploadDefinition item with given {uploadDefinitionId}

        ``DELETE /data-import/uploadDefinitions/{uploadDefinitionId}``

        Args:
            uploadDefinitionId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestFatalError: Server Error
        """
        return self.call("DELETE", f"/data-import/uploadDefinitions/{uploadDefinitionId}")

    def modify_uploadDefinition(self, uploadDefinitionId: str, uploadDefinition: dict):
        """Update uploadDefinition item with given {uploadDefinitionId}

        ``PUT /data-import/uploadDefinitions/{uploadDefinitionId}``

        Args:
            uploadDefinitionId (str)
            uploadDefinition (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiRequestFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImport_modify_uploadDefinition_request.schema
        """
        return self.call("PUT", f"/data-import/uploadDefinitions/{uploadDefinitionId}", data=uploadDefinition)

    def set_file(self, uploadDefinitionId: str, file: dict):
        """

        ``POST /data-import/uploadDefinitions/{uploadDefinitionId}/files``

        Args:
            uploadDefinitionId (str)
            file (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImport_set_file_request.schema
            .. literalinclude:: ../files/DataImport_set_file_return.schema 
        """
        return self.call("POST", f"/data-import/uploadDefinitions/{uploadDefinitionId}/files", data=file)

    def delete_file(self, uploadDefinitionId: str, fileId: str):
        """Delete file by id

        ``DELETE /data-import/uploadDefinitions/{uploadDefinitionId}/files/{fileId}``

        Args:
            uploadDefinitionId (str)
            fileId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestFatalError: Server Error
        """
        return self.call("DELETE", f"/data-import/uploadDefinitions/{uploadDefinitionId}/files/{fileId}")

    def upload_file(self, uploadDefinitionId: str, fileId: str, filePath: str):
        """Upload file

        ``POST /data-import/uploadDefinitions/{uploadDefinitionId}/files/{fileId}``

        Args:
            uploadDefinitionId (str)
            fileId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImport_upload_file_return.schema 
        """
        import os
        headers = {}
        headers["Content-Type"] = "application/octet-stream"
        headers["Content-length"] = str(os.path.getsize(filePath))
        headers["Content-Disposition"] = "attachment; filename=%s" % os.path.basename(
            filePath)
        with open(filePath, 'rb') as f:
            data = f.read()
        
        return self.call("POST", f"/data-import/uploadDefinitions/{uploadDefinitionId}/files/{fileId}", headers=headers, data=data)

    def set_assembleStorageFile(self, uploadDefinitionId: str, fileId: str, assembleStorageFile: dict):
        """Assemble the large file uploaded to storage by the UI

        ``POST /data-import/uploadDefinitions/{uploadDefinitionId}/files/{fileId}/assembleStorageFile``

        Args:
            uploadDefinitionId (str)
            fileId (str)
            assembleStorageFile (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImport_set_assembleStorageFile_request.schema
        """
        return self.call("POST", f"/data-import/uploadDefinitions/{uploadDefinitionId}/files/{fileId}/assembleStorageFile", data=assembleStorageFile)

    def set_processFile(self, uploadDefinitionId: str, processFile: dict):
        """Starts the file processing

        ``POST /data-import/uploadDefinitions/{uploadDefinitionId}/processFiles``

        Args:
            uploadDefinitionId (str)
            processFile (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImport_set_processFile_request.schema
        """
        return self.call("POST", f"/data-import/uploadDefinitions/{uploadDefinitionId}/processFiles", data=processFile)

    def delete_cancel(self, jobExecutionId: str):
        """

        ``DELETE /data-import/jobExecutions/{jobExecutionId}/cancel``

        Args:
            jobExecutionId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImport_delete_cancel_return.schema 
        """
        return self.call("DELETE", f"/data-import/jobExecutions/{jobExecutionId}/cancel")

    def get_downloadUrl_by_jobExecution(self, jobExecutionId: str):
        """

        ``GET /data-import/jobExecutions/{jobExecutionId}/downloadUrl``

        Args:
            jobExecutionId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/DataImport_get_downloadUrl_by_jobExecution_return.schema 
        """
        return self.call("GET", f"/data-import/jobExecutions/{jobExecutionId}/downloadUrl")

    def get_fileExtensions(self, **kwargs):
        """Get a list of definitions

        ``GET /data-import/fileExtensions``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example importBlocked=true
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - importBlocked=true
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImport_get_fileExtensions_return.schema 
        """
        return self.call("GET", "/data-import/fileExtensions", query=kwargs)

    def set_fileExtension(self, fileExtension: dict):
        """Create a new fileExtension item.

        ``POST /data-import/fileExtensions``

        Args:
            fileExtension (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created fileExtension item

        Schema:

            .. literalinclude:: ../files/DataImport_set_fileExtension_request.schema
        """
        return self.call("POST", "/data-import/fileExtensions", data=fileExtension)

    def get_fileExtension(self, fileExtensionsId: str):
        """Retrieve fileExtension item with given {fileExtensionId}

        ``GET /data-import/fileExtensions/{fileExtensionsId}``

        Args:
            fileExtensionsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImport_get_fileExtension_return.schema 
        """
        return self.call("GET", f"/data-import/fileExtensions/{fileExtensionsId}")

    def delete_fileExtension(self, fileExtensionsId: str):
        """Delete fileExtension item with given {fileExtensionId}

        ``DELETE /data-import/fileExtensions/{fileExtensionsId}``

        Args:
            fileExtensionsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestFatalError: Server Error
        """
        return self.call("DELETE", f"/data-import/fileExtensions/{fileExtensionsId}")

    def modify_fileExtension(self, fileExtensionsId: str, fileExtension: dict):
        """Update fileExtension item with given {fileExtensionId}

        ``PUT /data-import/fileExtensions/{fileExtensionsId}``

        Args:
            fileExtensionsId (str)
            fileExtension (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiRequestFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImport_modify_fileExtension_request.schema
        """
        return self.call("PUT", f"/data-import/fileExtensions/{fileExtensionsId}", data=fileExtension)

    def set_default(self):
        """Restore fileExtension settings to default

        ``POST /data-import/fileExtensions/restore/default``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImport_set_default_return.schema 
        """
        return self.call("POST", "/data-import/fileExtensions/restore/default")

    def get_dataTypes(self):
        """Get a list of data types

        ``GET /data-import/dataTypes``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImport_get_dataTypes_return.schema 
        """
        return self.call("GET", "/data-import/dataTypes")

    def get_splitStatuses(self):
        """Get the server configuration of file splitting

        ``GET /data-import/splitStatus``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImport_get_splitStatuses_return.schema 
        """
        return self.call("GET", "/data-import/splitStatus")

    def get_uploadUrls(self, **kwargs):
        """Get a presigned upload url for the first part of a file

        ``GET /data-import/uploadUrl``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            fileName ():  The name of the file that will be uploaded

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImport_get_uploadUrls_return.schema 
        """
        return self.call("GET", "/data-import/uploadUrl", query=kwargs)

    def get_subsequents(self, **kwargs):
        """Get a presigned upload url for later parts of a file

        ``GET /data-import/uploadUrl/subsequent``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            key ():  The key that will be uploaded to on S3
            uploadId ():  The upload ID
            partNumber (int):  The part number, postitive integers beginning at two (part 1 is uploaded with /uploadUrl)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImport_get_subsequents_return.schema 
        """
        return self.call("GET", "/data-import/uploadUrl/subsequent", query=kwargs)
