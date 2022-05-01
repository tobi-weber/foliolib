# -*- coding: utf-8 -*-
# Generated at 2022-04-28

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.authtoken")



class TokenAdmin(FolioAdminApi):
    """mod-authtoken API
    Administration

    
    """

    def token(self, signTokenPayload):
        """Sign token

        ``POST /token``

        Args:
            signTokenPayload (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Token_token_request.schema
            .. literalinclude:: ../files/Token_token_request.schema_response.schema
        """
        return self.call("POST", "/token", signTokenPayload)

    def refresh(self, refreshToken):
        """Sign token

        ``POST /refresh``

        Args:
            refreshToken (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Token_refresh_request.schema
            .. literalinclude:: ../files/Token_refresh_request.schema_response.schema
        """
        return self.call("POST", "/refresh", refreshToken)

    def refreshtoken(self, signRefreshToken):
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

            .. literalinclude:: ../files/Token_refreshtoken_request.schema
            .. literalinclude:: ../files/Token_refreshtoken_request.schema_response.schema
        """
        return self.call("POST", "/refreshtoken", signRefreshToken)
