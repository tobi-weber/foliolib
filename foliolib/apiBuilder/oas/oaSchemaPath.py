# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os
import re

from foliolib.apiBuilder.oas.oaSchemaMethod import OASchemaMethod

log = logging.getLogger("foliolib.apiBuilder.oas.schemaPath")


class OASchemaPath:

    def __init__(self, path, data, oaSchema):
        #print(json.dumps(data, indent=2))
        self._path = path if not path.endswith("/") else path[:-1]
        self._data = data
        self._oaSchema = oaSchema
        self._oaSchemaMethods = []
        self._create_oaSchemaMethods()
        log.info("OASchemaPath: %s", self.get_path())

    def get_path(self):
        return self._oaSchema.get_basePath() + self._path

    def get_data(self):
        return self._data

    def get_oaSchemaMethods(self):
        return self._oaSchemaMethods

    def _create_oaSchemaMethods(self):
        for k, v in self._data.items():
            if k.lower() in ["get", "post", "put", "delete"]:
                self._oaSchemaMethods.append(
                    OASchemaMethod(k, v, self, self._oaSchema))

    def get_code(self, adminMethods=False):
        if adminMethods:
            oaSchemaMethods = [oasm for oasm in self._oaSchemaMethods
                               if oasm.isAdminMethod()]
        else:
            oaSchemaMethods = [oasm for oasm in self._oaSchemaMethods
                               if not oasm.isAdminMethod()]

        if oaSchemaMethods:
            code = [oaSchemaMethod.get_code()
                    for oaSchemaMethod in oaSchemaMethods]
            return "\n\t\t".join(code)
        else:
            return ""
