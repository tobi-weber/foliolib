# -*- coding: utf-8 -*-
# Generated at 2024-03-23

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.circulationItem")



class Circulationitem(FolioApi):
    """Circulation item API

    
    """

    def getcirculationitemsbyquery(self, **kwargs):
        """Return a list of items based on query

        ``GET /circulation-item``

        Keyword Args:
            query (str): A query expressed as a CQL string (default: cql.allRecords=1)
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 1000, minimum: 1, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/Circulationitem_getcirculationitemsbyquery_response.schema
        """
        return self.call("GET", "/circulation-item", query=kwargs)

    def createcirculationitem(self, circulationItem, circulationItemId):
        """Add new circulation item

        ``POST /circulation-item/{circulationItemId}``

        Args:
            circulationItem (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiRequestFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulationitem_createcirculationitem_request.schema
            .. literalinclude:: ../files/Circulationitem_createcirculationitem_request.schema_response.schema
        """
        return self.call("POST", f"/circulation-item/{circulationItemId}", circulationItem)

		
    def retrievecirculationitembyid(self, circulationItemId):
        """Retrieve circulation item

        ``GET /circulation-item/{circulationItemId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Circulation Item not found
            OkapiRequestFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulationitem_retrievecirculationitembyid_response.schema
        """
        return self.call("GET", f"/circulation-item/{circulationItemId}")

		
    def updatecirculationitem(self, circulationItem, circulationItemId):
        """Change the circulation item

        ``PUT /circulation-item/{circulationItemId}``

        Args:
            circulationItem (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Circulation Item not found
            OkapiRequestFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulationitem_updatecirculationitem_request.schema
        """
        return self.call("PUT", f"/circulation-item/{circulationItemId}", circulationItem)
