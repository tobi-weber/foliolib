# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os
import pprint
import sys

from foliolib.config import Config
from foliolib.okapi.okapiClient import (OkapiClient, request_release,
                                        request_snapshot_version)
from foliolib.okapi.okapiModule import OkapiModule

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


def create_okapiModule(name: str, version: str = None):
    log.info("Create Descriptor: %s - %s", name, version)
    cache_dir = Config().foliolibcfg().get("Cache", "descriptors")
    descriptor_fname = f"ModuleDescriptor-{name}-{version}.json"
    fname_cache = os.path.join(cache_dir, descriptor_fname)
    if os.path.exists(fname_cache):
        log.info("Load descriptor from %s", fname_cache)
        with open(fname_cache) as f:
            descriptor = json.load(f)
        module = OkapiModule(descriptor)
    else:
        module = OkapiModule(name, version=version)
        log.debug("Create descriptor for %s", module.get_modId())
        descriptor_fname = f"ModuleDescriptor-{module.get_modId()}.json"
        fname_cache = os.path.join(cache_dir, descriptor_fname)
        log.debug("Write descriptor to %s", fname_cache)
        with open(fname_cache, "w") as f:
            json.dump(module.get_descriptor(), f, indent=2)
    log.debug("Docker Image: %s", module.get_docker_image())

    return module


def create_okapiModules(modlist: dict):
    return [create_okapiModule(name, version=version)
            for name, version in modlist.items()]


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


def enable_modules(modules, tenant: str,
                   loadSample: bool = False, loadReference: bool = False):
    okapi = OkapiClient()

    def get_tenant_modules():
        return [m["id"] for m in okapi.get_tenant_modules(tenant)]

    def add_module(name, module):
        log.info("Enable %s for tenant %s", name, tenant)
        okapi.enable_module(module.get_modId(), tenant,
                            loadSample=loadSample, loadReference=loadReference)

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


def install_okapi(fname, node: str, tenant: str, loadSample: bool = False, loadReference: bool = False):

    with open(fname) as f:
        data = json.load(f)
    if isinstance(data, dict):
        mods = data
    elif isinstance(data, list):
        mods = {}
        for m in data:
            p = m["id"].split("-")
            version = p.pop()
            name = "-".join(p)
            mods[name] = version
    if not tenant in [e["id"] for e in OkapiClient().get_tenants()]:
        OkapiClient().create_tenant(tenant)
    modules = create_okapiModules(mods)
    add_modules(modules)
    deploy_modules(modules, node)
    enable_modules(modules, tenant, loadSample=loadSample,
                   loadReference=loadReference)
