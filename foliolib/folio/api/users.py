# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.users")


class Departments(FolioApi):
    """mod-users Departments API

    This documents the API calls that can be made to query and manage departments of the system
    """

    def get_departments(self, **kwargs):
        """Return a list of departmants

        ``GET /departments``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - attributes.code=="*acc*"
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Departments_get_departments_return.schema 
        """
        return self.call("GET", "/departments", query=kwargs)

    def set_department(self, department: dict):
        """Create a departmant

        ``POST /departments``

        Args:
            department (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created department item

        Schema:

            .. literalinclude:: ../files/Departments_set_department_request.schema
        """
        return self.call("POST", "/departments", data=department)

    def get_department(self, departmentId: str):
        """Retrieve department item with given {departmentId}

        ``GET /departments/{departmentId}``

        Args:
            departmentId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Departments_get_department_return.schema 
        """
        return self.call("GET", f"/departments/{departmentId}")

    def delete_department(self, departmentId: str):
        """Delete department item with given {departmentId}

        ``DELETE /departments/{departmentId}``

        Args:
            departmentId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/departments/{departmentId}")

    def modify_department(self, departmentId: str, department: dict):
        """Update department item with given {departmentId}

        ``PUT /departments/{departmentId}``

        Args:
            departmentId (str)
            department (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Departments_modify_department_request.schema
        """
        return self.call("PUT", f"/departments/{departmentId}", data=department)


class ProxiesFor(FolioApi):
    """mod-users Proxy For API

    This documents the API calls that can be made to query and manage proxy relationships for users
    """

    def get_proxiesfors(self, **kwargs):
        """Return a list of all proxy relationships

        ``GET /proxiesfor``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ProxiesFor_get_proxiesfors_return.schema 
        """
        return self.call("GET", "/proxiesfor", query=kwargs)

    def set_proxiesfor(self, proxiesfor: dict):
        """Create a proxyFor relationship

        ``POST /proxiesfor``

        Args:
            proxiesfor (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created proxiesfor item

        Schema:

            .. literalinclude:: ../files/ProxiesFor_set_proxiesfor_request.schema
        """
        return self.call("POST", "/proxiesfor", data=proxiesfor)

    def get_proxiesfor(self, proxiesforId: str):
        """Retrieve proxiesfor item with given {proxiesforId}

        ``GET /proxiesfor/{proxiesforId}``

        Args:
            proxiesforId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ProxiesFor_get_proxiesfor_return.schema 
        """
        return self.call("GET", f"/proxiesfor/{proxiesforId}")

    def delete_proxiesfor(self, proxiesforId: str):
        """Delete proxiesfor item with given {proxiesforId}

        ``DELETE /proxiesfor/{proxiesforId}``

        Args:
            proxiesforId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/proxiesfor/{proxiesforId}")

    def modify_proxiesfor(self, proxiesforId: str, proxiesfor: dict):
        """Update proxiesfor item with given {proxiesforId}

        ``PUT /proxiesfor/{proxiesforId}``

        Args:
            proxiesforId (str)
            proxiesfor (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ProxiesFor_modify_proxiesfor_request.schema
        """
        return self.call("PUT", f"/proxiesfor/{proxiesforId}", data=proxiesfor)


class AddressTypes(FolioApi):
    """mod-users Address Types API

    This documents the API calls that can be made to query and manage user address types of the system
    """

    def get_addresstypes(self, **kwargs):
        """Return a list of address types

        ``GET /addresstypes``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - addressType=primary
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AddressTypes_get_addresstypes_return.schema 
        """
        return self.call("GET", "/addresstypes", query=kwargs)

    def set_addresstype(self, addresstype: dict):
        """Create an address type

        ``POST /addresstypes``

        Args:
            addresstype (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created addresstype item

        Schema:

            .. literalinclude:: ../files/AddressTypes_set_addresstype_request.schema
        """
        return self.call("POST", "/addresstypes", data=addresstype)

    def get_addresstype(self, addresstypeId: str):
        """Retrieve addresstype item with given {addresstypeId}

        ``GET /addresstypes/{addresstypeId}``

        Args:
            addresstypeId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AddressTypes_get_addresstype_return.schema 
        """
        return self.call("GET", f"/addresstypes/{addresstypeId}")

    def delete_addresstype(self, addresstypeId: str):
        """Delete addresstype item with given {addresstypeId}

        ``DELETE /addresstypes/{addresstypeId}``

        Args:
            addresstypeId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/addresstypes/{addresstypeId}")

    def modify_addresstype(self, addresstypeId: str, addresstype: dict):
        """Update addresstype item with given {addresstypeId}

        ``PUT /addresstypes/{addresstypeId}``

        Args:
            addresstypeId (str)
            addresstype (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AddressTypes_modify_addresstype_request.schema
        """
        return self.call("PUT", f"/addresstypes/{addresstypeId}", data=addresstype)


class Users(FolioApi):
    """mod-users API

    This documents the API calls that can be made to query and manage users of the system
    """

    def get_users(self, **kwargs):
        """Return a list of users

        ``GET /users``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - active=true sortBy username
            orderBy (str):  Order by field: field A, field B
                    
            order (str (desc|asc):): (default=desc) Order
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Users_get_users_return.schema 
        """
        return self.call("GET", "/users", query=kwargs)

    def set_user(self, user: dict):
        """Create a user

        ``POST /users``

        Args:
            user (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created user item

        Schema:

            .. literalinclude:: ../files/Users_set_user_request.schema
        """
        return self.call("POST", "/users", data=user)

    def delete_users(self):
        """

        ``DELETE /users``
        """
        return self.call("DELETE", "/users")

    def get_user(self, userId: str):
        """Get a single user

        ``GET /users/{userId}``

        Args:
            userId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Users_get_user_return.schema 
        """
        return self.call("GET", f"/users/{userId}")

    def delete_user(self, userId: str):
        """Delete user item with given {userId}

        ``DELETE /users/{userId}``

        Args:
            userId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/users/{userId}")

    def modify_user(self, userId: str, user: dict):
        """Update user item with given {userId}

        ``PUT /users/{userId}``

        Args:
            userId (str)
            user (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Users_modify_user_request.schema
        """
        return self.call("PUT", f"/users/{userId}", data=user)

    def set_timer(self):
        """Expire timer (timer event)

        ``POST /users/expire/timer``

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("POST", "/users/expire/timer")

    def set_process(self):
        """Read audit events from DB and send them to Kafka

        ``POST /users/outbox/process``
        """
        return self.call("POST", "/users/outbox/process")


class Groups(FolioApi):
    """mod-users Groups API

    This documents the API calls that can be made to query and manage user groups of the system
    """

    def get_groups(self, **kwargs):
        """Return a list of groups

        ``GET /groups``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - group=*grad*
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Groups_get_groups_return.schema 
        """
        return self.call("GET", "/groups", query=kwargs)

    def set_group(self, group: dict):
        """Create a group

        ``POST /groups``

        Args:
            group (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created group item

        Schema:

            .. literalinclude:: ../files/Groups_set_group_request.schema
        """
        return self.call("POST", "/groups", data=group)

    def get_group(self, groupId: str):
        """Retrieve group item with given {groupId}

        ``GET /groups/{groupId}``

        Args:
            groupId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Groups_get_group_return.schema 
        """
        return self.call("GET", f"/groups/{groupId}")

    def delete_group(self, groupId: str):
        """Delete group item with given {groupId}

        ``DELETE /groups/{groupId}``

        Args:
            groupId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/groups/{groupId}")

    def modify_group(self, groupId: str, group: dict):
        """Update group item with given {groupId}

        ``PUT /groups/{groupId}``

        Args:
            groupId (str)
            group (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Groups_modify_group_request.schema
        """
        return self.call("PUT", f"/groups/{groupId}", data=group)


class UserTenants(FolioApi):
    """mod-users User tenants API

    Records that show the primary tenant for a user when doing single-sign-on
    """

    def get_userTenants(self, **kwargs):
        """Return a list of user tenants

        ``GET /user-tenants``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/UserTenants_get_userTenants_return.schema 
        """
        return self.call("GET", "/user-tenants", query=kwargs)

    def set_userTenant(self, userTenant: dict):
        """Create a user-tenant

        ``POST /user-tenants``

        Args:
            userTenant (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created userTenant item

        Schema:

            .. literalinclude:: ../files/UserTenants_set_userTenant_request.schema
        """
        return self.call("POST", "/user-tenants", data=userTenant)


class Patronpin(FolioApi):
    """patron-pins API

    This documents the API calls that can be made to set and verify patron pins
    """

    def set_patronPin(self, patronPin: dict):
        """Set the PIN for a user

        ``POST /patron-pin``

        Args:
            patronPin (dict): See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Patronpin_set_patronPin_request.schema
        """
        return self.call("POST", "/patron-pin", data=patronPin)

    def delete_patronPins(self, patronPin: dict):
        """Remove the PIN for a user

        ``DELETE /patron-pin``

        Args:
            patronPin (dict): See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Patronpin_delete_patronPins_request.schema
        """
        return self.call("DELETE", "/patron-pin", data=patronPin)

    def set_verify(self, verify: dict):
        """Verify the pin posted

        ``POST /patron-pin/verify``

        Args:
            verify (dict): See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Patronpin_set_verify_request.schema
        """
        return self.call("POST", "/patron-pin/verify", data=verify)
