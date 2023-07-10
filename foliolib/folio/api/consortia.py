# -*- coding: utf-8 -*-
# Generated at 2023-07-10

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



class SharingInstance(FolioApi):
    """Sharing instance integration API

    Sharing instance integration API
    """

    def getsharinginstances(self, consortiumId, **kwargs):
        """Sharing instances

        ``GET /consortia/{consortiumId}/sharing/instances``

        Args:
            consortiumId (str):

        Keyword Args:
            instanceIdentifier (str):
            sourceTenantId (str): The ID of the source tenant
            targetTenantId (str): The ID of the target tenant
            status (str):
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Resource not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/SharingInstance_getsharinginstances_response.schema
        """
        return self.call("GET", f"/consortia/{consortiumId}/sharing/instances", query=kwargs)

		
    def start(self, consortiumId, sharingInstance):
        """

        ``POST /consortia/{consortiumId}/sharing/instances``

        Args:
            consortiumId (str):
            sharingInstance (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Resource not found
            OkapiRequestConflict: Validation errors
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/SharingInstance_start_request.schema
        """
        return self.call("POST", f"/consortia/{consortiumId}/sharing/instances", sharingInstance)

    def getsharinginstancebyid(self, consortiumId, actionId):
        """

        ``GET /consortia/{consortiumId}/sharing/instances/{actionId}``

        Args:
            consortiumId (str):
            actionId (str):

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Resource not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/SharingInstance_getsharinginstancebyid_response.schema
        """
        return self.call("GET", f"/consortia/{consortiumId}/sharing/instances/{actionId}")



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

		
    def savetenant(self, consortiumId, tenant, **kwargs):
        """

        ``POST /consortia/{consortiumId}/tenants``

        Args:
            consortiumId (str):
            tenant (dict): See Schema below.

        Keyword Args:
            adminUserId (str):

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
        return self.call("POST", f"/consortia/{consortiumId}/tenants", tenant, query=kwargs)

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

    def syncprimaryaffiliations(self, consortiumId, tenantId):
        """

        ``POST /consortia/{consortiumId}/tenants/{tenantId}/sync-primary-affiliations``

        Args:
            consortiumId (str):
            tenantId (str): The ID of the tenant

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Resource not found
            OkapiRequestConflict: Validation errors
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Internal server error
        """
        return self.call("POST", f"/consortia/{consortiumId}/tenants/{tenantId}/sync-primary-affiliations")

    def createprimaryaffiliations(self, consortiumId, tenantId, syncPrimaryAffiliationBody):
        """

        ``POST /consortia/{consortiumId}/tenants/{tenantId}/create-primary-affiliations``

        Args:
            consortiumId (str):
            tenantId (str): The ID of the tenant
            syncPrimaryAffiliationBody (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Resource not found
            OkapiRequestConflict: Validation errors
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Tenants_createprimaryaffiliations_request.schema
        """
        return self.call("POST", f"/consortia/{consortiumId}/tenants/{tenantId}/create-primary-affiliations", syncPrimaryAffiliationBody)



class Publications(FolioApi):
    """Publish coordinator API

    Publish coordinator API
    """

    def publishrequests(self, consortiumId, publicationRequest):
        """

        ``POST /consortia/{consortiumId}/publications``

        Args:
            consortiumId (str):
            publicationRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestConflict: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Publications_publishrequests_request.schema
            .. literalinclude:: ../files/Publications_publishrequests_request.schema_response.schema
        """
        return self.call("POST", f"/consortia/{consortiumId}/publications", publicationRequest)

    def getpublicationdetails(self, consortiumId, publicationId):
        """

        ``GET /consortia/{consortiumId}/publications/{publicationId}``

        Args:
            consortiumId (str):
            publicationId (str):

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Publications_getpublicationdetails_response.schema
        """
        return self.call("GET", f"/consortia/{consortiumId}/publications/{publicationId}")



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
