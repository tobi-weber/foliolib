# -*- coding: utf-8 -*-
# Copyright (C) 2024 Tobias Weber <tobi-weber@gmx.de>

import os
import sys

from foliolib import set_logging
from foliolib.config import Config
from foliolib.okapi.exceptions import (OkapiNotReachable,
                                       OkapiRequestFatalError,
                                       OkapiRequestForbidden,
                                       OkapiRequestNotFound,
                                       OkapiRequestUnauthorized)
from foliolib.okapi.okapiClient import OkapiClient

# pylint: disable=import-outside-toplevel


def __load_config():
    config = Config()
    fname = os.path.join(config.get_confdir(), ".server")
    if len(sys.argv) > 2 and sys.argv[1] == "server" and sys.argv[2] == "create":
        return True
    elif len(sys.argv) > 2 and sys.argv[1] == "server" and sys.argv[2] == "enable":
        return True
    elif len(sys.argv) > 2 and sys.argv[1] == "server" and sys.argv[2] == "delete":
        return True
    elif "FOLIOLIB_SERVER" in os.environ:
        config.set_server(os.environ["FOLIOLIB_SERVER"])
    elif os.path.exists(fname):
        with open(fname) as f:
            config.set_server(f.read())
        level = Config().servercfg().get("Cli", "loglevel", fallback="INFO")
        if "FOLIOLIB_LOGLEVEL" in os.environ:
            level = os.environ["FOLIOLIB_LOGLEVEL"]
        set_logging(level, traceback=False)
    else:
        print("\nEnable a server config or create a new one!\n")
        return False
    return True


def __check_okapi():
    try:
        OkapiClient().version()
        return 1
    except OkapiRequestUnauthorized:
        return 2
    except OkapiRequestForbidden:
        return 2
    except OkapiRequestNotFound:
        return 3
    except OkapiNotReachable:
        return 11
    except OkapiRequestFatalError as e:
        print(e)
        return 12


def __admin_cli():
    from foliolib.cli.admin import admin
    admin()


def __folio_cli():
    from foliolib.cli.folio import folio
    folio()


def __noauth_cli():
    from foliolib.cli.admin import noauth
    noauth()


def __err_cli():
    from foliolib.cli.err_cli import err
    err()


def cli():
    if __load_config():
        if len(sys.argv) > 1 and sys.argv[1] == "server":
            __err_cli()
        check_okapi = __check_okapi()
        if len(sys.argv) == 1:
            print(
                f"\n== Active server is {Config().get_server()} - {Config().get_url()}\n")
            if Config().is_kubernetes():
                print("== Kubernetes is enabled.\n")
        if Config().servercfg().getboolean("Cli", "isAdmin", fallback=False):
            if check_okapi == 1:
                __admin_cli()
                return
            elif check_okapi == 2:
                if len(sys.argv) == 1:
                    print("== No valid supertenant authentication avialable!\n")
                __noauth_cli()
                return
            elif check_okapi == 3:
                print("Okapi is not ready ...\n")
            elif check_okapi > 10:
                print("Okapi/Server not running?\n")
        else:
            if check_okapi in [1, 2]:
                __folio_cli()
                return
            elif check_okapi == 3:
                print("Okapi is not ready ...\n")
            elif check_okapi > 10:
                print("Okapi/Server not running?\n")
    __err_cli()
