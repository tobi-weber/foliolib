# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import argparse
import json
import os
import pprint
import shutil
import sys

import okapi
from okapi import (DB_HOST, DB_PORT, OKAPI_HOST, OKAPI_PORT, database, helper,
                   installer)
from okapi.okapiClient import OkapiClient
from okapi.okapiModule import OkapiModule


class OkapiCLI:

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='okapi command line interface',
            usage='''okapicli <command> [<args>]

   Commands:

    servers                 List available server configs
    setServer               Set server config
    db                      Set db in env
    installModules          Add, deploy and enable modules for a tenant
    installStripesModules   Add and enable stipes modules
    addModule               Add a modul from Moduledescriptor.json
    addModules              Add modules descriptors from dir with ModuleDescriptor.json files
    removeModule            Remove a modul
    deployModule            Deploy a modul for a node
    undeployModule          Undeploy a modul
    enableModule            Enable a modul for a tenant
    enable_modules          Enable a moduls for a tenant
    disableModule           Disable a modul
    createTenant            Create a tenant
    removeTenant            Remove a tenant

Inspection
    env                     Show env
    nodes                   Show nodes
    modules                 Show modules
    deployed                Show deployes modules
    tenants                 Show tenants
    tenantModules           Show mods of a tenant
    tenantInterface         Show interface for a tenant
    tenantInterfaces        Show interfaces for a tenant
    pgdb                    Show complete Postgres db
    descriptor              Show a descriptor from db
    descriptors             Show all descriptors from db

Database
    initdb                  Initialize okapi db
    initmoduledb            Initialize module db
    purgemoduledb           Purge module db and delete all users for a tenant

''')
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print("Unrecognized command")
            parser.print_help()
            exit(1)
        print("%s - %s" % (okapi.get_server(),
                           okapi.CONFIG.get("Okapi", "host")))
        getattr(self, args.command)()

    def setServer(self):
        parser = self.__get_parser("setServer")
        parser.add_argument("name", help="server name")
        parser.add_argument("-s", "--server", default="", help="")
        parser.add_argument("-p", "--port", default="9130", help="")
        args = self.__get_args(parser)
        okapi.set_server(args.name)
        if not os.path.exists(os.path.join(okapi.get_server_confdir(), "okapi.conf")):
            okapi.create_new_config(
                okapi_host=args.server, okapi_port=args.port)
        print(f"Load configs for server {args.name}")
        okapi.load_okapi_conf()

    def servers(self):
        self.__get_parser("servers")
        print(f"Active server is {okapi.get_server()}")
        for f in os.listdir(okapi.get_confdir()):
            if not f == ".server":
                print(f)

    def delServer(self):
        parser = self.__get_parser("delServer")
        parser.add_argument("name", help="server name")
        args = self.__get_args(parser)
        print(f"Del configs for server {args.name}")
        confdir = os.path.join(okapi.get_confdir(), args.name)
        if os.path.exists(confdir):
            print(f"Del {confdir}")
            shutil.rmtree(confdir)
        else:
            print(f"Config for {args.name} does not exist")
        okapi.set_server("default")
        okapi.load_okapi_conf()

    def db(self):
        parser = self.__get_parser("db")
        parser.add_argument("-u", "--user",
                            default="folio_admin", help=" ")
        parser.add_argument("-p", "--password",
                            default="folio_admin", help=" ")
        parser.add_argument("-d", "--database",
                            default="okapi_modules", help=" ")
        parser.add_argument("-s", "--server", default=DB_HOST, help="")
        parser.add_argument("-o", "--port", default=DB_PORT, help=" ")
        args = self.__get_args(parser)
        print("Set db parameters")
        helper.set_env_db(args.server, args.port, args.user,
                          args.password, args.database)

    def installModules(self):
        parser = self.__get_parser("installModules")
        parser.add_argument("file", help="path to okapi_install.json")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument("-n", "--node", default=OKAPI_HOST, help="node id")
        parser.add_argument("--loadSample",  help="", action="store_true")
        parser.add_argument("--purge",  help="", action="store_true")
        parser.add_argument("--simulate",  help="", action="store_true")
        parser.add_argument("--preRelease",  help="", action="store_true")
        parser.add_argument("--ignoreErrors", help="", action="store_true")
        parser.add_argument("--loadReference",  help="", action="store_true")
        parser.add_argument(
            "-c", "--cache",  help="path to cache dir", default="descriptors")
        args = self.__get_args(parser)
        installer.install_with_okapi_install_file(
            args.file, args.node, args.tenant, preRelease=args.preRelease,
            ignoreErrors=args.ignoreErrors, purge=args.purge, simulate=args.simulate,
            loadSample=args.loadSample, loadReference=args.loadReference, cache_dir=args.cache)

    def addModule(self):
        parser = self.__get_parser("addModule")
        parser.add_argument("descriptor",
                            help="Path to ModulDescriptor")
        parser.add_argument(
            "-m", "--modid", help="Modul id, e.g. mod-users-17.1.0")
        args = self.__get_args(parser)
        print(f"Add module {args.descriptor}")
        with open(args.descriptor) as f:
            descriptor = json.load(f)
        OkapiClient().add_module(OkapiModule(descriptor))

    def addModules(self):
        parser = self.__get_parser("addModules")
        parser.add_argument("path",
                            help="Path to ModulDescriptors dir")
        args = self.__get_args(parser)
        helper.add_modules_by_dir(args.path)

    def removeModule(self):
        parser = self.__get_parser("removeModule")
        parser.add_argument("modid", help="Modul id, e.g. mod-users-17.1.0")
        args = self.__get_args(parser)
        print(f"Remove module {args.modid}")
        OkapiClient().remove_module(args.modid)

    def deployModule(self):
        parser = self.__get_parser("deployModule")
        parser.add_argument("modid", help="Modul id, e.g. mod-users-17.1.0")
        parser.add_argument("-n", "--node", default=OKAPI_HOST, help="node id")
        args = self.__get_args(parser)
        print(f"Deploy module {args.modid} for node {args.node}")
        OkapiClient().deploy_module(args.modid, args.node)

    def undeployModule(self):
        parser = self.__get_parser("undeployModule")
        parser.add_argument("modid", help="Modul id, e.g. mod-users-17.1.0")
        parser.add_argument("-n", "--node", default=OKAPI_HOST, help="node id")
        parser.add_argument("-p", "--port", default=OKAPI_PORT, help="port")
        args = self.__get_args(parser)
        print(f"Unploy module {args.modid}")
        OkapiClient().undeploy_module(args.modid, args.node, args.port)

    def enableModule(self):
        parser = self.__get_parser("enableModule")
        parser.add_argument("modid", help="Modul id, e.g. mod-users-17.1.0")
        parser.add_argument("tenant", help="tenant id")
        args = self.__get_args(parser)
        print(f"Enable module {args.modid} for tenant {args.tenant}")
        OkapiClient().enable_module(args.modid, args.tenant)

    def enableModules(self):
        parser = self.__get_parser("enableModules")
        parser.add_argument("modules", help="Json modules file")
        parser.add_argument("tenant", help="tenant id")
        args = self.__get_args(parser)
        helper.enable_modules(args.modules, args.tenant)

    def disableModule(self):
        parser = self.__get_parser("disableModule")
        parser.add_argument("modid", help="Modul id, e.g. mod-users-17.1.0")
        parser.add_argument("tenant", help="tenant id")
        args = self.__get_args(parser)
        print(f"Disable module {args.modid} for tenant {args.tenant}")
        OkapiClient().disable_module(args.modid, args.tenant)

    def createTenant(self):
        parser = self.__get_parser("createTenant")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument("-a", "--name", default="", help="tenant name")
        parser.add_argument("-d", "--description", default="",
                            help="tenant description long")
        args = self.__get_args(parser)
        print(f"Create tenant: {args.tenant}")
        print(f"Name: {args.name}")
        print(f"Description: {args.description}")
        OkapiClient().create_tenant(args.tenant, args.name, args.description)

    def removeTenant(self):
        parser = self.__get_parser("removeTenant")
        parser.add_argument("tenant", help="tenant id")
        args = self.__get_args(parser)
        print(f"Remove tenant: {args.tenant}")
        OkapiClient().remove_tenant(args.tenant)

    def initdb(self):
        parser = self.__get_parser("initdb")
        parser.add_argument("-u", "--user", default="okapi", help=" ")
        parser.add_argument("-p", "--password",
                            default="okapi25", help=" ")
        parser.add_argument("-d", "--database", default="okapi", help=" ")
        args = self.__get_args(parser)

        database.create_okapi_db(user=args.user, password=args.password,
                                 database=args.database)

    def initmoduledb(self):
        parser = self.__get_parser("initmoduledb")
        parser.add_argument(
            "-u", "--user", default="folio_admin", help=" ")
        parser.add_argument("-p", "--password",
                            default="folio_admin", help=" ")
        parser.add_argument("-d", "--database",
                            default="okapi_modules", help=" ")
        args = self.__get_args(parser)
        database.create_modules_db(
            user=args.user, password=args.password, database=args.database)

    def purgemoduledb(self):
        parser = self.__get_parser("purgemoduledb")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument("-d", "--database",
                            default="okapi_modules", help=" ")
        args = self.__get_args(parser)
        database.purge_modules_db(args.tenant, database=args.database)

    def env(self):
        self.__get_parser("env")
        env = OkapiClient().get_env()
        if not env:
            print("No entries in okapi enviroment!")
        for e in env:
            k = e["name"].ljust(20)
            v = e["value"]
            print(f"{k}\t{v}")

    def nodes(self):
        self.__get_parser("nodes")
        nodes = OkapiClient().get_nodes()
        for e in nodes:
            k = e["nodeId"]
            v = e["url"]
            print(f"{k}\t{v}")

    def modules(self):
        self.__get_parser("modules")
        mods = OkapiClient().get_modules()
        for e in mods:
            k = e["id"].ljust(40)
            v = e["name"]
            print(f"{k}\t{v}")

    def deployed(self):
        parser = self.__get_parser("deployed")
        parser.add_argument("-v", "--verbose", help="increase output verbosity",
                            action="store_true")
        args = self.__get_args(parser)
        mods = OkapiClient().get_deployed_modules()
        if args.verbose:
            pp = pprint.PrettyPrinter(indent=2)
            for mod in mods:
                print()
                pp.pprint(mod)
        else:
            print("Mod-id\t\t\t\tNode\t\tDocker-URL\t\t\tDocker-Image")
            for e in mods:
                m = e["srvcId"].ljust(30)
                n = e["nodeId"]
                u = e["url"]
                if "dockerImage" in e["descriptor"]:
                    d = e["descriptor"]["dockerImage"]
                else:
                    d = ""
                print(f"{m}\t{n}\t{u}\t{d}")

    def tenants(self):
        self.__get_parser("tenants")
        tenants = OkapiClient().get_tenants()
        for e in tenants:
            k = e["id"].ljust(15)
            n = e["name"].ljust(20)
            d = e["description"]
            print(f"{k}\t{n}\t{d}")

    def tenantInterface(self):
        parser = self.__get_parser("tenantInterface")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument("interface", help="interface id")
        args = self.__get_args(parser)
        interface = OkapiClient().get_tenant_interface(args.interface, args.tenant)
        print(interface[0]["id"])

    def tenantInterfaces(self):
        parser = self.__get_parser("tenantInterfaces")
        parser.add_argument("tenant", help="tenant id")
        args = self.__get_args(parser)
        interfaces = OkapiClient().get_tenant_interfaces(args.tenant)
        for e in sorted(interfaces, key=lambda e: e["id"]):
            k = e["id"].ljust(35)
            n = e["version"]
            print(f"{k}\t{n}")

    def tenantModules(self):
        parser = self.__get_parser("tenantModules")
        parser.add_argument("tenant", help="tenant id")
        args = self.__get_args(parser)
        mods = OkapiClient().get_tenant_modules(args.tenant)
        for e in mods:
            k = e["id"]
            print(f"{k}")

    def pgdb(self):
        parser = self.__get_parser("pgdb")
        print("### Users:")
        for user in database.get_users():
            print(user)
        for db in database.get_databases():
            if "template" not in db and db != "postgres":
                print(f"### Database: {db}")
                for s in database.get_schemas(db):
                    print(f"\t### Schema: {s}")
                    print("\t\t### Tables:")
                    for t in database.get_tables(s, db):
                        print(f"\t\t\t{t}")

    def descriptor(self):
        parser = self.__get_parser("descriptor")
        parser.add_argument("modid", help="Modul id, e.g. mod-users-17.1.0")
        args = self.__get_args(parser)
        descriptor = database.get_descriptor(args.modid)
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(descriptor)

    def descriptors(self):
        self.__get_parser("descriptors")
        descriptors = database.get_descriptors()
        for d in descriptors:
            print(d)

    def __get_parser(self, cmd, description=""):
        return argparse.ArgumentParser(f"okapicli {cmd}",
                                       description=description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    def __get_args(self, parser):
        return parser.parse_args(sys.argv[2:])
