# -*- coding: utf-8 -*-
# Generated at 2024-03-01

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.usersKeycloak")



class Userskeycloak(FolioApi):
    """Users Keycloak API

    Users Keycloak API
    """

    def createuser(self, user, **kwargs):
        """Create a new user

        ``POST /users-keycloak/users``

        Args:
            user (dict): See Schema below.

        Keyword Args:
            keycloakOnly (bool): Create auth user only during user creation (default: False)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Userskeycloak_createuser_request.schema
        """
        return self.call("POST", f"/users-keycloak/users", user, query=kwargs)

		
    def getusers(self, **kwargs):
        """Retrieve a list of users

        ``GET /users-keycloak/users``

        Keyword Args:
            query (str): A CQL query string with search conditions.
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, default: 0)
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 10)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Userskeycloak_getusers_response.schema
        """
        return self.call("GET", "/users-keycloak/users", query=kwargs)

		
    def deleteusers(self, **kwargs):
        """Delete a collection of users selected by a CQL query; | this doesn't delete proxyFor records that reference them

        ``DELETE /users-keycloak/users``

        Keyword Args:
            query (str): A CQL query string with search conditions.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("DELETE", "/users-keycloak/users", query=kwargs)

    def updateuser(self, user, id_):
        """Update user with given id

        ``PUT /users-keycloak/users/{id}``

        Args:
            user (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Userskeycloak_updateuser_request.schema
        """
        return self.call("PUT", f"/users-keycloak/users/{id_}", user)

		
    def getuser(self, id_):
        """Get a single user

        ``GET /users-keycloak/users/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Userskeycloak_getuser_response.schema
        """
        return self.call("GET", f"/users-keycloak/users/{id_}")

		
    def deleteuser(self, id_):
        """Delete user with given id

        ``DELETE /users-keycloak/users/{id}``

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("DELETE", f"/users-keycloak/users/{id_}")

    def getuserbyselfreference(self, **kwargs):
        """Get a user by self reference

        ``GET /users-keycloak/_self``

        Keyword Args:
            include (list): Indicates which referenced fields should be populated (de-referenced) by the service (items: ($ref: #/components/schemas/includedField))
            expandPermissions (bool): Whether or not to expand permissions listings (default: False)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter
            OkapiRequestForbidden: Access denied
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Userskeycloak_getuserbyselfreference_response.schema
        """
        return self.call("GET", "/users-keycloak/_self", query=kwargs)

    def getmigrations(self, **kwargs):
        """Retrieve a list of user migrations

        ``GET /users-keycloak/migrations``

        Keyword Args:
            query (str): A CQL query string with search conditions.
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, default: 0)
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 10)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Userskeycloak_getmigrations_response.schema
        """
        return self.call("GET", "/users-keycloak/migrations", query=kwargs)

		
    def migrateusers(self):
        """Migrate users from mod-users to Keycloak

        ``POST /users-keycloak/migrations``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Userskeycloak_migrateusers_response.schema
        """
        return self.call("POST", "/users-keycloak/migrations")

    def getmigration(self, id_):
        """Retrieve a user migration

        ``GET /users-keycloak/migrations/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Userskeycloak_getmigration_response.schema
        """
        return self.call("GET", f"/users-keycloak/migrations/{id_}")

		
    def deletemigration(self, id_):
        """Delete a user migration

        ``DELETE /users-keycloak/migrations/{id}``
        """
        return self.call("DELETE", f"/users-keycloak/migrations/{id_}")

    def resetforgottenpassword(self, identifier):
        """called when a user has forgotten a password

        ``POST /users-keycloak/forgotten/password``

        Args:
            identifier (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Userskeycloak_resetforgottenpassword_request.schema
        """
        return self.call("POST", f"/users-keycloak/forgotten/password", identifier)

    def recoverforgottenusername(self, identifier):
        """called when a user has forgotten a username

        ``POST /users-keycloak/forgotten/username``

        Args:
            identifier (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Userskeycloak_recoverforgottenusername_request.schema
        """
        return self.call("POST", f"/users-keycloak/forgotten/username", identifier)

    def passwordreset(self, passwordReset):
        """

        ``POST /users-keycloak/password-reset/reset``

        Args:
            passwordReset (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Userskeycloak_passwordreset_request.schema
        """
        return self.call("POST", f"/users-keycloak/password-reset/reset", passwordReset)

    def generatepasswordresetlink(self, generateLinkRequest):
        """Generate and send password reset link

        ``POST /users-keycloak/password-reset/link``

        Args:
            generateLinkRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/Userskeycloak_generatepasswordresetlink_request.schema
            .. literalinclude:: ../files/Userskeycloak_generatepasswordresetlink_request.schema_response.schema
        """
        return self.call("POST", f"/users-keycloak/password-reset/link", generateLinkRequest)

    def validatepasswordresetlink(self):
        """Validates password reset link

        ``POST /users-keycloak/password-reset/validate``

        Raises:
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("POST", "/users-keycloak/password-reset/validate")
