# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import gzip
import json
import logging
import os
import sys
import tarfile
import tempfile
import zipfile

import requests
from foliolib.config import Config
from foliolib.exceptions import FoliolibError
from foliolib.helper import split_modid
from foliolib.helper.modules import (add_modules, deploy_modules,
                                     deploy_modules_async, enable_modules,
                                     load_install_file)
from foliolib.helper.okapi import clean_okapi
from foliolib.okapi.okapiClient import OkapiClient

log = logging.getLogger("foliolib.helper.platform")


def __process_platform(platform):
    tmp = tempfile.gettempdir()
    if os.path.isdir(platform):
        return platform
    elif platform.endswith(".tar.gz"):
        with tarfile.open(platform, "r:gz") as t:
            t.extractall(tmp)
            return os.path.join(tmp,
                                t.getmembers()[0].name)
    elif platform.endswith(".zip"):
        raise NotImplemented("zip support is not implemented yet")
        print("platform is zipfile")
        with zipfile.ZipFile(platform, "r") as z:
            z.extractall(tmp)
            print(z.filelist())
            return "ZIP"
    else:
        cache_dir = os.path.join(Config().foliolibcfg()[
                                 "Cache"]["platforms"])
        if not os.path.exists(cache_dir):
            os.mkdir(cache_dir)
        fname = os.path.join(cache_dir, f"folio-platform-{platform}.tar.gz")
        if not os.path.exists(fname):
            print("Download folio platform %s" % platform)
            url = f"https://api.github.com/repos/folio-org/platform-complete/tags"
            response = requests.get(url)
            tags = response.json()
            tarball_url = None
            for t in tags:
                if t["name"] == platform.strip():
                    tarball_url = t["tarball_url"]
            if tarball_url is None:
                print("Available folio platforms:")
                names = [t["name"] for t in tags]
                for name in sorted(names):
                    print(name)
                raise FoliolibError("Unknown platform %s" % platform)
            response = requests.get(tarball_url)
            with open(fname, "bw") as f:
                f.write(response.content)

        with tarfile.open(fname, "r:gz") as f:
            f.extractall(tmp)
            return os.path.join(tmp,
                                f.getmembers()[0].name)


def install_platform(platform: str, tenantid: str, node: str = None,
                     loadSample: bool = False, loadReference: bool = False,
                     deploy_async=False, **kwargs):
    """Install a folio platform.

    Args:
        platform(str): Path to the folder of the folio platform.
        tenantid (str): tenant id
        node (str): The node id on which module should be deployed. Default first node from nodes list.
        loadSample (bool, optional): load samples. Defaults to False.
        loadReference (bool, optional): load example reference data. Defaults to False.
        deploy_async (bool, optional): Wether to deploy asynchronously. Defaults to False.
        **kwargs (properties): Keyword Arguments

    Keyword Args:
        ignoreErrors (boolean): default = false
                    Okapi 4.2.0 and later, it is possible to ignore errors during the install operation. This is done by supplying parameter ignoreErrors=true.
                    In this case, Okapi will try to upgrade all modules in the modules list, regardless if one of them fails. However, for individual modules,
                    if they fail, their upgrade will not be commited.
                    This is an experimental parameter which was added to be able to inspect all problem(s) with module upgrade(s).
        invoke (boolean): default = true
                    Whether to invoke for tenant init/permissions/purge
        npmSnapshot (boolean): default = true
                    Whether to include NPM module snapshots (default:true).
        preRelease (boolean): default = true
                    Whether pre-releases should be considered for installation.
        purge (boolean): default = false
                    Disabled modules will also be purged.
        reinstall: (boolean - default: false)
                    Whether to install modules even if up-to-update.
        simulate (boolean): default = false
                    Whether the installation is simulated
    """

    def create_tenant():
        if not tenantid in [e["id"] for e in OkapiClient().get_tenants()]:
            print("\nTenant %s does not exist. Create tenant ..." % tenantid)
            OkapiClient().create_tenant(tenantid)

    platform = __process_platform(platform)
    # sys.exit(0)
    okapi_install = os.path.join(platform, "okapi-install.json")
    okapi_modules = load_install_file(okapi_install)
    stripes_install = os.path.join(platform, "stripes-install.json")
    stripes_modules = load_install_file(stripes_install)

    print("\nInstall platform %s" % platform)
    print("\tNode: %s" % node)
    print("\tTenant id: %s" % tenantid)
    print("\tLoad samples: %s" % str(loadSample))
    print("\tLoad references: %s" % str(loadReference))

    create_tenant()
    stripes_modules = [m for m in stripes_modules
                       if not m.get_id().startswith("edge-")]
    okapi_modules = [m for m in okapi_modules
                     if not m.get_id().startswith("edge-")]
    print("\nAdd modules ...")
    add_modules(okapi_modules + stripes_modules)
    print("\nDeploy modules ...")
    if deploy_async:
        deploy_modules_async(okapi_modules, node)
    else:
        deploy_modules(okapi_modules, node)
    print("\nEnable modules for tenant %s ..." % tenantid)
    enable_modules(tenantid, okapi_modules + stripes_modules,
                   loadSample=loadSample, loadReference=loadReference,
                   **kwargs)


