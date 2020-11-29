# -*- coding: utf-8 -*-
# Generated at 2020-11-29

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.orders")


class AcquisitionsUnits(FolioApi):
    """Acquisitions units

    **CRUD APIs used to manage acquisitions units.**
    """

    def get_units(self, **kwargs):
        """Get list of acquisitions units. In case client does not specify search criteria by "isDeleted" property, the logic will search for records with "isDeleted==false"

        ``GET /acquisitions-units/units``

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

            .. literalinclude:: ../files/AcquisitionsUnits_get_units_return.schema 
        """
        return self.call("GET", "/acquisitions-units/units", query=kwargs)

    def set_unit(self, unit: dict):
        """Create new acquisitions unit

        ``POST /acquisitions-units/units``

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

            .. literalinclude:: ../files/AcquisitionsUnits_set_unit_request.schema
        """
        return self.call("POST", "/acquisitions-units/units", data=unit)

    def get_unit(self, unitsId: str):
        """Retrieve unit item with given {unitId}

        ``GET /acquisitions-units/units/{unitsId}``

        Args:
            unitsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AcquisitionsUnits_get_unit_return.schema 
        """
        return self.call("GET", f"/acquisitions-units/units/{unitsId}")

    def delete_unit(self, unitsId: str):
        """In order to avoid reference integrity issues when deleting acquisition units that are assigned to records, the logic implements a "soft delete". Update acquisitions unit setting the "isDeleted" field to true

        ``DELETE /acquisitions-units/units/{unitsId}``

        Args:
            unitsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/acquisitions-units/units/{unitsId}")

    def modify_unit(self, unitsId: str, unit: dict):
        """Update acquisitions unit

        ``PUT /acquisitions-units/units/{unitsId}``

        Args:
            unitsId (str)
            unit (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AcquisitionsUnits_modify_unit_request.schema
        """
        return self.call("PUT", f"/acquisitions-units/units/{unitsId}", data=unit)

    def get_memberships(self, **kwargs):
        """Get list of acquisitions units memberships

        ``GET /acquisitions-units/memberships``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example acquisitionsUnitId
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["acquisitionsUnitId", "57c35c88-625d-4f0e-bc79-d22818d84d1c"]
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

            .. literalinclude:: ../files/AcquisitionsUnits_get_memberships_return.schema 
        """
        return self.call("GET", "/acquisitions-units/memberships", query=kwargs)

    def set_membership(self, membership: dict):
        """Create new acquisitions units membership

        ``POST /acquisitions-units/memberships``

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

            .. literalinclude:: ../files/AcquisitionsUnits_set_membership_request.schema
        """
        return self.call("POST", "/acquisitions-units/memberships", data=membership)

    def get_membership(self, membershipsId: str):
        """Retrieve membership item with given {membershipId}

        ``GET /acquisitions-units/memberships/{membershipsId}``

        Args:
            membershipsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AcquisitionsUnits_get_membership_return.schema 
        """
        return self.call("GET", f"/acquisitions-units/memberships/{membershipsId}")

    def delete_membership(self, membershipsId: str):
        """In order to avoid reference integrity issues when deleting acquisition units that are assigned to records, the logic implements a "soft delete". Update acquisitions unit setting the "isDeleted" field to true

        ``DELETE /acquisitions-units/memberships/{membershipsId}``

        Args:
            membershipsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/acquisitions-units/memberships/{membershipsId}")

    def modify_membership(self, membershipsId: str, membership: dict):
        """Update acquisitions units membership

        ``PUT /acquisitions-units/memberships/{membershipsId}``

        Args:
            membershipsId (str)
            membership (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AcquisitionsUnits_modify_membership_request.schema
        """
        return self.call("PUT", f"/acquisitions-units/memberships/{membershipsId}", data=membership)


class Order(FolioApi):
    """Orders Business Logic API

    **API for managing purchase orders**
    """

    def get_compositeOrders(self, **kwargs):
        """Retrieve a list of compositeOrder items.

        ``GET /orders/composite-orders``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    using CQL (indexes for purchase orders)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - workflow_status=="Pending"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Order_get_compositeOrders_return.schema 
        """
        return self.call("GET", "/orders/composite-orders", query=kwargs)

    def set_compositeOrder(self, compositeOrder: dict):
        """Post a purchase order (PO) and a number of PO lines; record fund transactions corresponding to the order. Only in case an acquisition unit has to be assigned to the Order it is required that user should have extra permission orders.acquisitions-units-assignments.item.post to create an purchase order.

        ``POST /orders/composite-orders``

        Args:
            compositeOrder (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created compositeOrder item

        Schema:

            .. literalinclude:: ../files/Order_set_compositeOrder_request.schema
        """
        return self.call("POST", "/orders/composite-orders", data=compositeOrder)

    def get_compositeOrder(self, compositeOrdersId: str):
        """Return a purchase order with given {id}

        ``GET /orders/composite-orders/{compositeOrdersId}``

        Args:
            compositeOrdersId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Order_get_compositeOrder_return.schema 
        """
        return self.call("GET", f"/orders/composite-orders/{compositeOrdersId}")

    def delete_compositeOrder(self, compositeOrdersId: str):
        """Delete a purchase order with given {id}

        ``DELETE /orders/composite-orders/{compositeOrdersId}``

        Args:
            compositeOrdersId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders/composite-orders/{compositeOrdersId}")

    def modify_compositeOrder(self, compositeOrdersId: str, compositeOrder: dict):
        """Update a purchase order with given {id}
        - if request does not include po_lines or includes "po_lines": [] or "po_lines": null - update just purchase order summary
        - if request includes array of "po_lines" - update PO lines as per request

        ``PUT /orders/composite-orders/{compositeOrdersId}``

        Args:
            compositeOrdersId (str)
            compositeOrder (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Order_modify_compositeOrder_request.schema
        """
        return self.call("PUT", f"/orders/composite-orders/{compositeOrdersId}", data=compositeOrder)

    def get_orderLines(self, **kwargs):
        """Retrieve a list of orderLine items.

        ``GET /orders/order-lines``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    using CQL (indexes for PO lines)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - payment_status=="Cancelled"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Order_get_orderLines_return.schema 
        """
        return self.call("GET", "/orders/order-lines", query=kwargs)

    def set_orderLine(self, orderLine: dict):
        """Post a PO lines to corresponding PO

        ``POST /orders/order-lines``

        Args:
            orderLine (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created orderLine item

        Schema:

            .. literalinclude:: ../files/Order_set_orderLine_request.schema
        """
        return self.call("POST", "/orders/order-lines", data=orderLine)

    def get_orderLine(self, orderLinesId: str):
        """Return a purchase order line with given {id}

        ``GET /orders/order-lines/{orderLinesId}``

        Args:
            orderLinesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Order_get_orderLine_return.schema 
        """
        return self.call("GET", f"/orders/order-lines/{orderLinesId}")

    def delete_orderLine(self, orderLinesId: str):
        """Delete a purchase order line with given {id}

        ``DELETE /orders/order-lines/{orderLinesId}``

        Args:
            orderLinesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders/order-lines/{orderLinesId}")

    def modify_orderLine(self, orderLinesId: str, orderLine: dict):
        """Update a purchase order line with given {id}

        ``PUT /orders/order-lines/{orderLinesId}``

        Args:
            orderLinesId (str)
            orderLine (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Order_modify_orderLine_request.schema
        """
        return self.call("PUT", f"/orders/order-lines/{orderLinesId}", data=orderLine)

    def get_poNumbers(self, **kwargs):
        """Get generated PO number

        ``GET /orders/po-number``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Order_get_poNumbers_return.schema 
        """
        return self.call("GET", "/orders/po-number", query=kwargs)

    def set_validate(self, validate: dict, **kwargs):
        """validate if the PO Number is unique and matches the pattern specified

        ``POST /orders/po-number/validate``

        Args:
            validate (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Order_set_validate_request.schema
        """
        return self.call("POST", "/orders/po-number/validate", data=validate, query=kwargs)

    def set_receive(self, receive: dict):
        """Receive items spanning one or more PO lines

        ``POST /orders/receive``

        Args:
            receive (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Order_set_receive_request.schema
            .. literalinclude:: ../files/Order_set_receive_return.schema 
        """
        return self.call("POST", "/orders/receive", data=receive)

    def set_checkIn(self, checkIn: dict):
        """Check-in items spanning one or more po_lines in this order

        ``POST /orders/check-in``

        Args:
            checkIn (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Order_set_checkIn_request.schema
            .. literalinclude:: ../files/Order_set_checkIn_return.schema 
        """
        return self.call("POST", "/orders/check-in", data=checkIn)

    def get_receivingHistories(self, **kwargs):
        """Get receiving history matching the provided criteria

        ``GET /orders/receiving-history``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    With valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - titleOrPackage==Harry Potter AND receiving_status==received sortBy po_line_number

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Order_get_receivingHistories_return.schema 
        """
        return self.call("GET", "/orders/receiving-history", query=kwargs)

    def set_piece(self, piece: dict):
        """Create piece record

        ``POST /orders/pieces``

        Args:
            piece (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Order_set_piece_request.schema
        """
        return self.call("POST", "/orders/pieces", data=piece)

    def modify_piece(self, piecesId: str, piece: dict):
        """Update a piece record with given {id}

        ``PUT /orders/pieces/{piecesId}``

        Args:
            piecesId (str)
            piece (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Order_modify_piece_request.schema
        """
        return self.call("PUT", f"/orders/pieces/{piecesId}", data=piece)

    def delete_piece(self, piecesId: str):
        """Delete a piece with given {id}

        ``DELETE /orders/pieces/{piecesId}``

        Args:
            piecesId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders/pieces/{piecesId}")

    def get_orderTemplates(self, **kwargs):
        """Get list of order templates

        ``GET /orders/order-templates``

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

            .. literalinclude:: ../files/Order_get_orderTemplates_return.schema 
        """
        return self.call("GET", "/orders/order-templates", query=kwargs)

    def set_orderTemplate(self, orderTemplate: dict):
        """Create new order template

        ``POST /orders/order-templates``

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

            .. literalinclude:: ../files/Order_set_orderTemplate_request.schema
        """
        return self.call("POST", "/orders/order-templates", data=orderTemplate)

    def get_orderTemplate(self, orderTemplatesId: str):
        """Return a purchase order line with given {id}

        ``GET /orders/order-templates/{orderTemplatesId}``

        Args:
            orderTemplatesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Order_get_orderTemplate_return.schema 
        """
        return self.call("GET", f"/orders/order-templates/{orderTemplatesId}")

    def delete_orderTemplate(self, orderTemplatesId: str):
        """Delete a purchase order line with given {id}

        ``DELETE /orders/order-templates/{orderTemplatesId}``

        Args:
            orderTemplatesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders/order-templates/{orderTemplatesId}")

    def modify_orderTemplate(self, orderTemplatesId: str, orderTemplate: dict):
        """Update order template

        ``PUT /orders/order-templates/{orderTemplatesId}``

        Args:
            orderTemplatesId (str)
            orderTemplate (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Order_modify_orderTemplate_request.schema
        """
        return self.call("PUT", f"/orders/order-templates/{orderTemplatesId}", data=orderTemplate)


class Configuration(FolioApi):
    """Orders configuration

    **API for managing purchase orders configuration**
    """

    def get_reasonsForClosures(self, **kwargs):
        """Get list of reasons for closure

        ``GET /orders/configuration/reasons-for-closure``

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
        return self.call("GET", "/orders/configuration/reasons-for-closure", query=kwargs)

    def set_reasonsForClosure(self, reasonsForClosure: dict):
        """Create new reason for closure

        ``POST /orders/configuration/reasons-for-closure``

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
        return self.call("POST", "/orders/configuration/reasons-for-closure", data=reasonsForClosure)

    def get_reasonsForClosure(self, reasonsForClosureId: str):
        """Retrieve reasonsForClosure item with given {reasonsForClosureId}

        ``GET /orders/configuration/reasons-for-closure/{reasonsForClosureId}``

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
        return self.call("GET", f"/orders/configuration/reasons-for-closure/{reasonsForClosureId}")

    def delete_reasonsForClosure(self, reasonsForClosureId: str):
        """Delete reasonsForClosure item with given {reasonsForClosureId}

        ``DELETE /orders/configuration/reasons-for-closure/{reasonsForClosureId}``

        Args:
            reasonsForClosureId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders/configuration/reasons-for-closure/{reasonsForClosureId}")

    def modify_reasonsForClosure(self, reasonsForClosureId: str, reasonsForClosure: dict):
        """Update reason for closure

        ``PUT /orders/configuration/reasons-for-closure/{reasonsForClosureId}``

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
        return self.call("PUT", f"/orders/configuration/reasons-for-closure/{reasonsForClosureId}", data=reasonsForClosure)

    def get_prefixes(self, **kwargs):
        """Get list of prefixes

        ``GET /orders/configuration/prefixes``

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
        return self.call("GET", "/orders/configuration/prefixes", query=kwargs)

    def set_prefix(self, prefix: dict):
        """Create new prefix

        ``POST /orders/configuration/prefixes``

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
        return self.call("POST", "/orders/configuration/prefixes", data=prefix)

    def get_prefix(self, prefixesId: str):
        """Retrieve prefix item with given {prefixId}

        ``GET /orders/configuration/prefixes/{prefixesId}``

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
        return self.call("GET", f"/orders/configuration/prefixes/{prefixesId}")

    def delete_prefix(self, prefixesId: str):
        """Delete prefix item with given {prefixId}

        ``DELETE /orders/configuration/prefixes/{prefixesId}``

        Args:
            prefixesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders/configuration/prefixes/{prefixesId}")

    def modify_prefix(self, prefixesId: str, prefix: dict):
        """Update prefix

        ``PUT /orders/configuration/prefixes/{prefixesId}``

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
        return self.call("PUT", f"/orders/configuration/prefixes/{prefixesId}", data=prefix)

    def get_suffixes(self, **kwargs):
        """Get list of suffixes

        ``GET /orders/configuration/suffixes``

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
        return self.call("GET", "/orders/configuration/suffixes", query=kwargs)

    def set_suffix(self, suffix: dict):
        """Create new suffix

        ``POST /orders/configuration/suffixes``

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
        return self.call("POST", "/orders/configuration/suffixes", data=suffix)

    def get_suffix(self, suffixesId: str):
        """Retrieve suffix item with given {suffixId}

        ``GET /orders/configuration/suffixes/{suffixesId}``

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
        return self.call("GET", f"/orders/configuration/suffixes/{suffixesId}")

    def delete_suffix(self, suffixesId: str):
        """Delete suffix item with given {suffixId}

        ``DELETE /orders/configuration/suffixes/{suffixesId}``

        Args:
            suffixesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders/configuration/suffixes/{suffixesId}")

    def modify_suffix(self, suffixesId: str, suffix: dict):
        """Update suffix

        ``PUT /orders/configuration/suffixes/{suffixesId}``

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
        return self.call("PUT", f"/orders/configuration/suffixes/{suffixesId}", data=suffix)


class Titles(FolioApi):
    """Titles

    **CRUD API to manage Titles.**
    """

    def get_titles(self, **kwargs):
        """Get list of titles

        ``GET /orders/titles``

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
        return self.call("GET", "/orders/titles", query=kwargs)

    def set_title(self, title: dict):
        """Create a new title item.

        ``POST /orders/titles``

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
        return self.call("POST", "/orders/titles", data=title)

    def get_title(self, titlesId: str):
        """Retrieve title item with given {titleId}

        ``GET /orders/titles/{titlesId}``

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
        return self.call("GET", f"/orders/titles/{titlesId}")

    def delete_title(self, titlesId: str):
        """Delete title item with given {titleId}

        ``DELETE /orders/titles/{titlesId}``

        Args:
            titlesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders/titles/{titlesId}")

    def modify_title(self, titlesId: str, title: dict):
        """Update title item with given {titleId}

        ``PUT /orders/titles/{titlesId}``

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
        return self.call("PUT", f"/orders/titles/{titlesId}", data=title)
