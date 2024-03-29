#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2023 Tobias Weber <tobi-weber@gmx.de>

import logging
import os
import shutil
import sys

from foliolib import set_logging
from foliolib.apiBuilder.build_api import build_api

log = logging.getLogger("foliolib.make_api")

API_PATH = "foliolib/folio/api"
SPHINX_DOC_SRC = os.path.join(os.getcwd(), "docs/source")

FOLIO_GITURL = "https://github.com/folio-org/"

FOLIO_MODS = [
    # ("edge-caiasoft", "OAS", "src/main/resources/swagger.api"),
    # ("edge-dematic", "OAS", "src/main/resources/swagger.api"),
    # ("edge-lti-courses", "RAML", "ramls"),
    # ("edge-ncip", "", ""),  # NO SCHEMA
    # ("edge-oai-pmh", "RAML", "ramls"),
    # ("edge-orders", "RAML", "ramls"),
    # ("edge-patron", "RAML", "ramls"),
    # ("edge-rtac", "RAML", "ramls"),
    # ("edge-sip2", "", ""),  # NO SCHEMA
    ("folio-custom-fields", "RAML", "ramls"),
    ("folio-spring-base", "OAS", "folio-spring-base/src/main/resources/swagger.api"),
    ("folio-vertx-lib", "OAS", "core/src/main/resources/openapi"),
    ("mgr-applications", "OAS", "src/main/resources/swagger.api"),
    ("mgr-tenants", "OAS", "src/main/resources/swagger.api"),
    ("mgr-tenant-entitlements", "OAS", "src/main/resources/swagger.api"),
    ("mod-agreements", "", ""),  # NO SCHEMA
    ("mod-audit", "RAML", "ramls"),
    ("mod-authtoken", "OAS", "src/main/resources/openapi"),
    ("mod-batch-print", "OAS", "src/main/resources/openapi"),
    ("mod-bulk-operations", "OAS", "src/main/resources/swagger.api"),
    ("mod-calendar", "OAS", "src/main/resources/api"),
    ("mod-circulation", "RAML", "ramls"),
    ("mod-circulation-item", "OAS", "src/main/resources/swagger.api"),
    ("mod-circulation-storage", "RAML", "ramls"),
    ("mod-codex-ekb", "", ""),  # NO SCHEMA
    ("mod-codex-inventory", "", ""),  # NO SCHEMA
    ("mod-codex-mux", "", ""),  # NO SCHEMA
    ("mod-configuration", "RAML", "ramls/configuration"),
    ("mod-consortia", "OAS", "src/main/resources/swagger.api"),
    ("mod-consortia-keycloak", "OAS", "src/main/resources/swagger.api"),
    ("mod-copycat", "RAML", "ramls"),
    ("mod-courses", "RAML", "ramls"),
    ("mod-data-export", "RAML", "ramls"),
    ("mod-data-export-spring", "OAS", "src/main/resources/swagger.api"),
    ("mod-data-export-worker", "OAS", "src/main/resources/swagger.api"),
    ("mod-data-import", "RAML", "ramls"),
    ("mod-data-import-converter-storage", "RAML", "ramls"),
    ("mod-dcb", "OAS", "src/main/resources/swagger.api"),
    ("mod-di-converter-storage", "RAML", "ramls"),
    ("mod-ebsconet", "OAS", "src/main/resources/swagger.api"),
    ("mod-email", "RAML", "ramls"),
    ("mod-entities-links", "OAS", "src/main/resources/swagger.api"),
    ("mod-erm-usage", "RAML", "ramls"),
    ("mod-erm-usage-harvester", "RAML", "ramls"),
    ("mod-eusage-reports", "OAS", "src/main/resources/openapi"),
    ("mod-event-config", "RAML", "ramls"),
    ("mod-feesfines", "RAML", "ramls"),
    ("mod-finance", "RAML", "ramls"),
    ("mod-finance-storage", "RAML", "ramls"),
    ("mod-finc-config", "RAML", "ramls"),
    ("mod-fqm-manager", "OAS", "src/main/resources/swagger.api"),
    ("mod-gobi", "RAML", "ramls"),
    ("mod-graphql", "", ""),  # NO SCHEMA
    ("mod-idm-connect", "RAML", "ramls"),
    ("mod-inn-reach", "OAS", "src/main/resources/swagger.api"),
    ("mod-inventory", "RAML", "ramls"),
    ("mod-inventory-storage", "RAML", "ramls"),
    ("mod-inventory-update", "RAML", "ramls"),
    ("mod-invoice", "RAML", "ramls"),
    ("mod-invoice-storage", "RAML", "ramls"),
    ("mod-kb-ebsco-java", "RAML", "ramls"),
    ("mod-ldp", "RAML", "ramls"),
    ("mod-licenses", "RAML", "ramls"),
    ("mod-lists", "OAS", "src/main/resources/swagger.api"),
    ("mod-login", "RAML", "ramls"),
    ("mod-login-saml", "RAML", "ramls"),
    ("mod-login-keycloak", "OAS", "src/main/resources/swagger.api"),
    ("mod-marccat", "RAML", "ramls"),
    ("mod-marc-migrations", "OAS", "src/main/resources/swagger.api"),
    ("mod-meta-storage", "OAS", "server/src/main/resources/openapi"),
    ("mod-ncip", "", ""),  # NO SCHEMA
    ("mod-notes", "OAS", "src/main/resources/swagger.api"),
    ("mod-notify", "RAML", "ramls"),
    ("mod-oai-pmh", "RAML", "ramls"),
    ("mod-orders", "RAML", "ramls"),
    ("mod-orders-storage", "RAML", "ramls"),
    ("mod-organizations", "RAML", "ramls"),
    ("mod-organizations-storage", "RAML", "ramls"),
    ("mod-password-validator",  "OAS", "src/main/resources/swagger.api"),
    ("mod-patron", "RAML", "ramls"),
    ("mod-patron-blocks", "RAML", "ramls"),
    ("mod-permissions", "RAML", "ramls"),
    ("mod-pubsub", "RAML", "ramls"),
    ("mod-quick-marc", "OAS", "src/main/resources/swagger.api"),
    ("mod-remote-storage", "OAS", "src/main/resources/swagger.api"),
    ("mod-requests-mediated", "OAS", "src/main/resources/swagger.api"),
    ("mod-reservoir", "OAS", "server/src/main/resources/openapi"),
    ("mod-rtac", "RAML", "ramls"),
    ("mod-roles-keycloak", "OAS", "src/main/resources/swagger.api"),
    ("mod-scheduler", "OAS", "src/main/resources/swagger.api"),
    ("mod-search", "OAS", "src/main/resources/swagger.api"),
    ("mod-sender", "RAML", "ramls"),
    ("mod-service-interaction", "", ""),
    ("mod-settings", "OAS", "src/main/resources/openapi"),
    ("mod-shared-index", "OAS", "server/src/main/resources/openapi"),
    ("mod-source-record-manager", "RAML", "ramls"),
    ("mod-source-record-storage", "RAML", "ramls"),
    ("mod-tags",  "OAS", "src/main/resources/swagger.api"),
    ("mod-template-engine", "RAML", "ramls"),
    ("mod-tlr", "OAS", "src/main/resources/swagger.api"),
    ("mod-user-import", "RAML", "ramls"),
    ("mod-users", "RAML", "ramls"),
    ("mod-users-bl", "RAML", "ramls"),
    ("mod-users-keycloak", "OAS", "src/main/resources/swagger.api"),
    # ("mod-z3950", "", ""),
]


