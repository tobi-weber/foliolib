# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.notify")


class Notify(FolioApi):
    """mod-notify API

    This documents the API calls that can be made to post notifications for users, and to get them
    """

    def get_notifies(self, **kwargs):
        """Retrieve a list of notify items.

        ``GET /notify``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example link = 1234
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - link=/users/1234
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

            .. literalinclude:: ../files/Notify_get_notifies_return.schema 
        """
        return self.call("GET", "/notify", query=kwargs)

    def set_notify(self, notify: dict):
        """Create a new notify item.

        ``POST /notify``

        Args:
            notify (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created notify item

        Schema:

            .. literalinclude:: ../files/Notify_set_notify_request.schema
        """
        return self.call("POST", "/notify", data=notify)

    def delete_notifies(self):
        """

        ``DELETE /notify``
        """
        return self.call("DELETE", "/notify")

    def set__username(self, username: str, _username: dict, **kwargs):
        """Send notification to the user by user name

        ``POST /notify/_username/{username}``

        Args:
            username (str)
            _username (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the notification            - **X-Okapi-Trace** - Okapi trace and timing

        Schema:

            .. literalinclude:: ../files/Notify_set__username_request.schema
        """
        return self.call("POST", f"/notify/_username/{username}", data=_username, query=kwargs)

    def get__selves(self, **kwargs):
        """Retrieve a list of _self items.

        ``GET /notify/user/_self``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example link = 1234
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - link=/users/1234
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

            .. literalinclude:: ../files/Notify_get__selves_return.schema 
        """
        return self.call("GET", "/notify/user/_self", query=kwargs)

    def set__self(self, _self: dict):
        """Create a new _self item.

        ``POST /notify/user/_self``

        Args:
            _self (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created _self item

        Schema:

            .. literalinclude:: ../files/Notify_set__self_request.schema
        """
        return self.call("POST", "/notify/user/_self", data=_self)

    def delete__selves(self):
        """

        ``DELETE /notify/user/_self``
        """
        return self.call("DELETE", "/notify/user/_self")

    def get_notify(self, notifyId: str):
        """Retrieve notify item with given {notifyId}

        ``GET /notify/{notifyId}``

        Args:
            notifyId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Notify_get_notify_return.schema 
        """
        return self.call("GET", f"/notify/{notifyId}")

    def delete_notify(self, notifyId: str):
        """Delete notify item with given {notifyId}

        ``DELETE /notify/{notifyId}``

        Args:
            notifyId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/notify/{notifyId}")

    def modify_notify(self, notifyId: str, notify: dict):
        """Update notify item with given {notifyId}

        ``PUT /notify/{notifyId}``

        Args:
            notifyId (str)
            notify (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Notify_modify_notify_request.schema
        """
        return self.call("PUT", f"/notify/{notifyId}", data=notify)


class PatronNotice(FolioApi):
    """mod-notify API

    This documents the API calls that can be made to post patron notices for users
    """

    def set_patronNotice(self, patronNotice: dict, **kwargs):
        """Send patron notice

        ``POST /patron-notice``

        Args:
            patronNotice (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PatronNotice_set_patronNotice_request.schema
        """
        return self.call("POST", "/patron-notice", data=patronNotice, query=kwargs)
