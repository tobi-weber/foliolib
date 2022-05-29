# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os

from foliolib.okapi.okapiClient import OkapiClient
from foliolib.okapi.okapiModule import (create_okapiModule,
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


def deploy_modules(node, modules, edge_module=None):
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
