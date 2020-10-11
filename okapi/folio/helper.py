# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging

from okapi import helper as okapi_helper
from okapi.config import CONFIG
from okapi.folio.inventory import InventoryServices
from okapi.folio.permissions import PermissionServices
from okapi.folio.users import UserServices
from okapi.okapiClient import OkapiClient

log = logging.getLogger("okapi.folio.helper")


def create_superuser(tenant: str, username: str = "admin", password: str = "folio"):
    okapi = OkapiClient()

    log.info("Disable authtoken for tenant.")
    try:
        mod_authtoken = okapi.get_tenant_interface("authtoken", tenant)[0]
        disabled_mods = okapi.disable_module(mod_authtoken["id"], tenant)
    except:
        pass

    userServices = UserServices(tenant)

    log.info("Create user record.")
    user = userServices.create_user(
        username, password, permissions=["perms.all"])

    log.info("Create service points for user record.")
    servicepoints = InventoryServices(tenant).get_servicePoints()
    servicepointsIds = [sp["id"] for sp in servicepoints["servicepoints"]]
    if servicepointsIds:
        log.debug(servicepoints)
        userServices.set_service_points(username, servicepointsIds,
                                        servicepointsIds[0])

    log.info("Enable mod-authtoken.")
    okapi.enable_modules([m["id"] for m in disabled_mods], tenant)

    log.info("Login as superuser")
    user_login = userServices.login(username, password)

    log.info("Generate list of permissions")
    query = {"query":
             "cql.allRecords=1 not permissionName==okapi.* not permissionName==modperms.* not permissionName==SYS#*",
             "length": "5000"}
    perms = PermissionServices(tenant).get_permissions(query=query)
    topLevelPermissions = []
    for permission in perms["permissions"]:
        mods_perms = 0
        for s in permission["childOf"]:
            if s.startswith("SYS#") or s.startswith("modperms"):
                mods_perms += 1
        if len(permission["childOf"]) == mods_perms:
            topLevelPermissions.append(permission["permissionName"])

    add_perms = ["okapi.proxy.modules.get"]
    topLevelPermissions.extend(add_perms)

    log.info("Assigning permissions")
    user_permissions = user_login["permissions"]["permissions"]
    user_perm_id = user_login["permissions"]["id"]
    for permission in topLevelPermissions:
        if not permission in user_permissions:
            res = okapi.call_tenant_service("POST", f"perms/users/{user_perm_id}/permissions", tenant,
                                            {"permissionName": permission})

            if res:
                log.debug("\t%s assigned", permission)
        else:
            log.debug("\t%s already assigned", permission)

    log.info("Superuser %s created.", username)

    return user


def login_supertenant(username, password):
    print("Logging in supertenant")
    CONFIG.set_okapicfg("Okapi", "token", "")
    userServices = UserServices("supertenant")
    user_login = userServices.login_authn(username, password)
    if user_login is not None:
        headers = userServices.get_okapiClient().headers
        CONFIG.set_okapicfg("Okapi", "token", headers["x-okapi-token"])
    else:
        print("Login failed")


def secure_supertenant(username: str = "okapi_admin", password: str = "admin"):
    tenant = "supertenant"
    permissions = [
        "okapi.all",
        "okapi.proxy.pull.modules.post",
        "perms.all",
        "login.all",
        "users.all"
    ]
    module_list = ['permissions', 'users', 'login']
    o = OkapiClient()
    modules = [m["id"] for m in o.get_modules() if m["name"] in module_list]
    res = o.enable_modules(modules, tenant)
    # print(res)

    userServices = UserServices(tenant)

    log.info("Create user record.")
    user = userServices.create_user(
        username, password, permissions=permissions)

    authtoken = [m["id"]
                 for m in o.get_modules() if m["name"] == "authtoken"][0]
    res = o.enable_module(authtoken, tenant)
    # print(res)

    login_supertenant(username, password)
    print("Successfully secured Okapi.")


def install_stripes(fname, tenant: str):

    with open(fname) as f:
        data = json.load(f)
    if isinstance(data, dict):
        mods = data
    elif isinstance(data, list):
        mods = {}
        for m in data:
            p = m["id"].split("-")
            version = p.pop()
            if "SNAPSHOT" in version:
                version = "%s-%s" % (p.pop(), version)
            name = "-".join(p)
            mods[name] = version
    if not tenant in [e["id"] for e in OkapiClient().get_tenants()]:
        OkapiClient().create_tenant(tenant)
    modules = okapi_helper.create_okapiModules(mods)
    okapi_helper.add_modules(modules)
    okapi_helper.enable_modules(modules, tenant)
