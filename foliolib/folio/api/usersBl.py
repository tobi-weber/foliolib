# -*- coding: utf-8 -*-
# Generated at 2024-03-23

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.usersBl")


class ModUsersBl(FolioApi):
    """Business Logic Users API

    A front end for mod-users and mod-permissions
    """

    def get_blUsers(self, **kwargs):
        """Get a number of user (and possibly related) records based on criteria in the user and related modules

        ``GET /bl-users``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - active=true
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            include (list):  indicates which referenced fields should be populated (de-referenced) by the service
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestForbidden: Forbidden
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ModUsersBl_get_blUsers_return.schema 
        """
        return self.call("GET", "/bl-users", query=kwargs)

    def get_byId(self, byId: str, **kwargs):
        """Get a user by "id"

        ``GET /bl-users/by-id/{byId}``

        Args:
            byId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            include (list):  indicates which referenced fields should be populated (de-referenced) by the service
                    
            expandPermissions (bool): (default=False) Whether or not to expand permissions listings

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestForbidden: Forbidden
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ModUsersBl_get_byId_return.schema 
        """
        return self.call("GET", f"/bl-users/by-id/{byId}", query=kwargs)

    def delete_byId(self, byId: str):
        """

        ``DELETE /bl-users/by-id/{byId}``

        Args:
            byId (str)
        """
        return self.call("DELETE", f"/bl-users/by-id/{byId}")

    def get_openTransactions_by_by(self, byId: str):
        """Check if user has any open transactions, and if so, how many. Identify user by "id"

        ``GET /bl-users/by-id/{byId}/open-transactions``

        Args:
            byId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ModUsersBl_get_openTransactions_by_by_return.schema 
        """
        return self.call("GET", f"/bl-users/by-id/{byId}/open-transactions")

    def get_byUsername(self, username: str, **kwargs):
        """Get a user by "username"

        ``GET /bl-users/by-username/{username}``

        Args:
            username (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            include (list):  indicates which referenced fields should be populated (de-referenced) by the service
                    
            expandPermissions (bool): (default=False) Whether or not to expand permissions listings

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestForbidden: Forbidden
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ModUsersBl_get_byUsername_return.schema 
        """
        return self.call("GET", f"/bl-users/by-username/{username}", query=kwargs)

    def delete_byUsername(self, username: str):
        """

        ``DELETE /bl-users/by-username/{username}``

        Args:
            username (str)
        """
        return self.call("DELETE", f"/bl-users/by-username/{username}")

    def get_openTransactions_by_username(self, username: str):
        """Check if user has any open transactions, and if so, how many. Identify user by "username"

        ``GET /bl-users/by-username/{username}/open-transactions``

        Args:
            username (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ModUsersBl_get_openTransactions_by_username_return.schema 
        """
        return self.call("GET", f"/bl-users/by-username/{username}/open-transactions")

    def get__selves(self, **kwargs):
        """Get a user by "self reference"

        ``GET /bl-users/_self``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            include (list):  indicates which referenced fields should be populated (de-referenced) by the service
                    
            expandPermissions (bool): (default=False) Whether or not to expand permissions listings

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestForbidden: Forbidden
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ModUsersBl_get__selves_return.schema 
        """
        return self.call("GET", "/bl-users/_self", query=kwargs)

    def delete__selves(self):
        """

        ``DELETE /bl-users/_self``
        """
        return self.call("DELETE", "/bl-users/_self")

    def set_login(self, login: dict, **kwargs):
        """Allow a new user to login and return an authtoken, along with a composite user record. Deprecated and will be removed in a future release. Please use /login-with-expiry.

        ``POST /bl-users/login``

        Args:
            login (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            expandPermissions (bool): (default=False) Whether or not to expand permissions listings
            include (list):  indicates which referenced fields should be populated (de-referenced) by the service
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestFatalError: Server Error

        Headers:
            - **x-okapi-token** 

        Schema:

            .. literalinclude:: ../files/ModUsersBl_set_login_request.schema
            .. literalinclude:: ../files/ModUsersBl_set_login_return.schema 
        """
        return self.call("POST", "/bl-users/login", data=login, query=kwargs)

    def set_loginWithExpiry(self, loginWithExpiry: dict, **kwargs):
        """Allow a new user to login and return two cookies, one containing the user's refresh token
        and one containing an access token. Both tokens have an expiration. The expiration time
        for each is contained in the composite user token expiration property.

        ``POST /bl-users/login-with-expiry``

        Args:
            loginWithExpiry (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            expandPermissions (bool): (default=False) Whether or not to expand permissions listings
            include (list):  indicates which referenced fields should be populated (de-referenced) by the service
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ModUsersBl_set_loginWithExpiry_request.schema
            .. literalinclude:: ../files/ModUsersBl_set_loginWithExpiry_return.schema 
        """
        return self.call("POST", "/bl-users/login-with-expiry", data=loginWithExpiry, query=kwargs)

    def set_username(self, username: dict):
        """called when a user has forgotten "a username"

        ``POST /bl-users/forgotten/username``

        Args:
            username (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ModUsersBl_set_username_request.schema
        """
        return self.call("POST", "/bl-users/forgotten/username", data=username)

    def set_password_forgotten(self, password: dict):
        """called when a user has forgotten "a password"

        ``POST /bl-users/forgotten/password``

        Args:
            password (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ModUsersBl_set_password_forgotten_request.schema
        """
        return self.call("POST", "/bl-users/forgotten/password", data=password)

    def set_password_myprofile(self, password: dict):
        """Allow change password for user

        ``POST /bl-users/settings/myprofile/password``

        Args:
            password (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ModUsersBl_set_password_myprofile_request.schema
        """
        return self.call("POST", "/bl-users/settings/myprofile/password", data=password)

    def set_link(self, link: dict):
        """Generate and send password reset link

        ``POST /bl-users/password-reset/link``

        Args:
            link (dict): See Schema below

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/ModUsersBl_set_link_request.schema
            .. literalinclude:: ../files/ModUsersBl_set_link_return.schema 
        """
        return self.call("POST", "/bl-users/password-reset/link", data=link)

    def set_reset(self, reset: dict):
        """Reset password

        ``POST /bl-users/password-reset/reset``

        Args:
            reset (dict): See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ModUsersBl_set_reset_request.schema
        """
        return self.call("POST", "/bl-users/password-reset/reset", data=reset)

    def set_validate(self):
        """

        ``POST /bl-users/password-reset/validate``

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestFatalError: Server Error
        """
        return self.call("POST", "/bl-users/password-reset/validate")
