# -*- coding: utf-8 -*-
# Copyright (C) 2023 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
from collections import UserDict

from foliolib.exceptions import InvalidUUID
from foliolib.folio import FolioAPIImpl
from foliolib.folio.api.inventoryStorage import ServicePointsUser
from foliolib.folio.api.login import Login
from foliolib.folio.api.users import AddressTypes, Departments, Groups, Users
from foliolib.folio.exceptions import (AddressTypeNotFound, DepartmentNotFound,
                                       GroupNotFound, LoginFailed,
                                       PermissionUserNotFound,
                                       ServicePointsUserNotFound, UserNotFound)
from foliolib.folio.inventoryImpl import InventoryImpl, InventoryReferenceData
from foliolib.folio.permissionsImpl import PermissionsImpl
from foliolib.helper import is_valid_uuid
from foliolib.okapi.exceptions import (OkapiRequestForbidden,
                                       OkapiRequestNotFound)

log = logging.getLogger("foliolib.folio.users")


class UserAddress(UserDict):

    def __init__(self, addressType, **kwargs):
        """Physical addresses associated with the user.

        Tihs class can be used for UserImpl.add_user and UserImpl.modify_user methods.

        Args:
            addressType (str): addressType name or id.

        Keyword Args:
            id (str): UUID of the address.
            primaryAddress (bool): Wether is primary address.
            countryId (str): The country code for this address.
            addressLine1 (str): Address, Line 1.
            addressLine2 (str): Address, Line 2.
            city (str): City name.
            region (str): Region.
            postalCode (str): Postal Code.
        """
        super().__init__({"addressTypeId": addressType})
        self.update(kwargs)


