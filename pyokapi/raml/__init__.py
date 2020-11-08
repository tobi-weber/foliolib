# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os

import yaml
from pyokapi.raml.codeBuilder import CodeBuilder
from pyokapi.raml.ramlUrl import RamlUrl

log = logging.getLogger("pyokapi.raml")


class IncludeTag(yaml.YAMLObject):
    yaml_tag = "!include"

    def __init__(self, include_var):
        if os.path.exists(include_var):
            with open(include_var) as f:
                if include_var.endswith(".raml"):
                    value = yaml.load(f, Loader=yaml.Loader)
                elif include_var.endswith(".json"):
                    value = json.load(f)
                else:
                    value = f.read()
        else:
            value = include_var
        self.value = value

    def __repr__(self):
        return "IncludeTag(value=%s)" % str(self.value)

    @classmethod
    def from_yaml(cls, loader, node):
        tag = IncludeTag(node.value)
        return tag.value


class Raml:

    def __init__(self, data, title):
        log.debug("Raml: %s", title)
        self._data = data
        self._title = title
        self._urls = []
        self._ramlGlobals = {}
        for k, v in data.items():
            if k.startswith("/"):
                self._urls.append(RamlUrl(k, data[k], self._ramlGlobals))
            else:
                self._ramlGlobals[k] = v

    def get_title(self):
        return self._title

    def get_data(self):
        return self._data

    def get_urls(self):
        return self._urls

    def get_globals(self):
        return self._ramlGlobals


def load_raml(path):
    dirname = os.path.dirname(path)
    basename = os.path.basename(path)
    if dirname:
        os.chdir(dirname)
    with open(basename) as f:
        data = yaml.load(f, Loader=yaml.Loader)

    raml = Raml(data, os.path.splitext(basename)[0])
    #builder = CodeBuilder(raml)
    # print(path)
    # print(builder.get_code())

    return raml
