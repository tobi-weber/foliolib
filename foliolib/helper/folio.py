# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import time
from distutils.version import StrictVersion

from foliolib.config import Config
from foliolib.folio.exceptions import UserNotFound
from foliolib.folio.permissionsImpl import PermissionsImpl
from foliolib.folio.usersImpl import UsersImpl
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
    users = UsersImpl(tenant)

    try:
        Config().del_token(tenant)
        log.info("Create user record.")
        try:
            users.get_user(username)
            log.info("User %s exist.", username)
            okapi.enable_modules(tenant, [m["id"] for m in disabled_mods])
            return
        except UserNotFound:
            pass
        user = users.add_user(
            username, password,
            permissions=["perms.all",
                         "users.all"],
            lastName="Superuser")
    except:
        log.error("Failed to create Superuser %s", username)
        log.info("Enable mod-authtoken.")
        okapi.enable_modules(tenant, [m["id"] for m in disabled_mods])
        raise

    log.info("Enable mod-authtoken.")
    okapi.enable_modules(tenant, [m["id"] for m in disabled_mods])

    log.info("Login as superuser")
    users.login(username, password)

    log.info("Generate list of permissions")
    topLevelPermissions = [p["permissionName"]
                           for p in PermissionsImpl(tenant).get_topLevelPermissions()]

    # topLevelPermissions.extend(
    #    ["codex.collection.get",
    #     "codex-mux.instances.collection.get"])
    if StrictVersion(okapi.version()) >= StrictVersion("4.0"):
        topLevelPermissions.extend(["okapi.proxy.modules.get"])

    for perm in topLevelPermissions:
        try:
            users.set_permission(username, perm)
            log.info("%s assigned" % perm)
        except:
            log.error("Cannot assign %s" % perm)
            pass

    log.info("Superuser %s created.", username)

    return user