class UsersImpl(FolioAPIImpl):
    """Implentations of user related functions.
    """

    def __init__(self, tenant: str) -> None:
        """
        Args:
            tenant (str): Tenant id
        """
        super().__init__(tenant)
        self._users = Users(tenant)
        self._permissions = PermissionsImpl(tenant)
        self._inventory = InventoryImpl(tenant)
        self._inventoryReferenceData = InventoryReferenceData(tenant)
        self._login = Login(tenant)
        self._servicePointsUser = ServicePointsUser(tenant)
        self._groups = GroupsImpl(tenant)
        self._departments = DepartmentsImpl(tenant)
        self._addressTypes = AddressTypesImpl(tenant)

    def login(self, username: str, password: str):
        """Make a authentication.

        Args:
            username (str): Username
            password (str): Password

        Returns:
            dict: Object of the authenticated user.

        Raises:
            LoginFailed: login failed.
        """
        self._login.set_login({"username": username,
                               "password": password})
        headers = self._login.get_okapiClient().headers
        if "x-okapi-token" in headers:
            return headers["x-okapi-token"]
        raise LoginFailed("Login failed for user %s" % username)

    def set_password(self, username: str, password: str):
        """Set a new password for given username.

        Args:
            username (str): Username of the user.
            password (str): Password of the user.
        Returns:
            bool: Wether set password was successful.
        """
        log.info("Set password for user %s", username)
        userId = self.get_user(username)["id"]
        try:
            self._login.delete_credentials(userId=userId)
        except OkapiRequestNotFound:
            log.error("User has no credentials Object")
        try:
            self._login.set_credential({"userId": userId,
                                        "password": password
                                        })
            return True
        except Exception as err:
            log.error(err)
            return False

    def get_users(self, query: str = None):
        """Get users by query or get all users.

        Args:
            query (str, optional): CQL string. Default to None, all objects will be returned. 

        Returns:
            list: List with user objects.
        """
        users = []
        count = self._users.get_users()["totalRecords"]
        query = query or "id=* sortby id"
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

    def add_user(self, username: str, password: str,
                 permissions: list = None, userServicePoints: bool = True,
                 **kwargs):
        """Add a user.

        A Credential, PermissionUser and ServicePointUser object will be
        also created.

        Args:
            username (str): Username.
            password (str): Password.
            permissions (list, optional): List with permissions. Defaults to None.
            userServicePoints (bool, optional): Wether to bind all available servicepoints to the user. Defaults to True.

        Keyword Args:
            uuid (str): UUID of the user.
            active (bool): Wether user is active. Defaults to True.
            barcode (str): Barcode.
            group (str): Groupname or id.
            departments (list, str): Departments list with names, codes or ids, or a department name, code or id.
            addresses (list, dict, UserAddress): List of UserAddress or dict instances. Or Useraddress or dict Instance.
            preferredContactTypeId (str): AddressType name or id of user's preferred contact type like Email, Mail or Text Message.
            lastName (str): The user's surname. [personal]
            firstName (str): The user's given name. [personal]
            middleName (str): The user's middle name (if any). [personal]
            preferredFirstName (str): The user's preferred name. [personal]
            email (str): The user's email address. [personal]
            phone (str): The user's primary phone number. [personal]
            mobilePhone (str): The user's mobile phone number. [personal]
            dateOfBirth (str): The user's birth date. [personal]
            type (str): The class of user like staff or patron; this is different from patronGroup.
            enrollmentDate (str): The date in which the user joined the organization (format: date-time).
            expirationDate (str): The date for when the user becomes inactive (format: date-time).
            tags (list): List of tags (str).
            customFields (dict): Dict that contains custom fields.

        Raises:
            GroupNotFound: Group not found.
            DepartmentNotFound: Department not found.
            AddressTypeNotFound: AddressType not found.

        Returns:
            dict: user object.
        """
        uuid = kwargs.pop("uuid") if "uuid" in kwargs else None
        active = kwargs.pop("active") if "active" in kwargs else True

        try:
            user = self.get_user(username)
            log.error("User %s already exists", username)
            return user
        except UserNotFound:
            pass

        try:
            if uuid is not None:
                user = self.get_user(uuid)
                log.error("A User (%s) for uuid %s already exists.",
                          user["username"], uuid)
                return user
            else:
                uuid = None
        except UserNotFound:
            pass

        log.info("Create user %s", username)

        user = {"username": username,
                "active": active}

        if uuid is not None:
            if is_valid_uuid(uuid):
                user["id"] = uuid
            else:
                raise InvalidUUID("UUID %s is invalid" % uuid)

        for k in ["barcode", "type", "enrollmentDate", "expirationDate", "customFields"]:
            if k in kwargs:
                user[k] = kwargs.pop(k)

        if "group" in kwargs:
            group = self._groups.get_group(kwargs.pop("group"))
            user["patronGroup"] = group["id"]

        if "departments" in kwargs:
            departments = kwargs.pop("departments")
            if isinstance(departments, list):
                user["departments"] = [self._departments.get_department(department)["id"]
                                       for department in departments]
            elif isinstance(departments, str):
                user["departments"] = [
                    self._departments.get_department(departments)["id"]]

        if "addresses" in kwargs:
            addresses = kwargs.pop("addresses")
            if isinstance(addresses, (dict, UserAddress)):
                addresses = [addresses]
            kwargs["addresses"] = self.__resolve_addressType(addresses)

        if "preferredContactTypeId" in kwargs:
            addresstype = self.get_addressType(
                kwargs.pop("preferredContactTypeId"))
            user["preferredContactTypeId"] = addresstype["id"]

        if "tags" in kwargs:
            user["tags"] = {"tagList": kwargs.pop("tags")}

        if kwargs:
            user["personal"] = kwargs

        log.debug(json.dumps(user, indent=2))
        user = self._users.set_user(user)

        log.info("Create login record.")
        self._login.set_credential({"userId": user["id"],
                                    "password": password
                                    })

        log.info("Add User to permissions")
        self._permissions.add_user(user["id"], permissions=permissions)

        log.info("Create servicePointsUser record.")
        self._servicePointsUser.set_servicePointsUser({"userId": user["id"]})
        if userServicePoints:
            servicepoints = self._inventoryReferenceData.get_servicePoints()
            servicepointsIds = [sp["id"]
                                for sp in servicepoints]
            if servicepointsIds:
                self.modify_servicePointsUser(username,
                                              servicepointsIds=servicepointsIds,
                                              defaultServicePointId=servicepointsIds[0])

        log.info("User %s created", username)

        return self.get_user(username)

    def modify_user(self, username: str, permissions: list = None, **kwargs):
        """Modify a user by username.

        If a keyword arg is None, the entry will be removed.

        Args:
            username (str): Username or id.
            permissions (list, optional): List with permissions to add to the user. Defaults to None.

        Keyword Args:
            active (bool): Wether user is active.
            barcode (str): Barcode.
            group (str): Groupname or id.
            departments (list, str): Departments list with names, codes or ids to replace. Or a department name, code or id to add.
            preferredContactTypeId (str): AddressType name or id of user's preferred contact type like Email, Mail or Text Message.
            lastName (str): The user's surname. [personal]
            firstName (str): The user's given name. [personal]
            middleName (str): The user's middle name (if any). [personal]
            preferredFirstName (str): The user's preferred name. [personal]
            email (str): The user's email address. [personal]
            phone (str): The user's primary phone number. [personal]
            mobilePhone (str): The user's mobile phone number. [personal]
            dateOfBirth (str): The user's birth date. [personal]
            addresses (list, dict, UserAddress): List of UserAddress or dict instances to replace addresses. Or Useraddress or dict Instance, to add a address.
            type (str): The class of user like staff or patron; this is different from patronGroup.
            enrollmentDate (str): The date in which the user joined the organization (format: date-time).
            expirationDate (str): The date for when the user becomes inactive (format: date-time).
            tags (list): List of tags (str).
            customFields (dict): Dict that contains custom fields.

        Raises:
            GroupNotFound: Group not found.
            DepartmentNotFound: Department not found.
            AddressTypeNotFound: AddressType not found.

        Returns:
            dict: user object.
        """
        user = self.get_user(username)
        log.info("Modify user %s", user["username"])

        for k in ["active", "barcode", "type", "enrollmentDate", "expirationDate", "customFields"]:
            if k in kwargs:
                user[k] = kwargs.pop(k)

        if "group" in kwargs:
            group = self._groups.get_group(kwargs.pop("group"))
            user["patronGroup"] = group["id"]

        if "departments" in kwargs:
            departments = kwargs.pop("departments")
            if departments is None:
                user["departments"] = None
            elif isinstance(departments, list):
                departments = [self._departments.get_department(department)["id"]
                               for department in departments]
                user["departments"] = departments
            elif isinstance(departments, str):
                if "departments" in user:
                    user["departments"].append(self._departments.get_department(departments)[
                        "id"])
                else:
                    user["departements"] += [
                        self._departments.get_department(departments)["id"]]

        if "addresses" in kwargs:
            addresses = kwargs.pop("addresses")
            if addresses is None:
                kwargs["addresses"] = []
            elif isinstance(addresses, (dict, UserAddress)):
                if "personal" in user and "addresses" in user["personal"]:
                    user["personal"]["addresses"] += self.__resolve_addressType([
                                                                                addresses])
            elif isinstance(addresses, list):
                kwargs["addresses"] = self.__resolve_addressType(addresses)

        if "preferredContactTypeId" in kwargs:
            addresstype = self.get_addressType(
                kwargs.pop("preferredContactTypeId"))
            user["preferredContactTypeId"] = addresstype["id"]

        if "tags" in kwargs:
            tags = kwargs.pop("tags")
            if tags is None:
                user["tags"] = None
            else:
                user["tags"] = {"tagList": tags}

        if kwargs:
            user["personal"].update(kwargs)

        log.debug(json.dumps(user, indent=2))
        self._users.modify_user(user["id"], user)
        user = self._users.get_user(user["id"])

        if permissions is not None:
            self.set_permissions(username, permissions)

        return user

    def delete_user(self, name_or_id: str):
        """Delete a user by username or id.

        The coresponding Credential, PermissionUser and ServicePointUser object will be
        also removed.

        Args:
            username (str): Username or id
        """
        user = self.get_user(name_or_id)
        userId = user["id"]
        userName = user["username"]
        log.info("Delete user %s", userName)
        try:
            self._permissions.delete_user(userId)
            log.info("PermissionUser Object for user %s deleted" % userName)
        except PermissionUserNotFound:
            log.error("User %s has no PermissionUser Object" % userName)
        try:
            self._login.delete_credentials(userId=userId)
            log.info("Credentials Object for user %s deleted" % userName)
        except OkapiRequestNotFound:
            log.error("User %s has no credentials Object" % userName)
        try:
            servicePointUserId = self._servicePointsUser.get_servicePointsUsers(
                query=f"userId={userId}")["servicePointsUsers"][0]["id"]
            self._servicePointsUser.delete_servicePointsUser(
                servicePointUserId)
            log.info("ServicePointUser Object for user %s deleted" % userName)
        except IndexError:
            log.error("User %s has no ServicePointUser Object" % userName)

        return self._users.delete_user(userId)

    def get_permissions(self, username: str):
        """Get permissions of a user

        Args:
            username (str): Username or id.

        Returns:
            dict: Dict with permissions
        """
        userId = self.get_user(username)["id"]
        return self._permissions.get_permissions_for_user(userId)

    def set_permission(self,  username: str, permissionName: str):
        """Set permission for a user.

        Args:
            username (str): Username or id.
            permissionName (str): Permission name.
        """
        self.set_permissions(username, [permissionName])

    def set_permissions(self,  username: str, permissionNames: list):
        """Set permissions for a user.

        Args:
            username (str): Username or id.
            permissionNames (list): List with permissions.
        """
        userId = self.get_user(username)["id"]
        perms = self.get_permissions(username)
        for permissionName in permissionNames:
            if not permissionName in perms:
                try:
                    self._permissions.set_permission_for_user(
                        userId, permissionName)
                except OkapiRequestForbidden as e:
                    log.error("Cannot assign permission %s to %s: %s",
                              permissionName, username, str(e))
                log.debug("%s assigned", permissionName)
            else:
                log.error("%s for %s already assigned",
                          permissionName, username)

    def delete_permission(self, username: str, permissionName: str):
        """Delete a permission for a user.

        Args:
            username (str): Username or id.
            permissionName (str): Permission name.
        """
        self.delete_permissions(username, [permissionName])

    def delete_permissions(self, username: str, permissionNames: list):
        """Delete given permissions for a user.

        Args:
            username (str): Username or id.
            permissionNames (list): List with permissions.
        """
        userId = self.get_user(username)["id"]
        usersPermissions = self.get_permissions(username)
        for permissionName in permissionNames:
            if permissionName in usersPermissions:
                self._permissions.delete_permission_for_user(
                    userId, permissionName)
                log.debug("%s for %s deleted", permissionName, username)

    def get_servicePointsUser(self, username: str):
        """Get servicepoints of a user.

        Args:
            username (str): Username or id.

        Returns:
            dict: Dict with servicepoints
        """
        userId = self.get_user(username)["id"]
        sp_user = self._servicePointsUser.get_servicePointsUsers(
            query=f"userId={userId}")
        try:
            return sp_user["servicePointsUsers"][0]
        except IndexError:
            log.error("User has no ServicePointsUser Object")
            raise ServicePointsUserNotFound(username)

    def modify_servicePointsUser(self, username: str, **kwargs):
        """Modify servicePointsUser obejct for a user.

        Args:
            username (str): Username or id.

        Keyword Args:
            servicePointsIds (list): List with service point ids.
            defaultServicePointId (str): The default servicepoint of a user.

        Returns:
            dict: ServicePointsUser object.
        """
        sp_user = self.get_servicePointsUser(username)
        if "servicePointsIds" in kwargs:
            sp_user["servicePointsIds"] = kwargs["servicePointsIds"]
        if "defaultServicePointId" in kwargs:
            sp_user["defaultServicePointId"] = kwargs["defaultServicePointId"]

        self._servicePointsUser.modify_servicePointsUser(
            sp_user["id"], sp_user)

        return self.get_servicePointsUser(username)

    def set_defaultServicePoint(self, username: str, defaultServicePointId: str):
        """Set default servicepoint for a user.

        Args:
            username (str): Username or id.
            defaultServicePointId (str): Servicepoint id.

        Returns:
            dict: ServicePointsUser object.
        """
        sp_user = self.get_servicePointsUser(username)
        sp_user["defaultServicePointId"] = defaultServicePointId

        self._servicePointsUser.modify_servicePointsUser(
            sp_user["id"], sp_user)

        return self.get_servicePointsUser(username)

    def add_servicePoint(self, username: str, servicePointId: str):
        """Add a servicepoint to a user.

        Args:
            username (str): Username or id.
            servicePointId (str): Servicepoint id.

        Returns:
            dict: ServicePointsUser object.
        """
        sp_user = self.get_servicePointsUser(username)
        sp_user["servicePointsIds"].append(servicePointId)

        self._servicePointsUser.modify_servicePointsUser(
            sp_user["id"], sp_user)

        return self.get_servicePointsUser(username)

    def remove_servicePoint(self, username: str, servicePointId: str):
        """Remove a servicepoint from a user.

        Args:
            username (str): Username or id.
            servicePointId (str): Servicepoint id.

        Returns:
            dict: ServicePointsUser object.
        """
        sp_user = self.get_servicePointsUser(username)
        sp_user["servicePointsIds"].remove(servicePointId)

        self._servicePointsUser.modify_servicePointsUser(
            sp_user["id"], sp_user)

        return self.get_servicePointsUser(username)

    def __resolve_addressType(self, userAddresses):
        addresses = []
        for a in userAddresses:
            a["addressTypeId"] = self._addressTypes.get_addressType(
                a["addressTypeId"])["id"]
            addresses.append({k: v for k, v in a.items()})
        return addresses


