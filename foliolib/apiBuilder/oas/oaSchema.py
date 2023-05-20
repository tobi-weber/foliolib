# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os
from urllib.parse import urlparse

import inflection
import yaml
from foliolib.apiBuilder.oas.baseoas import BaseOAS
from foliolib.apiBuilder.oas.oaSchemaPath import OASchemaPath

log = logging.getLogger("foliolib.oas.oaSchemaPath")


class OASchema(BaseOAS):

    def __init__(self, fname, sphinx_doc_src="docs/source", hasAdminMethods=False):
        super().__init__(fname, self)
        title = os.path.splitext(fname)[0].replace("mod-", "")
        log.info("OASchema: %s", title)
        self.spath = os.getcwd()
        self._referencedData = {fname: self._data}
        self._title = ''.join(
            [i for i in title if not i.isdigit() and i not in [".", "-"]])
        self._sphinx_doc_src = sphinx_doc_src
        self._hasAdminMethods = hasAdminMethods
        self._info = self._data["info"] if "info" in self._data else ""
        if "paths" in self._data:
            self._oaSchemaPaths = [OASchemaPath(k, v, self)
                                   for k, v in self._data["paths"].items()]
        else:
            self._oaSchemaPaths = []
        self._doc_include_fles = {}

    def get_title(self):
        return self._title

    def get_basePath(self):
        # print(json.dumps(self._data, indent=2))
        basePath = ""
        if "servers" in self._data:
            # print(self._data["servers"][0]["url"])
            url = self._data["servers"][0]["url"] if "url" in self._data["servers"][0] else None
            basePath = urlparse(url).path if url is not None else ""
            if basePath.endswith("/"):
                basePath = basePath[:-1]
        return basePath

    def get_classname(self):
        title = self._title.replace("-", "_")
        return inflection.camelize(title)

    def get_data(self):
        return self._data

    def get_info(self):
        return self._info

    def hasAdminMethods(self):
        return self._hasAdminMethods

    def get_oaSchemaPaths(self):
        return self._oaSchemaPaths

    def write_doc_include_file(self, filename, data):
        if self._sphinx_doc_src is not None:
            filespath = os.path.join(self._sphinx_doc_src, "files")
            if not os.path.exists(filespath):
                os.makedirs(filespath)
            filepath = os.path.join(filespath, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                if isinstance(data, dict):
                    json.dump(data, f, indent=4)
                else:
                    f.write(data)

    def get_code(self):
        if not self._oaSchemaPaths:
            return ""

        code = ""

        methods_code = [oaSchemaPath.get_code()
                        for oaSchemaPath in self._oaSchemaPaths
                        if oaSchemaPath.get_code()]
        if methods_code:
            code += "\n" + self.__get_class_code() + "".join(methods_code)

        methods_code = [oaSchemaPath.get_code(adminMethods=True)
                        for oaSchemaPath in self._oaSchemaPaths
                        if oaSchemaPath.get_code(adminMethods=True)]
        if methods_code:
            code += "\n" + self.__get_admin_class_code() + "".join(methods_code)

        return code

    def __get_class_code(self):
        classname = self.get_classname()

        doc_title = self._info["title"]
        doc_title = doc_title.strip()
        doc_title = doc_title.replace("<b>", "**").replace("</b>", "**")

        if "description" in self._info:
            doc_content = self._info["description"]
            doc_content = doc_content.strip().replace("\n", "\n\t\t")
            doc_content = doc_content.replace(
                "<b>", "**").replace("</b>", "**")
        else:
            doc_content = ""

        return f'''
class {classname}(FolioApi):
    """{doc_title}

    {doc_content}
    """
'''

    def __get_admin_class_code(self):
        title = self._title.replace("-", "_")
        classname = inflection.camelize(title) + "Admin"
        doc_title = self._info["title"]
        doc_content = self._info["description"] if "description" in self._info else ""
        doc_title = doc_title.strip()
        doc_title = doc_title.replace("<b>", "**").replace("</b>", "**")
        doc_content = doc_content.strip().replace("\n", "\n\t\t")
        doc_content = doc_content.replace("<b>", "**").replace("</b>", "**")

        return f'''
class {classname}(FolioAdminApi):
    """{doc_title}
    Administration

    {doc_content}
    """
'''
