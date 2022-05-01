# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
from collections import OrderedDict
from typing import TYPE_CHECKING

import inflection
from foliolib import RAISE
from foliolib.apiBuilder.raml import tpl
from foliolib.apiBuilder.raml.exceptions import CodeBuilderError
from foliolib.apiBuilder.raml.helper import pluralize, singularize
from foliolib.apiBuilder.raml.names import CLASSNAMES, METHODNAMES
from foliolib.apiBuilder.raml.ramlMethod import RamlMethod
from foliolib.apiBuilder.raml.ramlUrl import RamlUrl

if TYPE_CHECKING:
    from foliolib.apiBuilder.raml import Raml


log = logging.getLogger("foliolib.apiBuilder.raml.codeBuilder")


class CodeBuilder:

    def __init__(self, raml: "Raml",
                 sphinx_doc_src="docs/source"):
        log.info("CodeBuilder: %s", raml.get_title())
        self._raml = raml
        self._sphinx_doc_src = sphinx_doc_src
        methods = []
        for url in raml.get_urls():
            methods += self._get_methods(url)
        self._methods = self._generate_methodNames(methods)

    def classname(self):
        title = self._raml.get_title().replace("-", "_")
        title = inflection.camelize(title)
        if title in CLASSNAMES:
            title = CLASSNAMES[title]
        return title

    def get_code(self):
        return self.get_class_code()

    def get_class_code(self):
        log.info("Create class code for %s", self._raml.get_title())
        ramlGlobals = self._raml.get_globals()
        if "documentation" in ramlGlobals:
            title = ramlGlobals["documentation"][0]["title"]
            content = ramlGlobals["documentation"][0]["content"]
        else:
            title = ""
            content = ""
        code = tpl.get_class_code(self.classname(), title, content)

        for methodName, method in self._methods.items():
            code += self.get_method_code(methodName, method)

        return code

    def _get_methods(self, url: RamlUrl):
        methods = url.get_methods()
        for url in url.get_urls():
            methods += self._get_methods(url)
        return methods

    def get_method_code(self, methodName: str, ramlMethod: RamlMethod):
        log.info("Create method code for %s - %s %s", methodName,
                 ramlMethod.get_method(), ramlMethod.get_url())
        method = ramlMethod.get_method()
        data = ramlMethod.get_data()
        data["classname"] = self.classname()
        dataParam = self._get_dataParam(data)
        log.debug("Create Method %s - %s", method, ramlMethod.get_url())

        if method == "get":
            return tpl.get_method_code(methodName, ramlMethod,
                                       dataParam=dataParam,
                                       sphinx_doc_src=self._sphinx_doc_src)

        elif method == "post":
            return tpl.get_method_code(methodName, ramlMethod,
                                       dataParam=dataParam,
                                       sphinx_doc_src=self._sphinx_doc_src)
        elif method == "put":
            return tpl.get_method_code(methodName, ramlMethod,
                                       dataParam=dataParam,
                                       sphinx_doc_src=self._sphinx_doc_src)

        elif method == "delete":
            return tpl.get_method_code(methodName, ramlMethod,
                                       dataParam=dataParam,
                                       sphinx_doc_src=self._sphinx_doc_src)

        else:
            raise CodeBuilderError("Unknown method: " + method)

    def _get_dataParam(self, data):
        dataParam = None
        if data["request"] is not None:
            if "type" in data["request"]:
                dataParam = singularize(
                    data["resourcePathName"])
                if dataParam == "import":
                    dataParam = "import_"
                log.debug("Request parameter: %s", dataParam)
        return dataParam

    def _generate_methodNames(self, methods: list):
        methodNames = OrderedDict()
        for method in methods:
            data = method.get_data()
            methodName = data["resourcePathName"]
            methodParams = data["methodParams"]
            returns = data["returns"]
            requestPyType = None
            if "request" in data:
                if data["request"]:
                    requestPyType = data["request"]["pyType"]

            rest_method = f"{method.get_method().upper()} {method.get_url()}"
            if rest_method in METHODNAMES:
                methodName = METHODNAMES[rest_method]

            elif method.get_method() == "get":

                is_collection = False
                if returns is not None:
                    if "type" in returns:
                        if isinstance(returns["type"], dict):
                            if "properties" in returns["type"]:
                                if "totalRecords" in returns["type"]["properties"]:
                                    is_collection = True
                if data["resourceType"] == "collection" or not methodParams or is_collection:
                    # if data["resourceType"] in ["collection"] or is_collection:
                    methodName = pluralize(methodName)
                elif data["resourceType"] == "collection-item":
                    methodName = singularize(methodName)
                elif len(methodParams) > 0 and not method.get_url().endswith("}"):
                    s = methodParams[0].replace("Id", "")
                    if methodName == s or methodName == pluralize(s):
                        methodName = singularize(methodName)
                    else:
                        methodName = methodName + "_by_" + \
                            singularize(s)
                else:
                    methodName = singularize(methodName)
                methodName = "get_" + methodName
                if methodName in methodNames:
                    methodName = self._rename_method(methodName,
                                                     method, methodNames)

            elif method.get_method() == "post":

                if requestPyType in ["filePath", "binary"]:
                    methodName = "upload_" + \
                        singularize(methodName)
                elif data["resourceType"] is not None:
                    if "action" in data["resourceType"].lower():
                        methodName = singularize(methodName)
                    else:
                        methodName = "set_" + \
                            singularize(methodName)
                else:
                    methodName = "set_" + \
                        singularize(methodName)
                if methodName in methodNames:
                    methodName = self._rename_method(methodName, method,
                                                     methodNames)

            elif method.get_method() == "put":

                methodName = "modify_" + singularize(methodName)
                if data["resourceType"] is not None:
                    if "action" in data["resourceType"].lower():
                        methodName = singularize(methodName)
                if methodName in methodNames:
                    methodName = self._rename_method(methodName, method,
                                                     methodNames)

            elif method.get_method() == "delete":

                if data["resourceType"] in ["collection"] or not methodParams:
                    methodName = "delete_" + pluralize(methodName)
                else:
                    methodName = "delete_" + singularize(methodName)

                if methodName in methodNames:
                    methodName = self._rename_method(methodName, method,
                                                     methodNames)
                    if data["resourceType"] in ["collection"] or not methodParams:
                        methodName = pluralize(methodName)
                    else:
                        methodName = singularize(methodName)

            if methodName is not None:
                if not methodName in methodNames:
                    methodNames[methodName] = method
                else:
                    raise CodeBuilderError(f"""
                        Duplicate method name:
                        {methodName} : {method.get_url()}"
                        {methodName} : {methodNames[methodName].get_url()}"
                        """)
            else:
                log.error("No method name created for %s",
                          data["resourcePathName"])
                if RAISE:
                    print(json.dumps(data, indent=2, default=str))
                    raise CodeBuilderError("Create method name failed")

        return methodNames

    def _rename_method(self, methodName: str, method: RamlMethod,
                       methodNames: dict):
        def rename_method_by_parameter(methodName, methodParams):
            suffix = methodParams[0].replace(
                "_id_", "").replace("Id", "").replace("_id", "")
            suffix = singularize(suffix)
            if suffix in methodName:
                methodName = methodName + "_by_" + methodParams[0]
            else:
                methodName = methodName + "_for_" + suffix
            return methodName

        data = method.get_data()
        _method = methodNames[methodName]
        _data = _method.get_data()
        if len(data["methodParams"]) > len(_data["methodParams"]):
            log.debug("Rename: %s : %s", methodName, method.get_url())
            methodName = rename_method_by_parameter(methodName,
                                                    data["methodParams"])
            log.debug("Renamed: %s", methodName)
        elif len(_data["methodParams"]) > 0:
            log.debug("Rename conflict: %s : %s",
                      methodName, _method.get_url())
            _method = methodNames.pop(methodName)
            _methodName = rename_method_by_parameter(methodName,
                                                     _data["methodParams"])
            methodNames[_methodName] = _method
            log.debug("Renamed conflict: %s", _methodName)
        else:
            # Rename using path components
            url = method.get_url()
            _methodName = methodName
            methodName = methodName + "_" + url.split("/")[-2]
            _method = methodNames.pop(_methodName)
            _url = _method.get_url()
            _methodName = _methodName + "_" + _url.split("/")[-2]
            methodNames[_methodName] = _method

        return methodName
