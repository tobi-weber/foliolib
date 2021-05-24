# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os
from typing import Union

from foliolib.config import Config
from foliolib.okapi import okapiClient

log = logging.getLogger("foliolib.okapi.okapiModule")


def create_okapiModule(name: str, version: str = None):
    """Create a instance of OkapiModule

    Args:
        name (str): Name of the module
        version (str, optional): Version of the okapi module. Defaults to None.

    Returns:
        [OkapiModule]: Instance of OkapiModule
    """
    log.info("Create Descriptor: %s - %s", name, version)
    cache_dir = Config().foliolibcfg().get("Cache", "descriptors")
    descriptor_fname = f"ModuleDescriptor-{name}-{version}.json"
    fname_cache = os.path.join(cache_dir, descriptor_fname)
    if os.path.exists(fname_cache):
        log.info("Load descriptor from %s", fname_cache)
        with open(fname_cache) as f:
            descriptor = json.load(f)
        module = OkapiModule(descriptor)
    else:
        module = OkapiModule(name, version=version)
        log.debug("Create descriptor for %s", module.get_modId())
        descriptor_fname = f"ModuleDescriptor-{module.get_modId()}.json"
        fname_cache = os.path.join(cache_dir, descriptor_fname)
        log.debug("Write descriptor to %s", fname_cache)
        with open(fname_cache, "w") as f:
            json.dump(module.get_descriptor(), f, indent=2)
    log.debug("Docker Image: %s", module.get_docker_image())

    return module


def create_okapiModules(modlist: dict):
    return [create_okapiModule(name, version=version)
            for name, version in modlist.items()]


class OkapiModule:
    """Defines an okapi module.
    """

    def __init__(self, descriptor: Union[dict, str], version: str = None) -> None:
        """
        Args:
            descriptor (Union[dict, str]): ModuleDescriptor or Module name, e.g. mod-users
            version (str, optional): Optional module version if value of descriptor is a Module name. Defaults to None.
        """
        if isinstance(descriptor, dict):
            self._descriptor = descriptor
        elif isinstance(descriptor, str):
            self._descriptor = self.__get_descriptor(descriptor, version)
        self.__remove_db_config()
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

    def get_docker_image(self):
        """ Get docker image name

        Returns:
            str: Get the name of the docker image
        """
        if "launchDescriptor" in self._descriptor:
            return self._descriptor["launchDescriptor"]["dockerImage"]
        else:
            return ""

    def __get_descriptor(self, name: str, version: str = None):
        host = Config().foliolibcfg().get("PullNode", "host")
        port = Config().foliolibcfg().get("PullNode", "port")
        log.info("Pull descriptor for %s-%s from %s:%s",
                 name, str(version), host, port)
        client = okapiClient.OkapiClient(host=host, port=port)
        if version is None:
            log.info("Get version for %s from latest release", name)
            version = okapiClient.request_release(name)["version"]
            log.info("Version is %s", version)
        modId = f"{name}-{version}"
        descriptor = client.get_module(modId)
        if "launchDescriptor" in descriptor:
            descriptor["launchDescriptor"]["dockerPull"] = True
        return descriptor

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

    def __remove_db_config(self):
        if "launchDescriptor" in self._descriptor:
            if "env" in self._descriptor["launchDescriptor"]:
                env = [item for item in self._descriptor["launchDescriptor"]["env"]
                       if not item["name"].startswith("DB_")]
                self._descriptor["launchDescriptor"]["env"] = env
