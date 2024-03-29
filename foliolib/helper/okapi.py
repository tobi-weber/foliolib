# -*- coding: utf-8 -*-
# Copyright (C) 2023 Tobias Weber <tobi-weber@gmx.de>

import logging
import re

from foliolib.config import Config
from foliolib.folio.usersImpl import UsersImpl
from foliolib.helper import split_modid
from foliolib.helper.modules import remove_module
from foliolib.okapi.exceptions import OkapiRequestError
from foliolib.okapi.okapiClient import OkapiClient
from foliolib.okapi.okapiModule import (create_okapiModules,
                                        sort_modules_by_requirements)

log = logging.getLogger("foliolib.helper.okapi")


def login_supertenant(username: str, password: str):
    """Log in supertenant.

    Args:
        username (str): username for supertenant.
        password (str): password supertenant.
    """
    log.info("Logging in supertenant")
    userService = UsersImpl("supertenant")
    token = userService.login(username, password)
    if token is None:
        log.error("Login failed")


def secure_supertenant(username: str, password: str):
    """Secure supertenant.

    Args:
        username (str): username for supertenant.
        password (str): password supertenant.
    """
    tenant = "supertenant"
    permissions = [
        "okapi.all",
        "okapi.proxy.pull.modules.post",
        "perms.all",
        "login.all",
        "users.all"
    ]
    log.info("Enable modules permissions, users and login for supertenant")
    Config().del_token(tenant)
    module_list = ['mod-permissions', 'mod-users', 'mod-login']
    o = OkapiClient()
    modules = [m["id"]
               for m in o.get_modules() if split_modid(m["id"])[0] in module_list]
    res = o.enable_modules(tenant, modules)
    # print(res)

    userServices = UsersImpl(tenant)

    log.info("Create user record.")
    user = userServices.add_user(
        username, password, permissions=permissions,
        userServicePoints=False)

    authtoken = [m["id"]
                 for m in o.get_modules() if split_modid(m["id"])[0] == "mod-authtoken"][0]
    res = o.enable_module(tenant, authtoken)
    # print(res)

    login_supertenant(username, password)
    log.info("Successfully secured Okapi.")


def unsecure_supertenant():
    """Unsecure supertenant.
    """
    tenant = "supertenant"
    mods = ["permissions", "users", "login", "authtoken"]
    o = OkapiClient()
    for m in mods:
        for tm in [m["id"] for m in o.get_tenant_modules(tenant)]:
            if tm.startswith(f"mod-{m}"):
                log.info("Disable %s", m)
                o.disable_module(tm, tenant, purge=True)
                # o.disable_module(tm, tenant)

    log.info("Successfully unsecured Okapi.")


def clean_okapi():
    """Undeploy and remove all modules, that are not enabled
       in a tenant.
    """
    okapi = OkapiClient()
    tenants = okapi.get_tenants()

    enabledModules = []
    modsToRemove = []
    deployedModules = []
    okapiModule = None

    for tenant in tenants:
        for mod in okapi.get_tenant_modules(tenant["id"]):
            if not mod["id"] in enabledModules:
                enabledModules.append(mod["id"])
    for mod in okapi.get_deployed_modules():
        deployedModules.append(mod["srvcId"])
    for mod in okapi.get_modules():
        if not mod["id"] in enabledModules:
            if mod["id"].startswith("okapi-"):
                okapiModule = mod["id"]
            else:
                modsToRemove.append(mod["id"])

    # print(enabledModules)
    modsToRemove = sort_modules_by_requirements(
        create_okapiModules(modsToRemove))
    modsToRemove.reverse()

    for mod in modsToRemove:
        modId = mod.get_id()
        if modId in deployedModules:
            log.info("Undeploy %s", modId)
            okapi.undeploy_module(modId)
    remove_module(modsToRemove, resolve_incompatible=True)


    if okapiModule is not None:
        log.info("Remove %s", okapiModule)
        okapi.remove_module(okapiModule)
