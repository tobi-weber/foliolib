# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.dataExportWorker")





class Refreshpresignedurl(FolioApi):
    """Refresh presigned url API

    
    """

    def getrefreshedpresignedurl(self, **kwargs):
        """Get presigned Url for export file

        ``GET /refresh-presigned-url``

        Keyword Args:
            filePath (str): Path to exported file

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/Refreshpresignedurl_getrefreshedpresignedurl_response.schema
        """
        return self.call("GET", "/refresh-presigned-url", query=kwargs)



class Bulkedit(FolioApi):
    """Bulk edit API

    
    """

    def postitemcontentupdates(self, jobId, itemContentUpdateCollection, **kwargs):
        """Upload item content updates

        ``POST /bulk-edit/{jobId}/item-content-update/upload``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)
            itemContentUpdateCollection (dict): See Schema below.

        Keyword Args:
            limit (int): The numbers of records to return

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Bulkedit_postitemcontentupdates_request.schema
            .. literalinclude:: ../files/Bulkedit_postitemcontentupdates_request.schema_response.schema
        """
        return self.call("POST", f"/bulk-edit/{jobId}/item-content-update/upload", itemContentUpdateCollection, query=kwargs)

    def postusercontentupdates(self, jobId, userContentUpdateCollection, **kwargs):
        """Upload user content updates

        ``POST /bulk-edit/{jobId}/user-content-update/upload``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)
            userContentUpdateCollection (dict): See Schema below.

        Keyword Args:
            limit (int): The numbers of records to return

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Bulkedit_postusercontentupdates_request.schema
            .. literalinclude:: ../files/Bulkedit_postusercontentupdates_request.schema_response.schema
        """
        return self.call("POST", f"/bulk-edit/{jobId}/user-content-update/upload", userContentUpdateCollection, query=kwargs)

    def postholdingscontentupdates(self, jobId, holdingsContentUpdateCollection, **kwargs):
        """Upload holdings record content updates

        ``POST /bulk-edit/{jobId}/holdings-content-update/upload``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)
            holdingsContentUpdateCollection (dict): See Schema below.

        Keyword Args:
            limit (int): The numbers of records to return

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Bulkedit_postholdingscontentupdates_request.schema
            .. literalinclude:: ../files/Bulkedit_postholdingscontentupdates_request.schema_response.schema
        """
        return self.call("POST", f"/bulk-edit/{jobId}/holdings-content-update/upload", holdingsContentUpdateCollection, query=kwargs)

    def downloaditemspreviewbyjobid(self, jobId):
        """Download updated items preview as csv-file

        ``GET /bulk-edit/{jobId}/preview/updated-items/download``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration
        """
        return self.call("GET", f"/bulk-edit/{jobId}/preview/updated-items/download")

    def downloaduserspreviewbyjobid(self, jobId):
        """Download updated users preview as csv-file

        ``GET /bulk-edit/{jobId}/preview/updated-users/download``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration
        """
        return self.call("GET", f"/bulk-edit/{jobId}/preview/updated-users/download")

    def downloadholdingspreviewbyjobid(self, jobId):
        """Download updated holdings records preview as csv-file

        ``GET /bulk-edit/{jobId}/preview/updated-holdings/download``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration
        """
        return self.call("GET", f"/bulk-edit/{jobId}/preview/updated-holdings/download")

    def getpreviewusersbyjobid(self, jobId, **kwargs):
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

            .. literalinclude:: ../files/Bulkedit_getpreviewusersbyjobid_response.schema
        """
        return self.call("GET", f"/bulk-edit/{jobId}/preview/users", query=kwargs)

    def getpreviewitemsbyjobid(self, jobId, **kwargs):
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

            .. literalinclude:: ../files/Bulkedit_getpreviewitemsbyjobid_response.schema
        """
        return self.call("GET", f"/bulk-edit/{jobId}/preview/items", query=kwargs)

    def getpreviewholdingsbyjobid(self, jobId, **kwargs):
        """Get a list of holdings for preview

        ``GET /bulk-edit/{jobId}/preview/holdings``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)

        Keyword Args:
            limit (int): The numbers of holdings to return

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Bulkedit_getpreviewholdingsbyjobid_response.schema
        """
        return self.call("GET", f"/bulk-edit/{jobId}/preview/holdings", query=kwargs)

    def geterrorspreviewbyjobid(self, jobId, **kwargs):
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

            .. literalinclude:: ../files/Bulkedit_geterrorspreviewbyjobid_response.schema
        """
        return self.call("GET", f"/bulk-edit/{jobId}/errors", query=kwargs)

    def uploadcsvfile(self, jobId, filePath):
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
        
        return self.call("POST", f"/bulk-edit/{jobId}/upload", data=data)

    def startjob(self, jobId):
        """Start job

        ``POST /bulk-edit/{jobId}/start``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Bad Request
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration
        """
        return self.call("POST", f"/bulk-edit/{jobId}/start")

    def rollbackcsvfile(self, jobId):
        """Roll back csv file

        ``POST /bulk-edit/{jobId}/roll-back``

        Args:
            jobId (str): UUID of the JobCommand (format: uuid)

        Raises:
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration
        """
        return self.call("POST", f"/bulk-edit/{jobId}/roll-back")



