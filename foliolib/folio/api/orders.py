# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.orders")


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
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestConflict: Conflict
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
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AcquisitionsUnits_modify_membership_request.schema
        """
        return self.call("PUT", f"/acquisitions-units/memberships/{membershipsId}", data=membership)


class HoldingSummary(FolioApi):
    """Holding summaries

    **CRUD API to manage Holding summaries.**
    """

    def get_holdingSummaries(self, holdingSummaryId: str):
        """Retrieve a list of holdingSummary items.

        ``GET /orders/holding-summary/{holdingSummaryId}``

        Args:
            holdingSummaryId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/HoldingSummary_get_holdingSummaries_return.schema 
        """
        return self.call("GET", f"/orders/holding-summary/{holdingSummaryId}")


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
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestConflict: Conflict
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
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestConflict: Conflict
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
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Configuration_modify_suffix_request.schema
        """
        return self.call("PUT", f"/orders/configuration/suffixes/{suffixesId}", data=suffix)


class OrderLines(FolioApi):
    """Orders Business Logic API

    **API for managing purchase orders**
    """

    def get_orderLines(self, **kwargs):
        """Retrieve a list of orderLine items.

        ``GET /orders/order-lines``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/OrderLines_get_orderLines_return.schema 
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

            .. literalinclude:: ../files/OrderLines_set_orderLine_request.schema
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

            .. literalinclude:: ../files/OrderLines_get_orderLine_return.schema 
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

            .. literalinclude:: ../files/OrderLines_modify_orderLine_request.schema
        """
        return self.call("PUT", f"/orders/order-lines/{orderLinesId}", data=orderLine)

    def modify_validate(self, validate: dict):
        """Validate is cost amount equals to sum of all fund distributions

        ``PUT /orders/order-lines/fund-distributions/validate``

        Args:
            validate (dict): See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/OrderLines_modify_validate_request.schema
        """
        return self.call("PUT", "/orders/order-lines/fund-distributions/validate", data=validate)


class Pieces(FolioApi):
    """Orders Business Logic API

    **API for managing pieces**
    """

    def get_pieces(self, **kwargs):
        """Retrieve a list of piece items.

        ``GET /orders/pieces``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
                    
                    using CQL (indexes for piece records)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - format=="Physical"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Pieces_get_pieces_return.schema 
        """
        return self.call("GET", "/orders/pieces", query=kwargs)

    def set_piece(self, piece: dict):
        """Create piece record

        ``POST /orders/pieces``

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
        return self.call("POST", "/orders/pieces", data=piece)

    def get_piece(self, piecesId: str):
        """Return a piece record with given {id}

        ``GET /orders/pieces/{piecesId}``

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
        return self.call("GET", f"/orders/pieces/{piecesId}")

    def delete_piece(self, piecesId: str):
        """Delete a piece with given {id}

        ``DELETE /orders/pieces/{piecesId}``

        Args:
            piecesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders/pieces/{piecesId}")

    def modify_piece(self, piecesId: str, piece: dict):
        """Update a piece record with given {id}

        ``PUT /orders/pieces/{piecesId}``

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
        return self.call("PUT", f"/orders/pieces/{piecesId}", data=piece)


class ReceivingHistory(FolioApi):
    """Orders Business Logic API

    **API for retriving receiving history**
    """

    def get_receivingHistories(self, **kwargs):
        """Get receiving history matching the provided criteria

        ``GET /orders/receiving-history``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/ReceivingHistory_get_receivingHistories_return.schema 
        """
        return self.call("GET", "/orders/receiving-history", query=kwargs)


class CheckIn(FolioApi):
    """Orders Business Logic API

    **API for checking-in pieces**
    """

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

            .. literalinclude:: ../files/CheckIn_set_checkIn_request.schema
            .. literalinclude:: ../files/CheckIn_set_checkIn_return.schema 
        """
        return self.call("POST", "/orders/check-in", data=checkIn)


class Receive(FolioApi):
    """Orders Business Logic API

    **API for receiving pieces**
    """

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

            .. literalinclude:: ../files/Receive_set_receive_request.schema
            .. literalinclude:: ../files/Receive_set_receive_return.schema 
        """
        return self.call("POST", "/orders/receive", data=receive)