def upgrade_platform(platform: str, tenantid: str, node: str = None,
                     deploy_async: bool = False, exclude: list = None,
                     **kwargs):
    """Upgrade a folio platform.

    Args:
        platform (str): Path to the folder of the folio platform.
        tenantid (str): tenant id
        node (str): The node id on which module should be deployed. Default first node from nodes list.
        deploy_async (bool, optional): Wether to deploy asynchronously. Defaults to False.
        **kwargs (properties): Keyword Arguments

    Keyword Args:
        ignoreErrors (boolean): default = false
                    Okapi 4.2.0 and later, it is possible to ignore errors during the upgrade operation.
                    This is done by supplying parameter ignoreErrors=true.
                    In this case, Okapi will try to upgrade all modules in the modules list, regardless if one of them fails.
                    However, for individual modules, if they fail, their upgrade will not be commited. This is an experimental
                    parameter which was added to be able to inspect all problem(s) with module upgrade(s).
        invoke (boolean): default = true
                    Whether to invoke for tenant init/permissions/purge
        preRelease (boolean): default = true
                    Whether pre-releases should be considered for installation.
        simulate (boolean): default = false
                    Whether the upgrade is simulated
        tenantParameters (string): Parameters for Tenant init
    """
    def upgrade(tid):
        okapi = OkapiClient()
        for m in okapi_modules:
            if m.get_id().startswith("mod-authtoken"):
                print("Upgrade %s for tenant %s" % (m.get_id(), tid))
                msg = okapi.upgrade_modules(tid, [m.get_id()], invoke=False)
                print(json.dumps(msg, indent=2))
        print("Upgrade modules for tenant %s ..." % tid)
        msg = okapi.upgrade_modules(tid, **kwargs)
        print(json.dumps(msg, indent=2))
    platform = __process_platform(platform)

    okapi_install = os.path.join(platform, "okapi-install.json")
    okapi_modules = load_install_file(okapi_install)
    stripes_install = os.path.join(platform, "stripes-install.json")
    stripes_modules = load_install_file(stripes_install)
    stripes_modules = [m for m in stripes_modules
                       if not m.get_id().startswith("edge-")]
    okapi_modules = [m for m in okapi_modules
                     if not m.get_id().startswith("edge-")]

    if exclude is not None:
        for mod_name in exclude:
            stripes_modules = [m for m in stripes_modules
                               if not mod_name == split_modid(m.get_id())[0]]
            okapi_modules = [m for m in okapi_modules
                             if not mod_name == split_modid(m.get_id())[0]]

    add_modules(okapi_modules + stripes_modules)

    if deploy_async:
        deploy_modules_async(okapi_modules, node)
    else:
        deploy_modules(okapi_modules, node)

    if tenantid == "ALL":
        tenants = OkapiClient().get_tenants()
        for tenant in tenants:
            if not tenant["id"] == "supertenant":
                upgrade(tenant["id"])
    else:
        upgrade(tenantid)
    clean_okapi()
