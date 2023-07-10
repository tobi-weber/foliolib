# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.authtoken")



class Token(FolioApi):
    """mod-authtoken API

    
    """

    def token_legacy(self, signTokenPayload):
        """Sign token legacy

        ``POST /token``

        Args:
            signTokenPayload (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Token_token_legacy_request.schema
            .. literalinclude:: ../files/Token_token_legacy_request.schema_response.schema
        """
        return self.call("POST", f"/token", signTokenPayload)

    def token_sign_legacy(self, signRefreshToken):
        """Sign token

        ``POST /refreshtoken``

        Args:
            signRefreshToken (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Token_token_sign_legacy_request.schema
            .. literalinclude:: ../files/Token_token_sign_legacy_request.schema_response.schema
        """
        return self.call("POST", f"/refreshtoken", signRefreshToken)

    def token_sign(self, signTokenPayload):
        """Sign token

        ``POST /token/sign``

        Args:
            signTokenPayload (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Token_token_sign_request.schema
            .. literalinclude:: ../files/Token_token_sign_request.schema_response.schema
        """
        return self.call("POST", f"/token/sign", signTokenPayload)

    def token_refresh(self, refreshToken):
        """Get a new refresh token and a new access token

        ``POST /token/refresh``

        Args:
            refreshToken (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Token_token_refresh_request.schema
            .. literalinclude:: ../files/Token_token_refresh_request.schema_response.schema
        """
        return self.call("POST", f"/token/refresh", refreshToken)
