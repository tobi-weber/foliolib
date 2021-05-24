# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os
import pprint
import sys

from foliolib.config import Config
from foliolib.okapi.exceptions import TenantNotFound
from foliolib.okapi.okapiClient import (OkapiClient, request_release,
                                        request_snapshot_version)
from foliolib.okapi.okapiModule import (OkapiModule, create_okapiModule,
                                        create_okapiModules)

log = logging.getLogger("foliolib.okapi.helper")


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


def set_env_db(db_host: str, db_port: str = "5432", username: str = "folio_admin",
               password: str = "folio_admin", database: str = "okapi_modules"):
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
    okapi = OkapiClient()
    okapi_host = Config().okapicfg().get("Okapi", "host")
    okapi.set_env("KAFKA_HOST", kafka_host)
    okapi.set_env("KAFKA_PORT",  kafka_port)
    okapi.set_env("OKAPI_URL", f"http://{okapi_host}")


def add_modules(modules: list):
    added_modules = []
    okapi = OkapiClient()

    def add_requirements(name, mod):
        log.debug("Add requirements for %s", name)
        for require in mod.get_requires():
            log.debug("find %s", require)
            for module in modules:
                name = module.get_modId()
                if require in module.get_provides():
                    log.debug("Found in %s", name)
                    if not name in added_modules:
                        log.debug("Prepare %s", name)
                        add_requirements(name, module)
                        log.info("Add %s", name)
                        okapi.add_module(module)
                        added_modules.append(name)
                    else:
                        log.debug("%s already added", name)

    for module in modules:
        name = module.get_modId()
        if not name in added_modules:
            log.debug("Prepare %s", name)
            add_requirements(name, module)
            log.info("Add %s", name)
            okapi.add_module(module)
            added_modules.append(name)
        else:
            log.debug("%s already added", name)

    success = True
    added_modules = [m["id"] for m in okapi.get_modules()]
    for module in modules:
        name = module.get_modId()
        if not name in added_modules:
            log.error("Can not add modul %s", name)
            success = False

    return success


def add_modules_by_dir(path: str):
    if os.path.exists(path):
        modules = []
        for fname in os.listdir(path):
            with open(os.path.join(path, fname)) as f:
                descriptor = json.load(f)
            modules.append(OkapiModule(descriptor))
        add_modules(modules)
        return modules

    log.info("Path %s does not exist!", path)
    sys.exit(1)


def deploy_modules(modules: list, node: str):
    okapi = OkapiClient()
    deployed_modules = [m["srvcId"] for m in okapi.get_deployed_modules()]
    for module in modules:
        name = module.get_modId()
        if not name in deployed_modules:
            log.info("Deploy %s", name)
            okapi.deploy_module(name, node)
            deployed_modules.append(name)
        else:
            log.info("Module %s already deployed", name)
    # Check if all deployed
    deployed_modules = [m["srvcId"] for m in okapi.get_deployed_modules()]
    for module in modules:
        name = module.get_modId()
        if not name in deployed_modules:
            log.error("%s is not deployed", name)


def enable_modules(modules, tenant: str, loadSample: bool = False,
                   loadReference: bool = False, **kwargs):
    okapi = OkapiClient()

    def get_tenant_modules():
        return [m["id"] for m in okapi.get_tenant_modules(tenant)]

    def add_module(name, module):
        log.info("Enable %s for tenant %s", name, tenant)
        okapi.enable_module(module.get_modId(), tenant,
                            loadSample=loadSample, loadReference=loadReference, **kwargs)

    def add_requirements(name, mod):
        log.debug("Add requirements for %s", name)
        for require in mod.get_requires():
            log.debug("find %s", require)
            for module in modules:
                name = module.get_modId()
                if require in module.get_provides():
                    log.debug("Found in %s", name)
                    if not name in get_tenant_modules():
                        add_requirements(name, module)
                        add_module(name, module)
                    else:
                        log.debug("%s already enabled", name)
    for module in modules:
        name = module.get_modId()
        if not name in get_tenant_modules():
            add_requirements(name, module)
            add_module(name, module)
        else:
            log.debug("%s already enabled", name)


def disable_modules(tenant: str):
    okapi = OkapiClient()
    while okapi.get_tenant_modules(tenant):
        names = [m["id"] for m in okapi.get_tenant_modules(tenant)]
        for name in names:
            okapi.disable_module(name, tenant)


def install_okapi_modules(fname, node: str, tenant: str, loadSample: bool = False,
                          loadReference: bool = False, **kwargs):
    mods = parse_modules_file(fname)
    if not tenant in [e["id"] for e in OkapiClient().get_tenants()]:
        OkapiClient().create_tenant(tenant)
    modules = create_okapiModules(mods)
    add_modules(modules)
    deploy_modules(modules, node)
    enable_modules(modules, tenant, loadSample=loadSample,
                   loadReference=loadReference, **kwargs)


def upgrade_okapi_modules(fname, node: str, tenant: str, **kwargs):
    mods = parse_modules_file(fname)
    if not tenant in [e["id"] for e in OkapiClient().get_tenants()]:
        OkapiClient().create_tenant(tenant)
    modules = create_okapiModules(mods)
    add_modules(modules)
    deploy_modules(modules, node)
    log.info("Upgrade tenant %s", tenant)
    res = OkapiClient().upgrade_modules(tenant, **kwargs)

    return res


def removeUnusedModules():
    okapi = OkapiClient()
    tenants = okapi.get_tenants()
    enabledModules = []
    modsToRemove = []
    deployedModules = []
    for tenant in tenants:
        for mod in okapi.get_tenant_modules(tenant["id"]):
            if not mod["id"] in enabledModules:
                enabledModules.append(mod["id"])
    for mod in okapi.get_deployed_modules():
        deployedModules.append(mod["srvcId"])
    for mod in okapi.get_modules():
        if not mod["id"] in enabledModules:
            modsToRemove.append(mod["id"])
    for mod in modsToRemove:
        if mod in deployedModules:
            log.info("Undeploy %s", mod)
            okapi.undeploy_module(mod)
    for mod in modsToRemove:
        log.info("Remove %s", mod)
        okapi.remove_module(mod)

    return modsToRemove


def parse_modules_file(fname):
    mods = {}
    with open(fname) as f:
        data = json.load(f)
    if isinstance(data, dict):
        mods = data
    elif isinstance(data, list):
        for m in data:
            p = m["id"].split("-")
            version = p.pop()
            name = "-".join(p)
            mods[name] = version

    return mods
