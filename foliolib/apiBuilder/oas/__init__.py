# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os

import yaml
from foliolib.apiBuilder import get_module_code
from foliolib.apiBuilder.oas.oaSchema import OASchema

log = logging.getLogger("foliolib.oas")


def load_schema(path, sphinx_doc_src="docs/source"):
    dirname = os.path.dirname(path)
    basename = os.path.basename(path)
    curdir = os.getcwd()
    if dirname:
        os.chdir(dirname)
    with open(basename, encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.Loader)

    #print(json.dumps(data, indent=2))
    title = os.path.splitext(basename)[0].replace("mod-", "")

    oas = OASchema(data, title, basename,
                   sphinx_doc_src=sphinx_doc_src)
    os.chdir(curdir)

    return oas


def build_from_oas(schema_path, module_name,
                   api_path="foliolib/folio/api",
                   sphinx_doc_src="docs/source"):
    schemas = []

    for fname in os.listdir(schema_path):
        if fname.endswith(".yaml"):
            path = os.path.join(schema_path, fname)
            log.info("Read %s", path)
            schemas.append(load_schema(path,
                                       sphinx_doc_src=sphinx_doc_src))

    log_base_name = api_path.replace("/", ".")
    log_name = f"{log_base_name}.{module_name}"
    code = get_module_code(log_name)
    for s in schemas:
        code += "\n" + s.get_code()

    # print(code)

    filename = os.path.join(api_path, module_name + ".py")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
