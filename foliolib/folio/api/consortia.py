# -*- coding: utf-8 -*-
# Generated at 2023-05-20

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.consortia")



class UserTenants(FolioApi):
    """User Tenant Association integration API

    User Tenant Association integration API
    """

    def getusertenants(self, consortiumId, **kwargs):
        """User Tenant Associations

        ``GET /consortia/{consortiumId}/user-tenants``

        Args:
            consortiumId (str):

        Keyword Args:
            userId (str):
            username (str):  (description: The username of the user)
            tenantId (str): The ID of the tenant
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Resource not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/UserTenants_getusertenants_response.schema
        """
        return self.call("GET", f"/consortia/{consortiumId}/user-tenants", query=kwargs)

		
    def postusertenants(self, consortiumId, userTenant):
        """User Tenant Associations

        ``POST /consortia/{consortiumId}/user-tenants``

        Args:
            consortiumId (str):
            userTenant (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Resource not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/UserTenants_postusertenants_request.schema
        """
        return self.call("POST", f"/consortia/{consortiumId}/user-tenants", userTenant)

		
    def deleteusertenant(self, consortiumId, **kwargs):
        """Delete User Tenant Associations for particular user id and tenant id

        ``DELETE /consortia/{consortiumId}/user-tenants``

        Args:
            consortiumId (str):

        Keyword Args:
            userId (str):
            tenantId (str): The ID of the tenant

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Resource not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", f"/consortia/{consortiumId}/user-tenants", query=kwargs)

    def getusertenantbyassociationid(self, consortiumId, associationId):
        """

        ``GET /consortia/{consortiumId}/user-tenants/{associationId}``

        Args:
            consortiumId (str):
            associationId (str):

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Resource not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/UserTenants_getusertenantbyassociationid_response.schema
        """
        return self.call("GET", f"/consortia/{consortiumId}/user-tenants/{associationId}")



class ConsortiaConfiguration(FolioApi):
    """Consortia Configuration integration API

    Consortia Configuration integration API
    """

    def getconfiguration(self):
        """

        ``GET /consortia-configuration``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/ConsortiaConfiguration_getconfiguration_response.schema
        """
        return self.call("GET", "/consortia-configuration")

		
    def saveconfiguration(self, consortiaConfiguration):
        """

        ``POST /consortia-configuration``

        Args:
            consortiaConfiguration (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestConflict: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/ConsortiaConfiguration_saveconfiguration_request.schema
        """
        return self.call("POST", f"/consortia-configuration", consortiaConfiguration)



class Tenants(FolioApi):
    """Tenant integration API

    Tenant integration API
    """

    def gettenants(self, consortiumId, **kwargs):
        """

        ``GET /consortia/{consortiumId}/tenants``

        Args:
            consortiumId (str):

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Resource not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Tenants_gettenants_response.schema
        """
        return self.call("GET", f"/consortia/{consortiumId}/tenants", query=kwargs)

		
    def savetenant(self, consortiumId, tenant):
        """

        ``POST /consortia/{consortiumId}/tenants``

        Args:
            consortiumId (str):
            tenant (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Resource not found
            OkapiRequestConflict: Validation errors
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Tenants_savetenant_request.schema
        """
        return self.call("POST", f"/consortia/{consortiumId}/tenants", tenant)

    def updatetenant(self, consortiumId, tenantId, tenant):
        """

        ``PUT /consortia/{consortiumId}/tenants/{tenantId}``

        Args:
            consortiumId (str):
            tenantId (str): The ID of the tenant
            tenant (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Resource not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Tenants_updatetenant_request.schema
        """
        return self.call("PUT", f"/consortia/{consortiumId}/tenants/{tenantId}", tenant)

		
    def deletetenantbyid(self, consortiumId, tenantId):
        """

        ``DELETE /consortia/{consortiumId}/tenants/{tenantId}``

        Args:
            consortiumId (str):
            tenantId (str): The ID of the tenant

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Resource not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", f"/consortia/{consortiumId}/tenants/{tenantId}")



class Self(FolioApi):
    """Self integration API

    Self integration API
    """

    def getusertenantsforcurrentuser(self, consortiumId):
        """

        ``GET /consortia/{consortiumId}/_self``

        Args:
            consortiumId (str):

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestNotFound: Resource not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Self_getusertenantsforcurrentuser_response.schema
        """
        return self.call("GET", f"/consortia/{consortiumId}/_self")



class KafkaMessageSchemas(FolioApi):
    """mod-consortia schemas

    
    """

    def kafka_stub_endpoint(self):
        """

        ``GET /kafka-stub-endpoint``
        """
        return self.call("GET", "/kafka-stub-endpoint")



class Consortia(FolioApi):
    """Consortium integration API

    Consortium integration API
    """

    def getconsortiumcollection(self):
        """

        ``GET /consortia``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Consortia_getconsortiumcollection_response.schema
        """
        return self.call("GET", "/consortia")

		
    def saveconsortium(self, consortium):
        """

        ``POST /consortia``

        Args:
            consortium (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestConflict: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Consortia_saveconsortium_request.schema
        """
        return self.call("POST", f"/consortia", consortium)

    def getconsortium(self, consortiumId):
        """

        ``GET /consortia/{consortiumId}``

        Args:
            consortiumId (str):

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Consortia_getconsortium_response.schema
        """
        return self.call("GET", f"/consortia/{consortiumId}")

		
    def updateconsortium(self, consortiumId, consortium):
        """

        ``PUT /consortia/{consortiumId}``

        Args:
            consortiumId (str):
            consortium (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Resource not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Consortia_updateconsortium_request.schema
        """
        return self.call("PUT", f"/consortia/{consortiumId}", consortium)
