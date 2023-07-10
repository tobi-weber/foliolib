# -*- coding: utf-8 -*-
# Generated at 2023-07-10

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
            OkapiFatalError: Server Error
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
            OkapiFatalError: Server Error
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
            OkapiFatalError: Server Error

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
            OkapiFatalError: Server Error
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
            OkapiFatalError: Server Error
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
            OkapiFatalError: Server Error
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
            OkapiFatalError: Server Error
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
            OkapiFatalError: Server Error

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

    def set_processFile(self, uploadDefinitionId: str, processFile: dict):
        """Starts the file processing

        ``POST /data-import/uploadDefinitions/{uploadDefinitionId}/processFiles``

        Args:
            uploadDefinitionId (str)
            processFile (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImport_set_processFile_request.schema
        """
        return self.call("POST", f"/data-import/uploadDefinitions/{uploadDefinitionId}/processFiles", data=processFile)

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
            OkapiFatalError: Server Error
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
            OkapiFatalError: Server Error
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
            OkapiFatalError: Server Error

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
            OkapiFatalError: Server Error
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
            OkapiFatalError: Server Error
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
            OkapiFatalError: Server Error

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
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImport_get_dataTypes_return.schema 
        """
        return self.call("GET", "/data-import/dataTypes")
