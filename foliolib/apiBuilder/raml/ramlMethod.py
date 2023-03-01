# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import re

import inflection
from foliolib.apiBuilder.raml.exceptions import (RamlTraitDataError,
                                                 RamlTraitNotFound,
                                                 RamlUnknownDataType,
                                                 RamlUnknownStatusCode)
from foliolib.okapi.exceptions import (OkapiFatalError, OkapiMoved,
                                       OkapiRequestConflict, OkapiRequestError,
                                       OkapiRequestForbidden,
                                       OkapiRequestNotAcceptable,
                                       OkapiRequestNotFound,
                                       OkapiRequestPayloadToLarge,
                                       OkapiRequestTimeout,
                                       OkapiRequestUnauthorized,
                                       OkapiRequestUnprocessableEntity)
from foliolib.okapi.okapiClient import Success

log = logging.getLogger("foliolib.apiBuilder.raml.ramlMethod")


RESPONSES = {202: Success,
             204: Success,
             302: OkapiMoved,
             400: OkapiRequestError,
             401: OkapiRequestUnauthorized,
             403: OkapiRequestForbidden,
             404: OkapiRequestNotFound,
             406: OkapiRequestNotAcceptable,
             408: OkapiRequestTimeout,
             409: OkapiRequestConflict,
             413: OkapiRequestPayloadToLarge,
             415: OkapiRequestError,  # TODO:
             422: OkapiRequestUnprocessableEntity,
             }


class RamlMethod:

    def __init__(self, method, url, methodData, ramlGlobals, resourceType=None):
        log.info("RamlMethod: %s: %s - %s", method, url, resourceType)
        self._method = method
        self._url = url
        self._ramlGlobals = ramlGlobals
        self._data = {}
        self._data["resourceType"] = resourceType
        self._data["description"] = ""
        self._data["resourcePathName"] = methodData["resourcePathName"]
        self._data["methodParams"] = self._get_params()
        self._data["request"] = None
        self._data["queryParameters"] = {}
        self._data["returns"] = None
        self._data["redirect"] = None
        self._data["errors"] = []
        self._build_data(methodData)
        # print(json.dumps(self._data, indent=2, default=str))

    def get_method(self):
        return self._method

    def get_url(self):
        return self._url

    def get_data(self):
        return self._data

    def _get_params(self):
        params = re.findall("/{(.+?)}", self._url)
        for param in params:
            if "-" in param:
                i = params.index(param)
                _param = inflection.camelize(param.replace("-", "_"), False)
                params[i] = _param
                self._url = self._url.replace(param, _param)
            elif param == "type":
                i = params.index(param)
                self._url = self._url.replace("{type}", "{type_}")
                params[i] = "type_"
            elif param == "import":
                i = params.index(param)
                self._url = self._url.replace("{import}", "{import_}")
                params[i] = "import_"
            elif param == "id":
                _param = self._url.split("{id}")[0].split(
                    "/")[-2].replace("/", "")
                if _param == "id":
                    _param = "id_"
                elif not _param.lower().endswith("id"):
                    _param = _param + "Id"
                _param = inflection.camelize(_param.replace("-", "_"), False)
                i = params.index(param)
                self._url = self._url.replace("{id}", f"{{{_param}}}")
                params[i] = _param
        if params:
            log.debug("Method needs parameters: %s", str(params))
        return params

    def _build_data(self, methodData):
        # Resolve request types, resonse type and errors, query parameters, descriptions and examples
        if methodData is not None:
            log.debug("Read method data")
            if "description" in methodData:
                self._data["description"] = methodData["description"]
            if "body" in methodData:
                body = methodData["body"]
                log.debug("Method needs request data")
                self._data["request"] = self._parse_body(body)
            if "responses" in methodData:
                if methodData["responses"] is not None:
                    self._set_responses(methodData["responses"])
            if "queryParameters" in methodData:
                self._set_queryParameters(methodData["queryParameters"])
            if "is" in methodData:
                for k in methodData["is"]:
                    if isinstance(k, dict):
                        _is = [*k][0]
                        params = k[_is]
                    else:
                        _is = k
                        params = None
                    try:
                        traitData = self._ramlGlobals["traits"][_is]
                    except KeyError as e:
                        raise RamlTraitNotFound from e
                    if params is not None:
                        traitData = json.dumps(traitData, indent=2)
                        traitParams = re.findall("<<(.+?)>>", traitData)
                        for traitParam in traitParams:
                            v = params[traitParam]
                            if isinstance(v, str):
                                param = v.replace("\"",
                                                  "\\\"")
                                traitData = traitData.replace(f"<<{traitParam}>>",
                                                              param)
                        traitData = json.loads(traitData)
                    if "queryParameters" in traitData:
                        self._set_queryParameters(traitData["queryParameters"])
                    elif "responses" in traitData:
                        self._set_responses(traitData["responses"])
                    else:
                        raise RamlTraitDataError(
                            json.dumps(traitData, indent=2))
        else:
            log.error("No method data?")

    def _set_queryParameters(self, queryParameters):
        log.debug("QueryParameters found")
        self._data["queryParameters"].update(queryParameters)

    def _set_responses(self, responses):
        for k, v in responses.items():
            k = int(k)
            data = {}
            if v is not None:
                if "body" in v:
                    body = v["body"]
                    log.debug("Read response data: %s", k)
                    data = self._parse_body(body)
                if "headers" in v:
                    data["headers"] = v["headers"]
            if k == 200:
                self._data["returns"] = data
            elif k == 201:
                if self._data["returns"] is None:
                    self._data["returns"] = data
            elif 201 < k < 300:
                if self._data["returns"] is None:
                    self._data["returns"] = data
            elif 300 <= k < 400:
                self._data["redirect"] = RESPONSES[k]
            elif 400 <= k < 500:
                self._data["errors"].append(RESPONSES[k])
            elif k >= 500:
                self._data["errors"].append(OkapiFatalError)
            else:
                raise RamlUnknownStatusCode(str(k))

    def _parse_body(self, body):
        bodyData = {}
        if body:
            log.debug("Read body data: %s", [*body][0])
            data = body[[*body][0]]
            if data is not None:
                bodyData = {k: v for k, v in data.items()}
                if "schema" in bodyData:
                    bodyData["type"] = self._ramlGlobals["types"][bodyData["schema"]]
                elif "type" in bodyData:
                    if isinstance(bodyData["type"], str) and not " " in bodyData["type"]:
                        if "types" in self._ramlGlobals:
                            if bodyData["type"] in self._ramlGlobals["types"]:
                                # bodyData["schema"] = bodyData["type"]
                                bodyData["type"] = self._ramlGlobals["types"][bodyData["type"]]
            if "application/json" in body or "application/vnd.api+json" in body:
                bodyData["pyType"] = "dict"
            elif "multipart/form-data" in body:
                bodyData["pyType"] = "filePath"
            elif "application/x-www-form-urlencoded" in body:
                # bodyData["pyType"] = "form-urlencoded"
                bodyData["pyType"] = "str"
            elif "text/plain" in body or "application/xml" in body or\
                    "text/csv" in body or "text/json" in body or\
                    "text/html" in body or "text/xml" in body:
                bodyData["pyType"] = "str"
            elif "application/octet-stream" in body or "binary/octet-stream" in body:
                bodyData["pyType"] = "binary"
            else:
                raise RamlUnknownDataType([*body][0])
            bodyData["mimeType"] = [*body][0]
        return bodyData
