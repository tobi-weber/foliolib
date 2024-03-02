# -*- coding: utf-8 -*-
# Generated at 2024-03-01

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.authtoken")



class Token(FolioApi):
    """mod-authtoken API

    
    """

    def token_legacy(self, signTokenPayload):
        """Deprecated. Will be removed in a future release. Please use /token/sign instead. Returns a signed, non-expiring legacy access token.

        ``POST /token``

        Args:
            signTokenPayload (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Token_token_legacy_request.schema
            .. literalinclude:: ../files/Token_token_legacy_request.schema_response.schema
        """
        return self.call("POST", f"/token", signTokenPayload)

    def token_sign_legacy(self, signRefreshToken):
        """Returns a signed, expiring refresh token. This is a legacy endpoint and should not be
called by new code and will soon be fully depreciated.


        ``POST /refreshtoken``

        Args:
            signRefreshToken (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Token_token_sign_legacy_request.schema
            .. literalinclude:: ../files/Token_token_sign_legacy_request.schema_response.schema
        """
        return self.call("POST", f"/refreshtoken", signRefreshToken)

    def token_sign(self, signTokenPayload):
        """Returns a signed, expiring access token and refresh token. Also returns the expiration
of each token in the body of the response. The access token time to live is 10 minutes and
the refresh token is one week.


        ``POST /token/sign``

        Args:
            signTokenPayload (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Token_token_sign_request.schema
            .. literalinclude:: ../files/Token_token_sign_request.schema_response.schema
        """
        return self.call("POST", f"/token/sign", signTokenPayload)

    def token_refresh(self, refreshToken):
        """Returns a new refresh token and a new access token. Also returns the expiration of each token
in the body of the response. Time to live is 10 minutes for the access token and one week for
the refresh token.


        ``POST /token/refresh``

        Args:
            refreshToken (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Token_token_refresh_request.schema
            .. literalinclude:: ../files/Token_token_refresh_request.schema_response.schema
        """
        return self.call("POST", f"/token/refresh", refreshToken)

    def token_invalidate(self, refreshToken):
        """Invalidate a single token

        ``POST /token/invalidate``

        Args:
            refreshToken (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Token_token_invalidate_request.schema
        """
        return self.call("POST", f"/token/invalidate", refreshToken)

    def token_invalidate_all(self):
        """Invalidate all tokens for a user

        ``POST /token/invalidate-all``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestFatalError: Internal error
        """
        return self.call("POST", "/token/invalidate-all")
