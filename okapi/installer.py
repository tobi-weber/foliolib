# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import sys

from okapi import OKAPI_HOST, helper
from okapi.okapiClient import OkapiClient


def create_tenant(tenant: str):
    print("\n")
    print("#########################")
    print(f"#### Create Tenant #####")
    print("#########################")
    print("\n")
    print(f"Id: {tenant}")
    OkapiClient().create_tenant(tenant)


def create_module_descriptors(mods: list, cache_dir: str = "descriptors"):
    print("\n")
    print("####################################")
    print(f"#### Create ModuleDescriptors #####")
    print("####################################")
    print("\n")
    modules = helper.create_modules_from_releases(
        mods, cache_dir)

    return modules


def add_modules(modules: list):
    print("\n")
    print("#######################")
    print(f"#### Add Modules #####")
    print("#######################")
    print("\n")
    helper.add_modules(modules)


def deploy_modules(modules, node: str):
    print("\n")
    print("##########################")
    print(f"#### Deploy Modules #####")
    print("##########################")
    print("\n")
    helper.deploy_modules(modules, node)

    deployed_modules = [m["srvcId"]
                        for m in OkapiClient().get_deployed_modules()]
    for name in modules.keys():
        if not name in deployed_modules:
            print(f"ERROR: {name} is not deployed")


def enable_modules(modules: list, tenant: str, preRelease: bool = False, ignoreErrors: bool = False,
                   purge: bool = False, simulate: bool = False,
                   loadSample: bool = False, loadReference: bool = False):
    print("\n")
    print("##########################")
    print(f"#### Enable Modules #####")
    print("##########################")
    print("\n")
    helper.enable_modules(modules, tenant, preRelease=preRelease, ignoreErrors=ignoreErrors,
                          purge=purge, simulate=simulate, loadSample=loadSample,
                          loadReference=loadReference)


def install_with_okapi_install_file(fname, node: str, tenant: str, cache_dir: str = "descriptors",
                                    preRelease: bool = False, ignoreErrors: bool = False,
                                    purge: bool = False, simulate: bool = False,
                                    loadSample: bool = False, loadReference: bool = False):
    if OKAPI_HOST == "localhost":
        print("ERROR: Okapi host must be set to the host ip adress!")
        sys.exit(1)
    mods = helper.load_okapi_install(fname)
    if not tenant in [e["id"] for e in OkapiClient().get_tenants()]:
        create_tenant(tenant)
    modules = create_module_descriptors(mods, cache_dir)
    add_modules(modules)
    deploy_modules(modules, node)
    enable_modules(modules, tenant, preRelease=preRelease, ignoreErrors=ignoreErrors,
                   purge=purge, simulate=simulate, loadSample=loadSample,
                   loadReference=loadReference)
