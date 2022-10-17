# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import logging
import pprint

from foliolib.config import Config
from foliolib.folio.users import Users
from foliolib.helper import split_modid
from foliolib.okapi.okapiClient import OkapiClient
from foliolib.okapi.okapiModule import (create_okapiModules,
                                        sort_modules_by_requirements)

log = logging.getLogger("foliolib.helper.okapi")


def set_okapi_url_env():
    """Set Okapi URL enviroment variable.
    """
    okapi_host = Config().okapicfg().get("Okapi", "host")
    okapi_port = Config().okapicfg().get("Okapi", "port")
    OkapiClient().set_env("OKAPI_URL", f"http://{okapi_host}:{okapi_port}")


def set_db_env(db_host: str, db_port: str = "5432", username: str = "folio",
               password: str = "folio", database: str = "okapi_modules"):
    """Set database enviroment variables.

    Args:
        db_host (str): postgresql host.
        db_port (str, optional): postgresql port. Defaults to "5432".
        username (str, optional): postgresql admin username. Defaults to "folio".
        password (str, optional): postgresql admin database. Defaults to "folio".
        database (str, optional): postgresql okapi modules database. Defaults to "okapi_modules".
    """
    okapi = OkapiClient()
    okapi.set_env("DB_HOST", db_host)
    okapi.set_env("DB_PORT",  db_port)
    okapi.set_env("DB_USERNAME", username)
    okapi.set_env("DB_PASSWORD", password)
    okapi.set_env("DB_DATABASE", database)
    #okapi.set_env("DB_QUERYTIMEOUT", "60000")
    okapi.set_env("DB_QUERYTIMEOUT", "120000")
    okapi.set_env("DB_CHARSET", "UTF-8")
    #okapi.set_env("DB_MAXPOOLSIZE", "5")
    #okapi.set_env("DB_MAXPOOLSIZE", "15")


def set_kafka_env(kafka_host: str, kafka_port: str = "9092", replication_factor=1,
                  topicprefix=None):
    """Set kafka enviroment variables.

    Args:
        kafka_host (str): kafka host
        kafka_port (str, optional): kafka port. Defaults to "9092".
    """
    okapi = OkapiClient()
    okapi.set_env("KAFKA_HOST", kafka_host)
    okapi.set_env("KAFKA_PORT",  kafka_port)
    okapi.set_env("REPLICATION_FACTOR",  replication_factor)
    if topicprefix is not None:
        okapi.set_env("ENV",  topicprefix)


def login_supertenant(username: str, password: str):
    """Log in supertenant.

    Args:
        username (str): username for supertenant.
        password (str): password supertenant.
    """
    log.info("Logging in supertenant")
    userService = Users("supertenant")
    token = userService.login(username, password)
    if token is None:
        log.error("Login failed")


def secure_supertenant(username: str = "okapi_admin", password: str = "admin"):
    """Secure supertenant.

    Args:
        username (str, optional): username for supertenant. Defaults to "okapi_admin".
        password (str, optional): password supertenant. Defaults to "admin".
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

    userServices = Users(tenant)

    log.info("Create user record.")
    user = userServices.create_user(
        username, password, permissions=permissions)

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
                #o.disable_module(tm, tenant)

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
    for mod in modsToRemove:
        modId = mod.get_id()
        log.info("Remove %s", modId)
        okapi.remove_module(modId)

    if okapiModule is not None:
        log.info("Remove %s", okapiModule)
        okapi.remove_module(okapiModule)
