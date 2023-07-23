# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import logging

from foliolib.folio import FolioService
from foliolib.folio.api.inventoryStorage import ServicePoint, ServicePointsUser
from foliolib.folio.api.login import Login
from foliolib.folio.api.permissions import Permissions
from foliolib.folio.api.users import Users as UsersApi
from foliolib.folio.exceptions import (PermissionUserNotFound,
                                       ServicePointsUserNotFound, UserNotFound)
from foliolib.okapi.exceptions import OkapiRequestNotFound

log = logging.getLogger("foliolib.folio.users")


class Users(FolioService):
    """
    """

    def __init__(self, tenant: str) -> None:
        """
        Args:
            tenant (str): Tenant id
        """
        super().__init__(tenant)
        self._users = UsersApi(tenant)
        self._permissions = Permissions(tenant)
        self._login = Login(tenant)
        self._servicePoint = ServicePoint(tenant)
        self._servicePointsUser = ServicePointsUser(tenant)

    def login(self, username: str, password: str):
        """Make a authentication.

        Args:
            username (str): Username
            password (str): Password

        Returns:
            dict: Instance of the authenticated user. If login failed, None is returned.
        """
        self._login.set_login({"username": username,
                               "password": password})
        headers = self._login.get_okapiClient().headers
        if "x-okapi-token" in headers:
            return headers["x-okapi-token"]
        return None

    def set_password(self, username: str, password: str):
        """Set a new password for given username.

        Args:
            username (str): Username
            password (str): Password
        Returns:
            bool: Wether set password was successful
        """
        log.info("Set password for user %s", username)
        userId = self.get_user(username)["id"]
        try:
            self._login.delete_credentials(userId=userId)
            self._login.set_credential({"userId": userId,
                                        "password": password
                                        })
            return True
        except Exception as err:
            log.error(err)
            return False

    def get_users(self, query=None):
        """Get all users

        Returns:
            dic: Dict with users
        """
        return self._users.get_users()["users"]

    def get_user(self, username: str):
        """Get a user by username

        Args:
            username (str): Username

        Raises:
            UserNotFound: User not found

        Returns:
            dict: Dict with user data
        """
        users = self._users.get_users(query=f"username=={username}")
        if not users["users"]:
            raise UserNotFound(f"User {username} not found.")
        return users["users"][0]

    def create_user(self, username: str, password: str, permissions: list = None, **kwargs):
        """Create a user

        Args:
            username (str): Username
            password (str): Password
            permissions (list, optional): List with permissions. Defaults to None.

        Returns:
            dict: Dict with user data
        """
        try:
            user = self.get_user(username)
            log.info("User already exists")
            return user
        except UserNotFound:
            log.info("Create user %s", username)
            userData = {"username": username,
                        "active": True}
            userData.update(kwargs)
            user = self._users.set_user(userData)

            log.info("Create login record.")
            self._login.set_credential({"userId": user["id"],
                                        "password": password
                                        })
            log.info("Add User to permissions")
            data = {"userId":  user["id"]}
            if permissions is not None:
                data["permissions"] = permissions
            self._permissions.set_user(data)
        log.info("User %s created", username)
        return user

    def delete_user(self, username: str):
        """Delete a user by username.

        Args:
            username (str): Username
        """
        log.info("Delete user %s", username)
        userId = self.get_user(username)["id"]
        try:
            permUserId = self._permissions.get_users(
                query=f"userId={userId}")["permissionUsers"][0]["id"]
            self._permissions.delete_user(permUserId)
        except IndexError:
            log.error("User has no PermissionUser instance")
        try:
            self._login.delete_credentials(userId=userId)
        except OkapiRequestNotFound:
            log.error("User has no credentials")
        try:
            servicePointUserId = self._servicePointsUser.get_servicePointsUsers(
                query=f"userId={userId}")["servicePointsUsers"][0]["id"]
            self._servicePointsUser.delete_servicePointsUser(
                servicePointUserId)
        except IndexError:
            log.error("User has no ServicePointUser instance")

        return self._users.delete_user(userId)

    def modify_user(self, username: str, userData: dict):
        """Modify a user by username.

        Args:
            username (str): Username
        """
        log.info("Modify user %s", username)
        user = self.get_user(username)
        userId = user["id"]
        user.update(userData)

        return self._users.modify_user(userId, user)

    def get_permissions(self, username: str):
        """Get permissions of a user

        Args:
            username (str): Username

        Returns:
            dict: Dict with permissions
        """
        userId = self.get_user(username)["id"]
        try:
            permUserId = self._permissions.get_users(
                query=f"userId={userId}")["permissionUsers"][0]["id"]
        except IndexError:
            log.error("User has no PermissionUser instance")
            raise PermissionUserNotFound(username)
        return self._permissions.get_permissions_for_user(permUserId)["permissionNames"]

    def set_permission(self,  username: str, permissionName: str):
        """Set permission for a user

        Args:
            username (str): Username
            permissionName (str): Permission name.
        """
        self.set_permissions(username, [permissionName])

    def set_permissions(self,  username: str, permissionNames: list):
        """Set permissions for a user

        Args:
            username (str): Username
            permissionNames (list): List with permissions.
        """
        userId = self.get_user(username)["id"]
        try:
            permUserId = self._permissions.get_users(
                query=f"userId={userId}")["permissionUsers"][0]["id"]
        except IndexError:
            log.error("User has no PermissionUser instance")
            raise PermissionUserNotFound(username)
        perms = self.get_permissions(username)
        for permissionName in permissionNames:
            if not permissionName in perms:
                self._permissions.set_permission_for_user(permUserId,
                                                          {"permissionName": permissionName})
                log.debug("%s assigned", permissionName)
            else:
                log.error("%s for %s already assigned",
                          permissionName, username)

    def delete_permission(self, username: str, permissionName: str):
        """Delete a permission for a user

        Args:
            username (str): Username
            permissionName (str): Permission name.
        """
        self.delete_permissions(username, [permissionName])

    def delete_permissions(self, username: str, permissionNames: list):
        """Delete a permissions for a user

        Args:
            username (str): Username
            permissionNames (list): List with permissions.
        """
        userId = self.get_user(username)["id"]
        try:
            permUserId = self._permissions.get_users(
                query=f"userId={userId}")["permissionUsers"][0]["id"]
        except IndexError:
            log.error("User has no PermissionUser instance")
            raise PermissionUserNotFound(username)
        for permissionName in permissionNames:
            self._permissions.delete_permission_for_user(
                permUserId, permissionName)
            log.debug("%s for %s deleted", permissionName, username)

    def get_servicePoints(self):
        """Get all available service points

        Returns:
            dict: Dict with service points
        """
        return self._servicePoint.get_servicePoints()

    def get_usersServicePoints(self, username):
        """Get service points of a user.

        Returns:
            dict: Dict with service points
        """
        userId = self.get_user(username)["id"]
        try:
            sps = self._servicePointsUser.get_servicePointsUsers(
                query=f"userId={userId}")
            return sps["servicePointsUsers"][0]
        except IndexError:
            log.error("User has no ServicePointsUser instance")
            raise ServicePointsUserNotFound(username)

    def set_servicePoints(self, username: str, servicePointsIds: list, defaultServicePointId: str):
        """Set service points for a user.

        Args:
            username (str): Username.
            servicePointsIds (list): List with service point ids.
            defaultServicePointId (str): The default service point of a user.

        Returns:
            [type]: [description]
        """
        user = Users(self._tenant).get_user(username)
        log.debug(user)
        log.debug(servicePointsIds)
        sp_user = {
            "userId": user["id"],
            "servicePointsIds": servicePointsIds,
            "defaultServicePointId": defaultServicePointId
        }
        return self._servicePointsUser.set_servicePointsUser(sp_user)
