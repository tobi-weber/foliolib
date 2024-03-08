# -*- coding: utf-8 -*-
# Copyright (C) 2023 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os

import yaml

log = logging.getLogger("foliolib.oas.baseoas")


class BaseOAS:

    def __init__(self, data, parent=None):
        self._parent = parent
        self._schema_dir = parent.get_schema_dir() if parent else None
        self._filepath = None
        if isinstance(data, dict):
            # if "$ref" in data:
            if list(data.keys())[0] == "$ref":
                log.info("Data is $ref: %s" % str(data))
                fpath = data["$ref"]
                if fpath.startswith("#/components"):
                    component_path = fpath.replace("#/components/", "")
                    self._schema_dir = os.path.dirname(component_path)
                elif fpath.startswith("#/"):
                    log.info("$ref is a key: %s" % str(fpath))
                    self._schema_dir = self.get_parent_schema_dir()
                    self._filepath = self._parent.get_filepath()
                else:
                    self._schema_dir = os.path.dirname(fpath)
                # self._data = self.__load(fpath)
                self._data = self.get_ref(fpath)
            else:
                log.info("Data is object")
                self._data = data
        elif data.startswith("#/components"):
            log.info("Data is component: %s" % data)
            self._data = self.get_ref(data)
        elif data.startswith("#/"):
            log.info("Data is a key: %s" % str(data))
            self._filepath = self._parent.get_filepath()
            self._schema_dir = parent.get_schema_dir()
            self._data = self.get_ref(data)
        else:
            log.info("Data is file path: %s" % data)
            fpath = data
            dirname = os.path.dirname(fpath)
            if dirname:
                self._schema_dir = os.path.join(self.get_parent_schema_dir(), dirname)
            else:
                self._schema_dir = self.get_parent_schema_dir()
            self._data = self.__load(fpath)
        log.info("Current schema dir: %s", self._schema_dir)
        log.info("Current file path: %s", self._filepath)

    def __load(self, fpath):
        log.info("Load file %s", fpath)

        # Split key from path, if path FILE.json#/KEY
        key = None
        if "#/" in fpath:
            p = fpath.split("#/")
            fpath = p[0]
            key = p[1]

        if self.get_parent_schema_dir() and os.path.exists(
            os.path.join(self.get_parent_schema_dir(), fpath)
        ):
            fpath = os.path.join(self.get_parent_schema_dir(), fpath)

        if not os.path.exists(fpath):
            fpath = fpath.replace("../", "")

        log.info("File path: %s", fpath)
        self._filepath = fpath
        with open(fpath, encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.Loader)
        self._schema_dir = os.path.dirname(fpath)
        if key is not None:
            return data[key]
        else:
            return data

    def get_oaSchema(self):
        return self._parent.get_oaSchema()

    def get_parent(self):
        return self._parent

    def get_filepath(self):
        return self._filepath

    def get_data(self):
        return self._data

    def get_schema_dir(self):
        return self._schema_dir

    def get_parent_schema_dir(self):
        if self._parent is None:
            return "."
        else:
            return self._parent.get_schema_dir()

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
            log.info("Get reference from components")
            component = self.get_oaSchema().get_component(path)
            log.info("Component: %s" % component)
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
        elif path.startswith("#/"):
            with open(self._parent.get_filepath(), encoding="utf-8") as f:
                data = yaml.load(f, Loader=yaml.Loader)
            key = path.replace("#/", "")
            return data[key]
        else:
            return self.__load(path)
