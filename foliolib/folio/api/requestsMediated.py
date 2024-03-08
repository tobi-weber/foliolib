# -*- coding: utf-8 -*-
# Generated at 2024-03-23

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.requestsMediated")



class Requestsmediated(FolioApi):
    """Request Mediated API

    
    """

    def get(self, requestId):
        """Retrieve secure request object by id

        ``GET /requests-mediated/secure-requests/{requestId}``

        Args:
            requestId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not found
            OkapiRequestFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Requestsmediated_get_response.schema
        """
        return self.call("GET", f"/requests-mediated/secure-requests/{requestId}")
