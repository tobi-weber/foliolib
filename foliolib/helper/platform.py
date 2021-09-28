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
        print("Add module %s" % module.get_modId())
        OkapiClient().add_module(module)


def __deploy_modules(node, modules):
    for module in modules:
        print("Deploy module %s" % module.get_modId())
        OkapiClient().deploy_module(module.get_modId(), node)


def install_platform(platform_path: str, node: str, tenantid: str,
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
            OkapiClient().create_tenant(tenantid)

    def enable_modules(modules):
        for module in modules:
            print("Enable module %s for tenant %s" % (module.get_modId(),
                                                      tenantid))
            OkapiClient().enable_module(module.get_modId(), tenantid,
                                        loadSample=loadSample, loadReference=loadReference,
                                        **kwargs)

    okapi_modules = __get_modules("okapi-install.json", platform_path)
    stripes_modules = __get_modules("stripes-install.json", platform_path)

    create_tenant()
    __add_modules(okapi_modules + stripes_modules)
    __deploy_modules(node, okapi_modules)
    enable_modules(okapi_modules + stripes_modules)


def upgrade_platform(platform_path: str, node: str, tenantid: str,
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
    __deploy_modules(node, okapi_modules)

    OkapiClient().upgrade_modules(tenantid, **kwargs)
