# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.eventConfig")


class EventConfig(FolioApi):
    """Event config

    **CRUD APIs for event configuration.**
    """

    def get_eventConfigs(self, **kwargs):
        """Get list of funds

        ``GET /eventConfig``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    searchable using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name==RESET_PASSWORD_EVENT
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

            .. literalinclude:: ../files/EventConfig_get_eventConfigs_return.schema 
        """
        return self.call("GET", "/eventConfig", query=kwargs)

    def set_eventConfig(self, eventConfig: dict):
        """Create a new eventConfig item.

        ``POST /eventConfig``

        Args:
            eventConfig (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created eventConfig item

        Schema:

            .. literalinclude:: ../files/EventConfig_set_eventConfig_request.schema
        """
        return self.call("POST", "/eventConfig", data=eventConfig)

    def get_eventConfig(self, eventConfigId: str):
        """Retrieve eventConfig item with given {eventConfigId}

        ``GET /eventConfig/{eventConfigId}``

        Args:
            eventConfigId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/EventConfig_get_eventConfig_return.schema 
        """
        return self.call("GET", f"/eventConfig/{eventConfigId}")

    def delete_eventConfig(self, eventConfigId: str):
        """Delete eventConfig item with given {eventConfigId}

        ``DELETE /eventConfig/{eventConfigId}``

        Args:
            eventConfigId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/eventConfig/{eventConfigId}")

    def modify_eventConfig(self, eventConfigId: str, eventConfig: dict):
        """Update eventConfig item with given {eventConfigId}

        ``PUT /eventConfig/{eventConfigId}``

        Args:
            eventConfigId (str)
            eventConfig (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/EventConfig_modify_eventConfig_request.schema
        """
        return self.call("PUT", f"/eventConfig/{eventConfigId}", data=eventConfig)
