# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.login")


class Login(FolioApi):
    """mod-login API

    This module provides a username/password based login mechanism for FOLIO credentials
    """

    def get_loginAttempt(self, loginAttemptsId: str):
        """Get login attempts for a single user

        ``GET /authn/loginAttempts/{loginAttemptsId}``

        Args:
            loginAttemptsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Login_get_loginAttempt_return.schema 
        """
        return self.call("GET", f"/authn/loginAttempts/{loginAttemptsId}")

    def set_login(self, login: dict):
        """Get a new login token

        ``POST /authn/login``

        Args:
            login (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Headers:
            - **x-okapi-token**             - **refreshtoken** 

        Schema:

            .. literalinclude:: ../files/Login_set_login_request.schema
            .. literalinclude:: ../files/Login_set_login_return.schema 
        """
        return self.call("POST", "/authn/login", data=login)

    def set_update(self, update: dict):
        """Self-update existing credentials.  N.B. A non-empty password must be provided.

        ``POST /authn/update``

        Args:
            update (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Login_set_update_request.schema
        """
        return self.call("POST", "/authn/update", data=update)

    def set_credential(self, credential: dict):
        """Add a new login to the system. N.B. A non-empty password must be provided.

        ``POST /authn/credentials``

        Args:
            credential (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Login_set_credential_request.schema
        """
        return self.call("POST", "/authn/credentials", data=credential)

    def delete_credentials(self, **kwargs):
        """Remove a user's login credentials from the system

        ``DELETE /authn/credentials``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            userId (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  User Id

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("DELETE", "/authn/credentials", query=kwargs)

    def set_repeatable(self, repeatable: dict):
        """Validate password for repeatability

        ``POST /authn/password/repeatable``

        Args:
            repeatable (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Login_set_repeatable_request.schema
            .. literalinclude:: ../files/Login_set_repeatable_return.schema 
        """
        return self.call("POST", "/authn/password/repeatable", data=repeatable)

    def set_resetPassword(self, resetPassword: dict):
        """Resets password for user in record and deletes action record

        ``POST /authn/reset-password``

        Args:
            resetPassword (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Login_set_resetPassword_request.schema
            .. literalinclude:: ../files/Login_set_resetPassword_return.schema 
        """
        return self.call("POST", "/authn/reset-password", data=resetPassword)

    def set_passwordResetAction(self, passwordResetAction: dict):
        """Saves action to storage

        ``POST /authn/password-reset-action``

        Args:
            passwordResetAction (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Login_set_passwordResetAction_request.schema
            .. literalinclude:: ../files/Login_set_passwordResetAction_return.schema 
        """
        return self.call("POST", "/authn/password-reset-action", data=passwordResetAction)

    def get_passwordResetAction(self, actionId: str):
        """Retrieves action record by id

        ``GET /authn/password-reset-action/{actionId}``

        Args:
            actionId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Login_get_passwordResetAction_return.schema 
        """
        return self.call("GET", f"/authn/password-reset-action/{actionId}")

    def get_events(self, **kwargs):
        """Returns a list of events retrieved from storage

        ``GET /authn/log/events``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            length (int): (default=10) The maximum number of results to return.
                    
                    Example:
                    
                     - 10
            start (int): (default=1) The starting index in a list of results (starts at one).
            query (str):  A query string to filter users based on matching criteria in fields.

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Login_get_events_return.schema 
        """
        return self.call("GET", "/authn/log/events", query=kwargs)

    def set_event(self, event: dict):
        """Saves received event into the storage

        ``POST /authn/log/events``

        Args:
            event (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Login_set_event_request.schema
            .. literalinclude:: ../files/Login_set_event_return.schema 
        """
        return self.call("POST", "/authn/log/events", data=event)

    def delete_event(self, eventsId: str):
        """Removes events by filter

        ``DELETE /authn/log/events/{eventsId}``

        Args:
            eventsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Login_delete_event_return.schema 
        """
        return self.call("DELETE", f"/authn/log/events/{eventsId}")

    def get_credentialsExistences(self, **kwargs):
        """Returns single property 'credentialsExist' with true, if user has local password

        ``GET /authn/credentials-existence``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            userId (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  User id

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Login_get_credentialsExistences_return.schema 
        """
        return self.call("GET", "/authn/credentials-existence", query=kwargs)
