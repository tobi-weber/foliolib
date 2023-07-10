# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.folioCustomFields")


class CustomFields(FolioApi):
    """folio-custom-fields, a library and common interface for custom fields to be used by several modules

    FOLIO module library to store and maintain custom fields using Okapi's multiple interfaces feature.
		All modules that use this library share the CRUD interface POST/PUT/GET/DELETE on /custom-fields and /custom-fields/$id endpoints.
		The client must set the X-Okapi-Module-Id header, for details see
		[Okapi multiples interfaces documentation](https://github.com/folio-org/okapi/blob/master/doc/guide.md#multiple-interfaces),
		[folio-custom-fields introduction](https://github.com/folio-org/folio-custom-fields#introduction), and
		[Custom Field backend demo](https://wiki.folio.org/pages/viewpage.action?spaceKey=FOLIJET&title=MODCFIELDS-39+-+Custom+Field+backend+demo).
    """

    def get_customFields(self, **kwargs):
        """Retrieve a list of customField items.

        ``GET /custom-fields``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    Query should contain custom field attributes
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=department
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
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/CustomFields_get_customFields_return.schema 
        """
        return self.call("GET", "/custom-fields", query=kwargs)

    def set_customField(self, customField: dict):
        """Create a new customField item.

        ``POST /custom-fields``

        Args:
            customField (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created customField item

        Schema:

            .. literalinclude:: ../files/CustomFields_set_customField_request.schema
        """
        return self.call("POST", "/custom-fields", data=customField)

    def modify_customField(self):
        """

        ``PUT /custom-fields``
        """
        return self.call("PUT", "/custom-fields")

    def get_customField(self, customFieldsId: str):
        """Retrieve customField item with given {customFieldId}

        ``GET /custom-fields/{customFieldsId}``

        Args:
            customFieldsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CustomFields_get_customField_return.schema 
        """
        return self.call("GET", f"/custom-fields/{customFieldsId}")

    def delete_customField(self, customFieldsId: str):
        """Delete customField item with given {customFieldId}

        ``DELETE /custom-fields/{customFieldsId}``

        Args:
            customFieldsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/custom-fields/{customFieldsId}")

    def modify_customField_by_customFieldsId(self, customFieldsId: str, customField: dict):
        """Update customField item with given {customFieldId}

        ``PUT /custom-fields/{customFieldsId}``

        Args:
            customFieldsId (str)
            customField (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CustomFields_modify_customField_by_customFieldsId_request.schema
        """
        return self.call("PUT", f"/custom-fields/{customFieldsId}", data=customField)

    def get_stats_by_customField(self, customFieldsId: str, **kwargs):
        """Returns usage statistic of custom field with the given id

        ``GET /custom-fields/{customFieldsId}/stats``

        Args:
            customFieldsId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CustomFields_get_stats_by_customField_return.schema 
        """
        return self.call("GET", f"/custom-fields/{customFieldsId}/stats", query=kwargs)

    def get_stats_by_customField_by_customFieldsId(self, customFieldsId: str, optId: str):
        """Returns usage statistic of custom field option with the given optId

        ``GET /custom-fields/{customFieldsId}/options/{optId}/stats``

        Args:
            customFieldsId (str)
            optId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CustomFields_get_stats_by_customField_by_customFieldsId_return.schema 
        """
        return self.call("GET", f"/custom-fields/{customFieldsId}/options/{optId}/stats")
