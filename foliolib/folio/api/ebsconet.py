# -*- coding: utf-8 -*-
# Generated at 2023-04-16

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.ebsconet")



class EbsconetAdmin(FolioAdminApi):
    """Ebsconet integration API
    Administration

    Ebsconet integration API
    """

    def getValidation(self):
        """

        ``GET /ebsconet/validate``

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/Ebsconet_getValidation_response.schema
        """
        return self.call("GET", "/ebsconet/validate")

    def getEbsconetOrderLine(self, poLineNumber):
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

            .. literalinclude:: ../files/Ebsconet_getEbsconetOrderLine_response.schema
        """
        return self.call("GET", "/ebsconet/orders/order-lines/{poLineNumber}", poLineNumber)

		
    def putEbsconetOrderLine(self, poLineNumber, ebsconetOrderLine):
        """

        ``PUT /ebsconet/orders/order-lines/{poLineNumber}``

        Args:
            poLineNumber (str): product order line number
            ebsconetOrderLine (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the error (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiFatalError: Internal server error, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Ebsconet_putEbsconetOrderLine_request.schema
        """
        return self.call("PUT", "/ebsconet/orders/order-lines/{poLineNumber}", poLineNumber, ebsconetOrderLine)
