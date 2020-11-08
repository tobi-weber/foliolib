#!/usr/bin/env python3

import logging
import os
import shutil

import inflection

from pyokapi.raml import load_raml, tpl
from pyokapi.raml.codeBuilder import CodeBuilder

log = logging.getLogger("pyokapi.generate_api_code")

API_PATH = "pyokapi/folio/api"

FOLIO_GITURL = "https://github.com/folio-org/"

FOLIO_MODS = [
    # "edge-ncip",
    # "edge-oai-pmh",
    # "edge-orders",
    # "edge-patron",
    # "edge-rtac",
    # "edge-sip2",
    # "mod-agreements",
    # "mod-authtoken",
    "mod-calendar",
    "mod-circulation",
    "mod-circulation-storage",
    # "mod-codex-ekb",
    # "mod-codex-inventory",
    # "mod-codex-mux",
    "mod-configuration",
    "mod-courses",
    "mod-data-export",
    "mod-data-import",
    "mod-data-import-converter-storage",
    "mod-email",
    "mod-erm-usage",
    "mod-erm-usage-harvester",
    "mod-event-config",
    "mod-feesfines",
    "mod-finance",
    "mod-finance-storage",
    "mod-gobi",
    "mod-inventory",
    "mod-inventory-storage",
    "mod-invoice",
    "mod-invoice-storage",
    "mod-kb-ebsco-java",
    "mod-licenses",
    "mod-login",
    "mod-login-saml",
    # "mod-ncip",
    "mod-notes",
    "mod-notify",
    "mod-oai-pmh",
    "mod-orders",
    "mod-orders-storage",
    "mod-organizations",
    "mod-organizations-storage",
    "mod-password-validator",
    "mod-patron",
    "mod-patron-blocks",
    "mod-permissions",
    "mod-pubsub",
    "mod-quick-marc",
    "mod-rtac",
    "mod-sender",
    "mod-source-record-manager",
    "mod-source-record-storage",
    "mod-tags",
    "mod-template-engine",
    "mod-user-import",
    "mod-users",
    "mod-users-bl",
]


def create_dirs():
    cur_path = os.getcwd()
    if not os.path.exists("temp"):
        os.mkdir("temp")
    os.chdir(cur_path)
    if os.path.exists(API_PATH):
        shutil.rmtree(API_PATH)
    os.mkdir(API_PATH)


def get_ramls(mod):
    log.info("")
    log.info(mod)
    log.info("=====================")
    ramls = []
    cur_path = os.getcwd()
    os.chdir("temp")
    if not os.path.exists(mod):
        os.system(f"git clone --recurse-submodules {FOLIO_GITURL}{mod}.git")
    # TODO: check that raml-utils are cloned
    os.chdir(os.path.join(mod, "ramls"))
    if mod == "mod-configuration":
        os.chdir(os.path.join("configuration"))
    for fname in os.listdir():
        if fname.endswith(".raml"):
            log.info("Read %s", os.path.join(cur_path, "temp",
                                             mod, "ramls", fname))
            ramls.append(load_raml(fname))

    os.chdir(cur_path)

    return ramls


def write_api(mod, ramls):
    initfile = os.path.join(API_PATH, "__init__.py")
    with open(initfile, "w") as f:
        f.write("")
    modname = mod.replace("mod-", "").replace("-", "_")
    modname = inflection.camelize(modname, False)
    modfile = os.path.join(API_PATH, modname+".py")
    mod = tpl.get_module_code(modname)
    for raml in ramls:
        codeBuilder = CodeBuilder(raml)
        mod += "\n"
        mod += codeBuilder.get_class_code()
    with open(modfile, "w") as f:
        f.write(mod)


def main():
    create_dirs()
    for mod in FOLIO_MODS:
        ramls = get_ramls(mod)
        write_api(mod, ramls)


if __name__ == "__main__":
    main()
