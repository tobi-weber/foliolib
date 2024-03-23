# -*- coding: utf-8 -*-
# Generated at 2024-03-23

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
            OkapiRequestFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Tenant_posttenant_request.schema
        """
        return self.call("POST", f"/_/tenant", tenantAttributes)

    def gettenant(self, operationId):
        """Does tenant id already exist

        ``GET /_/tenant/{operationId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Tenant_gettenant_response.schema
        """
        return self.call("GET", f"/_/tenant/{operationId}")

		
    def deletetenant(self, operationId):
        """drop tenant id

        ``DELETE /_/tenant/{operationId}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestFatalError: Internal server error
        """
        return self.call("DELETE", f"/_/tenant/{operationId}")
