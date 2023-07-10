# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.pubsub")


class PubSub(FolioApi):
    """PubSub API

    API for event-driven approach
    """

    def get_eventTypes(self):
        """Get a list of evet type descriptors

        ``GET /pubsub/event-types``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PubSub_get_eventTypes_return.schema 
        """
        return self.call("GET", "/pubsub/event-types")

    def set_eventType(self, eventType: dict):
        """Create new event type

        ``POST /pubsub/event-types``

        Args:
            eventType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created eventType item

        Schema:

            .. literalinclude:: ../files/PubSub_set_eventType_request.schema
        """
        return self.call("POST", "/pubsub/event-types", data=eventType)

    def get_eventType(self, eventTypeName: str):
        """Retrieve eventType item with given {eventTypeId}

        ``GET /pubsub/event-types/{eventTypeName}``

        Args:
            eventTypeName (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PubSub_get_eventType_return.schema 
        """
        return self.call("GET", f"/pubsub/event-types/{eventTypeName}")

    def delete_eventType(self, eventTypeName: str):
        """Delete eventType item with given {eventTypeId}

        ``DELETE /pubsub/event-types/{eventTypeName}``

        Args:
            eventTypeName (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/pubsub/event-types/{eventTypeName}")

    def modify_eventType(self, eventTypeName: str, eventType: dict):
        """Update eventType item with given {eventTypeId}

        ``PUT /pubsub/event-types/{eventTypeName}``

        Args:
            eventTypeName (str)
            eventType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/PubSub_modify_eventType_request.schema
        """
        return self.call("PUT", f"/pubsub/event-types/{eventTypeName}", data=eventType)

    def get_publishers(self, eventTypeName: str):
        """API to retrieve registered Publishers

        ``GET /pubsub/event-types/{eventTypeName}/publishers``

        Args:
            eventTypeName (str)

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/PubSub_get_publishers_return.schema 
        """
        return self.call("GET", f"/pubsub/event-types/{eventTypeName}/publishers")

    def delete_publisher(self, eventTypeName: str, **kwargs):
        """Remove publisher declaration for certain event type

        ``DELETE /pubsub/event-types/{eventTypeName}/publishers``

        Args:
            eventTypeName (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            moduleId (str):  Publisher module name and version
                    
                    Example:
                    
                     - mod-pubsub-1.0.0
        """
        return self.call("DELETE", f"/pubsub/event-types/{eventTypeName}/publishers", query=kwargs)

    def get_subscribers(self, eventTypeName: str):
        """API to retrieve registered Subscribers

        ``GET /pubsub/event-types/{eventTypeName}/subscribers``

        Args:
            eventTypeName (str)

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/PubSub_get_subscribers_return.schema 
        """
        return self.call("GET", f"/pubsub/event-types/{eventTypeName}/subscribers")

    def delete_subscriber(self, eventTypeName: str, **kwargs):
        """API to remove Subscriber declaration for certain event type

        ``DELETE /pubsub/event-types/{eventTypeName}/subscribers``

        Args:
            eventTypeName (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            moduleId (str):  Subscriber module name and version
                    
                    Example:
                    
                     - mod-pubsub-1.0.0
        """
        return self.call("DELETE", f"/pubsub/event-types/{eventTypeName}/subscribers", query=kwargs)

    def set_publisher(self, publisher: dict):
        """Declare a publisher for a set of event types

        ``POST /pubsub/event-types/declare/publisher``

        Args:
            publisher (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PubSub_set_publisher_request.schema
        """
        return self.call("POST", "/pubsub/event-types/declare/publisher", data=publisher)

    def set_subscriber(self, subscriber: dict):
        """

        ``POST /pubsub/event-types/declare/subscriber``

        Args:
            subscriber (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PubSub_set_subscriber_request.schema
        """
        return self.call("POST", "/pubsub/event-types/declare/subscriber", data=subscriber)

    def get_histories(self, **kwargs):
        """Get activity history

        ``GET /pubsub/history``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            startDate (str):  start date of the period of time for which audit messages are required
                    
                    Example:
                    
                     - 2019-09-20 12:00:00
            endDate (str):  end date of the period of time for which audit messages are required
                    
                    Example:
                    
                     - 2019-09-27 12:00:00
            eventId (str):  eventId by which audit messages should be filtered
            eventType (str):  eventType by which audit messages should be filtered
            correlationId (str):  correlationId by which audit messages should be filtered

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PubSub_get_histories_return.schema 
        """
        return self.call("GET", "/pubsub/history", query=kwargs)

    def get_payload_by_event(self, eventId: str):
        """Get audit message payload by event id

        ``GET /pubsub/audit-messages/{eventId}/payload``

        Args:
            eventId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PubSub_get_payload_by_event_return.schema 
        """
        return self.call("GET", f"/pubsub/audit-messages/{eventId}/payload")

    def set_publish(self, publish: dict):
        """

        ``POST /pubsub/publish``

        Args:
            publish (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PubSub_set_publish_request.schema
        """
        return self.call("POST", "/pubsub/publish", data=publish)

    def delete_messagingModules(self, **kwargs):
        """

        ``DELETE /pubsub/messaging-modules``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            moduleId (str):  module name and version
                    
                    Example:
                    
                     - mod-pubsub-1.0.0
            moduleRole (str):  module role (PUBLISHER/SUBSCRIBER)
                    
                    Example:
                    
                     - PUBLISHER

        Raises:
            OkapiRequestError: Bad Request
        """
        return self.call("DELETE", "/pubsub/messaging-modules", query=kwargs)
