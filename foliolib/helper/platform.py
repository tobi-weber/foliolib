# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os

from foliolib.okapi.okapiClient import OkapiClient
from foliolib.okapi.okapiModule import (create_okapiModule,
                                        sort_modules_by_requirements)

log = logging.getLogger("foliolib.helper.okapi")


def __get_modules(fname, platform_path):
    log.debug("Load modules for %s", platform_path)
    with open(os.path.join(platform_path, fname)) as f:
        modules = sort_modules_by_requirements(
            [create_okapiModule(m["id"]) for m in json.load(f)]
        )
    return modules


def __add_modules(modules):
    for module in modules:
        if OkapiClient().is_module_added(module):
            print("%s is already added" % module.get_id())
        else:
            print("Add %s" % module.get_id())
            OkapiClient().add_module(module)


def __deploy_modules(node, modules, edge_module=None):
    edge_module = edge_module or []
    for module in modules:
        if module.has_launchDescriptor():
            if OkapiClient().is_module_deployed(module.get_id()):
                print("%s is already deployed" % module.get_id())
            elif module.get_id().startswith("edge-"):
                if not [m for m in edge_module if module.get_id().startswith(m)]:
                    try:
                        print("Deploy %s" % module.get_id())
                        OkapiClient().deploy_module(module.get_id(), node)
                    except:
                        print("Error: Deploy %s failed" % module.get_id())
            else:
                print("Deploy %s" % module.get_id())
                OkapiClient().deploy_module(module.get_id(), node)


def install_platform(platform_path: str, node: str,
                     tenantid: str, edge_module: list,
                     loadSample: bool = False, loadReference: bool = False,
                     **kwargs):
    """Install a folio platform.

    Args:
        platform_path (str): Path to the folder of the folio platform.
        node (str): node id
        tenantid (str): tenant id
        loadSample (bool, optional): load samples. Defaults to False.
        loadReference (bool, optional): load example reference data. Defaults to False.
    """

    def create_tenant():
        if not tenantid in [e["id"] for e in OkapiClient().get_tenants()]:
            print("\nTenant %s does not exist. Create tenant ..." % tenantid)
            OkapiClient().create_tenant(tenantid)

    def enable_modules(modules):
        for module in modules:
            if OkapiClient().is_module_enabled(module.get_id(), tenantid):
                print("Module %s is already enabled for tenant %s" %
                      (module.get_id(), tenantid))
            else:
                print("Enable %s" % module.get_id())
                OkapiClient().enable_module(module.get_id(), tenantid,
                                            loadSample=loadSample, loadReference=loadReference,
                                            **kwargs)

    okapi_modules = __get_modules("okapi-install.json", platform_path)
    stripes_modules = __get_modules("stripes-install.json", platform_path)

    print("\nInstall platform %s" % platform_path)
    print("\tNode: %s" % node)
    print("\tTenant id: %s" % tenantid)
    print("\tLoad samples: %s" % str(loadSample))
    print("\tLoad references: %s" % str(loadReference))

    create_tenant()
    print("\nAdd modules ...")
    __add_modules(okapi_modules + stripes_modules)
    print("\nDeploy modules ...")
    __deploy_modules(node,
                     okapi_modules + stripes_modules,
                     edge_module)
    print("\nEnable modules for tenant %s ..." % tenantid)
    enable_modules(okapi_modules + stripes_modules)


def upgrade_platform(platform_path: str, node: str,
                     tenantid: str, edge_module: list,
                     **kwargs):
    """Upgrade a folio platform.

    Args:
        platform_path (str): Path to the folder of the folio platform.
        node (str): node id
        tenantid (str): tenant id
        loadSample (bool, optional): load samples. Defaults to False.
    """
    okapi_modules = __get_modules("okapi-install.json", platform_path)
    stripes_modules = __get_modules("stripes-install.json", platform_path)

    __add_modules(okapi_modules + stripes_modules)
    __deploy_modules(node,
                     okapi_modules + stripes_modules,
                     edge_module)
    print("Upgrade modules for tenant %s ..." % tenantid)
    msg = OkapiClient().upgrade_modules(tenantid, **kwargs)
    print(json.dumps(msg, indent=2))
