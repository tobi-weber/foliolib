# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import argparse
import os
import shutil
import sys

from pyokapi.config import CONFIG
from pyokapi.okapi.okapiClient import OkapiClient


class BaseCLI:

    def __init__(self, description, usage, commands):
        commands = f"""
   Commands:

{commands}

  Pyokapi
    servers                 List available server configs
    setServer               Set server config
    createServer            Create new server config
    delServer               Delete a server config
    """

        usage = f"{usage}\n\n{commands}"
        parser = argparse.ArgumentParser(
            description=description,
            usage=usage)
        parser.add_argument('command', help='Subcommand to run')
        print("Config: %s - %s:%s" % (CONFIG.get_server(),
                                      CONFIG.okapicfg().get("Okapi", "host"),
                                      CONFIG.okapicfg().get("Okapi", "port")))
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print("Unrecognized command")
            parser.print_help()
            exit(1)
        getattr(self, args.command)()

    def setServer(self):
        parser = self._get_parser("setServer")
        parser.add_argument("name", help="server name")
        args = self._get_args(parser)
        if args.name in CONFIG.get_servers():
            print(f"Load configs for server {args.name}.")
            CONFIG.set_server(args.name)
            CONFIG.load_okapi_conf()
        else:
            print(f"Config for server {args.name} does not exist.")

    def createServer(self):
        parser = self._get_parser("createServer")
        parser.add_argument("name", help="server name")
        parser.add_argument("host", help="")
        parser.add_argument("-p", "--port", default="9130", help="")
        args = self._get_args(parser)
        if not args.name in CONFIG.get_servers():
            print(f"Create configs for server {args.name}.")
            CONFIG.create_okapi_conf(args.name, okapi_host=args.host,
                                     okapi_port=args.port, db_host=args.host)
        else:
            print("Config for server {args.name} exist already.")

    def servers(self):
        self._get_parser("servers")
        print(f"Active server is {CONFIG.get_server()}")
        for server in CONFIG.get_servers():
            print(server)
        # for f in os.listdir(CONFIG.get_confdir()):
        #    if os.path.exists(os.path.join(CONFIG.get_confdir(), f, "okapi.conf")):
        #        print(f)

    def delServer(self):
        parser = self._get_parser("delServer")
        parser.add_argument("name", help="server name")
        args = self._get_args(parser)
        print(f"Del configs for server {args.name}")
        confdir = os.path.join(CONFIG.get_confdir(), args.name)
        if os.path.exists(confdir):
            print(f"Del {confdir}")
            shutil.rmtree(confdir)
        else:
            print(f"Config for {args.name} does not exist")
        CONFIG.set_server("default")

    def clean(self):
        self._get_parser("clean")
        shutil.rmtree(CONFIG.pyokapicfg().get("Cache", "descriptors"))

    def _get_parser(self, cmd, description=""):
        return argparse.ArgumentParser(f"okapicli {cmd}",
                                       description=description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    def _get_args(self, parser):
        return parser.parse_args(sys.argv[2:])

    def _get_node(self):
        nodes = OkapiClient().get_nodes()
        host = CONFIG.okapicfg().get("Okapi", "host")
        port = CONFIG.okapicfg().get("Okapi", "port")
        for node in nodes:
            if "nodeName" in node:
                if f"{host}:{port}" in node["url"]:
                    return node["nodeName"]
        return host
