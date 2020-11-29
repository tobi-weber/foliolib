# -*- coding: utf-8 -*-
# Generated at 2020-11-29

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.marccat")


class Marccat(FolioApi):
    """MARCcat API

    **This documents the API calls for interacting with an marc authority or bibliographic record**
    """

    def get_searches(self, **kwargs):
        """Return a list of marc records and search metadata

        ``GET /marccat/search``

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
                    
                    using CCL query in q parameter and choosing authority or bibliographic in view parameter
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - q=na "manzoni, alessandro"&view=1

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestError: Bad Request

        Schema:

            .. literalinclude:: ../files/Marccat_get_searches_return.schema 
        """
        return self.call("GET", "/marccat/search", query=kwargs)

    def delete_searches(self):
        """Delete search item with given {searchId}

        ``DELETE /marccat/search``

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", "/marccat/search")

    def modify_search(self, search: dict):
        """Update search item with given {searchId}

        ``PUT /marccat/search``

        Args:
            search (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Marccat_modify_search_request.schema
        """
        return self.call("PUT", "/marccat/search", data=search)

    def get_mergedSearches(self, **kwargs):
        """Return a list of marc records and search metadata

        ``GET /marccat/mergedSearch``

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
                    
                    using CCL query in q parameter
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - q=na "manzoni, alessandro"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Marccat_get_mergedSearches_return.schema 
        """
        return self.call("GET", "/marccat/mergedSearch", query=kwargs)

    def set_mergedSearch(self, mergedSearch: dict):
        """Create a new mergedSearch item.

        ``POST /marccat/mergedSearch``

        Args:
            mergedSearch (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created mergedSearch item

        Schema:

            .. literalinclude:: ../files/Marccat_set_mergedSearch_request.schema
        """
        return self.call("POST", "/marccat/mergedSearch", data=mergedSearch)

    def get_searchVerticals(self, **kwargs):
        """Return a list of marc records in text formats

        ``GET /marccat/searchVertical``

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
                    
                    using CCL query in q parameter and choosing authority or bibliographic in view parameter
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - q=na "manzoni, alessandro"&view=1

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestError: Bad Request

        Schema:

            .. literalinclude:: ../files/Marccat_get_searchVerticals_return.schema 
        """
        return self.call("GET", "/marccat/searchVertical", query=kwargs)

    def delete_searchVerticals(self):
        """Delete searchVertical item with given {searchVerticalId}

        ``DELETE /marccat/searchVertical``

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", "/marccat/searchVertical")

    def modify_searchVertical(self, searchVertical: dict):
        """Update searchVertical item with given {searchVerticalId}

        ``PUT /marccat/searchVertical``

        Args:
            searchVertical (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Marccat_modify_searchVertical_request.schema
        """
        return self.call("PUT", "/marccat/searchVertical", data=searchVertical)

    def get_searchAuths(self, **kwargs):
        """Return a list of marc authority records and search metadata

        ``GET /marccat/searchAuth``

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
                    
                    using CCL query in q parameter
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - q=na "giannini"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestError: Bad Request

        Schema:

            .. literalinclude:: ../files/Marccat_get_searchAuths_return.schema 
        """
        return self.call("GET", "/marccat/searchAuth", query=kwargs)

    def delete_searchAuths(self):
        """Delete searchAuth item with given {searchAuthId}

        ``DELETE /marccat/searchAuth``

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", "/marccat/searchAuth")

    def modify_searchAuth(self, searchAuth: dict):
        """Update searchAuth item with given {searchAuthId}

        ``PUT /marccat/searchAuth``

        Args:
            searchAuth (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Marccat_modify_searchAuth_request.schema
        """
        return self.call("PUT", "/marccat/searchAuth", data=searchAuth)

    def get_authorityRecords(self, **kwargs):
        """Return a list of marc authority records and search metadata

        ``GET /marccat/authority-record``

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
                    
                    using CCL query in q parameter
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - q=na "giannini"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestError: Bad Request

        Schema:

            .. literalinclude:: ../files/Marccat_get_authorityRecords_return.schema 
        """
        return self.call("GET", "/marccat/authority-record", query=kwargs)

    def delete_authorityRecords(self):
        """Delete authorityRecord item with given {authorityRecordId}

        ``DELETE /marccat/authority-record``

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", "/marccat/authority-record")

    def modify_authorityRecord(self, authorityRecord: dict):
        """Update authorityRecord item with given {authorityRecordId}

        ``PUT /marccat/authority-record``

        Args:
            authorityRecord (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Marccat_modify_authorityRecord_request.schema
        """
        return self.call("PUT", "/marccat/authority-record", data=authorityRecord)

    def set_authorityRecord(self):
        """Create authority record

        ``POST /marccat/authority-record``

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("POST", "/marccat/authority-record")

    def get_fromTemplate(self, idTemplate: str, **kwargs):
        """Return a list of marc authority records and search metadata

        ``GET /marccat/authority-record/from-template/{idTemplate}``

        Args:
            idTemplate (str)
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
                    
                    using CCL query in q parameter
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - q=na "giannini"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestError: Bad Request

        Schema:

            .. literalinclude:: ../files/Marccat_get_fromTemplate_return.schema 
        """
        return self.call("GET", f"/marccat/authority-record/from-template/{idTemplate}", query=kwargs)

    def delete_fromTemplate(self, idTemplate: str):
        """Delete fromTemplate item with given {fromTemplateId}

        ``DELETE /marccat/authority-record/from-template/{idTemplate}``

        Args:
            idTemplate (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/marccat/authority-record/from-template/{idTemplate}")

    def modify_fromTemplate(self, idTemplate: str, fromTemplate: dict):
        """Update fromTemplate item with given {fromTemplateId}

        ``PUT /marccat/authority-record/from-template/{idTemplate}``

        Args:
            idTemplate (str)
            fromTemplate (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Marccat_modify_fromTemplate_request.schema
        """
        return self.call("PUT", f"/marccat/authority-record/from-template/{idTemplate}", data=fromTemplate)

    def set_fromTemplate(self, idTemplate: str):
        """Get authority record template

        ``POST /marccat/authority-record/from-template/{idTemplate}``

        Args:
            idTemplate (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("POST", f"/marccat/authority-record/from-template/{idTemplate}")

    def get_fixedFieldDisplayValues(self, **kwargs):
        """Return a list of marc authority records and search metadata

        ``GET /marccat/authority-record/fixed-field-display-value``

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
                    
                    using CCL query in q parameter
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - q=na "giannini"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestError: Bad Request

        Schema:

            .. literalinclude:: ../files/Marccat_get_fixedFieldDisplayValues_return.schema 
        """
        return self.call("GET", "/marccat/authority-record/fixed-field-display-value", query=kwargs)

    def delete_fixedFieldDisplayValues(self):
        """Delete fixedFieldDisplayValue item with given {fixedFieldDisplayValueId}

        ``DELETE /marccat/authority-record/fixed-field-display-value``

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", "/marccat/authority-record/fixed-field-display-value")

    def modify_fixedFieldDisplayValue(self, fixedFieldDisplayValue: dict):
        """Update fixedFieldDisplayValue item with given {fixedFieldDisplayValueId}

        ``PUT /marccat/authority-record/fixed-field-display-value``

        Args:
            fixedFieldDisplayValue (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Marccat_modify_fixedFieldDisplayValue_request.schema
        """
        return self.call("PUT", "/marccat/authority-record/fixed-field-display-value", data=fixedFieldDisplayValue)

    def set_fixedFieldDisplayValue(self):
        """Change the display value for 008 tag

        ``POST /marccat/authority-record/fixed-field-display-value``

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("POST", "/marccat/authority-record/fixed-field-display-value")

    def get_authFixedFieldsCodeGroups(self, **kwargs):
        """Return a list of marc authority records and search metadata

        ``GET /marccat/auth-fixed-fields-code-groups``

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
                    
                    using CCL query in q parameter
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - q=na "giannini"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestError: Bad Request

        Schema:

            .. literalinclude:: ../files/Marccat_get_authFixedFieldsCodeGroups_return.schema 
        """
        return self.call("GET", "/marccat/auth-fixed-fields-code-groups", query=kwargs)

    def delete_authFixedFieldsCodeGroups(self):
        """Delete authFixedFieldsCodeGroup item with given {authFixedFieldsCodeGroupId}

        ``DELETE /marccat/auth-fixed-fields-code-groups``

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", "/marccat/auth-fixed-fields-code-groups")

    def modify_authFixedFieldsCodeGroup(self, authFixedFieldsCodeGroup: dict):
        """Update authFixedFieldsCodeGroup item with given {authFixedFieldsCodeGroupId}

        ``PUT /marccat/auth-fixed-fields-code-groups``

        Args:
            authFixedFieldsCodeGroup (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Marccat_modify_authFixedFieldsCodeGroup_request.schema
        """
        return self.call("PUT", "/marccat/auth-fixed-fields-code-groups", data=authFixedFieldsCodeGroup)

    def set_authFixedFieldsCodeGroup(self):
        """Get authority control fields values

        ``POST /marccat/auth-fixed-fields-code-groups``

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("POST", "/marccat/auth-fixed-fields-code-groups")

    def get_authHeaderTypes(self):
        """Get the value for the header type of 008 authority tag

        ``GET /marccat/auth-header-types``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Marccat_get_authHeaderTypes_return.schema 
        """
        return self.call("GET", "/marccat/auth-header-types")
