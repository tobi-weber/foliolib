# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.configuration")


class Config(FolioApi):
    """Configuration API updating system wide configurations

    **This documents the API calls that can be made to update configurations in the system**
    """

    def get_entries(self, **kwargs):
        """Retrieve a list of entry items.

        ``GET /configurations/entries``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example module = CIRCULATION
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - scope.institution_id=aaa
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            facets (list):  facets to return in the collection result set, can be suffixed by a count of facet values to return, for example, patronGroup:10 default to top 5 facet values

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Config_get_entries_return.schema 
        """
        return self.call("GET", "/configurations/entries", query=kwargs)

    def set_entry(self, entry: dict):
        """Create a new entry item.

        ``POST /configurations/entries``

        Args:
            entry (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created entry item

        Schema:

            .. literalinclude:: ../files/Config_set_entry_request.schema
        """
        return self.call("POST", "/configurations/entries", data=entry)

    def get_entry(self, entryId: str):
        """Retrieve entry item with given {entryId}

        ``GET /configurations/entries/{entryId}``

        Args:
            entryId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Config_get_entry_return.schema 
        """
        return self.call("GET", f"/configurations/entries/{entryId}")

    def delete_entry(self, entryId: str):
        """Delete entry item with given {entryId}

        ``DELETE /configurations/entries/{entryId}``

        Args:
            entryId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/configurations/entries/{entryId}")

    def modify_entry(self, entryId: str, entry: dict):
        """Update entry item with given {entryId}

        ``PUT /configurations/entries/{entryId}``

        Args:
            entryId (str)
            entry (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Config_modify_entry_request.schema
        """
        return self.call("PUT", f"/configurations/entries/{entryId}", data=entry)

    def get_audits(self, **kwargs):
        """Retrieve a list of audit items.

        ``GET /configurations/audit``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example module = CIRCULATION
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - scope.institution_id=aaa
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
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Config_get_audits_return.schema 
        """
        return self.call("GET", "/configurations/audit", query=kwargs)
