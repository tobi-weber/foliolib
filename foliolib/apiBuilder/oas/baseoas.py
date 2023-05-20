# -*- coding: utf-8 -*-
# Copyright (C) 2023 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os

import yaml

log = logging.getLogger("foliolib.oas.baseoas")


class BaseOAS:

    def __init__(self, data, oaSchema, parent=None):
        self._oaSchema = oaSchema
        self._parent = parent or oaSchema
        self._schema_dir = parent.get_schema_dir() if parent else None
        if isinstance(data, dict):
            # if "$ref" in data:
            if list(data.keys())[0] == "$ref":
                fpath = data["$ref"]
                if not fpath.startswith("#/components"):
                    self._schema_dir = os.path.dirname(fpath)
                # self._data = self.__load(fpath)
                self._data = self.get_ref(fpath)
                log.info("Current schema dir: %s", self._schema_dir)
            else:
                self._data = data
        else:
            fpath = data
            self._schema_dir = os.path.dirname(fpath)
            self._data = self.__load(fpath)

    def __load(self, fpath):
        if self._parent.get_schema_dir():
            fpath = os.path.join(
                self._parent.get_schema_dir(), fpath)
        log.info("Load file %s", fpath)
        key = None
        if "#/" in fpath:
            p = fpath.split("#/")
            fpath = p[0]
            key = p[1]
        with open(fpath, encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.Loader)
        if key is not None:
            return data[key]
        else:
            return data

    def get_data(self):
        return self._data

    def get_schema_dir(self):
        return self._schema_dir

    def get_component(self, path):
        if path.startswith("#/components"):
            path = path.replace("#/components/", "").split("/")
            return self._data["components"][path[0]][path[1]]
        elif "#/components" in path:
            p = path.split("#/components/")
            data = self.get_ref(p[0])
            path = p[1].split("/")
            return data["components"][path[0]][path[1]]
        return None

    def get_ref(self, path):
        log.info("Get reference %s" % path)
        if "#/components" in path:
            component = self._oaSchema.get_component(path)
            # if "$ref" in component:
            if list(component.keys())[0] == "$ref":
                if "#/" in component["$ref"]:
                    p = component["$ref"].split("#/")
                    schema = self.__load(p[0])
                    return schema[p[1]]
                else:
                    return self.__load(component["$ref"])
            else:
                return component
        else:
            return self.__load(path)
