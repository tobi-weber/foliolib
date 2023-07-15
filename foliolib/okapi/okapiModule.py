# -*- coding: utf-8 -*-
# Copyright (C) 2023 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os
from configparser import NoOptionError
from typing import List, Union

from foliolib.config import Config

log = logging.getLogger("foliolib.okapi.okapiModule")


ENV_ARGS = ["DB_HOST",
            "DB_PORT",
            "DB_USERNAME",
            "DB_PASSWORD",
            "DB_DATABASE",
            "DB_QUERYTIMEOUT",
            "DB_CHARSET",
            # "DB_MAXPOOLSIZE",
            "KAFKA_HOST",
            "KAFKA_PORT",
            "OKAPI_URL",
            "ELASTICSEARCH_HOST",
            "ELASTICSEARCH_PORT",
            "ELASTICSEARCH_USERNAME",
            "ELASTICSEARCH_PASSWORD",
            "INITIAL_LANGUAGES",
            "ELASTICSEARCH_URL",
            ]


# workaround
REQUIREMENTS = {"inn-reach": ["login", "source-storage-records"]}


class OkapiModule:
    """Defines an okapi module.
    """

    def __init__(self, module: Union[dict, str]) -> None:
        """
        Args:
            module (Union[dict, str]): ModuleDescriptor or Module id, e.g. mod-users-17.1.0
        """
        # print("Create OkapiModule %s" % str(module))
        if isinstance(module, dict):
            self._descriptor = module
        elif isinstance(module, str):
            self._descriptor = self.__get_descriptor(module)
        log.debug("Create OkapiModule %s", self.get_id())
        self.__clean_env()
        self.__set_modules_parameters()
        # print(json.dumps(self._descriptor, indent=2))

    def get_id(self):
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
            list: Requirements
        """
        if "requires" in self._descriptor:
            requires = [r["id"] for r in self._descriptor["requires"]]
        else:
            requires = []
        for provide in self.get_provides():
            if provide in REQUIREMENTS:
                requires += REQUIREMENTS[provide]
        return requires

    def get_provides(self):
        """ Get provides

        Returns:
            list: Provides
        """
        if "provides" in self._descriptor:
            return [r["id"] for r in self._descriptor["provides"]]
        else:
            return []

    def has_requirement(self, require: str):
        return require in self.get_provides()

    def has_launchDescriptor(self):
        return "launchDescriptor" in self._descriptor

    def get_docker_image(self):
        """ Get docker image name

        Returns:
            str: Get the name of the docker image
        """
        if "launchDescriptor" in self._descriptor:
            return self._descriptor["launchDescriptor"]["dockerImage"]
        else:
            return None

    def get_docker_args(self):
        if "launchDescriptor" in self._descriptor:
            da = self._descriptor["launchDescriptor"]["dockerArgs"]
            if "Memory" in da["HostConfig"]:
                memory = da["HostConfig"]["Memory"]
            else:
                memory = None
            portBindings = list(da["HostConfig"]["PortBindings"].keys())[
                0].split("/")
            return {"memory": memory,
                    "port": int(portBindings[0]),
                    "protocol": portBindings[1]}
        else:
            return None

    def get_env(self):
        if "launchDescriptor" in self._descriptor:
            if "env" in self._descriptor["launchDescriptor"]:
                return self._descriptor["launchDescriptor"]["env"]
        return []

    def __get_descriptor(self, modId: str):
        log.debug("Load ModuleDescriptor for %s", modId)
        cache_dir = Config().foliolibcfg().get("Cache", "descriptors")
        host = Config().foliolibcfg().get("PullNode", "host")
        port = Config().foliolibcfg().get("PullNode", "port")
        try:
            ssl = Config().foliolibcfg().get("PullNode", "ssl")
        except NoOptionError:
            ssl = False

        log.debug("Try to pull descriptor from okapi.")
        from foliolib.okapi import okapiClient
        try:
            return okapiClient.OkapiClient().get_module(modId)
        except:
            pass
        # Try to load from cache
        descriptor_fname = f"ModuleDescriptor-{modId}.json"
        fname_cache = os.path.join(cache_dir, descriptor_fname)
        if os.path.exists(fname_cache):
            log.debug("Load descriptor from %s", fname_cache)
            with open(fname_cache, encoding="utf8") as f:
                return json.load(f)
        # Load from Okpai or from PullNode
        else:
            log.debug("Try to pull descriptor for %s from %s:%s",
                      modId, host, port)
            client = okapiClient.OkapiClient(host=host, port=port, ssl=ssl)
            descriptor = client.get_module(modId)
            descriptor_fname = f"ModuleDescriptor-{modId}.json"
            fname_cache = os.path.join(cache_dir, descriptor_fname)
            log.debug("Write descriptor to %s", fname_cache)
            with open(fname_cache, "w", encoding="utf8") as f:
                json.dump(descriptor, f, indent=2)

            return descriptor

    def __clean_env(self):
        if "launchDescriptor" in self._descriptor:
            if "env" in self._descriptor["launchDescriptor"]:
                env_args = ENV_ARGS.copy()
                env_args += [e.lower() for e in ENV_ARGS]
                env_args += [e.upper() for e in ENV_ARGS]
                env = [item for item in self._descriptor["launchDescriptor"]["env"]
                       if not item["name"] in env_args]
                self._descriptor["launchDescriptor"]["env"] = env

    def __set_modules_parameters(self):

        def remove_entry(env, name):
            # pylint: disable=undefined-loop-variable
            for entry in env:
                if entry["name"] == name:
                    env.remove(entry)
                elif entry["name"] == name.lower():
                    name = name.lower()
                    env.remove(entry)
                elif entry["name"] == name.upper():
                    name = name.upper()
                    env.remove(entry)
            if name.upper() in ENV_ARGS:
                name = name.upper()
            elif name.lower() in ENV_ARGS:
                name = name.lower()
            return name

        if "launchDescriptor" in self._descriptor:
            # print("Add Global env to module %s" % self.get_id())
            if "env" in self._descriptor["launchDescriptor"]:
                module_env = self._descriptor["launchDescriptor"]["env"]
            else:
                module_env = []
                self._descriptor["launchDescriptor"]["env"] = module_env
            for name, value in Config().get_env(True).items():
                # print("Add env %s: %s" % (name, value))
                name = name.upper()
                name = remove_entry(module_env, name)
                module_env.append({"name": name, "value": value})

            config = Config().modulescfg(self.get_id())
            # print("Add module env of %s" % self.get_id())
            if config is not None:
                if "Docker" in config:
                    if "Memory" in config["Docker"]:
                        self._descriptor["launchDescriptor"]["dockerArgs"]["HostConfig"]["Memory"]\
                            = config.getint(
                            "Docker", "Memory")
                if "Env" in config:
                    for name, value in config["Env"].items():
                        # print("Add env %s: %s" % (name, value))
                        name = name.upper()
                        name = remove_entry(module_env, name)
                        module_env.append({"name": name, "value": value})

                if Config().is_kubernetes():
                    dockerPull = False
                else:
                    dockerPull = True
                self._descriptor["launchDescriptor"]["dockerPull"] = dockerPull


def create_okapiModule(name: str):
    """Create a instance of OkapiModule by module id

    Args:
        name (str): Name of the module

    Returns:
        [OkapiModule]: Instance of OkapiModule
    """
    module = OkapiModule(name)
    log.debug("Docker Image: %s", module.get_docker_image())

    return module


def create_okapiModules(modIds: List[str]):
    """ Create instances of OkapiModule by module ids

    Args:
        modIds (List[str]): List of module ids

    Returns:
        list: Listwith instances of OkapiModule
    """
    return [create_okapiModule(modId)
            for modId in modIds]


def sort_modules_by_requirements(modules: List[OkapiModule]):
    """ Sort List with instances of OkapiModule by requirements

    Args:
        modules (List[OkapiModule]): List with instances of OkapiModule

    Returns:
        list: Listwith instances of OkapiModule
    """
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


def sort_modIds_by_requirements(modIds: List[str]):
    """ Sort List of modules ids by requirements

    Args:
        modIds (List[str]): List of module ids

    Returns:
        [type]: List of module ids
    """
    modules = sort_modules_by_requirements(create_okapiModules(modIds))
    return [m.get_id() for m in modules]
