# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
from distutils.version import StrictVersion

from foliolib.config import Config
from foliolib.folio.api.permissions import Permissions
from foliolib.folio.users import UserService
from foliolib.okapi import helper as okapi_helper
from foliolib.okapi.okapiClient import OkapiClient

log = logging.getLogger("foliolib.okapi.folio.helper")


def create_superuser(tenant: str, username: str = "admin", password: str = "folio"):
    okapi = OkapiClient()

    log.info("Disable authtoken for tenant.")
    try:
        mod_authtoken = okapi.get_tenant_interface("authtoken", tenant)[0]
        disabled_mods = okapi.disable_module(mod_authtoken["id"], tenant)
    except:
        disabled_mods = None

    userService = UserService(tenant)

    log.info("Create user record.")
    user = userService.create_user(
        username, password,
        permissions=["perms.all",
                     "users.collection.get"],
        personal={"lastName": "Superuser"})

    log.info("Create service points for user record.")
    servicepoints = userService.get_servicePoints()
    servicepointsIds = [sp["id"] for sp in servicepoints["servicepoints"]]
    if servicepointsIds:
        log.debug(servicepoints)
        userService.set_servicePoints(username, servicepointsIds,
                                      servicepointsIds[0])

    log.info("Enable mod-authtoken.")
    okapi.enable_modules([m["id"] for m in disabled_mods], tenant)

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
    userService.set_permissions(username, topLevelPermissions)

    log.info("Superuser %s created.", username)

    return user


def login_supertenant(username, password):
    print("Logging in supertenant")
    Config().set_okapicfg("Okapi", "token", "")
    userService = UserService("supertenant")
    token = userService.login(username, password)
    if token is not None:
        Config().set_okapicfg("Okapi", "token", token)
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

    userServices = UserService(tenant)

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
