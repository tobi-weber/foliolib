# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.folioSpringBase")



class Tenant(FolioApi):
    """Tenant API

    
    """

    def posttenant(self, tenantAttributes):
        """Create tenant job (create, upgrade, delete)

        ``POST /_/tenant``

        Args:
            tenantAttributes (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Tenant_posttenant_request.schema
        """
        return self.call("POST", f"/_/tenant", tenantAttributes)

    def gettenant(self, operationId):
        """Does tenant id already exist

        ``GET /_/tenant/{operationId}``

        Raises:
            OkapiFatalError: Internal server error
        """
        return self.call("GET", f"/_/tenant/{operationId}")

		
    def deletetenant(self, operationId):
        """drop tenant id

        ``DELETE /_/tenant/{operationId}``

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", f"/_/tenant/{operationId}")