class GroupsImpl(FolioAPIImpl):
    """Implentations of groups related functions.
    """

    def __init__(self, tenant: str) -> None:
        """
        Args:
            tenant (str): Tenant id
        """
        super().__init__(tenant)
        self._groups = Groups(tenant)

    def get_groups(self, query: str = None):
        """Get list of groups.

        Args:
            query (str, optional): CQL string. Default to None, all objects will be returned. 

        Returns:
            list: List of group Objects.
        """
        query = query or "id=* sortby id"
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
            dict: Group Object
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

    def add_group(self, name: str, **kwargs):
        """Add a group.

        Args:
            name (str): Name of the group.

        Keyword Args:
            uuid (str): Id of the group.
            desc (str): Description of the group. Defaults to None.
            expirationOffsetInDays (int): Expiration offset days. Defaults to 0.
            source: (str): Origin of the group record, i.e. 'System' or 'User'". Defaults to None.

        Returns:
            dict: Object of the group.
        """
        try:
            group = self.get_group(name)
            log.error("Group %s already exists", name)
            return group
        except GroupNotFound:
            pass

        try:
            if "uuid" in kwargs:
                uuid = kwargs["uuid"]
                group = self.get_group(uuid)
                log.error("A Group (%s) for uuid %s already exists.",
                          group["name"], uuid)
                return group
        except GroupNotFound:
            pass

        log.info("Add group %s", name)
        group = {"group": name}
        if "uuid" in kwargs:
            group["id"] = kwargs["uuid"]
        if "desc" in kwargs:
            group["desc"] = kwargs["desc"]
        if "expirationOffsetInDays" in kwargs:
            group["expirationOffsetInDays"] = kwargs["expirationOffsetInDays"]
        if "source" in kwargs:
            group["source"] = kwargs["source"]
        self._groups.set_group(group)

        return self.get_group(name)

    def modify_group(self, name: str, **kwargs):
        """Modify a group.

        In order to change the name of the group, the uuid of the group must be given.

        Args:
            name (str): Name of the group.

        Keyword Args:
            uuid (str): Id of the group.
            desc (str): Description of the group. Defaults to None.
            expirationOffsetInDays (int): Expiration offset days. Defaults to 0.
            source: (str): Origin of the group record, i.e. 'System' or 'User'". Defaults to None.

        Returns:
            dict: Object of the group.
        """
        if "uuid" in kwargs and kwargs["uuid"] is not None:
            group = self.get_group(kwargs["uuid"])
        else:
            group = self.get_group(name)

        log.info("Modify group %s", group["group"])
        group["group"] = name
        if "desc" in kwargs:
            group["desc"] = kwargs["desc"]
        if "expirationOffsetInDays" in kwargs:
            group["expirationOffsetInDays"] = kwargs["expirationOffsetInDays"]
        if "source" in kwargs:
            group["source"] = kwargs["source"]
        self._groups.modify_group(group["id"], group)

        return group

    def delete_group(self, name_or_id: str):
        """Delete a group.

        Args:
            name (str): Name of the group.
        """
        group = self.get_group(name_or_id)
        log.info("Delete group %s", group["group"])

        return self._groups.delete_group(group["id"])


