# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import time
from distutils.version import StrictVersion

from foliolib.config import Config
from foliolib.folio.api.permissions import Permissions
from foliolib.folio.exceptions import UserNotFound
from foliolib.folio.users import Users
from foliolib.okapi.okapiClient import OkapiClient

log = logging.getLogger("foliolib.helper.okapi")


def create_superuser(tenant: str, username: str,
                     password: str):
    """Create a superuser for a tenant.

    Args:
        tenant (str): tenant id.
        username (str, optional): username..
        password (str, optional): password..

    Returns:
        dict: User object
    """
    okapi = OkapiClient()

    log.info("Disable authtoken for tenant.")
    try:
        mod_authtoken = okapi.get_tenant_interface(tenant, "authtoken")[0]
        disabled_mods = okapi.disable_module(mod_authtoken["id"], tenant)
    except:
        disabled_mods = None

    log.debug("Disabled Mods: \n%s", json.dumps(disabled_mods, indent=2))
    userService = Users(tenant)

    try:
        Config().del_token(tenant)
        log.info("Create user record.")
        try:
            userService.get_user(username)
            log.info("User %s exist.", username)
            okapi.enable_modules(tenant, [m["id"] for m in disabled_mods])
            return
        except UserNotFound:
            pass
        user = userService.create_user(
            username, password,
            permissions=["perms.all",
                         "users.all"],
            personal={"lastName": "Superuser"})

        log.info("Create service points for user record.")
        servicepoints = userService.get_servicePoints()
        servicepointsIds = [sp["id"] for sp in servicepoints["servicepoints"]]
        if servicepointsIds:
            log.debug(servicepoints)
            userService.set_servicePoints(username, servicepointsIds,
                                          servicepointsIds[0])
    except:
        log.error("Failed to create Superuser %s", username)
        log.info("Enable mod-authtoken.")
        okapi.enable_modules(tenant, [m["id"] for m in disabled_mods])
        raise

    log.info("Enable mod-authtoken.")
    okapi.enable_modules(tenant, [m["id"] for m in disabled_mods])

    log.info("Login as superuser")
    userService.login(username, password)

    log.info("Generate list of permissions")
    perms = Permissions(tenant).get_permissions(
        query="cql.allRecords=1 not permissionName==okapi.* not permissionName==modperms.* not permissionName==SYS#*",
        length="5000")
    topLevelPermissions = []
    for permission in perms["permissions"]:
        mods_perms = 0
        for s in permission["childOf"]:
            if s.startswith("SYS#") or s.startswith("modperms"):
                mods_perms += 1
        if len(permission["childOf"]) == mods_perms:
            topLevelPermissions.append(permission["permissionName"])

    # topLevelPermissions.extend(
    #    ["codex.collection.get",
    #     "codex-mux.instances.collection.get"])
    if StrictVersion(okapi.version()) >= StrictVersion("4.0"):
        topLevelPermissions.extend(["okapi.proxy.modules.get"])

    for perm in topLevelPermissions:
        try:
            userService.set_permission(username, perm)
            log.info("%s assigned" % perm)
        except:
            log.error("Cannot assign %s" % perm)
            pass

    log.info("Superuser %s created.", username)

    return user
