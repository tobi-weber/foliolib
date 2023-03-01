# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import os
import re
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from foliolib.apiBuilder.raml.ramlMethod import RamlMethod

# pylint: disable=consider-using-f-string

TYPES = {"string": "str",
         "object": "dict",
         "array": "list",
         "string[]": "list",
         "integer": "int",
         "number": "long",
         "boolean": "bool",
         "datetime": "datetime",
         "UUID": "uuid",
         "currency_code": "currency_code",
         "recordTypes": "recordTypes", }


def get_module_code(name):
    return f'''# -*- coding: utf-8 -*-
# Generated at {date.today()}

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.{name}")
'''


def get_class_code(classname, doc_title, doc_content):
    doc_title = doc_title.strip()
    doc_title = doc_title.replace("<b>", "**").replace("</b>", "**")
    doc_content = doc_content.strip().replace("\n", "\n\t\t")
    doc_content = doc_content.replace("<b>", "**").replace("</b>", "**")
    return f'''
class {classname}(FolioApi):
    """{doc_title}

    {doc_content}
    """
'''


def get_method_code(methodName: str, method: 'RamlMethod', dataParam: str = None,
                    sphinx_doc_src="docs/source"):
    data = method.get_data()
    methodType = method.get_method()
    url = method.get_url()
    requests = data["request"]
    requestPyType = None
    if requests is not None:
        if "pyType" in requests:
            requestPyType = requests["pyType"]
    code = ""

    methodParams = [f"{p}: str" for p in data["methodParams"]]
    methodParams = ", " + ", ".join(methodParams) if methodParams else ""
    f = "f" if re.findall("/{(.+?)}", url) else ""
    requestParams = ""

    if dataParam is not None:
        requestParams += f", data={dataParam}"
        methodParams += f", {dataParam}: {requestPyType}"
    if requestPyType == "filePath":
        code = """
        import os
        import magic
        mimeType = magic.Magic(mime=True).from_file(filePath)
        filename = os.path.basename((filePath))
        files = {"mods": (filename, open(filePath, "rb"), mimeType)}
        """
        requestParams += ", files=files"
        methodParams += ", filePath: str"
    elif requestPyType == "binary":
        requestParams += ", headers=headers"
        code = """
        import os
        headers = {}
        headers[\"Content-Type\"] = \"application/octet-stream\"
        headers[\"Content-length\"] = str(os.path.getsize(filePath))
        headers[\"Content-Disposition\"] = \"attachment; filename=%s\" % os.path.basename(
            filePath)
        with open(filePath, 'rb') as f:
            data = f.read()
        """
        requestParams += ", data=data"
        methodParams += ", filePath: str"

    doc = get_doc(methodName, method, dataParam,
                  sphinx_doc_src=sphinx_doc_src)

    if data["queryParameters"]:
        methodParams += ", **kwargs"
        requestParams += ", query=kwargs"

    return f'''
    def {methodName}(self{methodParams}):
        """{doc}
        """{code}
        return self.call("{methodType.upper()}", {f}"{url}"{requestParams})
'''


