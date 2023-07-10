# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.folioVertxLib")



class Tenant(FolioApi):
    """Tenant API

    
    """

    def posttenant(self, tenantAttributes):
        """Start tenant operation

        ``POST /_/tenant``

        Args:
            tenantAttributes (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestPayloadToLarge: Payload Too large
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Tenant_posttenant_request.schema
        """
        return self.call("POST", f"/_/tenant", tenantAttributes)

    def gettenantjob(self, id_, **kwargs):
        """Get tenant job

        ``GET /_/tenant/{id}``

        Keyword Args:
            wait (int): wait until job change, but no longer than the wait time - in milliseconds. 0 means "no wait" and is behavior if omitted.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: job id not found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Tenant_gettenantjob_response.schema
        """
        return self.call("GET", f"/_/tenant/{id_}", query=kwargs)

		
    def deletetenantjob(self, id_):
        """delete tenant job

        ``DELETE /_/tenant/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: job id not found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", f"/_/tenant/{id_}")
