# -*- coding: utf-8 -*-
# Generated at 2020-11-29

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.ordersStorage")


class AcquisitionsUnit(FolioApi):
    """Acquisitions units

    **CRUD APIs used to manage acquisitions units.**
    """

    def get_units(self, **kwargs):
        """Get list of acquisitions units

        ``GET /acquisitions-units-storage/units``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example protectRead
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["protectRead", "false"]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AcquisitionsUnit_get_units_return.schema 
        """
        return self.call("GET", "/acquisitions-units-storage/units", query=kwargs)

    def set_unit(self, unit: dict):
        """Create new acquisitions unit

        ``POST /acquisitions-units-storage/units``

        Args:
            unit (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created unit item

        Schema:

            .. literalinclude:: ../files/AcquisitionsUnit_set_unit_request.schema
        """
        return self.call("POST", "/acquisitions-units-storage/units", data=unit)

    def get_unit(self, unitsId: str):
        """Retrieve unit item with given {unitId}

        ``GET /acquisitions-units-storage/units/{unitsId}``

        Args:
            unitsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AcquisitionsUnit_get_unit_return.schema 
        """
        return self.call("GET", f"/acquisitions-units-storage/units/{unitsId}")

    def delete_unit(self, unitsId: str):
        """Delete unit item with given {unitId}

        ``DELETE /acquisitions-units-storage/units/{unitsId}``

        Args:
            unitsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/acquisitions-units-storage/units/{unitsId}")

    def modify_unit(self, unitsId: str, unit: dict):
        """Update acquisitions unit

        ``PUT /acquisitions-units-storage/units/{unitsId}``

        Args:
            unitsId (str)
            unit (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AcquisitionsUnit_modify_unit_request.schema
        """
        return self.call("PUT", f"/acquisitions-units-storage/units/{unitsId}", data=unit)

    def get_memberships(self, **kwargs):
        """Get list of acquisitions units memberships

        ``GET /acquisitions-units-storage/memberships``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example acquisitionUnitId
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["acquisitionUnitId", "0ebb1f7d-983f-3026-8a4c-5318e0ebc041"]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AcquisitionsUnit_get_memberships_return.schema 
        """
        return self.call("GET", "/acquisitions-units-storage/memberships", query=kwargs)

    def set_membership(self, membership: dict):
        """Create new acquisitions unit

        ``POST /acquisitions-units-storage/memberships``

        Args:
            membership (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created membership item

        Schema:

            .. literalinclude:: ../files/AcquisitionsUnit_set_membership_request.schema
        """
        return self.call("POST", "/acquisitions-units-storage/memberships", data=membership)

    def get_membership(self, membershipsId: str):
        """Retrieve membership item with given {membershipId}

        ``GET /acquisitions-units-storage/memberships/{membershipsId}``

        Args:
            membershipsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AcquisitionsUnit_get_membership_return.schema 
        """
        return self.call("GET", f"/acquisitions-units-storage/memberships/{membershipsId}")

    def delete_membership(self, membershipsId: str):
        """Delete membership item with given {membershipId}

        ``DELETE /acquisitions-units-storage/memberships/{membershipsId}``

        Args:
            membershipsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/acquisitions-units-storage/memberships/{membershipsId}")

    def modify_membership(self, membershipsId: str, membership: dict):
        """Update acquisitions unit

        ``PUT /acquisitions-units-storage/memberships/{membershipsId}``

        Args:
            membershipsId (str)
            membership (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AcquisitionsUnit_modify_membership_request.schema
        """
        return self.call("PUT", f"/acquisitions-units-storage/memberships/{membershipsId}", data=membership)


class OrderTemplates(FolioApi):
    """Order Templates

    **This module implements the CRUD interface for Order Templates API. This API is intended for internal use only.**
    """

    def get_orderTemplates(self, **kwargs):
        """Get list of order templates

        ``GET /orders-storage/order-templates``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example templateCode
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["templateCode", "Amazon", "="]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/OrderTemplates_get_orderTemplates_return.schema 
        """
        return self.call("GET", "/orders-storage/order-templates", query=kwargs)

    def set_orderTemplate(self, orderTemplate: dict):
        """Create new order template

        ``POST /orders-storage/order-templates``

        Args:
            orderTemplate (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created orderTemplate item

        Schema:

            .. literalinclude:: ../files/OrderTemplates_set_orderTemplate_request.schema
        """
        return self.call("POST", "/orders-storage/order-templates", data=orderTemplate)

    def get_orderTemplate(self, orderTemplatesId: str):
        """Retrieve orderTemplate item with given {orderTemplateId}

        ``GET /orders-storage/order-templates/{orderTemplatesId}``

        Args:
            orderTemplatesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/OrderTemplates_get_orderTemplate_return.schema 
        """
        return self.call("GET", f"/orders-storage/order-templates/{orderTemplatesId}")

    def delete_orderTemplate(self, orderTemplatesId: str):
        """Delete orderTemplate item with given {orderTemplateId}

        ``DELETE /orders-storage/order-templates/{orderTemplatesId}``

        Args:
            orderTemplatesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders-storage/order-templates/{orderTemplatesId}")

    def modify_orderTemplate(self, orderTemplatesId: str, orderTemplate: dict):
        """Update order template

        ``PUT /orders-storage/order-templates/{orderTemplatesId}``

        Args:
            orderTemplatesId (str)
            orderTemplate (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/OrderTemplates_modify_orderTemplate_request.schema
        """
        return self.call("PUT", f"/orders-storage/order-templates/{orderTemplatesId}", data=orderTemplate)


class PoLineNumber(FolioApi):
    """Purchase Order Line Number

    **API used to manage Purchase Order Line number.  This API is intended for internal use only**
    """

    def get_poLineNumbers(self, **kwargs):
        """Get purchase order line number

        ``GET /orders-storage/po-line-number``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            purchaseOrderId (str):  Purchase Order Id
                    
                    Example:
                    
                     - 8ad4b87b-9b47-4199-b0c3-5480745c6b41
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PoLineNumber_get_poLineNumbers_return.schema 
        """
        return self.call("GET", "/orders-storage/po-line-number", query=kwargs)


class PurchaseOrder(FolioApi):
    """Purchase Order

    **This module implements the CRUD interface.  This API is intended for internal use only.  Please use the /orders/composite-orders API provided by mod-orders instead.**
    """

    def get_purchaseOrders(self, **kwargs):
        """Get list of purchase orders

        ``GET /orders-storage/purchase-orders``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PurchaseOrder_get_purchaseOrders_return.schema 
        """
        return self.call("GET", "/orders-storage/purchase-orders", query=kwargs)

    def set_purchaseOrder(self, purchaseOrder: dict):
        """Create a new purchaseOrder item.

        ``POST /orders-storage/purchase-orders``

        Args:
            purchaseOrder (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created purchaseOrder item

        Schema:

            .. literalinclude:: ../files/PurchaseOrder_set_purchaseOrder_request.schema
        """
        return self.call("POST", "/orders-storage/purchase-orders", data=purchaseOrder)

    def get_purchaseOrder(self, purchaseOrdersId: str):
        """Retrieve purchaseOrder item with given {purchaseOrderId}

        ``GET /orders-storage/purchase-orders/{purchaseOrdersId}``

        Args:
            purchaseOrdersId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PurchaseOrder_get_purchaseOrder_return.schema 
        """
        return self.call("GET", f"/orders-storage/purchase-orders/{purchaseOrdersId}")

    def delete_purchaseOrder(self, purchaseOrdersId: str):
        """Delete purchaseOrder item with given {purchaseOrderId}

        ``DELETE /orders-storage/purchase-orders/{purchaseOrdersId}``

        Args:
            purchaseOrdersId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders-storage/purchase-orders/{purchaseOrdersId}")

    def modify_purchaseOrder(self, purchaseOrdersId: str, purchaseOrder: dict):
        """Update purchaseOrder item with given {purchaseOrderId}

        ``PUT /orders-storage/purchase-orders/{purchaseOrdersId}``

        Args:
            purchaseOrdersId (str)
            purchaseOrder (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PurchaseOrder_modify_purchaseOrder_request.schema
        """
        return self.call("PUT", f"/orders-storage/purchase-orders/{purchaseOrdersId}", data=purchaseOrder)


class ReceivingHistory(FolioApi):
    """Receiving History

    **Get list of receiving history API.  This API is intended for internal use only.  Please use the /orders/receiving-history API provided by mod-orders instead.**
    """

    def get_receivingHistories(self, **kwargs):
        """Get list of receiving history

        ``GET /orders-storage/receiving-history``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ReceivingHistory_get_receivingHistories_return.schema 
        """
        return self.call("GET", "/orders-storage/receiving-history", query=kwargs)


class Alert(FolioApi):
    """Alerts

    **CRUD APIs used to manage alerts.**
    """

    def get_alerts(self, **kwargs):
        """Get list of alerts

        ``GET /orders-storage/alerts``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Alert_get_alerts_return.schema 
        """
        return self.call("GET", "/orders-storage/alerts", query=kwargs)

    def set_alert(self, alert: dict):
        """Create a new alert item.

        ``POST /orders-storage/alerts``

        Args:
            alert (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created alert item

        Schema:

            .. literalinclude:: ../files/Alert_set_alert_request.schema
        """
        return self.call("POST", "/orders-storage/alerts", data=alert)

    def get_alert(self, alertsId: str):
        """Retrieve alert item with given {alertId}

        ``GET /orders-storage/alerts/{alertsId}``

        Args:
            alertsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Alert_get_alert_return.schema 
        """
        return self.call("GET", f"/orders-storage/alerts/{alertsId}")

    def delete_alert(self, alertsId: str):
        """Delete alert item with given {alertId}

        ``DELETE /orders-storage/alerts/{alertsId}``

        Args:
            alertsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders-storage/alerts/{alertsId}")

    def modify_alert(self, alertsId: str, alert: dict):
        """Update alert item with given {alertId}

        ``PUT /orders-storage/alerts/{alertsId}``

        Args:
            alertsId (str)
            alert (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Alert_modify_alert_request.schema
        """
        return self.call("PUT", f"/orders-storage/alerts/{alertsId}", data=alert)


class PoLine(FolioApi):
    """PO Line

    **This module implements the CRUD interface.  This API is intended for internal use only.  Please use the /orders/order-lines API provided by mod-orders instead.**
    """

    def get_poLines(self, **kwargs):
        """Get list of po lines

        ``GET /orders-storage/po-lines``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PoLine_get_poLines_return.schema 
        """
        return self.call("GET", "/orders-storage/po-lines", query=kwargs)

    def set_poLine(self, poLine: dict):
        """Create a new poLine item.

        ``POST /orders-storage/po-lines``

        Args:
            poLine (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created poLine item

        Schema:

            .. literalinclude:: ../files/PoLine_set_poLine_request.schema
        """
        return self.call("POST", "/orders-storage/po-lines", data=poLine)

    def get_poLine(self, poLinesId: str):
        """Retrieve poLine item with given {poLineId}

        ``GET /orders-storage/po-lines/{poLinesId}``

        Args:
            poLinesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PoLine_get_poLine_return.schema 
        """
        return self.call("GET", f"/orders-storage/po-lines/{poLinesId}")

    def delete_poLine(self, poLinesId: str):
        """Delete poLine item with given {poLineId}

        ``DELETE /orders-storage/po-lines/{poLinesId}``

        Args:
            poLinesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders-storage/po-lines/{poLinesId}")

    def modify_poLine(self, poLinesId: str, poLine: dict):
        """Update poLine item with given {poLineId}

        ``PUT /orders-storage/po-lines/{poLinesId}``

        Args:
            poLinesId (str)
            poLine (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PoLine_modify_poLine_request.schema
        """
        return self.call("PUT", f"/orders-storage/po-lines/{poLinesId}", data=poLine)


class Configuration(FolioApi):
    """Orders configuration

    **Get list of orders-storage configuration API. This API is intended for internal use only.  Please use the /orders/configuration API provided by mod-orders instead.**
    """

    def get_reasonsForClosures(self, **kwargs):
        """Get list of reasons for closure

        ``GET /orders-storage/configuration/reasons-for-closure``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example reasonForClosure
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["reasonForClosure", "Denied", "="]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Configuration_get_reasonsForClosures_return.schema 
        """
        return self.call("GET", "/orders-storage/configuration/reasons-for-closure", query=kwargs)

    def set_reasonsForClosure(self, reasonsForClosure: dict):
        """Create new reason for closure

        ``POST /orders-storage/configuration/reasons-for-closure``

        Args:
            reasonsForClosure (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created reasonsForClosure item

        Schema:

            .. literalinclude:: ../files/Configuration_set_reasonsForClosure_request.schema
        """
        return self.call("POST", "/orders-storage/configuration/reasons-for-closure", data=reasonsForClosure)

    def get_reasonsForClosure(self, reasonsForClosureId: str):
        """Retrieve reasonsForClosure item with given {reasonsForClosureId}

        ``GET /orders-storage/configuration/reasons-for-closure/{reasonsForClosureId}``

        Args:
            reasonsForClosureId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Configuration_get_reasonsForClosure_return.schema 
        """
        return self.call("GET", f"/orders-storage/configuration/reasons-for-closure/{reasonsForClosureId}")

    def delete_reasonsForClosure(self, reasonsForClosureId: str):
        """Delete reasonsForClosure item with given {reasonsForClosureId}

        ``DELETE /orders-storage/configuration/reasons-for-closure/{reasonsForClosureId}``

        Args:
            reasonsForClosureId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders-storage/configuration/reasons-for-closure/{reasonsForClosureId}")

    def modify_reasonsForClosure(self, reasonsForClosureId: str, reasonsForClosure: dict):
        """Update reason for closure

        ``PUT /orders-storage/configuration/reasons-for-closure/{reasonsForClosureId}``

        Args:
            reasonsForClosureId (str)
            reasonsForClosure (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Configuration_modify_reasonsForClosure_request.schema
        """
        return self.call("PUT", f"/orders-storage/configuration/reasons-for-closure/{reasonsForClosureId}", data=reasonsForClosure)

    def get_prefixes(self, **kwargs):
        """Get list of prefixes

        ``GET /orders-storage/configuration/prefixes``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example prefix
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["prefix", "Prx", "="]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Configuration_get_prefixes_return.schema 
        """
        return self.call("GET", "/orders-storage/configuration/prefixes", query=kwargs)

    def set_prefix(self, prefix: dict):
        """Create new prefix

        ``POST /orders-storage/configuration/prefixes``

        Args:
            prefix (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created prefix item

        Schema:

            .. literalinclude:: ../files/Configuration_set_prefix_request.schema
        """
        return self.call("POST", "/orders-storage/configuration/prefixes", data=prefix)

    def get_prefix(self, prefixesId: str):
        """Retrieve prefix item with given {prefixId}

        ``GET /orders-storage/configuration/prefixes/{prefixesId}``

        Args:
            prefixesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Configuration_get_prefix_return.schema 
        """
        return self.call("GET", f"/orders-storage/configuration/prefixes/{prefixesId}")

    def delete_prefix(self, prefixesId: str):
        """Delete prefix item with given {prefixId}

        ``DELETE /orders-storage/configuration/prefixes/{prefixesId}``

        Args:
            prefixesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders-storage/configuration/prefixes/{prefixesId}")

    def modify_prefix(self, prefixesId: str, prefix: dict):
        """Update prefix

        ``PUT /orders-storage/configuration/prefixes/{prefixesId}``

        Args:
            prefixesId (str)
            prefix (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Configuration_modify_prefix_request.schema
        """
        return self.call("PUT", f"/orders-storage/configuration/prefixes/{prefixesId}", data=prefix)

    def get_suffixes(self, **kwargs):
        """Get list of suffixes

        ``GET /orders-storage/configuration/suffixes``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example suffix
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "Sfx", "="]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Configuration_get_suffixes_return.schema 
        """
        return self.call("GET", "/orders-storage/configuration/suffixes", query=kwargs)

    def set_suffix(self, suffix: dict):
        """Create new suffix

        ``POST /orders-storage/configuration/suffixes``

        Args:
            suffix (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created suffix item

        Schema:

            .. literalinclude:: ../files/Configuration_set_suffix_request.schema
        """
        return self.call("POST", "/orders-storage/configuration/suffixes", data=suffix)

    def get_suffix(self, suffixesId: str):
        """Retrieve suffix item with given {suffixId}

        ``GET /orders-storage/configuration/suffixes/{suffixesId}``

        Args:
            suffixesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Configuration_get_suffix_return.schema 
        """
        return self.call("GET", f"/orders-storage/configuration/suffixes/{suffixesId}")

    def delete_suffix(self, suffixesId: str):
        """Delete suffix item with given {suffixId}

        ``DELETE /orders-storage/configuration/suffixes/{suffixesId}``

        Args:
            suffixesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders-storage/configuration/suffixes/{suffixesId}")

    def modify_suffix(self, suffixesId: str, suffix: dict):
        """Update suffix

        ``PUT /orders-storage/configuration/suffixes/{suffixesId}``

        Args:
            suffixesId (str)
            suffix (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Configuration_modify_suffix_request.schema
        """
        return self.call("PUT", f"/orders-storage/configuration/suffixes/{suffixesId}", data=suffix)


class OrderLines(FolioApi):
    """Order-lines

    **API to get list of po lines by quering a view combining purchase_orders,po_lines. This API is intended for internal use only.  Please use the /orders/order-lines API provided by mod-orders instead.**
    """

    def get_orderLines(self, **kwargs):
        """Get list of po lines matching a query that can contain fields from purchase_order or/and po_line

        ``GET /orders-storage/order-lines``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/OrderLines_get_orderLines_return.schema 
        """
        return self.call("GET", "/orders-storage/order-lines", query=kwargs)


class ReportingCode(FolioApi):
    """Reporting Code

    **CRUD APIs used to manage reporting codes.**
    """

    def get_reportingCodes(self, **kwargs):
        """Get list of reporting Codes

        ``GET /orders-storage/reporting-codes``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ReportingCode_get_reportingCodes_return.schema 
        """
        return self.call("GET", "/orders-storage/reporting-codes", query=kwargs)

    def set_reportingCode(self, reportingCode: dict):
        """Create a new reportingCode item.

        ``POST /orders-storage/reporting-codes``

        Args:
            reportingCode (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created reportingCode item

        Schema:

            .. literalinclude:: ../files/ReportingCode_set_reportingCode_request.schema
        """
        return self.call("POST", "/orders-storage/reporting-codes", data=reportingCode)

    def get_reportingCode(self, reportingCodesId: str):
        """Retrieve reportingCode item with given {reportingCodeId}

        ``GET /orders-storage/reporting-codes/{reportingCodesId}``

        Args:
            reportingCodesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ReportingCode_get_reportingCode_return.schema 
        """
        return self.call("GET", f"/orders-storage/reporting-codes/{reportingCodesId}")

    def delete_reportingCode(self, reportingCodesId: str):
        """Delete reportingCode item with given {reportingCodeId}

        ``DELETE /orders-storage/reporting-codes/{reportingCodesId}``

        Args:
            reportingCodesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders-storage/reporting-codes/{reportingCodesId}")

    def modify_reportingCode(self, reportingCodesId: str, reportingCode: dict):
        """Update reportingCode item with given {reportingCodeId}

        ``PUT /orders-storage/reporting-codes/{reportingCodesId}``

        Args:
            reportingCodesId (str)
            reportingCode (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ReportingCode_modify_reportingCode_request.schema
        """
        return self.call("PUT", f"/orders-storage/reporting-codes/{reportingCodesId}", data=reportingCode)


class Orders(FolioApi):
    """Orders

    **Get list of purchase orders API.  This API is intended for internal use only.  Please use the /orders/composite-orders API provided by mod-orders instead.**
    """

    def get_orders(self, **kwargs):
        """Get list of purchase orders

        ``GET /orders-storage/orders``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Orders_get_orders_return.schema 
        """
        return self.call("GET", "/orders-storage/orders", query=kwargs)


class Titles(FolioApi):
    """Titles

    **CRUD API to manage Titles.  This API is intended for internal use only.  Please use the /orders/titles, /orders/receiving, /orders/check-in, and /orders/receiving-history APIs provided by mod-orders instead.**
    """

    def get_titles(self, **kwargs):
        """Get list of titles

        ``GET /orders-storage/titles``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example title
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["title", "TITLE", "="]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Titles_get_titles_return.schema 
        """
        return self.call("GET", "/orders-storage/titles", query=kwargs)

    def set_title(self, title: dict):
        """Create a new title item.

        ``POST /orders-storage/titles``

        Args:
            title (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created title item

        Schema:

            .. literalinclude:: ../files/Titles_set_title_request.schema
        """
        return self.call("POST", "/orders-storage/titles", data=title)

    def get_title(self, titlesId: str):
        """Retrieve title item with given {titleId}

        ``GET /orders-storage/titles/{titlesId}``

        Args:
            titlesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Titles_get_title_return.schema 
        """
        return self.call("GET", f"/orders-storage/titles/{titlesId}")

    def delete_title(self, titlesId: str):
        """Delete title item with given {titleId}

        ``DELETE /orders-storage/titles/{titlesId}``

        Args:
            titlesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders-storage/titles/{titlesId}")

    def modify_title(self, titlesId: str, title: dict):
        """Update title item with given {titleId}

        ``PUT /orders-storage/titles/{titlesId}``

        Args:
            titlesId (str)
            title (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Titles_modify_title_request.schema
        """
        return self.call("PUT", f"/orders-storage/titles/{titlesId}", data=title)


class OrderInvoiceRelns(FolioApi):
    """Order relationship

    **CRUD APIs used to manage relationship between order and invoice.**
    """

    def get_orderInvoiceRelns(self, **kwargs):
        """Get list of relationships

        ``GET /orders-storage/order-invoice-relns``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example purchaseOrderId
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["purchaseOrderId", "55b97a4a-6601-4488-84e1-8b0d47a3f523"]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/OrderInvoiceRelns_get_orderInvoiceRelns_return.schema 
        """
        return self.call("GET", "/orders-storage/order-invoice-relns", query=kwargs)

    def set_orderInvoiceReln(self, orderInvoiceReln: dict):
        """Create a new orderInvoiceReln item.

        ``POST /orders-storage/order-invoice-relns``

        Args:
            orderInvoiceReln (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created orderInvoiceReln item

        Schema:

            .. literalinclude:: ../files/OrderInvoiceRelns_set_orderInvoiceReln_request.schema
        """
        return self.call("POST", "/orders-storage/order-invoice-relns", data=orderInvoiceReln)

    def get_orderInvoiceReln(self, orderInvoiceRelnsId: str):
        """Retrieve orderInvoiceReln item with given {orderInvoiceRelnId}

        ``GET /orders-storage/order-invoice-relns/{orderInvoiceRelnsId}``

        Args:
            orderInvoiceRelnsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/OrderInvoiceRelns_get_orderInvoiceReln_return.schema 
        """
        return self.call("GET", f"/orders-storage/order-invoice-relns/{orderInvoiceRelnsId}")

    def delete_orderInvoiceReln(self, orderInvoiceRelnsId: str):
        """Delete orderInvoiceReln item with given {orderInvoiceRelnId}

        ``DELETE /orders-storage/order-invoice-relns/{orderInvoiceRelnsId}``

        Args:
            orderInvoiceRelnsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders-storage/order-invoice-relns/{orderInvoiceRelnsId}")

    def modify_orderInvoiceReln(self, orderInvoiceRelnsId: str, orderInvoiceReln: dict):
        """Update orderInvoiceReln item with given {orderInvoiceRelnId}

        ``PUT /orders-storage/order-invoice-relns/{orderInvoiceRelnsId}``

        Args:
            orderInvoiceRelnsId (str)
            orderInvoiceReln (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/OrderInvoiceRelns_modify_orderInvoiceReln_request.schema
        """
        return self.call("PUT", f"/orders-storage/order-invoice-relns/{orderInvoiceRelnsId}", data=orderInvoiceReln)


class Pieces(FolioApi):
    """Pieces

    **CRUD API to manage Pieces.  This API is intended for internal use only.  Please use the /orders/pieces, /orders/receiving, /orders/check-in, and /orders/receiving-history APIs provided by mod-orders instead.**
    """

    def get_pieces(self, **kwargs):
        """Get list of pieces

        ``GET /orders-storage/pieces``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Pieces_get_pieces_return.schema 
        """
        return self.call("GET", "/orders-storage/pieces", query=kwargs)

    def set_piece(self, piece: dict):
        """Create a new piece item.

        ``POST /orders-storage/pieces``

        Args:
            piece (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created piece item

        Schema:

            .. literalinclude:: ../files/Pieces_set_piece_request.schema
        """
        return self.call("POST", "/orders-storage/pieces", data=piece)

    def get_piece(self, piecesId: str):
        """Retrieve piece item with given {pieceId}

        ``GET /orders-storage/pieces/{piecesId}``

        Args:
            piecesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Pieces_get_piece_return.schema 
        """
        return self.call("GET", f"/orders-storage/pieces/{piecesId}")

    def delete_piece(self, piecesId: str):
        """Delete piece item with given {pieceId}

        ``DELETE /orders-storage/pieces/{piecesId}``

        Args:
            piecesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders-storage/pieces/{piecesId}")

    def modify_piece(self, piecesId: str, piece: dict):
        """Update piece item with given {pieceId}

        ``PUT /orders-storage/pieces/{piecesId}``

        Args:
            piecesId (str)
            piece (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Pieces_modify_piece_request.schema
        """
        return self.call("PUT", f"/orders-storage/pieces/{piecesId}", data=piece)


class PoNumber(FolioApi):
    """Purchase Order Number

    **API used to manage PO number.  This API is intended for internal use only.  Please use the /orders/po-number API provided by mod-orders instead.**
    """

    def get_poNumbers(self, **kwargs):
        """Get generated purchase order number

        ``GET /orders-storage/po-number``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PoNumber_get_poNumbers_return.schema 
        """
        return self.call("GET", "/orders-storage/po-number", query=kwargs)
