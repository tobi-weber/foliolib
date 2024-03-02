# -*- coding: utf-8 -*-
# Generated at 2024-03-01

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.mgrTenantEntitlements")



class Mgrtenantentitlements(FolioApi):
    """mgr-tenant-entitlements API

    Tenant Entitlement Manager API
    """

    def create(self, entitlementRequestBody, **kwargs):
        """Installs/enables application for tenant.
Basic authorization is required to perform request (e.g. Authorization=Basic dXNlcjp1c2Vy).


        ``POST /entitlements``

        Args:
            entitlementRequestBody (dict): See Schema below.

        Keyword Args:
            tenantParameters (str): Parameters for tenant init
            ignoreErrors (bool): Okapi 4.2.0 and later, it is possible to ignore errors during the
install operation. This is done by supplying parameter `ignoreErrors=true`.
In this case, Okapi will try to upgrade all modules in the modules list,
regardless if one of them fails. However, for individual modules, if they
fail, their upgrade will not be committed. This is an experimental parameter
which was added to be able to inspect all problem(s) with module upgrade(s).
 (default: False)
            async (bool): Enables asynchronous install operation (default: False)
            purgeOnRollback (bool): Defines if module data must be purged on rollback. (default: False)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenantentitlements_create_request.schema
            .. literalinclude:: ../files/Mgrtenantentitlements_create_request.schema_response.schema
        """
        return self.call("POST", f"/entitlements", entitlementRequestBody, query=kwargs)

		
    def findbyquery(self, **kwargs):
        """Retrieves all the entitlement using query tools (CQL query, limit and offset parameters).
Basic authorization is required to perform request (e.g. Authorization=Basic dXNlcjp1c2Vy).


        ``GET /entitlements``

        Keyword Args:
            query (str): A CQL query string with search conditions. (default: cql.allRecords=1)
            includeModules (bool): Indicates if list of modules should be loaded for each entitlement. (default: False)
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 10)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, default: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenantentitlements_findbyquery_response.schema
        """
        return self.call("GET", "/entitlements", query=kwargs)

		
    def delete(self, entitlementRequestBody, **kwargs):
        """Delete application installation by id, when making request add basic authorization
for an admin user (e.g. Basic YWRtaW46YWRtaW4=).


        ``DELETE /entitlements``

        Args:
            entitlementRequestBody (dict): See Schema below.

        Keyword Args:
            tenantParameters (str): Parameters for tenant init
            ignoreErrors (bool): Okapi 4.2.0 and later, it is possible to ignore errors during the
install operation. This is done by supplying parameter `ignoreErrors=true`.
In this case, Okapi will try to upgrade all modules in the modules list,
regardless if one of them fails. However, for individual modules, if they
fail, their upgrade will not be committed. This is an experimental parameter
which was added to be able to inspect all problem(s) with module upgrade(s).
 (default: False)
            purge (bool): Disabled modules will also be purged. (default: False)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenantentitlements_delete_request.schema
            .. literalinclude:: ../files/Mgrtenantentitlements_delete_request.schema_response.schema
        """
        return self.call("DELETE", f"/entitlements", entitlementRequestBody, query=kwargs)

    def findentitlementsbytenantid(self, tenantId, **kwargs):
        """List of tenant entitlements

        ``GET /entitlements/{tenantId}``

        Args:
            tenantId (str): Tenant id

        Keyword Args:
            includeModules (bool): Indicates if list of modules should be loaded for each entitlement. (default: False)
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 10)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, default: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenantentitlements_findentitlementsbytenantid_response.schema
        """
        return self.call("GET", f"/entitlements/{tenantId}", query=kwargs)

    def findentitledapplicationsbytenantname(self, tenantName, **kwargs):
        """List of application descriptors entitled for the tenant

        ``GET /entitlements/{tenantName}/applications``

        Args:
            tenantName (str): Tenant name

        Keyword Args:
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 10)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, default: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenantentitlements_findentitledapplicationsbytenantname_response.schema
        """
        return self.call("GET", f"/entitlements/{tenantName}/applications", query=kwargs)

    def getmoduleentitlements(self, moduleId, **kwargs):
        """Retrieve a list of module entitlements

        ``GET /entitlements/modules/{moduleId}``

        Args:
            moduleId (str): Module id

        Keyword Args:
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 10)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, default: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenantentitlements_getmoduleentitlements_response.schema
        """
        return self.call("GET", f"/entitlements/modules/{moduleId}", query=kwargs)

    def validate(self, entitlementRequestBody, **kwargs):
        """Validates an entitlement request against a set of pre-configured validators
that are also applied during the entitlement process or a single validator specified as a parameter.


        ``POST /entitlements/validate``

        Args:
            entitlementRequestBody (dict): See Schema below.

        Keyword Args:
            entitlementType (str): Entitlement type
            validator (str): Name of entitlement validator to be applied.
All existing validators will be applied if none specified


        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenantentitlements_validate_request.schema
        """
        return self.call("POST", f"/entitlements/validate", entitlementRequestBody, query=kwargs)

    def getentitlementflowbyid(self, flowId, **kwargs):
        """Retrieves a flow by id

        ``GET /entitlement-flows/{flowId}``

        Args:
            flowId (str): A flow identifier (format: uuid)

        Keyword Args:
            includeStages (bool): Defines if stages must be included in the response for entitlement/application flows (default: False)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenantentitlements_getentitlementflowbyid_response.schema
        """
        return self.call("GET", f"/entitlement-flows/{flowId}", query=kwargs)

    def findapplicationflows(self, **kwargs):
        """Retrieves an application entitlement flows by CQL query

        ``GET /application-flows``

        Keyword Args:
            query (str): A CQL query string with search conditions. (default: cql.allRecords=1)
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 10)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, default: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenantentitlements_findapplicationflows_response.schema
        """
        return self.call("GET", "/application-flows", query=kwargs)

    def getapplicationflowbyid(self, applicationFlowId, **kwargs):
        """Retrieves an entitlement flow per applicationId

        ``GET /application-flows/{applicationFlowId}``

        Args:
            applicationFlowId (str): An application flow identifier (format: uuid)

        Keyword Args:
            includeStages (bool): Defines if stages must be included in the response for entitlement/application flows (default: False)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenantentitlements_getapplicationflowbyid_response.schema
        """
        return self.call("GET", f"/application-flows/{applicationFlowId}", query=kwargs)

    def findentitlementstages(self, applicationFlowId):
        """Retrieves entitlement stages by application id

        ``GET /application-flows/{applicationFlowId}/stages``

        Args:
            applicationFlowId (str): An application flow identifier (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenantentitlements_findentitlementstages_response.schema
        """
        return self.call("GET", f"/application-flows/{applicationFlowId}/stages")

    def getentitlementstagebyname(self, applicationFlowId, stageName):
        """Retrieves entitlement stages by application id

        ``GET /application-flows/{applicationFlowId}/stages/{stageName}``

        Args:
            applicationFlowId (str): An application flow identifier (format: uuid)
            stageName (str): An application stage name

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Mgrtenantentitlements_getentitlementstagebyname_response.schema
        """
        return self.call("GET", f"/application-flows/{applicationFlowId}/stages/{stageName}")
