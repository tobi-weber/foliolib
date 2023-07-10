# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.permissions")


class TenantPermissions(FolioApi):
    """tenant permissions API implementation

    This API provides a callback point for Okapi when new permission sets are added to the tenant
    """

    def set_tenantpermission(self, tenantpermission: dict):
        """Load new permissionSets into the permission module when a module gets enabled for a tenant

        ``POST /_/tenantpermissions``

        Args:
            tenantpermission (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/TenantPermissions_set_tenantpermission_request.schema
        """
        return self.call("POST", "/_/tenantpermissions", data=tenantpermission)


class Permissions(FolioApi):
    """mod-permissions API

    This module is responsible for managing and retrieving permissions in the FOLIO system
    """

    def get_users(self, **kwargs):
        """Get a list of users

        ``GET /perms/users``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            length (int): (default=10) The maximum number of results to return. Deprecated: use limit
                    
                    Example:
                    
                     - 10
            start (int): (default=1) The starting index in a list of results starting from 1. Deprecated: use offset
            sortBy (str):  A comma-separated list of fieldnames to sort by
            query (str):  A query string to filter users based on matching criteria in fields.
            hasPermissions (str):  A list of permissions that any returned users must possess.

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestForbidden: Forbidden
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Permissions_get_users_return.schema 
        """
        return self.call("GET", "/perms/users", query=kwargs)

    def set_user(self, user: dict):
        """Add a new user

        ``POST /perms/users``

        Args:
            user (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestForbidden: Forbidden
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Permissions_set_user_request.schema
        """
        return self.call("POST", "/perms/users", data=user)

    def get_user(self, usersId: str, **kwargs):
        """Get a permission user

        ``GET /perms/users/{usersId}``

        Args:
            usersId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            indexField (str):  Specify a field other than 'id' to look up the permission user by
                    
                    Example:
                    
                     - userId

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestForbidden: Forbidden
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Permissions_get_user_return.schema 
        """
        return self.call("GET", f"/perms/users/{usersId}", query=kwargs)

    def modify_user(self, usersId: str, user: dict):
        """Modify an existing user

        ``PUT /perms/users/{usersId}``

        Args:
            usersId (str)
            user (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestForbidden: Forbidden
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Permissions_modify_user_request.schema
        """
        return self.call("PUT", f"/perms/users/{usersId}", data=user)

    def delete_user(self, usersId: str):
        """Remove a user

        ``DELETE /perms/users/{usersId}``

        Args:
            usersId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/perms/users/{usersId}")

    def get_permissions_for_user(self, usersId: str, **kwargs):
        """Get permissions that a user has

        ``GET /perms/users/{usersId}/permissions``

        Args:
            usersId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            expanded (str):  Recursively return all subpermissions
                    
                    Example:
                    
                     - true
            full (str):  Return full permission objects, as opposed to just permission names
                    
                    Example:
                    
                     - true
            indexField (str):  Specify a field other than 'id' to look up the permission user by
                    
                    Example:
                    
                     - userId

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestForbidden: Forbidden
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Permissions_get_permissions_for_user_return.schema 
        """
        return self.call("GET", f"/perms/users/{usersId}/permissions", query=kwargs)

    def get_permissions(self, **kwargs):
        """Get a list of existing permissions

        ``GET /perms/permissions``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            expandSubs (str):  Return one level of subpermissions as objects if true. If false or omitted, expanded will be considered.
                    
                    Example:
                    
                     - true
            expanded (str):  Recursively return all subpermissions as strings if true. Is only considered if expandSubs is false or omitted.
                    
                    Example:
                    
                     - true
            includeDummy (str):  Return placeholder 'dummy' permissions
                    
                    Example:
                    
                     - true
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            length (int): (default=10) The maximum number of results to return. Deprecated: use limit
                    
                    Example:
                    
                     - 10
            start (int): (default=1) The starting index in a list of results starting from 1. Deprecated: use offset
            sortBy (str):  A comma-separated list of fieldnames to sort by
            query (str):  A query string to filter users based on matching criteria in fields.
            memberOf (str):  A list of permission names that any returned permission must be a sub-permission of.
            ownedBy (str):  A list of user names that any returned permissions must belong to.

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Permissions_get_permissions_return.schema 
        """
        return self.call("GET", "/perms/permissions", query=kwargs)

    def set_permission_for_user(self, usersId: str, permission: dict, **kwargs):
        """Add a permission to a user

        ``POST /perms/users/{usersId}/permissions``

        Args:
            usersId (str)
            permission (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            indexField (str):  Specify a field other than 'id' to look up the permission user by
                    
                    Example:
                    
                     - userId

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestForbidden: Forbidden
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Permissions_set_permission_for_user_request.schema
        """
        return self.call("POST", f"/perms/users/{usersId}/permissions", data=permission, query=kwargs)

    def set_permission(self, permission: dict):
        """Add a new permission

        ``POST /perms/permissions``

        Args:
            permission (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Permissions_set_permission_request.schema
        """
        return self.call("POST", "/perms/permissions", data=permission)

    def get_permission(self, permissionsId: str):
        """Get an existing permission by id

        ``GET /perms/permissions/{permissionsId}``

        Args:
            permissionsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Permissions_get_permission_return.schema 
        """
        return self.call("GET", f"/perms/permissions/{permissionsId}")

    def modify_permission(self, permissionsId: str, permission: dict):
        """Modify an existing permission

        ``PUT /perms/permissions/{permissionsId}``

        Args:
            permissionsId (str)
            permission (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestForbidden: Forbidden
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Permissions_modify_permission_request.schema
        """
        return self.call("PUT", f"/perms/permissions/{permissionsId}", data=permission)

    def delete_permission_for_user(self, usersId: str, permissionname: str, **kwargs):
        """Remove a permission from a user

        ``DELETE /perms/users/{usersId}/permissions/{permissionname}``

        Args:
            usersId (str)
            permissionname (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            indexField (str):  Specify a field other than 'id' to look up the permission user by
                    
                    Example:
                    
                     - userId

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/perms/users/{usersId}/permissions/{permissionname}", query=kwargs)

    def delete_permission(self, permissionsId: str):
        """Remove a permission

        ``DELETE /perms/permissions/{permissionsId}``

        Args:
            permissionsId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/perms/permissions/{permissionsId}")

    def set_purgeDeprecated(self):
        """purge deprecated permissions

        ``POST /perms/purge-deprecated``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Permissions_set_purgeDeprecated_return.schema 
        """
        return self.call("POST", "/perms/purge-deprecated")
