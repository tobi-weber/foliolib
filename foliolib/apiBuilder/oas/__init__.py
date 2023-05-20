# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import logging
import os

from foliolib.apiBuilder import get_module_code
from foliolib.apiBuilder.oas.oaSchema import OASchema

log = logging.getLogger("foliolib.oas")

HAS_ADMIN_METHODS = ["mod-search.yaml"]


def build_from_oas(schema_path, module_name,
                   api_path="foliolib/folio/api",
                   sphinx_doc_src="docs/source"):
    log.info("Build OAS for %s" % module_name)
    schemas = []

    curdir = os.getcwd()
    log.info("Change to dir %s", schema_path)
    os.chdir(schema_path)

    for fname in os.listdir("."):
        if fname.endswith(".yaml") or fname.endswith(".yml"):
            hasAdminMethods = True if fname in HAS_ADMIN_METHODS else False
            path = os.path.join(schema_path, fname)
            log.info("Read %s", path)
            schemas.append(
                OASchema(fname, sphinx_doc_src=sphinx_doc_src, hasAdminMethods=hasAdminMethods))

    log_name = f"foliolib.folio.api.{module_name}"
    code = get_module_code(log_name)
    for s in schemas:
        code += "\n" + s.get_code()

    log.info("Change back to dir %s", curdir)
    os.chdir(curdir)

    filename = os.path.join(api_path, module_name + ".py")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
