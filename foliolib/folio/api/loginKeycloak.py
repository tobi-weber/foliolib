# -*- coding: utf-8 -*-
# Generated at 2024-03-01

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.loginKeycloak")



class Loginkeycloak(FolioApi):
    """Mod Login Keycloak API

    Mod Login Keycloak API
    """

    def getloginattempts(self, userId):
        """Get login attempts for a single user

        ``GET /authn/loginAttempts/{userId}``

        Args:
            userId (str): User identifier

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Loginkeycloak_getloginattempts_response.schema
        """
        return self.call("GET", f"/authn/loginAttempts/{userId}")

    def login(self, loginCredentials):
        """Get a new login token

        ``POST /authn/login``

        Args:
            loginCredentials (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestUnprocessableEntity: Error response in JSON format for unprocessable entity.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Loginkeycloak_login_request.schema
            .. literalinclude:: ../files/Loginkeycloak_login_request.schema_response.schema
        """
        return self.call("POST", f"/authn/login", loginCredentials)

    def loginwithexpiry(self, loginCredentials):
        """Get an expiring refresh and access token

        ``POST /authn/login-with-expiry``

        Args:
            loginCredentials (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestUnprocessableEntity: Error response in JSON format for unprocessable entity.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Loginkeycloak_loginwithexpiry_request.schema
            .. literalinclude:: ../files/Loginkeycloak_loginwithexpiry_request.schema_response.schema
        """
        return self.call("POST", f"/authn/login-with-expiry", loginCredentials)

    def refreshtoken(self):
        """Get a new refresh and access token

        ``POST /authn/refresh``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestUnprocessableEntity: Error response in JSON format for unprocessable entity.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Loginkeycloak_refreshtoken_response.schema
        """
        return self.call("POST", "/authn/refresh")

    def logout(self):
        """Logs the user out on their current device

        ``POST /authn/logout``

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestUnprocessableEntity: Error response in JSON format for unprocessable entity.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("POST", "/authn/logout")

    def logoutall(self):
        """Logs the user out on all of their devices

        ``POST /authn/logout-all``

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestUnprocessableEntity: Error response in JSON format for unprocessable entity.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("POST", "/authn/logout-all")

    def token(self, **kwargs):
        """Get a new login token from the authorization code

        ``GET /authn/token``

        Keyword Args:
            code (str): temporary authentication code
            redirect-uri (str): initial uri that was used as redirect uri for getting authentication code

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestUnprocessableEntity: Error response in JSON format for unprocessable entity.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Loginkeycloak_token_response.schema
        """
        return self.call("GET", "/authn/token", query=kwargs)

    def updatecredentials(self, updateCredentials):
        """Self-update existing credentials.

        ``POST /authn/update``

        Args:
            updateCredentials (dict): See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestUnauthorized: Error response in JSON format if user is not authorized to perform operation.
            OkapiRequestUnprocessableEntity: Error response in JSON format for unprocessable entity.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Loginkeycloak_updatecredentials_request.schema
        """
        return self.call("POST", f"/authn/update", updateCredentials)

    def createcredentials(self, loginCredentials):
        """Add a new login to the system.

        ``POST /authn/credentials``

        Args:
            loginCredentials (dict): See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestUnprocessableEntity: Error response in JSON format for unprocessable entity.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Loginkeycloak_createcredentials_request.schema
        """
        return self.call("POST", f"/authn/credentials", loginCredentials)

		
    def deletecredentials(self, **kwargs):
        """Delete credentials for user

        ``DELETE /authn/credentials``

        Keyword Args:
            userId (str): User identifier

        Raises:
            OkapiRequestNotFound: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("DELETE", "/authn/credentials", query=kwargs)

    def validatepasswordrepeatability(self, password):
        """Validate password for repeatability

        ``POST /authn/password/repeatable``

        Args:
            password (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Loginkeycloak_validatepasswordrepeatability_request.schema
            .. literalinclude:: ../files/Loginkeycloak_validatepasswordrepeatability_request.schema_response.schema
        """
        return self.call("POST", f"/authn/password/repeatable", password)

    def resetpassword(self, passwordResetAction):
        """Resets password for user in record and deletes action record

        ``POST /authn/reset-password``

        Args:
            passwordResetAction (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Loginkeycloak_resetpassword_request.schema
            .. literalinclude:: ../files/Loginkeycloak_resetpassword_request.schema_response.schema
        """
        return self.call("POST", f"/authn/reset-password", passwordResetAction)

    def createresetpasswordaction(self, passwordCreateAction):
        """Saves password reset action to storage

        ``POST /authn/password-reset-action``

        Args:
            passwordCreateAction (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Loginkeycloak_createresetpasswordaction_request.schema
            .. literalinclude:: ../files/Loginkeycloak_createresetpasswordaction_request.schema_response.schema
        """
        return self.call("POST", f"/authn/password-reset-action", passwordCreateAction)

    def getpasswordactionbyid(self, actionId):
        """Retrieves action record by id

        ``GET /authn/password-reset-action/{actionId}``

        Args:
            actionId (str): Action Identifier

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Loginkeycloak_getpasswordactionbyid_response.schema
        """
        return self.call("GET", f"/authn/password-reset-action/{actionId}")

    def getlogevents(self, **kwargs):
        """Returns a list of events retrieved from storage

        ``GET /authn/log/events``

        Keyword Args:
            length (int): The maximum number of results to return. (minimum: 1, default: 10)
            start (int): The starting index in a list of results (starts at one). (minimum: 1, default: 1)
            query (str): A query string to filter users based on matching criteria in fields.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Loginkeycloak_getlogevents_response.schema
        """
        return self.call("GET", "/authn/log/events", query=kwargs)

		
    def savelogevent(self, logEvent):
        """Saves received event into the storage

        ``POST /authn/log/events``

        Args:
            logEvent (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Loginkeycloak_savelogevent_request.schema
            .. literalinclude:: ../files/Loginkeycloak_savelogevent_request.schema_response.schema
        """
        return self.call("POST", f"/authn/log/events", logEvent)

    def deletelogevent(self, eventId):
        """Saves received event into the storage

        ``DELETE /authn/log/events/{eventId}``

        Args:
            eventId (str): Event Identifier

        Raises:
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("DELETE", f"/authn/log/events/{eventId}")

    def checkcredentialsexistence(self, **kwargs):
        """Returns single property 'credentialsExist' with true, if user has local password

        ``GET /authn/credentials-existence``

        Keyword Args:
            userId (str): User identifier

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Loginkeycloak_checkcredentialsexistence_response.schema
        """
        return self.call("GET", "/authn/credentials-existence", query=kwargs)
