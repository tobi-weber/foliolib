# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import re

import inflection
from foliolib import RAISE
from foliolib.apiBuilder.raml.exceptions import (CodeBuilderError,
                                                 RamlResourceTypeNotFound)
from foliolib.apiBuilder.raml.helper import merge_dict, pluralize, singularize
from foliolib.apiBuilder.raml.ramlMethod import RamlMethod

log = logging.getLogger("foliolib.apiBuilder.raml.ramlUrl")


class RamlUrl:

    def __init__(self, url, data, ramlGlobals):
        log.info("RamlUrl: %s", url)
        self._url = url if not url.endswith("/") else url[:-1]
        self._data = data
        self._ramlGlobals = ramlGlobals
        self._urls = []
        self._methods = []
        self._create_ramlUrls()
        self._create_methods()

    def get_url(self):
        return self._url

    def get_data(self):
        return self._data

    def get_urls(self):
        return self._urls

    def get_methods(self):
        return self._methods

    def _create_methods(self):
        if "type" in self._data:
            dataType = self._data["type"]  # Type defined in the url
            resourceType = None  # Resource type defined in url
            urlTypes = None  # Types defined in urls resource type
            if isinstance(dataType, dict):
                for k in dataType:
                    resourceType = k
                    urlTypes = dataType[resourceType]
            else:
                resourceType = dataType
            log.debug("ResourceType: %s", resourceType)
            if resourceType in self._ramlGlobals["resourceTypes"]:

                globalMethods = self._ramlGlobals["resourceTypes"][resourceType]
                # print(self._data)
                # print(globalMethods)
                globalMethods = merge_dict(globalMethods,
                                           self._data)
                methods = [k for k in globalMethods if k in [
                    "get", "post", "delete", "put"]]
                log.debug("ResourceType methods: %s", str(methods))

                if not methods:
                    log.error(
                        "No methods in resourceTypes[%s] found", resourceType)

                for method in methods:
                    methodData = self._resolve_methodData(globalMethods[method],
                                                          urlTypes=urlTypes)
                    if methodData is not None:
                        self._methods.append(RamlMethod(method, self._url, methodData,
                                                        self._ramlGlobals, resourceType=resourceType))
            else:
                raise RamlResourceTypeNotFound(resourceType)
        else:
            methods = [k for k in self._data if k in [
                "get", "post", "delete", "put"]]
            log.debug("Methods: %s", str(methods))
            for method in methods:
                methodData = self._resolve_methodData(self._data[method])
                if methodData is not None:
                    self._methods.append(RamlMethod(method, self._url, methodData,
                                                    self._ramlGlobals))

    def _create_ramlUrls(self):
        for k in self._data:
            if k.startswith("/"):
                self._urls.append(RamlUrl(self._url+k, self._data[k],
                                          self._ramlGlobals))

    def _resolve_methodData(self, methodData, urlTypes=None):
        # TODO: decode datetime object
        if methodData is not None:
            methodData = json.dumps(methodData, indent=2, default=str)
            params = re.findall("<<(.+?)>>", methodData)
            resourcePathName = self._get_resourcePathName()
            for param in params:
                if param.startswith("resourcePathName"):
                    if param.endswith("singularize"):
                        methodData = methodData.replace(f"<<{param}>>", singularize(
                            resourcePathName))
                    else:
                        methodData = methodData.replace(f"<<{param}>>", pluralize(
                            resourcePathName))
                else:
                    value = urlTypes[param]

                    if isinstance(value, str) and not " " in value:
                        if value in self._ramlGlobals["types"]:
                            value = self._ramlGlobals["types"][value]
                    value = json.dumps(value, indent=2)
                    if re.findall(f"\"<<{param}>>\"", methodData):
                        methodData = methodData.replace(
                            f"\"<<{param}>>\"", value)
                    else:
                        value = value.replace("\"", "\\\"")
                        methodData = methodData.replace(f"<<{param}>>", value)
            methodData = json.loads(methodData)
            methodData["resourcePathName"] = resourcePathName
        else:
            log.warning("Cannot resolve method data.")
            if RAISE:
                log.debug("\n%s", json.dumps(
                    self._data, indent=2, default=str))
                raise CodeBuilderError("No methodData available?")

        return methodData

    def _get_resourcePathName(self):
        parts = re.sub("/{(.+?)}", "", self._url).split("/")
        while True:
            name = parts.pop()
            if name not in ["type", "id"]:
                break

        name = name.replace("-", "_")
        name = inflection.camelize(name, False)

        return name
