# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import logging

from pyokapi.folio import FolioServices
from pyokapi.folio.exceptions import PermissionUserNotFound, UserNotFound
from pyokapi.okapi.exceptions import OkapiInvalid

log = logging.getLogger("okapi.folio.users")


class UserServices(FolioServices):
    """
    mod-login, mod-users, mod-permissions

    Create a user:
    set user => userId 
                        -> set credential => credentialId
                        -> set permissionUser => permissionUserId
    """

    def get_user(self, username: str):
        users = self.get_users(query=f"username=={username}")
        if not users["users"]:
            raise UserNotFound(f"User {username} not found.")
        return users["users"][0]

    def get_users(self, **query):
        return self.call("GET", "users", query=query)

    def set_user(self, username: str, active: bool = True, **userdata):
        try:
            userId = self.get_user(username)["id"]
            user = {
                "id": userId,
                "username": username,
                "active": active
            }
            user.update(userdata)
            return self.call("PUT", f"users/{userId}", data=user)
        except UserNotFound:
            user = {
                "username": username,
                "active": active
            }
            user.update(userdata)
            return self.call("POST", "users", data=user)

    def delete_user(self, username: str):
        userId = self.get_user(username)["id"]
        return self.call("DELETE", f"users/{userId}")

    def create_user(self, username: str, password: str, permissions: list = None, **userdata):
        try:
            user = self.get_user(username)
            log.info("User already exists")
            return user
        except UserNotFound:
            log.info("Create user record.")
            user = self.set_user(username, **userdata)
            # print(user)

            log.info("Create login record.")
            self.set_credentials(username, password)

            if permissions is not None:
                log.info("Set permissions %s for user record.",
                         str(permissions))
                self.set_permission_user(username, permissions)

    def login(self, username: str, password: str):
        credentials = {"username": username, "password": password}
        return self.call("POST", "/authn/login", credentials)

    def set_credentials(self, username: str, password: str):
        user = self.get_user(username)
        credentials = {
            "userId": user["id"],
            "password": password
        }
        return self.call("POST", "/authn/credentials", data=credentials)

    def is_credentials(self, username: str):
        userId = self.get_user(username)["id"]
        return self.call("GET", "/authn/credentials-existence", query={"userId": userId})

    def delete_credentials(self, username: str):
        user = self.get_user(username)
        return self.call("Delete", "/authn/credentials", query={"userId": user["id"]})

    def get_permission_user(self, username: str):
        userId = self.get_user(username)["id"]
        perm_users = self.get_permission_users(query=f"userId={userId}")
        if not perm_users["permissionUsers"]:
            raise PermissionUserNotFound(
                f"PermissionUser for {username} not found.")
        return perm_users["permissionUsers"][0]

    def get_permission_users(self, **query):
        """
        length: (integer - default: 10 - minimum: 1 - maximum: 2147483647)
        The maximum number of results to return.

        start: (integer - default: 1 - minimum: 1 - maximum: 2147483647)
        The starting index in a list of results (starts at one).

        sortBy: (string)
        A comma-separated list of fieldnames to sort by

        query: (string)
        A query string to filter users based on matching criteria in fields.

        hasPermissions: (string)
        A list of permissions that any returned users must possess.
        """
        return self.call("GET", "perms/users", query=query)

    def set_permission_user(self, username: str, permissions: str):
        try:
            permUserId = self.get_permission_user(username)["id"]
            return self.call("PUT", f"perms/users/{permUserId}")
        except PermissionUserNotFound:
            user = self.get_user(username)
            perms_user = {"userId":  user["id"],
                          "permissions": permissions
                          }
            return self.call("POST", "perms/users", data=perms_user)

    def delete_permission_user(self, username: str):
        permUserId = self.get_permission_user(username)["id"]
        return self.call("DELETE", f"perms/users/{permUserId}")

    def get_permissions(self, username: str, **query):
        """
        Query Parameters
        expanded: (string)
        Recursively return all subpermissions

        Example:

        true
        full: (string)
        Return full permission objects, as opposed to just permission names

        Example:

        true
        indexField: (string)
        Specify a field other than 'id' to look up the permission user by
        """
        permUserId = self.get_permission_user(username)["id"]
        return self.call("GET", f"perms/users/{permUserId}/permissions", query=query)

    def set_permission(self, username: str, permissionName: str):
        self.set_permissions(username, [permissionName])

    def set_permissions(self,  username: str, permissionNames: list):
        permUserId = self.get_permission_user(username)["id"]
        perms = self.get_permissions(username)["permissionNames"]
        for permissionName in permissionNames:
            if not permissionName in perms:
                self.call("POST", f"perms/users/{permUserId}/permissions",
                          {"permissionName": permissionName})
                log.debug("%s assigned", permissionName)
            else:
                log.error("%s for %s already assigned",
                          permissionName, username)

    def delete_permission(self, username: str, permissionName: str):
        permUserId = self.get_permission_user(username)["id"]
        self.call(
            "DELETE", f"perms/users/{permUserId}/permissions/{permissionName}")
        log.debug("%s for %s deleted", permissionName, username)

    def get_exisiting_permissions(self, **query):
        """
        Query Parameters
        expandSubs: (string)
        Return one level of subpermissions as objects if true. If false or omitted, expanded will be considered.

        Example: true

        expanded: (string)
        Recursively return all subpermissions as strings if true. Is only considered if expandSubs is false or omitted.

        Example: true

        includeDummy: (string)
        Return placeholder 'dummy' permissions

        Example: true

        length: (integer - default: 10 - minimum: 1 - maximum: 2147483647)
        The maximum number of results to return.

        start: (integer - default: 1 - minimum: 1 - maximum: 2147483647)
        The starting index in a list of results (starts at one).

        sortBy: (string)
        A comma-separated list of fieldnames to sort by

        query: (string)
        A query string to filter users based on matching criteria in fields.

        memberOf: (string)
        A list of permission names that any returned permission must be a sub-permission of.

        ownedBy: (string)
        A list of user names that any returned permissions must belong to.
        """
        return self.call("GET", "perms/permissions", query=query)

    def set_new_permission(self, permission: dict):
        return self.call("POST", "perms/permissions", data=permission)

    def get_exisiting_permission(self, permissionId: str):
        return self.call("GET", f"perms/permissions/{permissionId}")

    def modify_existing_permission(self, permissionId: str, permission: dict):
        return self.call("PUT", f"perms/permissions/{permissionId}", data=permission)

    def delete_existing_permission(self, permissionId: str):
        return self.call("DELETE", f"perms/permissions/{permissionId}")
