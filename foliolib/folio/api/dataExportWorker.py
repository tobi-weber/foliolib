# -*- coding: utf-8 -*-
# Generated at 2023-04-16

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.dataExportWorker")





class BulkeditAdmin(FolioAdminApi):
    """Bulk edit API
    Administration

    
    """

    def postContentUpdates(self, jobId, contentUpdateCollection, **kwargs):
        """Upload content updates

        ``POST /bulk-edit/{jobId}/items-content-update/upload``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)
            contentUpdateCollection (dict): See Schema below.

        Keyword Args:
            limit (int): The numbers of records to return

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Bulkedit_postContentUpdates_request.schema
            .. literalinclude:: ../files/Bulkedit_postContentUpdates_request.schema_response.schema
        """
        return self.call("POST", "/bulk-edit/{jobId}/items-content-update/upload", jobId, contentUpdateCollection, query=kwargs)

    def downloadPreviewByJobId(self, jobId):
        """Download preview as csv-file

        ``GET /bulk-edit/{jobId}/preview/updated-items/download``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration
        """
        return self.call("GET", "/bulk-edit/{jobId}/preview/updated-items/download", jobId)

    def getPreviewUsersByJobId(self, jobId, **kwargs):
        """Get a list of users for preview

        ``GET /bulk-edit/{jobId}/preview/users``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)

        Keyword Args:
            limit (int): The numbers of users to return

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Bad Request
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Bulkedit_getPreviewUsersByJobId_response.schema
        """
        return self.call("GET", "/bulk-edit/{jobId}/preview/users", jobId, query=kwargs)

    def getPreviewItemsByJobId(self, jobId, **kwargs):
        """Get a list of items for preview

        ``GET /bulk-edit/{jobId}/preview/items``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)

        Keyword Args:
            limit (int): The numbers of items to return

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Bulkedit_getPreviewItemsByJobId_response.schema
        """
        return self.call("GET", "/bulk-edit/{jobId}/preview/items", jobId, query=kwargs)

    def getErrorsPreviewByJobId(self, jobId, **kwargs):
        """Get a list of errors for preview

        ``GET /bulk-edit/{jobId}/errors``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)

        Keyword Args:
            limit (int): The numbers of users to return

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: No found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Bulkedit_getErrorsPreviewByJobId_response.schema
        """
        return self.call("GET", "/bulk-edit/{jobId}/errors", jobId, query=kwargs)

    def uploadCsvFile(self, jobId, filePath):
        """Upload csv file

        ``POST /bulk-edit/{jobId}/upload``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)
            filePath (str): Path of file to upload.

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration
        """
        import os
        headers = {}
        headers["Content-Type"] = "application/octet-stream"
        headers["Content-length"] = str(os.path.getsize(filePath))
        headers["Content-Disposition"] = "attachment; filename=%s" % os.path.basename(
            filePath)
        with open(filePath, 'rb') as f:
            data = f.read()
        
        return self.call("POST", "/bulk-edit/{jobId}/upload", jobId, data=data)

    def startJob(self, jobId):
        """Start job

        ``POST /bulk-edit/{jobId}/start``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Bad Request
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration
        """
        return self.call("POST", "/bulk-edit/{jobId}/start", jobId)

    def rollBackCsvFile(self, jobId):
        """Roll back csv file

        ``POST /bulk-edit/{jobId}/roll-back``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)

        Raises:
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration
        """
        return self.call("POST", "/bulk-edit/{jobId}/roll-back", jobId)

