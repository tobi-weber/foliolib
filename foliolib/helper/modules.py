# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os
from threading import Thread

from foliolib.okapi.okapiClient import OkapiClient
from foliolib.okapi.okapiModule import (OkapiModule, create_okapiModule,
                                        sort_modules_by_requirements)

log = logging.getLogger("foliolib.helper.modules")


def load_install_file(install_file: str):
    """Load folio platform install file.

    Args:
        install_file (str): Path to install file.

    Returns:
        list: Instances of OkapiModule.
    """
    log.debug("Load modules for %s", install_file)
    with open(install_file) as f:
        modules = [create_okapiModule(m["id"]) for m in json.load(f)]
    return modules


def add_modules(modules: list):
    """Add module to okapi.

    Args:
        modules (list): Instances of OkapiModule.
    """
    for module in sort_modules_by_requirements(modules):
        if OkapiClient().is_module_added(module):
            log.warning("%s is already added", module.get_id())
        else:
            log.info("Add %s", module.get_id())
            OkapiClient().add_module(module)


def deploy_modules(modules: list, node: str = None):
    """Deploy modules.

    Args:
        modules (list): Instances of OkapiModule.
        node (str, optional): The node id on which module should be deployed. Default first node from nodes list.
    """
    for module in sort_modules_by_requirements(modules):
        if module.has_launchDescriptor():
            if OkapiClient().is_module_deployed(module.get_id()):
                log.warning("%s is already deployed", module.get_id())
            else:
                log.info("Deploy %s", module.get_id())
                OkapiClient().deploy_module(module.get_id(), node)


def deploy_modules_async(modules: list, node: str = None):
    """Deploy modules asynchronously.

    Args:
        modules (list): Instances of OkapiModule.
        node (str, optional): The node id on which module should be deployed. Default first node from nodes list.
    """
    class Deploy(Thread):
        def __init__(self, module, node):
            super().__init__(name=module.get_id())
            self.module = module
            self.node = node

        def run(self):
            self.exc = None
            try:
                OkapiClient().deploy_module(self.module.get_id(), self.node)
            except BaseException as e:
                self.exc = e

        def join(self):
            Thread.join(self)
            if self.exc:
                log.error("Deploy failed for %s", self.name)
                raise self.exc
    threads = []

    for module in sort_modules_by_requirements(modules):
        if module.has_launchDescriptor():
            if OkapiClient().is_module_deployed(module.get_id()):
                log.warning("%s is already deployed", module.get_id())
            else:
                log.info("Deploy %s", module.get_id())
                t = Deploy(module, node)
                t.start()
                threads.append(t)
    log.info("Deploying please wait ...")
    for t in threads:
        t.join()
    log.info("Deploy done.")


def enable_modules(tenantid: str, modules: list, loadSample: bool = False, loadReference: bool = False, **kwargs):
    """Enable modules for a tenant.

    Args:
        tenantid (str): Tenant id
        modules (list): Instances of OkapiModule.
        loadSample (bool, optional): load samples. Defaults to False.
        loadReference (bool, optional): load example reference data. Defaults to False.
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
        simulate (boolean): default = false
                    Whether the installation is simulated
    """
    for module in sort_modules_by_requirements(modules):
        if isinstance(module, OkapiModule):
            module = module.get_id()
        if OkapiClient().is_module_enabled(module, tenantid):
            log.warning(
                "Module %s is already enabled for tenant %s", module, tenantid)
        else:
            log.info("Enable %s", module)
            OkapiClient().enable_module(tenantid, module,
                                        loadSample=loadSample, loadReference=loadReference,
                                        **kwargs)
