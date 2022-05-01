
import json
import logging
import os
from urllib.parse import urlparse

import inflection
import yaml
from foliolib.apiBuilder.oas.oaSchemaPath import OASchemaPath

log = logging.getLogger("foliolib.oas.oaSchemaPath")


class OASchema:

    def __init__(self, data, title, fname, sphinx_doc_src="docs/source"):
        log.debug("OASchema: %s", title)
        self._data = data
        self._referencedData = {fname: data}
        self._ref_data = self._load_refs(data)
        title = ''.join(
            [i for i in title if not i.isdigit() and i not in [".", "-"]])
        self._title = title
        self._sphinx_doc_src = sphinx_doc_src
        self._info = data["info"] if "info" in data else ""
        self._components = self._data["components"]
        if "paths" in data:
            self._oaSchemaPaths = [OASchemaPath(k, v, self)
                                   for k, v in data["paths"].items()]
        else:
            self._oaSchemaPaths = []
        self._doc_include_fles = {}

    def get_title(self):
        return self._title

    def get_basePath(self):
        #print(json.dumps(self._data, indent=2))
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

    def get_oaSchemaPaths(self):
        return self._oaSchemaPaths

    def get_component(self, path):
        if path.startswith("#/components"):
            path = path.replace("#/components/", "").split("/")
            return self._components[path[0]][path[1]]
        elif "#/components" in path:
            path = path.split("#/components/")
            data = self._referencedData[path[0]]
            path = path[1].split("/")
            return data["components"][path[0]][path[1]]
        return None

    def get_ref(self, path):
        if "#/components" in path:
            ref = self.get_component(path)
            if "$ref" in ref:
                if "#/" in ref["$ref"]:
                    ref = ref["$ref"].split("#/")
                    schema = self._ref_data[ref[0]]
                    example = self._ref_data[ref[1]]
                else:
                    schema = self._ref_data[ref["$ref"]]
                    example = None
                return schema
            return ref
        else:
            try:
                return self._ref_data[path]
            except:
                print(self._ref_data.keys())
                raise

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

    def _load_refs(self, data):
        ref_data = {}

        def get_data(path):
            if os.path.exists(path):
                with open(path, encoding="utf-8") as f:
                    if path.endswith(".json"):
                        try:
                            data = json.load(f)
                            return data
                        except json.JSONDecodeError:
                            pass
                    if path.endswith(".yaml"):
                        try:
                            data = yaml.load(f, Loader=yaml.Loader)
                            return data
                        except json.JSONDecodeError:
                            pass
                    return f.read()
            else:
                log.error("File not found %s", path)

        def walk(d):
            if isinstance(d, dict):
                for k, v in d.items():
                    if isinstance(v, dict):
                        walk(v)
                    elif isinstance(v, list):
                        for e in v:
                            walk(e)
                    elif k == "$ref":
                        if not v.startswith("#"):
                            if "#/" in v:
                                ref = v.split("#/")
                                data = get_data(ref[0])
                                if ref[0].endswith(".yaml"):
                                    self._referencedData[ref[0]] = data
                                else:
                                    ref_data[ref[0]] = data
                                    ref_data[ref[1]] = data[ref[1]]
                            else:
                                ref_data[v] = get_data(v)
                    elif k == "example":
                        if not v.startswith("#"):
                            ref_data[v] = get_data(v)

        walk(data)

        return ref_data

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
