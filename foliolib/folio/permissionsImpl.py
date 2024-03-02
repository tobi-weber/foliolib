# -*- coding: utf-8 -*-
# Copyright (C) 2023 Tobias Weber <tobi-weber@gmx.de>

import logging

from foliolib.folio import FolioAPIImpl
from foliolib.folio.api.permissions import Permissions
from foliolib.folio.exceptions import (PermissionNotFound,
                                       PermissionUserNotFound)
from foliolib.helper import is_valid_uuid
from foliolib.okapi.exceptions import OkapiRequestNotFound

log = logging.getLogger("foliolib.folio.permission")


class PermissionsImpl(FolioAPIImpl):
    """Implentations of permissions related functions.
    """

    def __init__(self, tenant: str) -> None:
        """
        Args:
            tenant (str): Tenant id
        """
        super().__init__(tenant)
        self._permissions = Permissions(tenant)

    def get_permission(self, name_or_id):
        """Get a permission by permissionName or id

        Args:
            name_or_id (str): PermissionName or id

        Raises:
            PermissionNotFound: Permission not found.

        Returns:
            dict: Dict with permission data
        """
        if is_valid_uuid(name_or_id):
            try:
                return self._permissions.get_permission(name_or_id)
            except OkapiRequestNotFound:
                raise PermissionNotFound(f"Permission {name_or_id} not found.")
        else:
            perms = self._permissions.get_permissions(
                query=f"permissionName={name_or_id}")
            if not perms["permissions"]:
                raise PermissionNotFound(f"Permission {name_or_id} not found.")
            return perms["permissions"][0]

    def get_permissions(self, query: str = None):
        """Get permissions by query or get all permissions.

        Args:
            query (str, optional): CQL string. Default to None, all objects will be returned.

        Returns:
            list: List with permission objects.
        """
        permissions = []
        count = self._permissions.get_permissions()["totalRecords"]
        query = query or "id=* sortby id"
        for i in range(0, count, 1000):
            permissions += self._permissions.get_permissions(query=query,
                                                             offset=i, limit=1000)["permissions"]

        return permissions

    def get_user(self, userId: str):
        """Get a permissionUser by user id.

        Raises:
            PermissionUserNotFound: User not found.

        Args:
            userId (str): user id.
        """
        try:
            return self._permissions.get_users(query=f"userId={userId}")["permissionUsers"][0]
        except IndexError:
            raise PermissionUserNotFound(
                f"PermissionUser for user {userId} not found.")

    def get_users(self, query: str = None):
        """Get permissionUsers.

        Args:
            query (str, optional): CQL string. Default to None, all objects will be returned.

        Returns:
            list: List with permissionUser objects.
        """
        permissionUsers = []
        count = self._permissions.get_users()["totalRecords"]
        query = query or "id=* sortby id"
        for i in range(0, count, 1000):
            permissionUsers += self._permissions.get_users(query=query,
                                                           offset=i, limit=1000)["permissionUsers"]

        return permissionUsers

    def add_user(self, userId: str, permissions: list = None):
        """Add a permissionUser.

        Args:
            userId (str): user id.
            permissions (list, optional): List of permissionNames. Defaults to None.
        """

        data = {"userId":  userId}
        if permissions is not None:
            data["permissions"] = permissions
        self._permissions.set_user(data)

    def delete_user(self, userId: str):
        """Delete a permissionUser.

        Raises:
            PermissionUserNotFound: User not found.

        Args:
            userId (str): user id.
        """
        permUserId = self.get_user(userId)["id"]
        self._permissions.delete_user(permUserId)

    def get_permissions_for_user(self, userId: str):
        """Get permissions fof a user.

        Raises:
            PermissionUserNotFound: User not found.

        Args:
            userId (str): user id.
        """
        permUserId = self.get_user(userId)["id"]
        return self._permissions.get_permissions_for_user(permUserId)["permissionNames"]

    def set_permission_for_user(self, userId: str, permissionName: str):
        """Set a permission by permissionName for a user.

        Raises:
            PermissionUserNotFound: User not found.

        Args:
            userId (str): user id.
            permissionName (str): permission name.
        """
        permUserId = self.get_user(userId)["id"]
        self._permissions.set_permission_for_user(permUserId,
                                                  {"permissionName": permissionName})

    def delete_permission_for_user(self, userId: str, permissionName: str):
        """Delete a permission by permissionName for a user.

        Raises:
            PermissionUserNotFound: User not found.

        Args:
            userId (str): user id.
            permissionName (str): permission name.
        """
        permUserId = self.get_user(userId)["id"]
        self._permissions.delete_permission_for_user(
            permUserId, permissionName)

    def get_topLevelPermissions(self):
        """Get all available top level permissions.

        Returns:
            list: List with permission instances.
        """
        perms = self._permissions.get_permissions(
            query="cql.allRecords=1 not permissionName==okapi.* not permissionName==modperms.* not permissionName==SYS#*",
            length="5000")
        topLevelPermissions = []
        for permission in perms["permissions"]:
            mods_perms = 0
            for s in permission["childOf"]:
                if s.startswith("SYS#") or s.startswith("modperms"):
                    mods_perms += 1
            if len(permission["childOf"]) == mods_perms:
                topLevelPermissions.append(permission)

        return sorted(topLevelPermissions, key=lambda d: d["permissionName"])
