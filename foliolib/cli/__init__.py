# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import logging
import os
import sys

from foliolib import set_logging
from foliolib.config import Config, ServerConfigNotFound
from foliolib.okapi.exceptions import (OkapiFatalError, OkapiNotReachable,
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
    except OkapiFatalError as e:
        print(e)
        return 12


def __confirmation():
    if not Config().servercfg().getboolean("Cli", "confirm", fallback=True):
        return True
    confirmFile = os.path.join(Config().get_confdir(), ".confirm")
    confirmServer = None
    if os.path.exists(confirmFile):
        with open(confirmFile, encoding="utf8") as f:
            confirmServer = f.read()
    if len(sys.argv) > 2:
        if confirmServer is not None:
            if Config().get_server() == confirmServer:
                return True
            else:
                os.remove(confirmFile)
        confirm = input(
            "== Do you want to continue [%s]? [y/n/a] " % (" ".join(sys.argv[1:])))
        if confirm == "y":
            return True
        elif confirm == "n":
            return False
        elif confirm == "a":
            with open(confirmFile, "w", encoding="utf8") as f:
                confirmServer = f.write(Config().get_server())
            return True
        else:
            return False
    else:
        return True


def __run_cli():
    from foliolib.cli.main import main
    main()


def __run_auth_cli():
    from foliolib.cli.main_noauth import main
    main()


def __run_err_cli():
    from foliolib.cli.main_err import main
    main()


def cli():
    if __load_config():
        if len(sys.argv) > 1 and sys.argv[1] == "server":
            __run_err_cli()
        check_okapi = __check_okapi()
        print(
            f"== Active server is {Config().get_server()} - {Config().get_url()}")
        if check_okapi == 1:
            if not __confirmation():
                return
            __run_cli()
            return
        elif check_okapi == 2:
            print("No valid supertenant authentication!\n")
            __run_auth_cli()
            return
        elif check_okapi == 3:
            print("Okapi is not ready ...\n")
            return
        elif check_okapi > 10:
            print("Okapi/Server not running?\n")
    __run_err_cli()
