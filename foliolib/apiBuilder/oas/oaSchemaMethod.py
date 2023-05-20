# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os
import re
from types import MethodType

import inflection
from foliolib.apiBuilder.oas.baseoas import BaseOAS
from foliolib.apiBuilder.oas.operationIds import operationIds
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

log = logging.getLogger("foliolib.apiBuilder.oas.oaSchemaMethod")


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
             500: OkapiFatalError,
             }

TYPES = {"string": "str",
         "array": "list",
         "integer": "int",
         "boolean": "bool", }

FILEUPLOAD_CODE = """
        import os
        headers = {}
        headers[\"Content-Type\"] = \"application/octet-stream\"
        headers[\"Content-length\"] = str(os.path.getsize(filePath))
        headers[\"Content-Disposition\"] = \"attachment; filename=%s\" % os.path.basename(
            filePath)
        with open(filePath, 'rb') as f:
            data = f.read()
        """


class OASchemaMethod(BaseOAS):

    def __init__(self, method, data, oaSchemaPath, oaSchema):
        super().__init__(data, oaSchema, oaSchemaPath)
        self._method = method
        self._data = data
        self._oaSchemaPath = oaSchemaPath
        self._path = oaSchemaPath.get_path()
        log.info("OASchemaMethod: %s: %s - %s", method,
                 oaSchemaPath.get_path(), self.get_operationId())

    def isAdminMethod(self):
        if not self._oaSchema.hasAdminMethods():
            return False
        for oaParameter in self.get_oaParameters():
            if oaParameter.get_name() == "x-okapi-tenant":
                return False

        return True

    def hasQuery(self):
        for oaParameter in self.get_oaParameters():
            if oaParameter.get_in() == "query":
                return True

        return False

    def get_method(self):
        return self._method

    def get_path(self):
        return self._path

    def get_data(self):
        return self._data

    def get_operationId(self):
        operationId = self._data["operationId"] if "operationId" in self._data else None
        if operationId is None:
            if self._path in operationIds:
                operationId = operationIds[self._path]
            else:
                # raise Exception("No operationId available- %s" % self._path)
                operationId = os.path.basename(self._path)
        if operationId is not None:
            return operationId.lower().replace("-", "_")
        else:
            return None

    def get_description(self):
        return self._data["description"]if "description" in self._data else ""

    def get_RequestParameters(self):
        pass

    def get_oaParameters(self):
        if "parameters" in self._data:
            oaParameters = [OAParameter(p, self._oaSchema, self)
                            for p in self._data["parameters"]]

            return oaParameters

        return []

    def getPathParameters(self):
        params = []
        for name in re.findall("/{(.+?)}", self._path):
            if name == "id":
                name = "id_"
            if name == "type":
                name = "type_"
            params.append(name)

        return params

    def get_requestContent(self):
        if "requestBody" in self._data:
            requestBody = self._data["requestBody"]
            if "$ref" in requestBody:
                requestBody = self.get_ref(requestBody["$ref"])
            if "content" in requestBody:
                content = requestBody["content"]

                return [OAContent(k, v, self._oaSchema, self)
                        for k, v in content.items()][0]

        return None

    def get_oaResponses(self):
        if "responses" in self._data:
            responses = [OAResponse(k, v, self._oaSchema, self)
                         for k, v in self._data["responses"].items()]

            return responses

        return None

    def get_code(self):
        methodName = self.get_operationId()
        if methodName is None:
            return ""
        params = []
        code = ""
        call_path = self._path.replace(
            "{id}", "{id_}").replace("{type}", "{type_}")
        requestContent = self.get_requestContent()

        for oaParameter in self.get_oaParameters():
            if oaParameter.get_in() == "path" and \
                    oaParameter.get_name() != "x-okapi-tenant" and \
                    "{%s}" % oaParameter.get_name() in self._path:
                params.append(oaParameter.get_name())
        if requestContent is not None and requestContent.get_schema_name() is not None:
            params.append(requestContent.get_schema_name())

        params = [p.replace("-", "_") for p in params]
        pathParams = [p for p in self.getPathParameters()
                      if not p in params]
        params += pathParams
        methodParams = ", " + ", ".join(params) if params else ""

        rp = [
            p for p in params if not "{%s}" % p in call_path]
        request_parameters = ", " + ", ".join(rp) if rp else ""

        if requestContent is not None and requestContent.get_mime_type() == "multipart/form-data":
            methodParams += ", filePath"
            request_parameters += ", data=data"
            code = FILEUPLOAD_CODE

        methodType = self._method.upper()
        f = "f" if methodParams else ""

        if self.hasQuery():
            methodParams += ", " + "**kwargs"
            request_parameters += ", query=kwargs"

        doc = self.__get_parameter_doc()

        return f'''
    def {methodName}(self{methodParams}):
        """{doc}
        """{code}
        return self.call("{methodType.upper()}", {f}"{call_path}"{request_parameters})
'''

    def __get_parameter_doc(self):
        doc = self.get_description()
        args_oaParameters = [oap for oap in self.get_oaParameters()
                             if oap.get_in() == "path" and
                             "{%s}" % oap.get_name() in self._path]
        kwargs_oaParameters = [oap for oap in self.get_oaParameters()
                               if oap.get_in() == "query"]
        doc += f"\n\n\t\t``{self._method.upper()} {self._path}``"
        requestContent = self.get_requestContent()
        requestSchema, responseSchema = self.__get_schemas(requestContent)

        # Args:
        if args_oaParameters or requestContent is not None:
            doc += "\n\n\t\tArgs:"
        if args_oaParameters:
            for oaParameter in args_oaParameters:
                doc += "\n\t\t\t" + oaParameter.get_doc()
        if requestContent is not None:
            if requestContent.get_mime_type() == "multipart/form-data":
                doc += "\n\t\t\tfilePath (str): Path of file to upload."
            elif requestContent.get_schema_name() is not None:
                doc += "\n\t\t\t%s (dict): See Schema below."\
                    % requestContent.get_schema_name()

        # Kwargs
        if kwargs_oaParameters:
            doc += "\n\n\t\tKeyword Args:"

            for oaParameter in kwargs_oaParameters:
                doc += "\n\t\t\t" + oaParameter.get_doc(isQuery=True)

        # Returns:
        if responseSchema is not None:
            doc += "\n\n\t\tReturns:"
            doc += "\n\t\t\tdict: See Schema below."

        # Raises:
        responses = [oar for oar in self.get_oaResponses()
                     if oar.get_code() >= 400]
        if responses:
            doc += "\n\n\t\tRaises:"
            for response in responses:
                code = response.get_code()
                error_class = RESPONSES[code].__name__
                description = response.get_description()
                doc += "\n\t\t\t%s: %s" % (error_class, description)

        # Headers:

        # Request or Response Schema:
        fname = "%s_%s" % (self._oaSchema.get_classname(),
                           self.get_operationId())
        if requestSchema is not None or responseSchema is not None:
            doc += "\n\n\t\tSchema:\n"
            if requestSchema is not None:
                fname += "_request.schema"
                doc += "\n\t\t\t.. literalinclude:: ../files/" + fname
                self._oaSchema.write_doc_include_file(fname, requestSchema)
            if responseSchema is not None and requestSchema != responseSchema:
                fname += "_response.schema"
                doc += "\n\t\t\t.. literalinclude:: ../files/" + fname
                self._oaSchema.write_doc_include_file(fname, responseSchema)

        doc = doc.replace("\t", "    ")

        return doc

    def __get_schemas(self, requestContent):
        requestSchema = None
        responseSchema = None
        if requestContent is not None:
            requestSchema = requestContent.get_schema()
        responseContents = [oar for oar in self.get_oaResponses()
                            if 200 <= oar.get_code() < 300]
        if responseContents:
            responseContent = responseContents[0].get_content()
            if responseContent is not None:
                responseSchema = responseContent.get_schema()

        return requestSchema, responseSchema


