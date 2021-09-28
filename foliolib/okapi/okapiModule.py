# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os
from typing import List, Union

from foliolib.config import Config
from foliolib.okapi import okapiClient

log = logging.getLogger("foliolib.okapi.okapiModule")


class OkapiModule:
    """Defines an okapi module.
    """

    def __init__(self, module: Union[dict, str]) -> None:
        """
        Args:
            module (Union[dict, str]): ModuleDescriptor or Module name, e.g. mod-users
            version (str, optional): Optional module version if value of descriptor is a Module name. Defaults to None.
        """
        if isinstance(module, dict):
            self._descriptor = module
        elif isinstance(module, str):
            self._descriptor = self.__get_descriptor(module)
        log.debug("OkapiModule %s", self.get_modId())
        self.__clean_env()
        self.__set_modules_parameters()

    def get_modId(self):
        """ Get module name

        Returns:
            str: Module name
        """
        return self._descriptor["id"]

    def get_descriptor(self):
        """ Get ModuleDescriptor

        Returns:
            dict: ModuleDescriptor
        """
        return self._descriptor

    def get_requires(self):
        """ Get requirements for the module

        Returns:
            dict: Dict with requirements
        """
        if "requires" in self._descriptor:
            return [r["id"] for r in self._descriptor["requires"]]
        else:
            return []

    def get_provides(self):
        """ Get provides

        Returns:
            dict: Dict with provides
        """
        if "provides" in self._descriptor:
            return [r["id"] for r in self._descriptor["provides"]]
        else:
            return []

    def has_requirement(self, require: str):
        return require in self.get_provides()

    def get_docker_image(self):
        """ Get docker image name

        Returns:
            str: Get the name of the docker image
        """
        if "launchDescriptor" in self._descriptor:
            return self._descriptor["launchDescriptor"]["dockerImage"]
        else:
            return ""

    def __get_descriptor(self, modId: str):
        host = Config().foliolibcfg().get("PullNode", "host")
        port = Config().foliolibcfg().get("PullNode", "port")
        log.info("Pull descriptor for %s from %s:%s",
                 modId, host, port)
        client = okapiClient.OkapiClient(host=host, port=port)
        descriptor = client.get_module(modId)
        if "launchDescriptor" in descriptor:
            descriptor["launchDescriptor"]["dockerPull"] = True
        return descriptor

    def __clean_env(self):
        if "launchDescriptor" in self._descriptor:
            if "env" in self._descriptor["launchDescriptor"]:
                env = [item for item in self._descriptor["launchDescriptor"]["env"]
                       if not item["name"].startswith("DB_")
                       and not item["name"].startswith("KAFKA_")
                       and not item["name"].startswith(("OKAPI_URL"))]
                self._descriptor["launchDescriptor"]["env"] = env

    def __set_modules_parameters(self):

        def remove_entry(l, name):
            for e in l:
                if e["name"].lower() == name.lower():
                    l.remove(e)

        config = Config().modulescfg(self.get_modId())
        if config is not None:
            if "Docker" in config:
                if "Memory" in config["Docker"]:
                    self._descriptor["launchDescriptor"]["dockerArgs"]["HostConfig"]["Memory"] = config.getint(
                        "Docker", "Memory")
            if "Env" in config:
                env = self._descriptor["launchDescriptor"]["env"]
                for k, v in config["Env"].items():
                    remove_entry(env, k)
                    env.append({"name": k.upper(), "value": v})


def create_okapiModule(name: str):
    """Create a instance of OkapiModule

    Args:
        name (str): Name of the module

    Returns:
        [OkapiModule]: Instance of OkapiModule
    """
    log.info("Create Descriptor: %s", name)
    cache_dir = Config().foliolibcfg().get("Cache", "descriptors")
    descriptor_fname = f"ModuleDescriptor-{name}.json"
    fname_cache = os.path.join(cache_dir, descriptor_fname)
    if os.path.exists(fname_cache):
        log.info("Load descriptor from %s", fname_cache)
        with open(fname_cache) as f:
            descriptor = json.load(f)
        module = OkapiModule(descriptor)
    else:
        module = OkapiModule(name)
        log.debug("Create descriptor for %s", module.get_modId())
        descriptor_fname = f"ModuleDescriptor-{module.get_modId()}.json"
        fname_cache = os.path.join(cache_dir, descriptor_fname)
        log.debug("Write descriptor to %s", fname_cache)
        with open(fname_cache, "w") as f:
            json.dump(module.get_descriptor(), f, indent=2)
    log.debug("Docker Image: %s", module.get_docker_image())

    return module


def create_okapiModules(modIds: List[str]):
    return [create_okapiModule(modId)
            for modId in modIds]


def sort_modules_by_requirements(modules: List[OkapiModule]):
    _modules = []

    def add_module(module):
        if not module in _modules:
            _modules.append(module)

    def resolve_requirements(module):
        for require in module.get_requires():
            for module in modules:
                if require in module.get_provides():
                    resolve_requirements(module)
                    add_module(module)

    for module in modules:
        resolve_requirements(module)
        add_module(module)

    return _modules
