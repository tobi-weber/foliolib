# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>


import configparser
import logging
import os
import pathlib
import socket
import sys

path = os.path.abspath(__file__)
MODPATH = os.path.dirname(path)
SRCPATH = os.path.dirname(MODPATH)

# Global Vars
OKAPI_FORWARDING = False
OKAPI_HOST = "localhost"
OKAPI_PORT = "9130"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
PYOKAPI_CONFIG = None
CONFIG = None

log = logging.getLogger("okapi")


def set_logging(level=logging.INFO):
    if "PYOKAPI_DEBUG" in os.environ:
        level = logging.DEBUG
    log.setLevel(level)
    if level == logging.INFO:
        formatter = logging.Formatter("%(message)s")
    else:
        formatter = logging.Formatter("[%(name)s] %(levelname)s %(message)s")
    h = logging.StreamHandler()
    h.setFormatter(formatter)
    log.addHandler(h)


def get_confdir():
    if "PYOKAPI_CONFDIR" in os.environ:
        confdir = os.environ["PYOKAPI_CONFDIR"]
    else:
        confdir = os.path.join(pathlib.Path.home(), ".pyokapi")
    if not os.path.exists(confdir):
        os.mkdir(confdir)
    return confdir


def set_server(name):
    fname = os.path.join(get_confdir(), ".server")
    with open(fname, "w") as f:
        f.write(name)
        return name


def get_server():
    fname = os.path.join(get_confdir(), ".server")
    if os.path.exists(fname):
        with open(fname) as f:
            return f.read()
    else:
        return set_server("default")


def set_config(section, option, value):
    fname = os.path.join(get_server_confdir(), "okapi.conf")
    CONFIG.set(section, option, value)
    with open(fname, "w") as f:
        CONFIG.write(f)


def get_server_confdir():
    sdir = os.path.join(get_confdir(), get_server())
    if not os.path.exists(sdir):
        os.mkdir(sdir)
        os.mkdir(os.path.join(sdir, "modules"))
    return sdir


def load_pyokapi_config():
    global PYOKAPI_CONFIG
    fname = os.path.join(get_confdir(), "pyokapi.conf")
    PYOKAPI_CONFIG = configparser.ConfigParser()
    if not os.path.exists(fname):
        PYOKAPI_CONFIG["GitHub"] = {}
        PYOKAPI_CONFIG["GitHub"]["access-token"] = ""
        with open(fname, "w") as f:
            PYOKAPI_CONFIG.write(f)
    else:
        PYOKAPI_CONFIG.read(fname)


def create_new_config(okapi_host=None, okapi_port=None, db_host=None, db_port=None):
    global CONFIG
    okapi_host = okapi_host or OKAPI_HOST
    okapi_port = okapi_port or "9130"
    db_host = db_host or okapi_host
    db_port = db_port or "5432"

    fname = os.path.join(get_server_confdir(), "okapi.conf")
    log.debug("Write new config %s", fname)
    CONFIG = configparser.ConfigParser()
    CONFIG["Okapi"] = {}
    CONFIG["Okapi"]["host"] = okapi_host
    CONFIG["Okapi"]["port"] = okapi_port
    CONFIG["Postgres"] = {}
    CONFIG["Postgres"]["host"] = db_host
    CONFIG["Postgres"]["port"] = db_port
    CONFIG["Postgres"]["user"] = DB_USER
    CONFIG["Postgres"]["password"] = DB_PASSWORD
    with open(fname, "w") as f:
        CONFIG.write(f)
    fname = os.path.join(get_server_confdir(), "modules", "mod-pubsub.conf")
    with open(fname, "w") as f:
        f.write(f"""
[Env]
KAFKA_HOST = {okapi_host}
KAFKA_PORT = 9092
OKAPI_URL = http://{okapi_host}:{okapi_port}
""")
    print(f"Configuration created in {get_server_confdir()}")


def load_okapi_conf():
    global OKAPI_HOST, OKAPI_PORT, CONFIG, OKAPI_FORWARDING
    global DB_HOST, DB_PORT, DB_USER, DB_PASSWORD
    fname = os.path.join(get_server_confdir(), "okapi.conf")
    CONFIG = configparser.ConfigParser()
    if not os.path.exists(fname):
        create_new_config()
    else:
        log.debug("Load config from %s", fname)
        CONFIG.read(fname)
        OKAPI_HOST = CONFIG.get("Okapi", "host")
        OKAPI_PORT = CONFIG.get("Okapi", "port")
        DB_HOST = CONFIG.get("Postgres", "host")
        DB_PORT = CONFIG.get("Postgres", "port")
        DB_USER = CONFIG.get("Postgres", "user")
        DB_PASSWORD = CONFIG.get("Postgres", "password")
        if "forwarding" in CONFIG["Okapi"]:
            OKAPI_FORWARDING = CONFIG.get("Okapi", "forwarding")
        else:
            OKAPI_FORWARDING = False


def get_modules_config(modId):
    modules_dir = os.path.join(get_server_confdir(), "modules")
    conf_file = None
    for f in os.listdir(modules_dir):
        if os.path.splitext(f)[0] in modId:
            conf_file = os.path.join(modules_dir, f)
    config = configparser.ConfigParser()
    config.optionxform = lambda option: option
    if conf_file is not None:
        config.read(conf_file)
        return config
    else:
        return None


load_pyokapi_config()
load_okapi_conf()
