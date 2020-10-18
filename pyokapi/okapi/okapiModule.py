# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import logging

from pyokapi.config import CONFIG

log = logging.getLogger("okapi.okapiModule")


class OkapiModule:

    def __init__(self, descriptor: str) -> None:
        self._descriptor = descriptor
        self.__remove_db_config()
        self.__set_modules_parameters()

    def get_modId(self):
        return self._descriptor["id"]

    def get_descriptor(self):
        return self._descriptor

    def get_requires(self):
        if "requires" in self._descriptor:
            return [r["id"] for r in self._descriptor["requires"]]
        else:
            return []

    def get_provides(self):
        if "provides" in self._descriptor:
            return [r["id"] for r in self._descriptor["provides"]]
        else:
            return []

    def get_docker_image(self):
        if "launchDescriptor" in self._descriptor:
            return self._descriptor["launchDescriptor"]["dockerImage"]
        else:
            return ""

    def __set_modules_parameters(self):

        def remove_entry(l, name):
            for e in l:
                if e["name"].lower() == name.lower():
                    l.remove(e)

        config = CONFIG.modulescfg(self.get_modId())
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
