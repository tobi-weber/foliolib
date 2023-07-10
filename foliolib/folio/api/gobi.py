# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.gobi")


class GobiMappings(FolioApi):
    """GOBI® (Global Online Bibliographic Information) Integration

    GOBI® (Global Online Bibliographic Information) is the leading web-based
		acquisitions tool for finding, ordering and managing e-books and print
		books for libraries. This module allows GOBI initiated orders to be
		fulfilled by FOLIO.
    """

    def get_fields(self):
        """Get list of Folio fields

        ``GET /gobi/orders/mappings/fields``

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/GobiMappings_get_fields_return.schema 
        """
        return self.call("GET", "/gobi/orders/mappings/fields")

    def get_translators(self):
        """Get list of Gobi fields to Folio fields translators

        ``GET /gobi/orders/mappings/translators``

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/GobiMappings_get_translators_return.schema 
        """
        return self.call("GET", "/gobi/orders/mappings/translators")

    def get_types(self):
        """Get list of types of the GOBI order

        ``GET /gobi/orders/mappings/types``

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/GobiMappings_get_types_return.schema 
        """
        return self.call("GET", "/gobi/orders/mappings/types")


class GobiCustomMappings(FolioApi):
    """GOBI® (Global Online Bibliographic Information) Integration

    GOBI® (Global Online Bibliographic Information) is the leading web-based
		acquisitions tool for finding, ordering and managing e-books and print
		books for libraries. This module allows GOBI initiated orders to be
		fulfilled by FOLIO.
    """

    def get_customMappings(self, **kwargs):
        """Get list of acquisition methods

        ``GET /gobi/orders/custom-mappings``

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

            .. literalinclude:: ../files/GobiCustomMappings_get_customMappings_return.schema 
        """
        return self.call("GET", "/gobi/orders/custom-mappings", query=kwargs)

    def set_customMapping(self, customMapping: dict):
        """Create a new customMapping item.

        ``POST /gobi/orders/custom-mappings``

        Args:
            customMapping (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created customMapping item

        Schema:

            .. literalinclude:: ../files/GobiCustomMappings_set_customMapping_request.schema
        """
        return self.call("POST", "/gobi/orders/custom-mappings", data=customMapping)

    def get_customMapping(self, orderType: str):
        """Retrieve customMapping item with given {customMappingId}

        ``GET /gobi/orders/custom-mappings/{orderType}``

        Args:
            orderType (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/GobiCustomMappings_get_customMapping_return.schema 
        """
        return self.call("GET", f"/gobi/orders/custom-mappings/{orderType}")

    def delete_customMapping(self, orderType: str):
        """Delete customMapping item with given {customMappingId}

        ``DELETE /gobi/orders/custom-mappings/{orderType}``

        Args:
            orderType (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/gobi/orders/custom-mappings/{orderType}")

    def modify_customMapping(self, orderType: str, customMapping: dict):
        """Update customMapping item with given {customMappingId}

        ``PUT /gobi/orders/custom-mappings/{orderType}``

        Args:
            orderType (str)
            customMapping (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/GobiCustomMappings_modify_customMapping_request.schema
        """
        return self.call("PUT", f"/gobi/orders/custom-mappings/{orderType}", data=customMapping)


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
