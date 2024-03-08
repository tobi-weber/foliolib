# -*- coding: utf-8 -*-
# Generated at 2024-03-23

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.loginSaml")


class SamlLogin(FolioApi):
    """mod-login-saml API

    This module provides an SAML2-based login mechanism to authenticate user in FOLIO through SSO credentials
    """

    def get_regenerates(self):
        """Regenerate SAML configuration (keyfile and passwords). The response contains the sp-metadata.xml file

        ``GET /saml/regenerate``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/SamlLogin_get_regenerates_return.schema 
        """
        return self.call("GET", "/saml/regenerate")

    def set_login(self, login: dict):
        """Generates SAMLRequest and RelayState parameters for initiating a SAML login process

        ``POST /saml/login``

        Args:
            login (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/SamlLogin_set_login_request.schema
            .. literalinclude:: ../files/SamlLogin_set_login_return.schema 
        """
        return self.call("POST", "/saml/login", data=login)

    def set_callback(self, callback: str):
        """Redirect browser to sso-landing page with generated token. Deprecated.

        ``POST /saml/callback``

        Args:
            callback (str): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestForbidden: Forbidden
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/SamlLogin_set_callback_request.schema
        """
        return self.call("POST", "/saml/callback", data=callback)

    def set_callbackWithExpiry(self, callbackWithExpiry: str):
        """Redirect browser to sso-landing page with expiring access and refresh tokens.

        ``POST /saml/callback-with-expiry``

        Args:
            callbackWithExpiry (str): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestForbidden: Forbidden
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/SamlLogin_set_callbackWithExpiry_request.schema
        """
        return self.call("POST", "/saml/callback-with-expiry", data=callbackWithExpiry)

    def get_checks(self):
        """Decides if SSO login is configured properly, returns true or false

        ``GET /saml/check``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/SamlLogin_get_checks_return.schema 
        """
        return self.call("GET", "/saml/check")

    def get_configurations(self):
        """

        ``GET /saml/configuration``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/SamlLogin_get_configurations_return.schema 
        """
        return self.call("GET", "/saml/configuration")

    def modify_configuration(self, configuration: dict):
        """Save SAML module configuration

        ``PUT /saml/configuration``

        Args:
            configuration (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/SamlLogin_modify_configuration_request.schema
            .. literalinclude:: ../files/SamlLogin_modify_configuration_return.schema 
        """
        return self.call("PUT", "/saml/configuration", data=configuration)

    def get_validates(self, **kwargs):
        """

        ``GET /saml/validate``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            type (str):  The type of configuration directive
                    
                    Example:
                    
                     - idpurl
            value (str):  The value of configuration directive
                    
                    Example:
                    
                     - http://localhost

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/SamlLogin_get_validates_return.schema 
        """
        return self.call("GET", "/saml/validate", query=kwargs)
