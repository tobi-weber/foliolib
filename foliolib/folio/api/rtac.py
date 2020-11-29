# -*- coding: utf-8 -*-
# Generated at 2020-11-29

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.rtac")


class Rtac(FolioApi):
    """DEPRECATED Real Time Availability Checker Integration

    This module allows 3rd party discovery services to check for FOLIO inventory availability
    """

    def get_rtac(self, rtacId: str):
        """Retrieve rtac item with given {rtacId}

        ``GET /rtac/{rtacId}``

        Args:
            rtacId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestError: Bad Request
            OkapiRequestForbidden: Forbidden

        Schema:

            .. literalinclude:: ../files/Rtac_get_rtac_return.schema 
        """
        return self.call("GET", f"/rtac/{rtacId}")


class RtacBatch(FolioApi):
    """Real Time Availability Checker Integration

    This module allows 3rd party discovery services to check for FOLIO inventory availability
    """

    def set_rtacBatch(self, rtacBatch: dict):
        """Retrieve holding information from inventory in a batch

        ``POST /rtac-batch``

        Args:
            rtacBatch (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestForbidden: Forbidden
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/RtacBatch_set_rtacBatch_request.schema
            .. literalinclude:: ../files/RtacBatch_set_rtacBatch_return.schema 
        """
        return self.call("POST", "/rtac-batch", data=rtacBatch)
