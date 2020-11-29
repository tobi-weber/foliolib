# -*- coding: utf-8 -*-
# Generated at 2020-11-29

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.tags")


class Tags(FolioApi):
    """mod-tags API

    This documents the API calls that can be made to post tags that can be attached to various objects
    """

    def get_tags(self, **kwargs):
        """Retrieve a list of tag items.

        ``GET /tags``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example label=foo
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - label=foo
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

            .. literalinclude:: ../files/Tags_get_tags_return.schema 
        """
        return self.call("GET", "/tags", query=kwargs)

    def set_tag(self, tag: dict):
        """Create a new tag item.

        ``POST /tags``

        Args:
            tag (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created tag item

        Schema:

            .. literalinclude:: ../files/Tags_set_tag_request.schema
        """
        return self.call("POST", "/tags", data=tag)

    def get_tag(self, tagsId: str):
        """Retrieve tag item with given {tagId}

        ``GET /tags/{tagsId}``

        Args:
            tagsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Tags_get_tag_return.schema 
        """
        return self.call("GET", f"/tags/{tagsId}")

    def delete_tag(self, tagsId: str):
        """Delete tag item with given {tagId}

        ``DELETE /tags/{tagsId}``

        Args:
            tagsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/tags/{tagsId}")

    def modify_tag(self, tagsId: str, tag: dict):
        """Update tag item with given {tagId}

        ``PUT /tags/{tagsId}``

        Args:
            tagsId (str)
            tag (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Tags_modify_tag_request.schema
        """
        return self.call("PUT", f"/tags/{tagsId}", data=tag)
