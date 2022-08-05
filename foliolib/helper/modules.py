# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os
from threading import Thread

from foliolib.okapi import okapiModule
from foliolib.okapi.okapiClient import OkapiClient
from foliolib.okapi.okapiModule import (OkapiModule, create_okapiModule,
                                        sort_modules_by_requirements)

log = logging.getLogger("foliolib.helper.modules")


def load_modules(install_file):
    log.debug("Load modules for %s", install_file)
    with open(os.path.join(install_file)) as f:
        modules = sort_modules_by_requirements(
            [create_okapiModule(m["id"]) for m in json.load(f)]
        )
    return modules


def add_modules(modules):
    for module in modules:
        if OkapiClient().is_module_added(module):
            print("%s is already added" % module.get_id())
        else:
            print("Add %s" % module.get_id())
            OkapiClient().add_module(module)


def deploy_modules(node, modules):
    for module in modules:
        if module.has_launchDescriptor():
            if OkapiClient().is_module_deployed(module.get_id()):
                print("%s is already deployed" % module.get_id())
            else:
                print("Deploy %s" % module.get_id())
                OkapiClient().deploy_module(module.get_id(), node)


def deploy_modules_threaded(node, modules):
    class Deploy(Thread):
        def __init__(self, node, module):
            super().__init__(name=module.get_id())
            self.node = node
            self.module = module

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

    for module in modules:
        if module.has_launchDescriptor():
            if OkapiClient().is_module_deployed(module.get_id()):
                print("%s is already deployed" % module.get_id())
            else:
                print("Deploy %s" % module.get_id())
                t = Deploy(node, module)
                t.start()
                threads.append(t)
    print("Deploying please wait ...")
    for t in threads:
        t.join()
    print("Deploy done.")


def enable_modules(tenantid, modules, loadSample=False, loadReference=False, **kwargs):
    for module in modules:
        if isinstance(module, OkapiModule):
            module = module.get_id()
        if OkapiClient().is_module_enabled(module, tenantid):
            print("Module %s is already enabled for tenant %s" %
                  (module, tenantid))
        else:
            print("Enable %s" % module)
            OkapiClient().enable_module(module, tenantid,
                                        loadSample=loadSample, loadReference=loadReference,
                                        **kwargs)