# -*- coding: utf-8 -*-
# Generated at 2024-03-01

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.mgrTenants")



class Mgrtenants(FolioApi):
    """Mgr-Tenants API

    Tenant Manager API
    """

    def createtenant(self, tenant):
        """Create a new tenant

        ``POST /tenants``

        Args:
            tenant (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenants_createtenant_request.schema
        """
        return self.call("POST", f"/tenants", tenant)

		
    def gettenantsbyquery(self, **kwargs):
        """Get tenants by query

        ``GET /tenants``

        Keyword Args:
            query (str): A CQL query string with search conditions.
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, default: 0)
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 10)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenants_gettenantsbyquery_response.schema
        """
        return self.call("GET", "/tenants", query=kwargs)

    def gettenantbyid(self, id_):
        """Get tenant by id

        ``GET /tenants/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenants_gettenantbyid_response.schema
        """
        return self.call("GET", f"/tenants/{id_}")

		
    def updatetenantbyid(self, tenant, id_):
        """Update a tenant

        ``PUT /tenants/{id}``

        Args:
            tenant (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenants_updatetenantbyid_request.schema
        """
        return self.call("PUT", f"/tenants/{id_}", tenant)

		
    def deletetenantbyid(self, id_):
        """Remove a tenant by id

        ``DELETE /tenants/{id}``

        Raises:
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("DELETE", f"/tenants/{id_}")

    def gettenantattributes(self, tenantId, **kwargs):
        """Retrieve list of available tenant attributes by tenant id

        ``GET /tenants/{tenantId}/tenant-attributes``

        Args:
            tenantId (str): Tenant id (format: uuid)

        Keyword Args:
            query (str): A CQL query string with search conditions.
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, default: 0)
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 10)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenants_gettenantattributes_response.schema
        """
        return self.call("GET", f"/tenants/{tenantId}/tenant-attributes", query=kwargs)

		
    def createtenantattributes(self, tenantId, tenantAttributes):
        """Create or replace tenant-attributes associated with the specified tenant. Idempotent operation


        ``POST /tenants/{tenantId}/tenant-attributes``

        Args:
            tenantId (str): Tenant id (format: uuid)
            tenantAttributes (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenants_createtenantattributes_request.schema
        """
        return self.call("POST", f"/tenants/{tenantId}/tenant-attributes", tenantAttributes)

    def gettenantattribute(self, tenantId, id_):
        """Retrieve tenant attribute by id

        ``GET /tenants/{tenantId}/tenant-attributes/{id}``

        Args:
            tenantId (str): Tenant id (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenants_gettenantattribute_response.schema
        """
        return self.call("GET", f"/tenants/{tenantId}/tenant-attributes/{id_}")

		
    def updatetenantattribute(self, tenantId, tenantAttribute, id_):
        """Update tenant attribute

        ``PUT /tenants/{tenantId}/tenant-attributes/{id}``

        Args:
            tenantId (str): Tenant id (format: uuid)
            tenantAttribute (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenants_updatetenantattribute_request.schema
        """
        return self.call("PUT", f"/tenants/{tenantId}/tenant-attributes/{id_}", tenantAttribute)

		
    def deletetenantattribute(self, tenantId, id_):
        """Delete tenant attribute

        ``DELETE /tenants/{tenantId}/tenant-attributes/{id}``

        Args:
            tenantId (str): Tenant id (format: uuid)

        Raises:
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("DELETE", f"/tenants/{tenantId}/tenant-attributes/{id_}")
