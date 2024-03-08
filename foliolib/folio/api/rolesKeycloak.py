# -*- coding: utf-8 -*-
# Generated at 2024-03-23

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.rolesKeycloak")



class Roleskeycloak(FolioApi):
    """Mod Roles Keycloak API

    Mod Roles Keycloak API
    """

    def getrole(self, id_):
        """Get role by ID

        ``GET /roles/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_getrole_response.schema
        """
        return self.call("GET", f"/roles/{id_}")

		
    def updaterole(self, role, id_):
        """Update a role

        ``PUT /roles/{id}``

        Args:
            role (dict): See Schema below.

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_updaterole_request.schema
        """
        return self.call("PUT", f"/roles/{id_}", role)

		
    def deleterole(self, id_):
        """Delete a role

        ``DELETE /roles/{id}``
        """
        return self.call("DELETE", f"/roles/{id_}")

    def findroles(self, **kwargs):
        """Get roles by query

        ``GET /roles``

        Keyword Args:
            query (str): A query string to filter users based on matching criteria in fields.
            limit (int): Limit the number of elements returned in the response. (default: 10, minimum: 0)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_findroles_response.schema
        """
        return self.call("GET", "/roles", query=kwargs)

		
    def createrole(self, role):
        """Create a role

        ``POST /roles``

        Args:
            role (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_createrole_request.schema
        """
        return self.call("POST", f"/roles", role)

    def createroles(self, rolesRequest):
        """Create one or more roles

        ``POST /roles/batch``

        Args:
            rolesRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_createroles_request.schema
            .. literalinclude:: ../files/Roleskeycloak_createroles_request.schema_response.schema
        """
        return self.call("POST", f"/roles/batch", rolesRequest)

    def assignrolestouser(self, userRolesRequest):
        """Create a record associating role with user

        ``POST /roles/users``

        Args:
            userRolesRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_assignrolestouser_request.schema
            .. literalinclude:: ../files/Roleskeycloak_assignrolestouser_request.schema_response.schema
        """
        return self.call("POST", f"/roles/users", userRolesRequest)

		
    def finduserroles(self, **kwargs):
        """Search user-role relations by CQL query

        ``GET /roles/users``

        Keyword Args:
            query (str): A query string to filter users based on matching criteria in fields.
            limit (int): Limit the number of elements returned in the response. (default: 10, minimum: 0)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_finduserroles_response.schema
        """
        return self.call("GET", "/roles/users", query=kwargs)

    def getuserroles(self, id_):
        """Get roles user by user ID

        ``GET /roles/users/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_getuserroles_response.schema
        """
        return self.call("GET", f"/roles/users/{id_}")

		
    def updateuserroles(self, userRolesRequest, id_):
        """Update a roles user by user ID

        ``PUT /roles/users/{id}``

        Args:
            userRolesRequest (dict): See Schema below.

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_updateuserroles_request.schema
        """
        return self.call("PUT", f"/roles/users/{id_}", userRolesRequest)

		
    def deleteuserroles(self, id_):
        """Delete a roles user by user ID

        ``DELETE /roles/users/{id}``
        """
        return self.call("DELETE", f"/roles/users/{id_}")

    def createrolecapabilities(self, roleCapabilitiesRequest):
        """Create a record associating one or more capabilities with the role

        ``POST /roles/capabilities``

        Args:
            roleCapabilitiesRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_createrolecapabilities_request.schema
            .. literalinclude:: ../files/Roleskeycloak_createrolecapabilities_request.schema_response.schema
        """
        return self.call("POST", f"/roles/capabilities", roleCapabilitiesRequest)

		
    def getrolecapabilities(self, **kwargs):
        """Get role-capability relation items by CQL query and pagination parameters

        ``GET /roles/capabilities``

        Keyword Args:
            query (str): A query string to filter users based on matching criteria in fields.
            limit (int): Limit the number of elements returned in the response. (default: 10, minimum: 0)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_getrolecapabilities_response.schema
        """
        return self.call("GET", "/roles/capabilities", query=kwargs)

    def findcapabilitiesbyroleid(self, id_, **kwargs):
        """Get capabilities assigned to role by role identifier

        ``GET /roles/{id}/capabilities``

        Keyword Args:
            expand (bool): Defines if capability sets must be expanded (default: False)
            limit (int): Limit the number of elements returned in the response. (default: 10, minimum: 0)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_findcapabilitiesbyroleid_response.schema
        """
        return self.call("GET", f"/roles/{id_}/capabilities", query=kwargs)

		
    def updaterolecapabilities(self, capabilitiesUpdateRequest, id_):
        """Modifies the set of capabilities assigned to the specified role.

        ``PUT /roles/{id}/capabilities``

        Args:
            capabilitiesUpdateRequest (dict): See Schema below.

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_updaterolecapabilities_request.schema
        """
        return self.call("PUT", f"/roles/{id_}/capabilities", capabilitiesUpdateRequest)

		
    def deleterolecapabilities(self, id_):
        """Removes all capabilities assignments for the specified role identifier

        ``DELETE /roles/{id}/capabilities``

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("DELETE", f"/roles/{id_}/capabilities")

    def createrolecapabilitysets(self, roleCapabilitySetsRequest):
        """Create a record associating one or more capabilities with the role

        ``POST /roles/capability-sets``

        Args:
            roleCapabilitySetsRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_createrolecapabilitysets_request.schema
            .. literalinclude:: ../files/Roleskeycloak_createrolecapabilitysets_request.schema_response.schema
        """
        return self.call("POST", f"/roles/capability-sets", roleCapabilitySetsRequest)

		
    def getrolecapabilitysets(self, **kwargs):
        """Get role-capability-set relation items by CQL query

        ``GET /roles/capability-sets``

        Keyword Args:
            query (str): A query string to filter users based on matching criteria in fields.
            limit (int): Limit the number of elements returned in the response. (default: 10, minimum: 0)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_getrolecapabilitysets_response.schema
        """
        return self.call("GET", "/roles/capability-sets", query=kwargs)

    def getcapabilitysetsbyroleid(self, id_, **kwargs):
        """Get capability sets assigned to role by role identifier

        ``GET /roles/{id}/capability-sets``

        Keyword Args:
            limit (int): Limit the number of elements returned in the response. (default: 10, minimum: 0)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_getcapabilitysetsbyroleid_response.schema
        """
        return self.call("GET", f"/roles/{id_}/capability-sets", query=kwargs)

		
    def updaterolecapabilitysets(self, capabilitySetsUpdateRequest, id_):
        """Modifies the set of capability sets assigned to the specified role.

        ``PUT /roles/{id}/capability-sets``

        Args:
            capabilitySetsUpdateRequest (dict): See Schema below.

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_updaterolecapabilitysets_request.schema
        """
        return self.call("PUT", f"/roles/{id_}/capability-sets", capabilitySetsUpdateRequest)

		
    def deleterolecapabilitysets(self, id_):
        """Removes all capability sets assignments for the specified role identifier

        ``DELETE /roles/{id}/capability-sets``

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("DELETE", f"/roles/{id_}/capability-sets")

    def getpolicy(self, id_):
        """Get policy by ID

        ``GET /policies/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_getpolicy_response.schema
        """
        return self.call("GET", f"/policies/{id_}")

		
    def updatepolicy(self, policy, id_):
        """Update a policy

        ``PUT /policies/{id}``

        Args:
            policy (dict): See Schema below.

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_updatepolicy_request.schema
        """
        return self.call("PUT", f"/policies/{id_}", policy)

		
    def deletepolicy(self, id_):
        """Delete a policy

        ``DELETE /policies/{id}``
        """
        return self.call("DELETE", f"/policies/{id_}")

    def findpolicies(self, **kwargs):
        """Get policies by query

        ``GET /policies``

        Keyword Args:
            query (str): A query string to filter users based on matching criteria in fields.
            limit (int): Limit the number of elements returned in the response. (default: 10, minimum: 0)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_findpolicies_response.schema
        """
        return self.call("GET", "/policies", query=kwargs)

		
    def createpolicy(self, policy):
        """Create a policy

        ``POST /policies``

        Args:
            policy (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_createpolicy_request.schema
        """
        return self.call("POST", f"/policies", policy)

    def createpolicies(self, policiesRequest):
        """Create one or more policies

        ``POST /policies/batch``

        Args:
            policiesRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_createpolicies_request.schema
            .. literalinclude:: ../files/Roleskeycloak_createpolicies_request.schema_response.schema
        """
        return self.call("POST", f"/policies/batch", policiesRequest)

    def migratepolicies(self):
        """Migrate user policies from mod-permission to keycloak

        ``POST /roles-keycloak/migrate``

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("POST", "/roles-keycloak/migrate")

    def findcapabilities(self, **kwargs):
        """Get capabilities by query

        ``GET /capabilities``

        Keyword Args:
            query (str): A query string to filter users based on matching criteria in fields.
            limit (int): Limit the number of elements returned in the response. (default: 10, minimum: 0)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_findcapabilities_response.schema
        """
        return self.call("GET", "/capabilities", query=kwargs)

    def getcapabilitybyid(self, id_):
        """Get capability by ID

        ``GET /capabilities/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_getcapabilitybyid_response.schema
        """
        return self.call("GET", f"/capabilities/{id_}")

    def createcapabilityset(self, capabilitySet):
        """Create a capability set

        ``POST /capability-sets``

        Args:
            capabilitySet (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_createcapabilityset_request.schema
        """
        return self.call("POST", f"/capability-sets", capabilitySet)

		
    def findcapabilitysets(self, **kwargs):
        """Get capabilities by query

        ``GET /capability-sets``

        Keyword Args:
            query (str): A query string to filter users based on matching criteria in fields.
            limit (int): Limit the number of elements returned in the response. (default: 10, minimum: 0)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_findcapabilitysets_response.schema
        """
        return self.call("GET", "/capability-sets", query=kwargs)

    def createcapabilitysets(self, capabilitySets):
        """Create one or more capability sets

        ``POST /capability-sets/batch``

        Args:
            capabilitySets (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_createcapabilitysets_request.schema
        """
        return self.call("POST", f"/capability-sets/batch", capabilitySets)

    def getcapabilitysetbyid(self, id_):
        """Get capability set by ID

        ``GET /capability-sets/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_getcapabilitysetbyid_response.schema
        """
        return self.call("GET", f"/capability-sets/{id_}")

		
    def updatecapabilityset(self, capabilitySet, id_):
        """Update a capability set

        ``PUT /capability-sets/{id}``

        Args:
            capabilitySet (dict): See Schema below.

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_updatecapabilityset_request.schema
        """
        return self.call("PUT", f"/capability-sets/{id_}", capabilitySet)

		
    def deletecapabilityset(self, id_):
        """Delete a capability set

        ``DELETE /capability-sets/{id}``

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("DELETE", f"/capability-sets/{id_}")

    def findcapabilitiesbycapabilitysetid(self, id_, **kwargs):
        """Find capabilities by capability set ID

        ``GET /capability-sets/{id}/capabilities``

        Keyword Args:
            limit (int): Limit the number of elements returned in the response. (default: 10, minimum: 0)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_findcapabilitiesbycapabilitysetid_response.schema
        """
        return self.call("GET", f"/capability-sets/{id_}/capabilities", query=kwargs)

    def createusercapabilities(self, userCapabilitiesRequest):
        """Create a record associating one or more capabilities with a user.

        ``POST /users/capabilities``

        Args:
            userCapabilitiesRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_createusercapabilities_request.schema
            .. literalinclude:: ../files/Roleskeycloak_createusercapabilities_request.schema_response.schema
        """
        return self.call("POST", f"/users/capabilities", userCapabilitiesRequest)

		
    def getusercapabilities(self, **kwargs):
        """Search user capabilities by CQL query

        ``GET /users/capabilities``

        Keyword Args:
            query (str): A query string to filter users based on matching criteria in fields.
            limit (int): Limit the number of elements returned in the response. (default: 10, minimum: 0)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_getusercapabilities_response.schema
        """
        return self.call("GET", "/users/capabilities", query=kwargs)

    def findcapabilitiesbyuserid(self, id_, **kwargs):
        """Retrieve capabilities assigned to role by role identifier

        ``GET /users/{id}/capabilities``

        Keyword Args:
            expand (bool): Defines if capability sets must be expanded (default: False)
            limit (int): Limit the number of elements returned in the response. (default: 10, minimum: 0)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_findcapabilitiesbyuserid_response.schema
        """
        return self.call("GET", f"/users/{id_}/capabilities", query=kwargs)

		
    def updateusercapabilities(self, capabilitiesUpdateRequest, id_):
        """Modifies the set of capabilities assigned to the specified user.

        ``PUT /users/{id}/capabilities``

        Args:
            capabilitiesUpdateRequest (dict): See Schema below.

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_updateusercapabilities_request.schema
        """
        return self.call("PUT", f"/users/{id_}/capabilities", capabilitiesUpdateRequest)

		
    def deleteusercapabilities(self, id_):
        """Removes all capability assignments for the specified user identifier

        ``DELETE /users/{id}/capabilities``

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("DELETE", f"/users/{id_}/capabilities")

    def createusercapabilitysets(self, userCapabilitySetsRequest):
        """Create a record associating one or more capabilities with a user.

        ``POST /users/capability-sets``

        Args:
            userCapabilitySetsRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_createusercapabilitysets_request.schema
            .. literalinclude:: ../files/Roleskeycloak_createusercapabilitysets_request.schema_response.schema
        """
        return self.call("POST", f"/users/capability-sets", userCapabilitySetsRequest)

		
    def getusercapabilitysets(self, **kwargs):
        """Get user capabilities by CQL query and pagination parameters

        ``GET /users/capability-sets``

        Keyword Args:
            query (str): A query string to filter users based on matching criteria in fields.
            limit (int): Limit the number of elements returned in the response. (default: 10, minimum: 0)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_getusercapabilitysets_response.schema
        """
        return self.call("GET", "/users/capability-sets", query=kwargs)

    def getcapabilitysetsbyuserid(self, id_, **kwargs):
        """Retrieve capability sets assigned to role by role identifier

        ``GET /users/{id}/capability-sets``

        Keyword Args:
            limit (int): Limit the number of elements returned in the response. (default: 10, minimum: 0)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_getcapabilitysetsbyuserid_response.schema
        """
        return self.call("GET", f"/users/{id_}/capability-sets", query=kwargs)

		
    def updateusercapabilitysets(self, capabilitySetsUpdateRequest, id_):
        """Modifies the set of capability sets assigned to the specified user.

        ``PUT /users/{id}/capability-sets``

        Args:
            capabilitySetsUpdateRequest (dict): See Schema below.

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_updateusercapabilitysets_request.schema
        """
        return self.call("PUT", f"/users/{id_}/capability-sets", capabilitySetsUpdateRequest)

		
    def deleteusercapabilitysets(self, id_):
        """Removes all capability set assignments for the specified user identifier

        ``DELETE /users/{id}/capability-sets``

        Raises:
            OkapiRequestNotFound: Not found error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("DELETE", f"/users/{id_}/capability-sets")

    def getpermissionsuser(self, id_, **kwargs):
        """Get permissions by user ID

        ``GET /permissions/users/{id}``

        Keyword Args:
            onlyVisible (bool): Return only visible permission sets (default: False)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotImplemented: Operation is not supported error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Roleskeycloak_getpermissionsuser_response.schema
        """
        return self.call("GET", f"/permissions/users/{id_}", query=kwargs)