class OAParameter(BaseOAS):

    def __init__(self, data, oaSchema, oaSchemaMethod):
        """[summary]

        Args:
            data ([type]): [description]
            oaSchema ([type]): [description]
        """
        super().__init__(data, oaSchema, oaSchemaMethod)
        self._oaSchemaMethod = oaSchemaMethod
        if "$ref" in data:
            data = self._oaSchema.get_ref(data["$ref"])
            self._data = data
        else:
            self._data = data

    def get_name(self, isQuery=False):
        name = self._data["name"]
        if not isQuery:
            if name == "id":
                name = "id_"
            if name == "type":
                name = "type_"
        return name

    def get_in(self):
        return self._data["in"]

    def get_description(self):
        if "description" in self._data:
            return self._data["description"]
        elif "$ref" in self.get_schema():
            return os.path.splitext(os.path.split(self.get_schema()["$ref"])[1])[0]
        else:
            return ""

    def is_required(self):
        return self._data["required"]\
            if "required" in self._data else False

    def is_deprecated(self):
        return self._data["deprecated"]\
            if "deprecated" in self._data else False

    def allowEmptyValue(self):
        return self._data["allowEmptyValue"]\
            if "allowEmptyValue" in self._data else False

    def get_schema(self):
        schema = self._data["schema"] if "schema" in self._data else None
        if "$ref" in schema:
            return self._oaSchema.get_component(schema["$ref"])
        return schema

    def get_doc(self, isQuery=False):
        try:
            type_ = self.get_schema()["type"]
        except:
            type_ = "string"
        if type_ in TYPES:
            type_ = TYPES[type_]
        else:
            raise Exception(f"Type {type_} not found")
        doc = f"{self.get_name(isQuery)} ({type_}):"
        try:
            doc += " " + self.__get_type_doc()
        except:
            log.error("Error get doc of typ for parameter")
        return doc

    def __get_type_doc(self):
        schema = self.get_schema()
        if "$ref" in schema:
            return self.get_description()
        type_des = []
        for k, v in schema.items():
            if k == "$ref":
                type_des
            elif k != "type":
                if isinstance(v, dict):
                    v = "(" + \
                        ", ".join(
                            [f"{k}: {v_}" for k, v_ in v.items()]) + ")"
                type_des.append(f"{k}: {v}")

        type_des = ", ".join(type_des)
        if schema["type"] == "boolean":
            type_des.replace("false", "False").replace("true", "True")

        doc = self.get_description()
        if type_des:
            doc += " (%s)" % type_des

        return doc


