import argparse
import sys

import okapi
from okapi import helper
from okapi.folio import helper as folio_helper


class FolioCLI:

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='folio command line interface',
            usage='''foliocli <command> [<args>]

   Commands:

    installStripesModules   Add and enable stipes modules
    superuser               Create a superuser
    secureOkapi             Secure Okapi
    loginOkapi              Login Okapi

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

    def installStripesModules(self):
        parser = self.__get_parser("stripes")
        parser.add_argument("path", help="Path to ModulDescriptors dir")
        parser.add_argument("tenant", help="tenant id")
        args = parser.parse_args(sys.argv[2:])
        modules = helper.add_modules_by_dir(args.path)
        helper.enable_modules(modules, args.tenant)

    def superuser(self):
        parser = self.__get_parser("superuser")
        parser.add_argument("tenant", help="tenant id")
        parser.add_argument("-u", "--user", default="folio_admin", help=" ")
        parser.add_argument("-p", "--password", default="admin", help=" ")
        args = parser.parse_args(sys.argv[2:])
        print(
            f"Create superuser {args.user}:{args.password} for tenant {args.tenant}")
        folio_helper.create_superuser(args.tenant, args.user, args.password)

    def secureOkapi(self):
        parser = self.__get_parser("secureOkapi")
        parser.add_argument("-u", "--user", default="okapi_admin", help=" ")
        parser.add_argument("-p", "--password", default="admin", help=" ")
        args = parser.parse_args(sys.argv[2:])
        print(
            f"Create supertenant user {args.user}:{args.password}")
        folio_helper.secure_supertenant(args.user, args.password)

    def loginOkapi(self):
        parser = self.__get_parser("loginOkapi")
        parser.add_argument("user", default="okapi_admin", help=" ")
        parser.add_argument("password", default="admin", help=" ")
        args = parser.parse_args(sys.argv[2:])
        print(
            f"Login supertenant with {args.user}:{args.password}")
        folio_helper.login_supertenant(args.user, args.password)

    def __get_parser(self, cmd, description=""):
        return argparse.ArgumentParser(f"okapicli {cmd}",
                                       description=description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
