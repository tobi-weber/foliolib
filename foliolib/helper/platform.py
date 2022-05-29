# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os

from foliolib.helper.modules import add_modules, deploy_modules, load_modules
from foliolib.okapi.okapiClient import OkapiClient

log = logging.getLogger("foliolib.helper.platform")


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

    okapi_install = os.path.join(platform_path, "okapi-install.json")
    okapi_modules = load_modules(okapi_install)
    stripes_install = os.path.join(platform_path, "stripes-install.json")
    stripes_modules = load_modules(stripes_install)

    print("\nInstall platform %s" % platform_path)
    print("\tNode: %s" % node)
    print("\tTenant id: %s" % tenantid)
    print("\tLoad samples: %s" % str(loadSample))
    print("\tLoad references: %s" % str(loadReference))

    create_tenant()
    print("\nAdd modules ...")
    add_modules(okapi_modules + stripes_modules)
    print("\nDeploy modules ...")
    deploy_modules(node,
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
    def upgrade(tid):
        print("Upgrade modules for tenant %s ..." % tid)
        msg = OkapiClient().upgrade_modules(tid, **kwargs)
        print(json.dumps(msg, indent=2))

    okapi_install = os.path.join(platform_path, "okapi-install.json")
    okapi_modules = load_modules(okapi_install)
    stripes_install = os.path.join(platform_path, "stripes-install.json")
    stripes_modules = load_modules(stripes_install)

    add_modules(okapi_modules + stripes_modules)
    deploy_modules(node,
                   okapi_modules + stripes_modules,
                   edge_module)

    if tenantid == "ALL":
        tenants = OkapiClient().get_tenants()
        for tenant in tenants:
            upgrade(tenant["id"])
    else:
        upgrade(tenantid)
