# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import logging
import uuid

from okapi.folio import FolioServices

log = logging.getLogger("okapi.folio.users")


class UserServices(FolioServices):
    """
    Requires: mod-users, mod-users-bl
    """

    def login(self, username: str, password: str):
        credentials = {"username": username, "password": password}
        return self._okapi.call_tenant_service("POST", "bl-users/login",
                                               self._tenant, credentials)

    def login_authn(self, username: str, password: str):
        credentials = {"username": username, "password": password}
        return self._okapi.call_tenant_service("POST", "/authn/login",
                                               self._tenant, credentials)

    def get_user(self, username: str):
        users = self.get_users()
        if users is None:
            log.error("No permission to call service users")
            return None
        else:
            for user in users["users"]:
                if username in user["username"]:
                    print(user)
                if user["username"] == username:
                    return user
        return None

    def get_users(self):
        return self._okapi.call_tenant_service("GET", "users", self._tenant)

    def set_user(self, username: str, active: bool = True, personal: dict = None):
        userId = str(uuid.uuid4())
        personal = personal or {}
        user = {
            "id": userId,
            "username": username,
            "active": active,
            "personal": personal
        }
        return self._okapi.call_tenant_service(
            "POST", "users", self._tenant, data=user)

    def set_password(self, username: str, password: str):
        user = self.get_user(username)
        if user:
            login = {
                "userId": user["id"],
                "password": password
            }
            res = self._okapi.call_tenant_service("POST", "/authn/credentials",
                                                  self._tenant, data=login)
            return res

    def create_user(self, username: str, password: str, permissions: list = None):
        try:
            user = self.get_user(username)
            # print(user)
            if user is None:
                log.info("Create user record.")
                user = self.set_user(username, personal={
                                     "lastName": "Superuser"})
                # print(user)

                log.info("Create login record.")
                self.set_password(username, password)

                if permissions is not None:
                    log.info("Set permissions %s for user record.",
                             str(permissions))
                    self.set_permissions(username, permissions)
            else:
                log.info("User already exists")
                return user
        except:
            log.info("No permission to call services")
            raise

    def get_permissions(self, username: str):
        user = self.get_user(username)
        if user is None:
            print("Are you logged in?")
            return
        else:
            userId = user["id"]
            return self._okapi.call_tenant_service("GET", f"perms/users/{userId}",
                                                   self._tenant)

    def set_permissions(self, username: str, permissions: str):
        user = self.get_user(username)
        perms_user = {"userId":  user["id"],
                      "permissions": permissions
                      }
        res = self._okapi.call_tenant_service("POST", "perms/users",
                                              self._tenant, data=perms_user)

        #user_permissions = self.get_permissions(username)
        #user_perm_id = user_permissions["id"]
        # for permission in permissions:
        #    if not permission in user_permissions["permissions"]:
        #        res = self._okapi.call_tenant_service(f"perms/users/{user_perm_id}/permissions",
        #                                              self._tenant, {"permissionName": permission})

        return res

    def set_service_points(self, username: str, servicePointsIds: str, defaultServicePointId: str):
        user = self.get_user(username)
        log.debug(user)
        log.debug(servicePointsIds)
        sp_user = {
            "userId": user["id"],
            "servicePointsIds": servicePointsIds,
            "defaultServicePointId": defaultServicePointId
        }
        return self._okapi.call_tenant_service("POST", "service-points-users",
                                               self._tenant, data=sp_user)

    def del_user(self, userId: str):
        #self._okapi.call_service("DELETE", )
        pass
