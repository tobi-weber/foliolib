# -*- coding: utf-8 -*-
# Generated at 2020-11-29

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.gobi")


class Gobi(FolioApi):
    """GOBI® (Global Online Bibliographic Information) Integration

    GOBI® (Global Online Bibliographic Information) is the leading web-based
		acquisitions tool for finding, ordering and managing e-books and print
		books for libraries. This module allows GOBI initiated orders to be
		fulfilled by FOLIO.
    """

    def get_validates(self):
        """Validates the user has proper access to the module

        ``GET /gobi/validate``

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestForbidden: Forbidden
            OkapiFatalError: Server Error
        """
        return self.call("GET", "/gobi/validate")

    def set_validate(self):
        """Validates the user has proper access to the module

        ``POST /gobi/validate``

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestForbidden: Forbidden
            OkapiFatalError: Server Error
        """
        return self.call("POST", "/gobi/validate")

    def set_order(self, order: str):
        """Fulfill an order that is delivered in GOBI format

        ``POST /gobi/orders``

        Args:
            order (str): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestForbidden: Forbidden
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Gobi_set_order_request.schema
        """
        return self.call("POST", "/gobi/orders", data=order)
