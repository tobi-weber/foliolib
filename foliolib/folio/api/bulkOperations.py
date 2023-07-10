# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.bulkOperations")



class Bulkoperations(FolioApi):
    """Bulk operations API

    Bulk operations API
    """

    def uploadcsvfile(self, filePath, **kwargs):
        """Upload csv file with identifiers list (barcodes, UUIDs, HRIDs, etc.) or csv-file with already updated entities

        ``POST /bulk-operations/upload``

        Args:
            filePath (str): Path of file to upload.

        Keyword Args:
            entityType (str): Entity type (USER, ITEM, HOLDINGS_RECORD)
            identifierType (str): Identifier type (ID, BARCODE, etc.)
            manual (bool): Key if manual approach is used (default: False)
            operationId (str): UUID of the Bulk Operation (applicable for (manual = true) case) (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Bulkoperations_uploadcsvfile_response.schema
        """
        import os
        headers = {}
        headers["Content-Type"] = "application/octet-stream"
        headers["Content-length"] = str(os.path.getsize(filePath))
        headers["Content-Disposition"] = "attachment; filename=%s" % os.path.basename(
            filePath)
        with open(filePath, 'rb') as f:
            data = f.read()
        
        return self.call("POST", f"/bulk-operations/upload", data=data, query=kwargs)

    def postcontentupdates(self, operationId, bulkOperationRuleCollection):
        """Upload content updates

        ``POST /bulk-operations/{operationId}/content-update``

        Args:
            operationId (str): UUID of the Bulk Operation (format: uuid)
            bulkOperationRuleCollection (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Bulkoperations_postcontentupdates_request.schema
        """
        return self.call("POST", f"/bulk-operations/{operationId}/content-update", bulkOperationRuleCollection)

    def getpreviewbyoperationid(self, operationId, **kwargs):
        """Get preview

        ``GET /bulk-operations/{operationId}/preview``

        Args:
            operationId (str): UUID of the Bulk Operation (format: uuid)

        Keyword Args:
            step (str): Key if manual approach is used
            limit (int): The numbers of records to return
            offset (int): Query offset (default: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Bulkoperations_getpreviewbyoperationid_response.schema
        """
        return self.call("GET", f"/bulk-operations/{operationId}/preview", query=kwargs)

    def startbulkoperation(self, operationId, bulkOperationStart):
        """Start Bulk Operation

        ``POST /bulk-operations/{operationId}/start``

        Args:
            operationId (str): UUID of the Bulk Operation (format: uuid)
            bulkOperationStart (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Bad Request
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Bulkoperations_startbulkoperation_request.schema
            .. literalinclude:: ../files/Bulkoperations_startbulkoperation_request.schema_response.schema
        """
        return self.call("POST", f"/bulk-operations/{operationId}/start", bulkOperationStart)

    def geterrorspreviewbyoperationid(self, operationId, **kwargs):
        """Get a list of errors for preview

        ``GET /bulk-operations/{operationId}/errors``

        Args:
            operationId (str): UUID of the Bulk Operation (format: uuid)

        Keyword Args:
            limit (int): The numbers of errors to return

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: No found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Bulkoperations_geterrorspreviewbyoperationid_response.schema
        """
        return self.call("GET", f"/bulk-operations/{operationId}/errors", query=kwargs)

    def getbulkoperationcollection(self, **kwargs):
        """Get a list of operations

        ``GET /bulk-operations``

        Keyword Args:
            query (str): Request query
            offset (int): Query offset
            limit (int): Query limit

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Bulkoperations_getbulkoperationcollection_response.schema
        """
        return self.call("GET", "/bulk-operations", query=kwargs)

    def downloadfilebyoperationid(self, operationId, **kwargs):
        """Download file by operation id

        ``GET /bulk-operations/{operationId}/download``

        Args:
            operationId (str): UUID of the Bulk Operation (format: uuid)

        Keyword Args:
            fileContentType (str): The file content type

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration
        """
        return self.call("GET", f"/bulk-operations/{operationId}/download", query=kwargs)

    def getbulkoperationbyid(self, operationId):
        """Get bulk operation by id

        ``GET /bulk-operations/{operationId}``

        Args:
            operationId (str): UUID of the Bulk Operation (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Bulkoperations_getbulkoperationbyid_response.schema
        """
        return self.call("GET", f"/bulk-operations/{operationId}")

    def cleanuplogfiles(self):
        """Removed all files older than 30 days

        ``POST /bulk-operations/clean-up-log-files``

        Raises:
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration
        """
        return self.call("POST", "/bulk-operations/clean-up-log-files")
