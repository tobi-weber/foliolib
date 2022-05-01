# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import logging
import pprint

from foliolib.config import Config
from foliolib.folio.users import Users
from foliolib.okapi.okapiClient import OkapiClient
from foliolib.okapi.okapiModule import (create_okapiModules,
                                        sort_modules_by_requirements)

log = logging.getLogger("foliolib.helper.okapi")


def set_env_db(db_host: str, db_port: str = "5432", username: str = "folio_admin",
               password: str = "folio_admin", database: str = "okapi_modules"):
    """Set database enviroment.

    Args:
        db_host (str): postgresql host.
        db_port (str, optional): postgresql port. Defaults to "5432".
        username (str, optional): postgresql admin username. Defaults to "folio_admin".
        password (str, optional): postgresql admin database. Defaults to "folio_admin".
        database (str, optional): postgresql okapi modules database. Defaults to "okapi_modules".
    """
    okapi = OkapiClient()
    okapi.set_env("DB_HOST", db_host)
    okapi.set_env("DB_PORT",  db_port)
    okapi.set_env("DB_USERNAME", username)
    okapi.set_env("DB_PASSWORD", password)
    okapi.set_env("DB_DATABASE", database)
    okapi.set_env("DB_QUERYTIMEOUT", "60000")
    okapi.set_env("DB_CHARSET", "UTF-8")
    okapi.set_env("DB_MAXPOOLSIZE", "5")


def set_env_kafka(kafka_host: str, kafka_port: str = "9092"):
    """Set kafka enviroment.

    Args:
        kafka_host (str): kafka host
        kafka_port (str, optional): kafka port. Defaults to "9092".
    """
    okapi = OkapiClient()
    okapi_host = Config().okapicfg().get("Okapi", "host")
    okapi_port = Config().okapicfg().get("Okapi", "port")
    okapi.set_env("KAFKA_HOST", kafka_host)
    okapi.set_env("KAFKA_PORT",  kafka_port)
    okapi.set_env("OKAPI_URL", f"http://{okapi_host}:{okapi_port}")


def set_env_elastic(elastic_host: str, elastic_port: str = "9200",
                    elastic_user: str = "elastic", elastic_password: str = "",
                    languages: tuple = ("eng",)):
    """Set elasticsearch enviroment

    Args:
        elastic_host (str): elasticsearch host
        elastic_port (str, optional): elasticsearch password. Defaults to "9200".
        elastic_user (str, optional): elasticsearch username. Defaults to "elastic".
        elastic_password (str, optional): elasticsearch password. Defaults to "".
        languages (tuple, optional): elasticsearch  initial languages. Defaults to ("eng",).
    """
    okapi = OkapiClient()
    okapi_host = Config().okapicfg().get("Okapi", "host")
    okapi_port = Config().okapicfg().get("Okapi", "port")
    okapi.set_env("ELASTICSEARCH_HOST", elastic_host)
    okapi.set_env("ELASTICSEARCH_PORT", elastic_port)
    okapi.set_env("ELASTICSEARCH_USERNAME", elastic_user)
    okapi.set_env("ELASTICSEARCH_PASSWORD", elastic_password)
    okapi.set_env("INITIAL_LANGUAGES", ",".join(languages))
    okapi.set_env("ELASTICSEARCH_URL", f"http://{elastic_host}:{elastic_port}")
    okapi.set_env("OKAPI_URL", f"http://{okapi_host}:{okapi_port}")


def login_supertenant(username: str, password: str):
    """Log in supertenant.

    Args:
        username (str): username for supertenant.
        password (str): password supertenant.
    """
    print("Logging in supertenant")
    userService = Users("supertenant")
    token = userService.login(username, password)
    if token is None:
        print("Login failed")


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
    module_list = ['permissions', 'users', 'login']
    o = OkapiClient()
    modules = [m["id"] for m in o.get_modules() if m["name"] in module_list]
    res = o.enable_modules(modules, tenant)
    # print(res)

    userServices = Users(tenant)

    log.info("Create user record.")
    user = userServices.create_user(
        username, password, permissions=permissions)

    authtoken = [m["id"]
                 for m in o.get_modules() if m["name"] == "authtoken"][0]
    res = o.enable_module(authtoken, tenant)
    # print(res)

    login_supertenant(username, password)
    print("Successfully secured Okapi.")


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
                # o.disable_module(tm, tenant, purge=True)
                o.disable_module(tm, tenant)

    print("Successfully unsecured Okapi.")


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


def print_okapi_all():
    pp = pprint.PrettyPrinter(indent=2)
    okapi = OkapiClient()
    print("# Env")
    pp.pprint(okapi.get_env())
    print("# Nodes")
    pp.pprint(okapi.get_nodes())
    print("# Modules")
    pp.pprint(okapi.get_modules())
    print("# Deployed Modules")
    pp.pprint(okapi.get_deployed_modules())
    print("# Tenants")
    pp.pprint(okapi.get_tenants())