class OAResponse(BaseOAS):

    def __init__(self, code, data, oaSchema, oaSchemaMethod):
        super().__init__(data, oaSchema, oaSchemaMethod)
        self._code = int(code)

    def get_code(self):
        return self._code

    def get_description(self):
        if "description" in self._data:
            return self._data["description"]
        else:
            if "$ref" in self._data:
                error_ref = self._oaSchema.get_ref(self._data["$ref"])
                if "description" in error_ref:
                    return error_ref["description"]

        return ""

    def get_content(self):
        if "content" in self._data:
            return [OAContent(k, v, self._oaSchema, self)
                    for k, v in self._data["content"].items()][0]


class RequestParameter:

    def __init__(self, name, data):
        self._name = name
        self._data = data

    def get_name(self):
        return self._name

    def get_type(self):
        return self._
        dData["type"]

    def get_default(self):
        return self._data["default"]

    def get_description(self):
        return self._data["description"]


class OAContent(BaseOAS):

    def __init__(self, mime_type, data, oaSchema, oaSchemaMethod):
        super().__init__(data, oaSchema, oaSchemaMethod)
        self._mime_type = mime_type

    def get_mime_type(self):
        return self._mime_type

    def get_schema_name(self):
        if "schema" in self._data:
            schema = self._data["schema"]
            if "$ref" in schema:
                schema_name = os.path.basename(schema["$ref"].replace("#", ""))
                schema_name = os.path.splitext(schema_name)[0]
                return schema_name[0].lower() + schema_name[1:]
        return None

    def get_schema(self):
        if "schema" in self._data:
            schema = self._data["schema"]
            if "$ref" in schema:
                schema = self.get_ref(schema["$ref"])
                return schema
        return None

    def get_example(self):
        if "example" in self._data:
            return self._oaSchema.get_ref(self._data["example"])
        return None
