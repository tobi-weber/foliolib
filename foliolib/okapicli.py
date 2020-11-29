# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import pprint

from foliolib.basecli import BaseCLI
from foliolib.config import Config
from foliolib.okapi import database, helper
from foliolib.okapi.okapiClient import OkapiClient
from foliolib.okapi.okapiModule import OkapiModule


class OkapiCLI(BaseCLI):

    def __init__(self):
        description = "Okapi command line interface"
        usage = "okapicli <command> [<args>]"
        commands = """
    db                      Set db in env
    installModules          Add, deploy and enable modules for a tenant
    addModule               Add module by name and version
    addModules              Add modules descriptors from json dict
    addModuleDescriptor     Add a modul from Moduledescriptor.json
    addModuleDescriptors    Add modules descriptors from dir with ModuleDescriptor.json files
    removeModule            Remove a modul
    deployModule            Deploy a modul for a node
    undeployModule          Undeploy a modul
    enableModule            Enable a modul for a tenant
    enableModules           Enable a moduls for a tenant
    disableModule           Disable a modul
    addTenant               Create a tenant
    removeTenant            Remove a tenant

  Inspection
    version                 Show Okapi version
    health                  Show health of modules
    env                     Show env
    nodes                   Show nodes
    module                  Show ModulDescriptor of a module
    modules                 Show modules
    deployed                Show deployes modules
    tenants                 Show tenants
    tenantModules           Show mods of a tenant
    tenantInterface         Show interface for a tenant
    tenantInterfaces        Show interfaces for a tenant

  Database
    initdb                  Initialize okapi db
    initmoduledb            Initialize module db

"""
        super().__init__(description, usage, commands)

    def db(self):
        parser = self._get_parser("db")
        parser.add_argument("-u", "--user",
                            default="folio_admin", help=" ")
        parser.add_argument("-p", "--password",
                            default="folio_admin", help=" ")
        parser.add_argument("-d", "--database",
                            default="okapi_modules", help=" ")
        args = self._get_args(parser)
        server = Config().okapicfg().get("Postgres", "host")
        port = Config().okapicfg().get("Postgres", "port")
        print("Set db parameters:")
        print(f"\tdb server: \t{server}")
        print(f"\tdb port: \t{port}")
        print(f"\tdatabase \t{args.database}")
        print(f"\tusername: \t{args.user}")
        print(f"\tpassword: \t{args.password}")
        helper.set_env_db(server, port, args.user,
                          args.password, args.database)

    def addModule(self):
        parser = self._get_parser("addModule")
        parser.add_argument("module", help="Module, e.g. mod-users")
        parser.add_argument("-v", "--version", help="Version, e.g. 17.1.0")
        args = self._get_args(parser)
        print(f"Add module {args.module} {args.version}")
        module = helper.create_okapiModule(
            args.module, version=args.version)
        OkapiClient().add_module(module)

    def addModules(self):
        parser = self._get_parser("addModules")
        parser.add_argument("file",
                            help="Path to json object, e.g. {'MODULE1': 'VERSION', 'MODULE2': 'VERSION'}]")
        args = self._get_args(parser)
        with open(args.file) as f:
            mods = json.load(f)
        modules = helper.create_okapiModules(mods)
        helper.add_modules(modules)

    def addModuleDescriptor(self):
        parser = self._get_parser("addModule")
        parser.add_argument("file",
                            help="Path to ModulDescriptor")
        args = self._get_args(parser)
        print(f"Add module {args.file}")
        with open(args.file) as f:
            descriptor = json.load(f)
        OkapiClient().add_module(OkapiModule(descriptor))

    def addModuleDescriptors(self):
        parser = self._get_parser("addModules")
        parser.add_argument("dir",
                            help="Path to ModulDescriptors dir")
        args = self._get_args(parser)
        helper.add_modules_by_dir(args.dir)

    def removeModule(self):
        parser = self._get_parser("removeModule")
        parser.add_argument("modid", nargs='?',
                            help="Modul id, e.g. mod-users-17.1.0")
        args = self._get_args(parser)
        print(f"Remove module {args.modid}")
        for modid in args.modid:
            OkapiClient().remove_module(modid)

    def deployModule(self):
        parser = self._get_parser("deployModule")
        parser.add_argument(
            "modid", nargs='?', help="Modul id, e.g. mod-users-17.1.0. Can be repeated")
        args = self._get_args(parser)
        print(f"Deploy module {args.modid} for node {args.node}")
        for modid in args.modid:
            OkapiClient().deploy_module(modid, args.node)

    def undeployModule(self):
        parser = self._get_parser("undeployModule")
        parser.add_argument(
            "modid", nargs='?', help="Modul id, e.g. mod-users-17.1.0. Can be repeated")
        args = self._get_args(parser)
        print(f"Undeploy module {args.modid}")
        for modid in args.modid:
            OkapiClient().undeploy_module(modid)

    def undeployAll(self):
        self._get_parser("undeployAll")
        print("Undeploy all modules")
        OkapiClient().undeploy_modules()

    def enableModule(self):
        parser = self._get_parser("enableModule")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument(
            "modid", nargs='?', help="Modul id, e.g. mod-users-17.1.0. Can be repeated")
        parser.add_argument("--loadSample",  help="", action="store_true")
        parser.add_argument("--loadReference",  help="", action="store_true")
        parser.add_argument(
            "--async",  action="store_true", help="Install in the background")
        parser.add_argument(
            "--deploy",  action="store_true", help="Deploy modules")
        parser.add_argument(
            "--ignoreErrors",  action="store_true", help="Ignore errors during the install operation")
        parser.add_argument(
            "--invoke",  action="store_false", help="Not invoke for tenant init/permissions/purge")
        parser.add_argument(
            "--npmSnapshot",  action="store_false", help="Not include NPM module snapshots")
        parser.add_argument(
            "--preRelease",  action="store_false", help="Pre-releases should be considered for installation")
        parser.add_argument(
            "--simulate",  action="store_true", help="Simulate the installation")
        args = self._get_args(parser)
        kwargs = {}
        if getattr(args, "async"):
            kwargs["async"] = getattr(args, "async")
        if args.deploy:
            kwargs["deploy"] = args.deploy
        if args.ignoreErrors:
            kwargs["ignoreErrors"] = args.ignoreErrors
        if args.simulate:
            kwargs["simulate"] = args.simulate
        if not args.invoke:
            kwargs["invoke"] = args.invoke
        if not args.npmSnapshot:
            kwargs["npmSnapshot"] = args.npmSnapshot
        if not args.preRelease:
            kwargs["preRelease"] = args.preRelease
        print(f"Enable module {args.modid} for tenant {args.tenant}")
        for modid in args.modid:
            OkapiClient().enable_module(modid, args.tenant,
                                        loadSample=args.loadSample,
                                        loadReference=args.loadReference,
                                        **kwargs)

    def disableModule(self):
        parser = self._get_parser("disableModule")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument("modid", nargs='?',
                            help="Modul id, e.g. mod-users-17.1.0. Can be repeated")
        parser.add_argument(
            "--async",  action="store_true", help="Uninstall in the background")
        parser.add_argument(
            "--undeploy",  action="store_true", help="Undeploy modules")
        parser.add_argument(
            "--ignoreErrors",  action="store_true", help="Ignore errors during the uninstall operation")
        parser.add_argument(
            "--invoke",  action="store_false", help="Not invoke for tenant init/permissions/purge")
        parser.add_argument(
            "--purge",  action="store_true", help="Modules will also be purged.")
        parser.add_argument(
            "--simulate",  action="store_true", help="Simulate the installation")
        args = self._get_args(parser)
        kwargs = {}
        if getattr(args, "async"):
            kwargs["async"] = getattr(args, "async")
        if args.undeploy:
            kwargs["deploy"] = args.undeploy
        if args.ignoreErrors:
            kwargs["ignoreErrors"] = args.ignoreErrors
        if args.purge:
            kwargs["purge"] = args.purge
        if args.simulate:
            kwargs["simulate"] = args.simulate
        if not args.invoke:
            kwargs["invoke"] = args.invoke
        print(f"Disable module {args.modid} for tenant {args.tenant}")
        for modid in args.modid:
            OkapiClient().disable_module(modid, args.tenant, **kwargs)

    def addTenant(self):
        parser = self._get_parser("createTenant")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument("-a", "--name", default="", help="tenant name")
        parser.add_argument("-d", "--description", default="",
                            help="tenant description long")
        args = self._get_args(parser)
        print(f"Create tenant: {args.tenant}")
        print(f"Name: {args.name}")
        print(f"Description: {args.description}")
        OkapiClient().create_tenant(args.tenant, args.name, args.description)

    def removeTenant(self):
        parser = self._get_parser("removeTenant")
        parser.add_argument("tenant", help="tenant id")
        args = self._get_args(parser)
        print(f"Remove tenant: {args.tenant}")
        OkapiClient().remove_tenant(args.tenant)

    def installModules(self):
        parser = self._get_parser("installModules")
        parser.add_argument(
            "file", help="Path to okapi_install.json file or file with json object, e.g. {'MODULE1': 'VERSION', 'MODULE2': 'VERSION'}]")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument(
            "-n", "--node", default=self._get_node(), help="node id")
        parser.add_argument("--loadSample",  help="", action="store_true")
        parser.add_argument("--loadReference",  help="", action="store_true")
        parser.add_argument(
            "--async",  action="store_true", help="Install in the background")
        parser.add_argument(
            "--deploy",  action="store_true", help="Deploy modules")
        parser.add_argument(
            "--ignoreErrors",  action="store_true", help="Ignore errors during the install operation")
        parser.add_argument(
            "--invoke",  action="store_false", help="Not invoke for tenant init/permissions/purge")
        parser.add_argument(
            "--npmSnapshot",  action="store_false", help="Not include NPM module snapshots")
        parser.add_argument(
            "--preRelease",  action="store_false", help="Pre-releases should be considered for installation")
        parser.add_argument(
            "--simulate",  action="store_true", help="Simulate the installation")
        args = self._get_args(parser)
        kwargs = {}
        if getattr(args, "async"):
            kwargs["async"] = getattr(args, "async")
        if args.deploy:
            kwargs["deploy"] = args.deploy
        if args.ignoreErrors:
            kwargs["ignoreErrors"] = args.ignoreErrors
        if args.simulate:
            kwargs["simulate"] = args.simulate
        if not args.invoke:
            kwargs["invoke"] = args.invoke
        if not args.npmSnapshot:
            kwargs["npmSnapshot"] = args.npmSnapshot
        if not args.preRelease:
            kwargs["preRelease"] = args.preRelease
        helper.install_okapi(args.file, args.node, args.tenant,
                             loadSample=args.loadSample,
                             loadReference=args.loadReference,
                             **kwargs)

    def version(self):
        self._get_parser("version")
        print(OkapiClient().version())

    def health(self):
        parser = self._get_parser("health")
        parser.add_argument("-s", "--serviceId", help="")
        parser.add_argument("-i", "--instanceId", help="requires serviceId")
        args = self._get_args(parser)
        res = OkapiClient().health(args.serviceId, args.instanceId)
        if isinstance(res, dict):
            res = [res]
        print("Service ID\t\t\t\t\tMessage\t\tInstall ID\t\t\t\tStatus")
        for e in res:
            print("%s\t%s\t\t%s\t%s" % (e["srvcId"].ljust(
                40), e["healthMessage"], e["instId"], e["healthStatus"]))

    def env(self):
        self._get_parser("env")
        env = OkapiClient().get_env()
        if not env:
            print("No entries in okapi enviroment!")
        for e in env:
            k = e["name"].ljust(20)
            v = e["value"]
            print(f"{k}\t{v}")

    def nodes(self):
        self._get_parser("nodes")
        nodes = OkapiClient().get_nodes()
        for e in nodes:
            s = ""
            s += e["nodeId"]
            s += "\t"
            s += e["url"].ljust(25)
            if "nodeName" in e:
                s += "\t"
                s += e["nodeName"]
            print(s)

    def module(self):
        parser = self._get_parser("module")
        parser.add_argument("modid", help="Modul id, e.g. mod-users-17.1.0")
        args = self._get_args(parser)
        mod = OkapiClient().get_module(args.modid)
        print(json.dumps(mod, indent=2))

    def modules(self):
        parser = self._get_parser("modules")
        parser.add_argument(
            "--full",  help="Full MD should be returned")
        args = self._get_args(parser)
        kwargs = {}
        if args.full:
            kwargs["full"] = args.full
        mods = OkapiClient().get_modules(**kwargs)
        for e in mods:
            k = e["id"].ljust(40)
            v = e["name"]
            print(f"{k}\t{v}")

    def deployed(self):
        parser = self._get_parser("deployed")
        parser.add_argument("-v", "--verbose", help="increase output verbosity",
                            action="store_true")
        args = self._get_args(parser)
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
        self._get_parser("tenants")
        tenants = OkapiClient().get_tenants()
        for e in tenants:
            k = e["id"].ljust(15)
            n = e["name"].ljust(20)
            d = e["description"]
            print(f"{k}\t{n}\t{d}")

    def tenantModules(self):
        parser = self._get_parser("tenantModules")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument(
            "--full",  help="Full MD should be returned")
        args = self._get_args(parser)
        kwargs = {}
        if args.full:
            kwargs["full"] = args.full
        mods = OkapiClient().get_tenant_modules(args.tenant,
                                                **kwargs)
        for e in mods:
            k = e["id"]
            print(f"{k}")

    def tenantInterface(self):
        parser = self._get_parser("tenantInterface")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument("interface", help="interface id")
        args = self._get_args(parser)
        interface = OkapiClient().get_tenant_interface(args.interface, args.tenant)
        print(interface[0]["id"])

    def tenantInterfaces(self):
        parser = self._get_parser("tenantInterfaces")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument(
            "--full",  help="Full MD should be returned")
        args = self._get_args(parser)
        kwargs = {}
        if args.full:
            kwargs["full"] = args.full
        interfaces = OkapiClient().get_tenant_interfaces(args.tenant,
                                                         **kwargs)
        for e in sorted(interfaces, key=lambda e: e["id"]):
            k = e["id"].ljust(35)
            n = e["version"]
            print(f"{k}\t{n}")

    def pgdb(self):
        self._get_parser("pgdb")
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
                        if not t.startswith("rmb_"):
                            print(f"\t\t\t{t}")

    def initdb(self):
        parser = self._get_parser("initdb")
        parser.add_argument("-u", "--user", default="okapi", help=" ")
        parser.add_argument("-p", "--password",
                            default="okapi25", help=" ")
        parser.add_argument("-d", "--database", default="okapi", help=" ")
        args = self._get_args(parser)

        database.create_okapi_db(user=args.user, password=args.password,
                                 database=args.database)

    def initmoduledb(self):
        parser = self._get_parser("initmoduledb")
        parser.add_argument(
            "-u", "--user", default="folio_admin", help=" ")
        parser.add_argument("-p", "--password",
                            default="folio_admin", help=" ")
        parser.add_argument("-d", "--database",
                            default="okapi_modules", help=" ")
        args = self._get_args(parser)
        database.create_modules_db(
            user=args.user, password=args.password, database=args.database)

    def purgemoduledb(self):
        parser = self._get_parser("purgemoduledb")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument("-d", "--database",
                            default="okapi_modules", help=" ")
        args = self._get_args(parser)
        print(
            f"Purge modules for tenant {args.tenant} in database {args.database}")
        database.purge_modules_db(args.tenant, database=args.database)

    def schemas(self):
        parser = self._get_parser("schemas")
        parser.add_argument("-d", "--database",
                            default="okapi_modules", help=" ")
        args = self._get_args(parser)
        schemas = database.get_schemas(args.database)
        for schema in schemas:
            print(schema)

    def tables(self):
        parser = self._get_parser("tables")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument("module",
                            help="module, e.g. mod-inventory-storage")
        parser.add_argument("-d", "--database",
                            default="okapi_modules", help=" ")
        args = self._get_args(parser)
        with database.Postgres(database=args.database) as pg:
            module = args.module.replace("-", "_")
            schema = f"{args.tenant}_{module}"
            r = pg.get_tables(schema)
            print(r)

    def table(self):
        parser = self._get_parser("table")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument("module",
                            help="module, e.g. mod-inventory-storage")
        parser.add_argument("table", help="table name")
        parser.add_argument("-d", "--database",
                            default="okapi_modules", help=" ")
        args = self._get_args(parser)
        with database.Postgres(database=args.database) as pg:
            module = args.module.replace("-", "_")
            schema = f"{args.tenant}_{module}"
            r = pg.get_table(args.table, schema)
            for e in r:
                print(json.dumps(e[1], indent=2))
