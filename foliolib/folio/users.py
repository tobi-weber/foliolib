# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import logging

from foliolib.folio import FolioService
from foliolib.folio.api.inventoryStorage import ServicePoint, ServicePointsUser
from foliolib.folio.api.login import Login
from foliolib.folio.api.permissions import Permissions
from foliolib.folio.api.users import Departments, Groups
from foliolib.folio.api.users import Users as UsersApi
from foliolib.folio.exceptions import (DepartmentNotFound, GroupNotFound,
                                       PermissionUserNotFound,
                                       ServicePointsUserNotFound, UserNotFound)
from foliolib.helper import is_valid_uuid
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
        self._groups = Groups(tenant)
        self._departments = Departments(tenant)
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
        except OkapiRequestNotFound:
            log.error("User has no credentials instance")
        try:
            self._login.set_credential({"userId": userId,
                                        "password": password
                                        })
            return True
        except Exception as err:
            log.error(err)
            return False

    def get_users(self, query=None):
        """Get users by query or get all users.

        Returns:
            list: List with users
        """
        users = []
        count = self._users.get_users()["totalRecords"]
        query = query or "id=* sortby username"
        for i in range(0, count, 1000):
            users += self._users.get_users(query=query,
                                           offset=i, limit=1000)["users"]

        return users

    def get_user(self, name_or_id: str):
        """Get a user by username or id

        Args:
            name_or_id (str): Username or id

        Raises:
            UserNotFound: User not found

        Returns:
            dict: Dict with user data
        """
        if is_valid_uuid(name_or_id):
            try:
                user = self._users.get_user(name_or_id)
                return user
            except OkapiRequestNotFound:
                raise UserNotFound(f"User {name_or_id} not found.")
        else:
            users = self._users.get_users(query=f"username=={name_or_id}")
            if not users["users"]:
                raise UserNotFound(f"User {name_or_id} not found.")
            return users["users"][0]

    def create_user(self, username: str, password: str,
                    permissions: list = None, firstname: str = None,
                    lastname: str = None, email: str = None, barcode: str = None,
                    group: str = None, departments: list = None, inactive: bool = False,
                    userServicePoints: bool = True, userData: dict = None):
        """Create a user

        Args:
            username (str): Username
            password (str): Password
            permissions (list, optional): List with permissions. Defaults to None.
            firstname (str, optional): First name. Defaults to None.
            lastname (str, optional): Last name. Defaults to None.
            email (str, optional): EMail address. Defaults to None.
            barcode (str, optional): Barcode. Defaults to None.
            group (str, optional): Groupname or id. Defaults to None.
            departments (list, optional): Departments list with names, codes or ids. Defaults to None.
            inactive (bool, optional): Wether user is inactive. Defaults to False.
            userServicePoints (bool, optional): Wether to bind servicepoints to the user. Defaults to True.
            userData (dict, optional): Data for the user as a dict. This data will be merged into the user instance. Default to None.

        Raises:
            GroupNotFound: _description_

        Returns:
            dict: Dict with user data
        """
        try:
            user = self.get_user(username)
            log.info("User already exists")
            return user
        except UserNotFound:
            log.info("Create user %s", username)

            user = {"username": username,
                    "active": False if inactive else True}

            if firstname or lastname or email:
                personal = user["personal"] = {}
                if firstname:
                    personal["firstName"] = firstname
                if lastname:
                    personal["lastName"] = lastname
                if email:
                    personal["email"] = email

            if barcode:
                user["barcode"] = barcode

            if group is not None:
                group = self.get_group(group)
                user["patronGroup"] = group["id"]

            if departments:
                user["departments"] = [self.get_department(department)["id"]
                                       for department in departments]

            if userData is not None:
                log.debug("Merge userData: %s" % str(userData))
                user.update(userData)

            user = self._users.set_user(user)

            log.info("Create login record.")
            self._login.set_credential({"userId": user["id"],
                                        "password": password
                                        })

            log.info("Add User to permissions")
            data = {"userId":  user["id"]}
            if permissions is not None:
                data["permissions"] = permissions
            self._permissions.set_user(data)

            if userServicePoints:
                log.info("Create service points for user record.")
                servicepoints = self.get_servicePoints()
                servicepointsIds = [sp["id"]
                                    for sp in servicepoints["servicepoints"]]
                if servicepointsIds:
                    log.debug(servicepoints)
                    self.set_servicePoints(username, servicepointsIds,
                                           servicepointsIds[0])

        log.info("User %s created", username)

        return user

    def delete_user(self, name_or_id: str):
        """Delete a user by username or id.

        Args:
            username (str): Username or id
        """
        user = self.get_user(name_or_id)
        userId = user["id"]
        log.info("Delete user %s", user["username"])
        try:
            permUserId = self._permissions.get_users(
                query=f"userId={userId}")["permissionUsers"][0]["id"]
            self._permissions.delete_user(permUserId)
            log.info("PermissionUser instance deleted")
        except IndexError:
            log.error("User has no PermissionUser instance")
        try:
            self._login.delete_credentials(userId=userId)
            log.info("Credentials instance deleted")
        except OkapiRequestNotFound:
            log.error("User has no credentials instance")
        try:
            servicePointUserId = self._servicePointsUser.get_servicePointsUsers(
                query=f"userId={userId}")["servicePointsUsers"][0]["id"]
            self._servicePointsUser.delete_servicePointsUser(
                servicePointUserId)
            log.info("ServicePointUser instance deleted")
        except IndexError:
            log.error("User has no ServicePointUser instance")

        return self._users.delete_user(userId)

    def modify_user(self, name_or_id: str, userData: dict):
        """Modify a user by username or id.

        Args:
            username (str): Username or id
        """
        user = self.get_user(name_or_id)
        log.info("Modify user %s", user["username"])
        userId = user["id"]
        user.update(userData)

        return self._users.modify_user(userId, user)

    def get_groups(self, query: str = None):
        """Get list of groups.

        Args:
            query (str, optional): CQL query string. Defaults to None.

        Returns:
            list: List of group instances.
        """
        query = query or "id=* sortby group"
        groups = self._groups.get_groups(
            query=query, limit=10000)["usergroups"]

        return groups

    def get_group(self, name_or_id: str):
        """Get group by given name or id.

        Args:
            name_or_id (str): Group name or id

        Raises:
            GroupNotFound: Group not found

        Returns:
            dict: Group instance
        """
        if is_valid_uuid(name_or_id):
            try:
                group = self._groups.get_group(name_or_id)
            except OkapiRequestNotFound:
                raise GroupNotFound(f"Group {name_or_id} not found.")
            return group
        else:
            groups = self.get_groups(query=f"group=={name_or_id}")
            if not len(groups):
                raise GroupNotFound(f"Group {name_or_id} not found.")
            return groups[0]

    def create_group(self, name: str, desc: str = None,
                     expirationOffsetInDays: int = 0):
        """Create a group.

        Args:
            name (str): Name of the group.
            desc (str, optional): Description of the group. Defaults to None.
            expirationOffsetInDays (int, optional): Expiration offset days. Defaults to 0.

        Returns:
            dict: Instance of the group.
        """
        log.info("Create group %s", name)
        group = {"group": name}
        if desc is not None:
            group["desc"] = desc
        if expirationOffsetInDays:
            group["expirationOffsetInDays"] = expirationOffsetInDays
        self._groups.set_group(group)
        group = self.get_group(name)

        return group

    def delete_group(self, name_or_id: str):
        """Delete a group.

        Args:
            name (str): Name of the group.
        """
        group = self.get_group(name_or_id)
        log.info("Delete group %s", group["group"])

        return self._groups.delete_group(group["id"])

    def get_departments(self, query: str = None):
        """Get list of departments.

        Args:
            query (str, optional): CQL query string. Defaults to None.

        Returns:
            list: List of department instances.
        """
        query = query or "id=* sortby ame"
        departments = self._departments.get_departments(
            query=query, limit=10000)["departments"]

        return departments

    def get_department(self, name_or_code_or_id: str):
        """Get department by given name, code or id.

        Args:
            name_or_code_or_id (str): Department name, code or id.

        Raises:
            DepartmentNotFound: Department not found

        Returns:
            dict: Department instance
        """
        if is_valid_uuid(name_or_code_or_id):
            try:
                department = self._departments.get_department(
                    name_or_code_or_id)
            except OkapiRequestNotFound:
                raise DepartmentNotFound(
                    f"Department {name_or_code_or_id} not found.")
            return department
        else:
            departments = self.get_departments(
                query=f"name=={name_or_code_or_id}")
            if not len(departments):
                departments = self.get_departments(
                    query=f"code=={name_or_code_or_id}")
                if not len(departments):
                    raise DepartmentNotFound(
                        f"Department {name_or_code_or_id} not found.")
            return departments[0]

    def create_department(self, name: str, code: str):
        """Create a department.

        Args:
            name (str): Name of the department.
            code (str): Code of the department.

        Returns:
            dict: Instance of the department.
        """
        log.info("Create department %s", name)
        department = {"name": name, "code": code}
        self._departments.set_department(department)
        department = self.get_department(name)

        return department

    def delete_department(self, name_or_code_or_id: str):
        """Delete a department.

        Args:
            name_or_code_or_id (str): Department name, code or id.
        """
        department = self.get_department(name_or_code_or_id)
        log.info("Delete department %s", department["name"])

        return self._departments.delete_department(department["id"])

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

    def get_topLevelPermissions(self):
        """Get all available top level permissions.

        Returns:
            list: List with permission instances.
        """
        perms = Permissions(self._tenant).get_permissions(
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

        return topLevelPermissions

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
