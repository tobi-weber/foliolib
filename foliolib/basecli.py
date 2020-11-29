# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import argparse
import os
import shutil
import sys

from foliolib.config import Config
from foliolib.okapi.okapiClient import OkapiClient


class BaseCLI:

    def __init__(self, description, usage, commands):
        commands = f"""
   Commands:

{commands}

  foliolib
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
        print("Config: %s - %s:%s" % (Config().get_server(),
                                      Config().okapicfg().get("Okapi", "host"),
                                      Config().okapicfg().get("Okapi", "port")))
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
        if args.name in Config().get_servers():
            print(f"Load configs for server {args.name}.")
            Config().set_server(args.name)
            Config().load_okapi_conf()
        else:
            print(f"Config for server {args.name} does not exist.")

    def createServer(self):
        parser = self._get_parser("createServer")
        parser.add_argument("name", help="server name")
        parser.add_argument("host", help="")
        parser.add_argument("-p", "--port", default="9130", help="")
        args = self._get_args(parser)
        if not args.name in Config().get_servers():
            print(f"Create configs for server {args.name}.")
            Config().create_okapi_conf(args.name, okapi_host=args.host,
                                       okapi_port=args.port, db_host=args.host)
        else:
            print("Config for server {args.name} exist already.")

    def servers(self):
        self._get_parser("servers")
        print(f"Active server is {Config().get_server()}")
        for server in Config().get_servers():
            print(server)
        # for f in os.listdir(Config().get_confdir()):
        #    if os.path.exists(os.path.join(Config().get_confdir(), f, "okapi.conf")):
        #        print(f)

    def delServer(self):
        parser = self._get_parser("delServer")
        parser.add_argument("name", help="server name")
        args = self._get_args(parser)
        print(f"Del configs for server {args.name}")
        confdir = os.path.join(Config().get_confdir(), args.name)
        if os.path.exists(confdir):
            print(f"Del {confdir}")
            shutil.rmtree(confdir)
        else:
            print(f"Config for {args.name} does not exist")
        Config().set_server("default")

    def clean(self):
        self._get_parser("clean")
        shutil.rmtree(Config().foliolibcfg().get("Cache", "descriptors"))

    def _get_parser(self, cmd, description=""):
        return argparse.ArgumentParser(f"okapicli {cmd}",
                                       description=description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    def _get_args(self, parser):
        return parser.parse_args(sys.argv[2:])

    def _get_node(self):
        try:
            nodes = OkapiClient().get_nodes()
        except:
            nodes = []
        host = Config().okapicfg().get("Okapi", "host")
        port = Config().okapicfg().get("Okapi", "port")
        for node in nodes:
            if "nodeName" in node:
                if f"{host}:{port}" in node["url"]:
                    return node["nodeName"]
        return host
