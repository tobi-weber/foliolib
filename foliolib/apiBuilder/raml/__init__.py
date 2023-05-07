# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os

import yaml
from foliolib.apiBuilder import get_module_code
from foliolib.apiBuilder.raml.codeBuilder import CodeBuilder
from foliolib.apiBuilder.raml.ramlUrl import RamlUrl

log = logging.getLogger("foliolib.raml")


class IncludeTag(yaml.YAMLObject):
    yaml_tag = "!include"

    def __init__(self, include_var):
        if os.path.exists(include_var):
            with open(include_var, encoding="utf-8") as f:
                if include_var.endswith(".raml"):
                    value = yaml.load(f, Loader=yaml.Loader)
                elif include_var.endswith(".json"):
                    try:
                        value = json.load(f)
                    except:
                        value = ""  # f.read()
                else:
                    value = f.read()
        else:
            value = include_var
        self.value = value

    def __repr__(self):
        return f"IncludeTag(value={str(self.value)})"

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
    curdir = os.getcwd()
    if dirname:
        os.chdir(dirname)
    with open(basename, encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.Loader)

    raml = Raml(data, os.path.splitext(basename)[0])

    os.chdir(curdir)

    return raml


def build_from_raml(schema_path, module_name,
                    api_path="foliolib/folio/api",
                    sphinx_doc_src="docs/source"):
    ramls = []

    for fname in os.listdir(schema_path):
        if fname.endswith(".raml"):
            path = os.path.join(schema_path, fname)
            log.info("Read %s", path)
            ramls.append(load_raml(path))

    log_base_name = api_path.replace("/", ".")[1:]
    log_name = f"{log_base_name}.{module_name}"
    code = get_module_code(log_name)
    for raml in ramls:
        codeBuilder = CodeBuilder(raml,
                                  sphinx_doc_src=sphinx_doc_src)
        code += "\n" + codeBuilder.get_class_code()

    # print(code)

    filename = os.path.join(api_path, module_name + ".py")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
