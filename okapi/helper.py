# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os
import pprint
import sys

from okapi.okapiClient import OkapiClient
from okapi.okapiModule import (OkapiModule, makeOkapiModule,
                               makeOkapiModule_with_pkg)

log = logging.getLogger("okapi.helper")


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


def load_okapi_install(fname: str):
    mods = []
    with open(fname) as f:
        d = json.load(f)
        for m in d:
            p = m["id"].split("-")
            version = p.pop()
            name = "-".join(p)
            mods.append((name, version))

    return mods


def create_modules_from_snapshots(modlist: str, cache_dir: str = "/tmp/descriptors",
                                  docker_repository: str = "folioci"):
    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)
    modules = {}
    for name, version in modlist:
        print(f"Create Descriptor: {name} - {version}")
        descriptor_fname = f"ModuleDescriptor-{name}-snapshot.json"
        fname = os.path.join("descriptors", descriptor_fname)
        fname_cache = os.path.join(cache_dir, descriptor_fname)
        if os.path.exists(fname_cache):
            print(f"Load descriptor from {fname_cache}")
            with open(fname_cache) as f:
                descriptor = json.load(f)
            m = OkapiModule(descriptor=descriptor)
        elif os.path.exists(fname):
            print(f"Load descriptor from {fname}")
            with open(fname) as f:
                descriptor = json.load(f)
            m = makeOkapiModule(name, version=version, descriptor=descriptor,
                                docker_repository=docker_repository)
            with open(fname_cache, "w") as f:
                json.dump(m.get_descriptor(), f, indent=2)
        else:
            m = makeOkapiModule(name, version=version,
                                docker_repository=docker_repository)
            print(f"Write descriptor to {fname_cache}")
            with open(fname_cache, "w") as f:
                json.dump(m.get_descriptor(), f, indent=2)
        modules[m.get_modId()] = m
        print(f"Docker Image: {m.get_docker_image()}")

    return modules


def create_modules_from_releases(modlist: str, cache_dir: str = "descriptors", pkg_dir: str = "pkg"):
    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)
    modules = {}
    for name, version in modlist:
        print(f"Create Descriptor: {name} - {version}")
        descriptor_fname = f"ModuleDescriptor-{name}-{version}.json"
        fname_cache = os.path.join(cache_dir, descriptor_fname)
        if os.path.exists(fname_cache):
            print(f"Load descriptor from {fname_cache}")
            with open(fname_cache) as f:
                descriptor = json.load(f)
            m = OkapiModule(descriptor=descriptor)
        else:
            m = makeOkapiModule_with_pkg(
                name, version=version, pkg_dir=pkg_dir)
            descriptor_fname = f"ModuleDescriptor-{m.get_modId()}.json"
            fname_cache = os.path.join(cache_dir, descriptor_fname)
            print(f"Write descriptor to {fname_cache}")
            with open(fname_cache, "w") as f:
                json.dump(m.get_descriptor(), f, indent=2)
        modules[m.get_modId()] = m
        print(f"Docker Image: {m.get_docker_image()}")

    return modules


def add_modules(modules: list):
    added_modules = []
    okapi = OkapiClient()

    def add_requirements(name, mod):
        print(f"\t Add requirements for {name}")
        for require in mod.get_requires():
            print(f"\t\t find {require}")
            for name, module in modules.items():
                if require in module.get_provides():
                    print(f"\t\t Found in {name}")
                    if not name in added_modules:
                        print(f"\t Add {name}")
                        add_requirements(name, module)
                        okapi.add_module(module)
                        added_modules.append(name)
                    else:
                        print(f"\t {name} already added")

    for name, module in modules.items():
        if not name in added_modules:
            print(f"Add {name}")
            add_requirements(name, module)
            okapi.add_module(module)
            added_modules.append(name)
        else:
            print(f"{name} already added")

    success = True
    added_modules = [m["id"] for m in okapi.get_modules()]
    for name in modules.keys():
        if not name in added_modules:
            print(f"ERROR: Can not add modul {name}")
            success = False

    return success


def add_modules_by_dir(path: str):
    if os.path.exists(path):
        modules = {}
        for fname in os.listdir(path):
            with open(os.path.join(path, fname)) as f:
                try:
                    descriptor = json.load(f)
                except:
                    pp = pprint.PrettyPrinter(indent=2)
                    print(os.path.join(path, fname))
                    pp.pprint((descriptor))
                    raise
            modules[descriptor["id"]] = OkapiModule(descriptor)
        add_modules(modules)
        return modules
    else:
        print(f"Path {path} does not exist!")
        sys.exit(1)


def deploy_modules(modules: list, node: str):
    okapi = OkapiClient()
    deployed_modules = [m["srvcId"] for m in okapi.get_deployed_modules()]
    for name in modules.keys():
        if not name in deployed_modules:
            print(f"Deploy {name}")
            okapi.deploy_module(name, node)
            deployed_modules.append(name)
        else:
            print(f"Module {name} already deployed")
    # Check if all is deployed
    deployed_modules = [m["srvcId"] for m in okapi.get_deployed_modules()]
    for name in modules.keys():
        if not name in deployed_modules:
            print(f"ERROR: {name} is not deployed")


def enable_modules(modules, tenant: str, preRelease: bool = False,
                   ignoreErrors: bool = False, purge: bool = False, simulate: bool = False,
                   deploy: bool = False, loadSample: bool = False, loadReference: bool = False):
    pp = pprint.PrettyPrinter(indent=2)
    okapi = OkapiClient()

    def get_tenant_modules():
        return [m["id"] for m in okapi.get_tenant_modules(tenant)]

    def add_module(name, module):
        print(f"Add {name} to tenant {tenant}")
        res = okapi.enable_module(module.get_modId(), tenant,
                                  preRelease=preRelease, deploy=deploy,
                                  ignoreErrors=ignoreErrors, purge=purge, simulate=simulate,
                                  loadSample=loadSample, loadReference=loadReference)
        # pp.pprint(res)
        # pp.pprint(o.get_tenant_modules(tenant))

    def add_requirements(name, mod):
        print(f"Add requirements for {name}")
        for require in mod.get_requires():
            print(f"\t find {require}")
            for name, module in modules.items():
                if require in module.get_provides():
                    print(f"\t Found in {name}")
                    if not name in get_tenant_modules():
                        add_requirements(name, module)
                        add_module(name, module)
                    else:
                        print(f"{name} already enabled")
    for name, module in modules.items():
        if not name in get_tenant_modules():
            add_requirements(name, module)
            add_module(name, module)
        else:
            print(f"{name} already enabled")


def disable_modules(tenant: str):
    okapi = OkapiClient()
    while okapi.get_tenant_modules(tenant):
        names = [m["id"] for m in okapi.get_tenant_modules(tenant)]
        for name in names:
            okapi.disable_module(name, tenant)