class DepartmentsImpl(FolioAPIImpl):
    """Implentations of departments related functions.
    """

    def __init__(self, tenant: str) -> None:
        """
        Args:
            tenant (str): Tenant id
        """
        super().__init__(tenant)
        self._departments = Departments(tenant)

    def get_departments(self, query: str = None):
        """Get list of departments.

        Args:
            query (str, optional): CQL string. Default to None, all objects will be returned. 

        Returns:
            list: List of department Objects.
        """
        query = query or "id=* sortby id"
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
            dict: Department Object
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

    def add_department(self, name: str, code: str, **kwargs):
        """Add a department.

        Args:
            name (str): Name of the department.
            code (str): Code of the department.

        Keyword Args:
            uuid (str): Id of the department.

        Returns:
            dict: Object of the department.
        """
        log.info("Add department %s", name)
        try:
            department = self.get_department(name)
            log.error("Department %s already exists", name)
            return department
        except DepartmentNotFound:
            pass

        try:
            if "uuid" in kwargs:
                uuid = kwargs["uuid"]
                department = self.get_department(uuid)
                log.error("A Department (%s) for uuid %s already exists.",
                          department["name"], uuid)
                return department
        except DepartmentNotFound:
            pass

        department = {"name": name, "code": code}
        if "uuid" in kwargs:
            department["id"] = kwargs["uuid"]
        self._departments.set_department(department)
        department = self.get_department(name)

        return department

    def modify_department(self, name: str, **kwargs):
        """Modify a department.

        In order to change the name of a department, the uuid or the code of the departemnt
        must be given.

        Args:
            name (str): Name of the department.

        Keyword Args:
            uuid (str): Id of the department.
            code (str): Code of the department.

        Returns:
            dict: Object of the department.
        """
        department = None
        try:
            department = self.get_department(name)
        except DepartmentNotFound:
            if "code" in kwargs:
                try:
                    department = self.get_department(kwargs["code"])
                except DepartmentNotFound:
                    pass
                if "uuid" in kwargs:
                    try:
                        department = self.get_department(kwargs["uuid"])
                    except DepartmentNotFound:
                        pass
        if department is None:
            raise DepartmentNotFound(
                "Departement not found for given name or code or uuid")

        log.info("Modify department %s", department["name"])

        department["name"] = name

        if "code" in kwargs:
            department["code"] = kwargs["code"]

        self._departments.modify_department(department["id"], department)

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