def get_doc(methodName: str, method: 'RamlMethod', dataParam: str = None,
            sphinx_doc_src="docs/source"):
    filespath = os.path.join(sphinx_doc_src, "files")
    if not os.path.exists(filespath):
        os.makedirs(filespath)

    data = method.get_data()
    description = data["description"] if data["description"] is not None else ""
    methodParams = data["methodParams"]
    requests = data["request"]
    returns = data["returns"]
    errors = data["errors"]

    args = []
    kwargs = []
    requestType = None
    requestTypeFile = "{}_{}_request.schema".format(
        data["classname"], methodName)
    requestExample = None
    requestExampleFile = "{}_{}_request.example".format(
        data["classname"], methodName)
    requestPyType = None
    if requests is not None:
        if "pyType" in requests:
            requestPyType = requests["pyType"]
    returnPyType = None
    returnType = None
    returnTypeFile = "{}_{}_return.schema".format(
        data["classname"], methodName)
    returnExample = None
    returnExampleFile = "{}_{}_return.example".format(
        data["classname"], methodName)
    returnHeaders = None
    raises = []
    if methodParams:
        for param in methodParams:
            args.append(f"{param} (str)")
    if dataParam is not None:
        args.append(f"{dataParam} ({requestPyType})")
        if isinstance(requests["type"], dict):
            requestType = json.dumps(requests["type"], indent=2)
        else:
            requestType = requests["type"]
        with open(os.path.join(filespath, requestTypeFile), "w",
                  encoding="utf-8") as f:
            f.write(requestType)
        if "example" in requests:
            if isinstance(requests["example"], dict) or isinstance(requests["example"], list):
                requestExample = json.dumps(
                    requests["example"], indent=2)
            else:
                requestExample = requests["example"]
            with open(os.path.join(filespath, requestExampleFile), "w",
                      encoding="utf-8") as f:
                f.write(requestExample)
    if requestPyType == "filePath":
        args.append("filePath (str): Path to the file.")
    if data["queryParameters"]:
        args.append("**kwargs (properties): Keyword Arguments")
        kwargs = _get_query_args(data["queryParameters"])

    if returns is not None:
        if "type" in returns:
            returnPyType = returns["pyType"]
            # if returnPyType == "dict":
            if isinstance(returns["type"], dict):
                returnType = json.dumps(returns["type"],
                                        indent=2)
            else:
                returnType = returns["type"]
            with open(os.path.join(filespath, returnTypeFile), "w",
                      encoding="utf-8") as f:
                f.write(returnType)
            if "example" in returns:
                if "value" in returns["example"] and isinstance(returns["example"], dict):
                    example = returns["example"]["value"]
                else:
                    example = returns["example"]
                if isinstance(example, (dict, list)):
                    example = json.dumps(example,
                                         indent=2)
                returnExample = example
                with open(os.path.join(filespath, returnExampleFile), "w",
                          encoding="utf-8") as f:
                    f.write(returnExample)
        if "headers" in returns:
            returnHeaders = returns["headers"]

    if errors is not None:
        for err in errors:
            raises.append(f"{err.__name__}: {err.description}")

    description = description.strip().replace("\n", "\n\t\t")
    doc = f"{description}"
    doc += f"\n\n\t\t``{method.get_method().upper()} {method.get_url()}``"
    if args:
        doc += "\n\n"
        doc += "\t\tArgs:\n"
        doc += "\n".join([f"\t\t\t{arg}" for arg in args])
        if requestType:
            doc += ": See Schema below"
    if kwargs:
        doc += "\n\n"
        doc += "\t\tKeyword Args:\n"
        doc += "\n".join([f"\t\t\t{arg}" for arg in kwargs])
    if returnPyType or returnType:
        doc += "\n\n"
        doc += "\t\tReturns:\n"
        doc += f"\t\t\t{returnPyType}: "
        if returnType:
            doc += "See Schema below"
    if raises:
        doc += "\n\n"
        doc += "\t\tRaises:\n"
        doc += "\n".join([f"\t\t\t{r}" for r in raises])
    if returnHeaders:
        doc += "\n\n"
        doc += "\t\tHeaders:\n"
        for name, header in returnHeaders.items():
            headerDescription = ""
            if header:
                headerDescription = "- " + header["description"]
            doc += f"\t\t\t- **{name}** {headerDescription}"
    if returnType or requestType:
        doc += "\n\n"
        doc += "\t\tSchema:\n"
        if requestType:
            doc += "\n"
            doc += f"\t\t\t.. literalinclude:: ../files/{requestTypeFile}"
        if returnType:
            if returnType != requestType:
                doc += "\n"
                doc += f"\t\t\t.. literalinclude:: ../files/{returnTypeFile} "

    doc = doc.replace("\t", "    ")
    return doc


def _get_query_args(queryData):
    args = []
    for k, v in queryData.items():
        # print(k, v)
        t = ""
        if "type" in v:
            if "type" == "enum":
                t = "str: "+"|".join(v["enum"])
            else:
                if v["type"] in TYPES:
                    t = TYPES[v["type"]]
                else:
                    t = v["type"]
        elif "enum" in v:
            t = "str ({}):".format("|".join(v["enum"]))
        elif "pattern" in v:
            t = "str ({}):".format(v["pattern"])
        elif "rules" in queryData:
            t = ""
        else:
            # TODO: e.g. isbn | ..
            print(json.dumps(queryData, indent=2))
            # raise Exception()
        description = ""
        d = "(default={})".format(v["default"]) if "default" in v else ""
        if "description" in v:
            description = v["description"].replace("\n", "\n\t\t\t\t\t")
        if "example" in v:
            description += "\n\t\t\t\t\t\n\t\t\t\t\t"
            description += "Example:"
            examples = str(v["example"]).split("\n")
            for s in examples:
                if s:
                    description += "\n\t\t\t\t\t\n\t\t\t\t\t"
                    description += " - " + \
                        s.replace("\n", "\n\t\t\t\t\t\n\t\t\t\t\t")
        args.append(f"{k} ({t}): {d} {description}")

    return args
