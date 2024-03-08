# -*- coding: utf-8 -*-
# Generated at 2024-03-23

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.batchPrint")



class BatchPrint(FolioApi):
    """Batch printing

    
    """

    def getprintentries(self, **kwargs):
        """Get batch printing entries with optional CQL query. X-Okapi-Permissions must include batch-print.entries.collection.get


        ``GET /print/entries``

        Keyword Args:
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0)
            offset (int): Skip over number of elements (default is first element) (default: 0, minimum: 0)
            query (str): CQL query

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiRequestFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/BatchPrint_getprintentries_response.schema
        """
        return self.call("GET", "/print/entries", query=kwargs)

		
    def deleteprintentries(self, **kwargs):
        """Delete batch printing entries by  comma separated IDs. X-Okapi-Permissions must include batch-print.entries.collection.delete


        ``DELETE /print/entries``

        Keyword Args:
            ids (str): Comma seperated IDs of items

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestFatalError: Internal error
        """
        return self.call("DELETE", "/print/entries", query=kwargs)

		
    def postprintentry(self, entry):
        """Create print entry. X-Okapi-Permissions must include batch-print.entries.item.post


        ``POST /print/entries``

        Args:
            entry (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestForbidden: Forbidden
            OkapiRequestPayloadToLarge: Payload Too Large
            OkapiRequestFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/BatchPrint_postprintentry_request.schema
        """
        return self.call("POST", f"/print/entries", entry)

    def getprintentry(self, id_):
        """Get print entry by id. X-Okapi-Permissions must include batch-print.entries.item.get


        ``GET /print/entries/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestForbidden: Forbidden
            OkapiRequestNotFound: Not Found
            OkapiRequestFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/BatchPrint_getprintentry_response.schema
        """
        return self.call("GET", f"/print/entries/{id_}")

		
    def deleteprintentry(self, id_):
        """Delete print entry. X-Okapi-Permissions must include batch-print.entries.item.delete


        ``DELETE /print/entries/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiRequestFatalError: Internal error
        """
        return self.call("DELETE", f"/print/entries/{id_}")

		
    def updateprintentry(self, entry, id_):
        """Update print entry. X-Okapi-Permissions must include batch-print.entries.item.put


        ``PUT /print/entries/{id}``

        Args:
            entry (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiRequestFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/BatchPrint_updateprintentry_request.schema
        """
        return self.call("PUT", f"/print/entries/{id_}", entry)

    def savemail(self, messageRequest):
        """Send mail to create print entry. X-Okapi-Permissions must include batch-print.entries.mail.post


        ``POST /mail``

        Args:
            messageRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestForbidden: Forbidden
            OkapiRequestFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/BatchPrint_savemail_request.schema
            .. literalinclude:: ../files/BatchPrint_savemail_request.schema_response.schema
        """
        return self.call("POST", f"/mail", messageRequest)

    def createbatch(self):
        """Send mail to create print entry. X-Okapi-Permissions must include batch-print.print.write


        ``POST /print/batch-creation``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestForbidden: Forbidden
            OkapiRequestFatalError: Internal error
        """
        return self.call("POST", "/print/batch-creation")
