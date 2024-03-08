# -*- coding: utf-8 -*-
# Generated at 2024-03-23

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.tags")



class Tags(FolioApi):
    """Tags API

    
    """

    def gettagcollection(self, **kwargs):
        """Retrieve a list of tag items.

        ``GET /tags``

        Keyword Args:
            query (str): A query expressed as a CQL string (default: cql.allRecords=1)
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 1000, minimum: 1, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiRequestFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Tags_gettagcollection_response.schema
        """
        return self.call("GET", "/tags", query=kwargs)

		
    def posttag(self, tagDto):
        """Create a new tag.

        ``POST /tags``

        Args:
            tagDto (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiRequestFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Tags_posttag_request.schema
        """
        return self.call("POST", f"/tags", tagDto)

    def gettagbyid(self, id_):
        """Retrieve tag with given ID

        ``GET /tags/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestNotFound: Item with a given ID not found
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiRequestFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Tags_gettagbyid_response.schema
        """
        return self.call("GET", f"/tags/{id_}")

		
    def puttagbyid(self, tagDto, id_):
        """Update tag with given ID. When renaming the tag label mod-tags doesn't update it in other modules, the client must ensure this.

        ``PUT /tags/{id}``

        Args:
            tagDto (dict): See Schema below.

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestNotFound: Item with a given ID not found
            OkapiRequestFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Tags_puttagbyid_request.schema
        """
        return self.call("PUT", f"/tags/{id_}", tagDto)

		
    def deletetagbyid(self, id_):
        """Delete tag with given ID. This neither checks whether other modules still use the tag label nor does it delete the tag from other modules. The client must ensure this.

        ``DELETE /tags/{id}``

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestNotFound: Item with a given ID not found
            OkapiRequestFatalError: Unexpected error
        """
        return self.call("DELETE", f"/tags/{id_}")