def get_repos():
    cur_path = os.getcwd()
    if not os.path.exists("temp"):
        os.mkdir("temp")
    os.chdir("temp")
    for mod in FOLIO_MODS:
        mod_name = mod[0]
        log.info("")
        log.info("Get repository: %s", mod_name)
        log.info("=========================================")
        if not os.path.exists(mod_name):
            os.system(
                f"git clone --recurse-submodules {FOLIO_GITURL}{mod_name}.git")
        else:
            os.chdir(mod_name)
            os.system(
                f"git pull --recurse-submodules {FOLIO_GITURL}{mod_name}.git")
        os.chdir(os.path.join(cur_path, "temp"))
    os.chdir(cur_path)


def process():
    for fname in os.listdir(API_PATH):
        if not fname == "__init__.py":
            fpath = os.path.join(API_PATH, fname)
            log.info("Delete %s", fpath)
            if os.path.isdir(fpath):
                shutil.rmtree(fpath)
            else:
                os.remove(fpath)
    cur_path = os.getcwd()
    for mod in FOLIO_MODS:
        module_name = mod[0]
        schema_type = mod[1]
        schema_path = mod[2]
        if schema_type:
            log.info("")
            log.info("%s: %s - %s", module_name, schema_type, schema_path)
            log.info("=====================")
            module_dir = os.path.join("temp", module_name)
            build_api(module_dir, schema_path, schema_type,
                      api_path=API_PATH,
                      sphinx_doc_src=SPHINX_DOC_SRC)
            os.chdir(cur_path)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "pull":
        get_repos()
    else:
        set_logging(level="INFO")
        process()


if __name__ == "__main__":
    main()