class AddressTypesImpl(FolioAPIImpl):
    """Implentations of addressTypes related functions.
    """

    def __init__(self, tenant: str) -> None:
        """
        Args:
            tenant (str): Tenant id
        """
        super().__init__(tenant)
        self._addressTypes = AddressTypes(tenant)

    def get_addressTypes(self, query: str = None):
        """Get list of addressTypes.

        Args:
            query (str, optional): CQL string. Default to None, all objects will be returned. 

        Returns:
            list: List of addresstType Objects.
        """
        query = query or "id=* sortby id"
        addresstypes = self._addressTypes.get_addresstypes(
            query=query, limit=10000)["addressTypes"]

        return addresstypes

    def get_addressType(self, name_or_id: str):
        """Get addressType by given name, code or id.

        Args:
            name_or_id (str): AddressType name or id.

        Raises:
            AddressTypeNotFound: AddressType not found

        Returns:
            dict: AddressType Object.
        """
        if is_valid_uuid(name_or_id):
            try:
                addressType = self._addressTypes.get_addresstype(
                    name_or_id)
            except OkapiRequestNotFound:
                raise AddressTypeNotFound(
                    f"AddressType {name_or_id} not found.")
            return addressType
        else:
            addressTypes = self.get_addressTypes(
                query=f"addressType=={name_or_id}")
            if not len(addressTypes):
                raise AddressTypeNotFound(
                    f"AddressType {name_or_id} not found.")
            return addressTypes[0]

    def add_addressType(self, name: str, **kwargs):
        """Add a addressType.

        Args:
            name (str): Name of the addressType.

        Keyword Args:
            desc (str): Description of the addressType.
            uuid (str): Id of the addressType.

        Returns:
            dict: Object of the addressType.
        """
        log.info("Add addressType %s", name)
        addressType = {}
        addressType["addressType"] = name
        if "desc" in kwargs:
            addressType["desc"] = kwargs["desc"]
        self._addressTypes.set_addresstype(addressType)
        addressType = self.get_addressType(name)

        return addressType

    def modify_addressType(self, name: str, **kwargs):
        """Modify a addressType.

        In order to change the name of a addressType, the uuid of the addressType
        must be given.

        Args:
            name (str): Name of the addressType.

        Keyword Args:
            desc (str): Description of the addressType.
            uuid (str): Id of the addressType.

        Returns:
            dict: Object of the addressType.
        """
        print(kwargs)
        if "uuid" in kwargs and kwargs["uuid"] is not None:
            addressType = self.get_addressType(kwargs["uuid"])
        else:
            addressType = self.get_addressType(name)

        log.info("Modify addressType %s", addressType["addressType"])

        addressType["addressType"] = name

        if "desc" in kwargs:
            addressType["desc"] = kwargs["desc"]
        self._addressTypes.modify_addresstype(addressType["id"], addressType)
        addressType = self.get_addressType(name)

        return addressType

    def delete_addressType(self, name_or_id: str):
        """Delete a addressType.

        Args:
            name_or_id (str): addressType name or id.
        """
        addressType = self.get_addressType(name_or_id)
        log.info("Delete addressType %s", addressType["addressType"])

        return self._addressTypes.delete_addresstype(addressType["id"])