class Rollover(FolioApi):
    """Orders Business Logic API

    **API for running Orders rollover**
    """

    def set_rollover(self, rollover: dict):
        """

        ``POST /orders/rollover``

        Args:
            rollover (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Rollover_set_rollover_request.schema
        """
        return self.call("POST", "/orders/rollover", data=rollover)


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
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

    def set_reEncumber(self, compositeOrdersId: str):
        """

        ``POST /orders/composite-orders/{compositeOrdersId}/re-encumber``

        Args:
            compositeOrdersId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("POST", f"/orders/composite-orders/{compositeOrdersId}/re-encumber")


class ExportHistory(FolioApi):
    """Export history Logic API

    **API for managing export history**
    """

    def get_exportHistories(self, **kwargs):
        """Retrieve exportHistory item with given {exportHistoryId}

        ``GET /orders/export-history``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
                    
                    using CQL (indexes for export-history records)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - exportType=="EDIFACT_ORDERS_EXPORT"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ExportHistory_get_exportHistories_return.schema 
        """
        return self.call("GET", "/orders/export-history", query=kwargs)


class OrderTemplates(FolioApi):
    """Orders Business Logic API

    **API for managing order templates**
    """

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
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/OrderTemplates_set_orderTemplate_request.schema
        """
        return self.call("POST", "/orders/order-templates", data=orderTemplate)

    def get_orderTemplate(self, orderTemplatesId: str):
        """Retrieve orderTemplate item with given {orderTemplateId}

        ``GET /orders/order-templates/{orderTemplatesId}``

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
        return self.call("GET", f"/orders/order-templates/{orderTemplatesId}")

    def delete_orderTemplate(self, orderTemplatesId: str):
        """Delete orderTemplate item with given {orderTemplateId}

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

            .. literalinclude:: ../files/OrderTemplates_modify_orderTemplate_request.schema
        """
        return self.call("PUT", f"/orders/order-templates/{orderTemplatesId}", data=orderTemplate)


class AcquisitionMethod(FolioApi):
    """Acquisition method

    **CRUD APIs used to manage acquisition method.**
    """

    def get_acquisitionMethods(self, **kwargs):
        """Get list of acquisition methods

        ``GET /orders/acquisition-methods``

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
                    
                     - ["value", "Purchase At Vendor System", "="]
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/AcquisitionMethod_get_acquisitionMethods_return.schema 
        """
        return self.call("GET", "/orders/acquisition-methods", query=kwargs)

    def set_acquisitionMethod(self, acquisitionMethod: dict):
        """Create a new acquisitionMethod item.

        ``POST /orders/acquisition-methods``

        Args:
            acquisitionMethod (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created acquisitionMethod item

        Schema:

            .. literalinclude:: ../files/AcquisitionMethod_set_acquisitionMethod_request.schema
        """
        return self.call("POST", "/orders/acquisition-methods", data=acquisitionMethod)

    def get_acquisitionMethod(self, acquisitionMethodsId: str):
        """Retrieve acquisitionMethod item with given {acquisitionMethodId}

        ``GET /orders/acquisition-methods/{acquisitionMethodsId}``

        Args:
            acquisitionMethodsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AcquisitionMethod_get_acquisitionMethod_return.schema 
        """
        return self.call("GET", f"/orders/acquisition-methods/{acquisitionMethodsId}")

    def delete_acquisitionMethod(self, acquisitionMethodsId: str):
        """Delete acquisitionMethod item with given {acquisitionMethodId}

        ``DELETE /orders/acquisition-methods/{acquisitionMethodsId}``

        Args:
            acquisitionMethodsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/orders/acquisition-methods/{acquisitionMethodsId}")

    def modify_acquisitionMethod(self, acquisitionMethodsId: str, acquisitionMethod: dict):
        """Update acquisitionMethod item with given {acquisitionMethodId}

        ``PUT /orders/acquisition-methods/{acquisitionMethodsId}``

        Args:
            acquisitionMethodsId (str)
            acquisitionMethod (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AcquisitionMethod_modify_acquisitionMethod_request.schema
        """
        return self.call("PUT", f"/orders/acquisition-methods/{acquisitionMethodsId}", data=acquisitionMethod)


class PoNumber(FolioApi):
    """Orders Business Logic API

    **API for managing PO numbers**
    """

    def get_poNumbers(self):
        """Get generated PO number

        ``GET /orders/po-number``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/PoNumber_get_poNumbers_return.schema 
        """
        return self.call("GET", "/orders/po-number")

    def set_validate(self, validate: dict):
        """validate if the PO Number is unique and matches the pattern specified

        ``POST /orders/po-number/validate``

        Args:
            validate (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/PoNumber_set_validate_request.schema
        """
        return self.call("POST", "/orders/po-number/validate", data=validate)


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
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Titles_modify_title_request.schema
        """
        return self.call("PUT", f"/orders/titles/{titlesId}", data=title)
