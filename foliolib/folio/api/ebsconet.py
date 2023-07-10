# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.ebsconet")



class Ebsconet(FolioApi):
    """Ebsconet integration API

    Ebsconet integration API
    """

    def getvalidation(self):
        """

        ``GET /ebsconet/validate``

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/Ebsconet_getvalidation_response.schema
        """
        return self.call("GET", "/ebsconet/validate")

    def getebsconetorderline(self, poLineNumber):
        """

        ``GET /ebsconet/orders/order-lines/{poLineNumber}``

        Args:
            poLineNumber (str): product order line number

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the error (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiRequestNotFound: Purchase order line with a given number not found
            OkapiFatalError: Internal server error, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Ebsconet_getebsconetorderline_response.schema
        """
        return self.call("GET", f"/ebsconet/orders/order-lines/{poLineNumber}")

		
    def putebsconetorderline(self, poLineNumber, ebsconetOrderLine):
        """

        ``PUT /ebsconet/orders/order-lines/{poLineNumber}``

        Args:
            poLineNumber (str): product order line number
            ebsconetOrderLine (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the error (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiFatalError: Internal server error, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Ebsconet_putebsconetorderline_request.schema
        """
        return self.call("PUT", f"/ebsconet/orders/order-lines/{poLineNumber}", ebsconetOrderLine)
