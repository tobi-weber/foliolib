# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import sys

from foliolib.basecli import BaseCLI
from foliolib.folio import helper as folio_helper


class FolioCLI(BaseCLI):

    def __init__(self):
        description = "Folio command line interface"
        usage = "foliocli <command> [<args>]"
        commands = """
    installStripesModules   Add and enable stripes modules
    upgradeStripesModules   Upgrade stripes modules
    superuser               Create a superuser
    secureOkapi             Secure Okapi
    unsecureOkapi           Unsecure Okapi
    loginOkapi              Login Okapi

"""
        super().__init__(description, usage, commands)

    def installStripesModules(self):
        parser = self._get_parser("stripes")
        parser.add_argument(
            "file", help="Path to stripes_install.json file or file with json object, e.g. {'MODULE1': 'VERSION', 'MODULE2': 'VERSION'}]")
        parser.add_argument("tenant", help="tenant id")
        args = self._get_args(parser)
        folio_helper.install_stripes(args.file, args.tenant)

    def upgradeStripesModules(self):
        parser = self._get_parser("stripes")
        parser.add_argument(
            "file", help="Path to stripes_install.json file or file with json object, e.g. {'MODULE1': 'VERSION', 'MODULE2': 'VERSION'}]")
        parser.add_argument("tenant", help="tenant id")
        args = self._get_args(parser)
        res = folio_helper.upgrade_stripes(args.file, args.tenant)

        print(json.dumps(res, indent=2))

    def superuser(self):
        parser = self._get_parser("superuser")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument("-u", "--user", default="folio_admin", help=" ")
        parser.add_argument("-p", "--password", default="admin", help=" ")
        args = self._get_args(parser)
        print(
            f"Create superuser {args.user}:{args.password} for tenant {args.tenant}")
        folio_helper.create_superuser(args.tenant, args.user, args.password)

    def secureOkapi(self):
        parser = self._get_parser("secureOkapi")
        parser.add_argument("-u", "--user", default="okapi_admin", help=" ")
        parser.add_argument("-p", "--password", default="admin", help=" ")
        args = self._get_args(parser)
        print(
            f"Create supertenant user {args.user}:{args.password}")
        folio_helper.secure_supertenant(args.user, args.password)

    def unsecureOkapi(self):
        parser = self._get_parser("unsecureOkapi")
        args = self._get_args(parser)
        print("Remove supertenant user")
        folio_helper.unsecure_supertenant()

    def loginOkapi(self):
        parser = self._get_parser("loginOkapi")
        parser.add_argument("user", default="okapi_admin", help=" ")
        parser.add_argument("password", default="admin", help=" ")
        args = self._get_args(parser)
        print(
            f"Login supertenant with {args.user}:{args.password}")
        folio_helper.login_supertenant(args.user, args.password)


def cli():
    FolioCLI()
