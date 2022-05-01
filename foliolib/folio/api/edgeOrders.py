# -*- coding: utf-8 -*-
# Generated at 2022-04-08

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.edgeOrders")


class EdgeOrders(FolioApi):
    """Edge API - Orders

    Edge API to interface with FOLIO for 3rd party purchasing systems for placing orders
    """

    def get_validates(self, **kwargs):
        """Validate that the API Key provided can be used to place an order.

        ``GET /orders/validate``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            type (str):  purchasing system type
            apikey (str):  API Key

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestTimeout: Request Timeout
            OkapiFatalError: Server Error
        """
        return self.call("GET", "/orders/validate", query=kwargs)

    def set_validate(self, **kwargs):
        """Validate that the API Key provided can be used to place an order.

        ``POST /orders/validate``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            type (str):  purchasing system type
            apikey (str):  API Key

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestTimeout: Request Timeout
            OkapiFatalError: Server Error
        """
        return self.call("POST", "/orders/validate", query=kwargs)

    def set_order(self, **kwargs):
        """Place an order.

        ``POST /orders``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            type (str):  purchasing system type
            apikey (str):  API Key

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestTimeout: Request Timeout
            OkapiFatalError: Server Error
        """
        return self.call("POST", "/orders", query=kwargs)

    def get_orderLine(self, orderLinesId: str, **kwargs):
        """Get order line by id

        ``GET /orders/order-lines/{orderLinesId}``

        Args:
            orderLinesId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            type (str):  purchasing system type
            apikey (str):  API Key

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestTimeout: Request Timeout
            OkapiFatalError: Server Error
        """
        return self.call("GET", f"/orders/order-lines/{orderLinesId}", query=kwargs)

    def modify_orderLine(self, orderLinesId: str, **kwargs):
        """Update order line

        ``PUT /orders/order-lines/{orderLinesId}``

        Args:
            orderLinesId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            type (str):  purchasing system type
            apikey (str):  API Key

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestTimeout: Request Timeout
            OkapiFatalError: Server Error
        """
        return self.call("PUT", f"/orders/order-lines/{orderLinesId}", query=kwargs)

    def get_healths(self):
        """Health Check

        ``GET /admin/health``
        """
        return self.call("GET", "/admin/health")
