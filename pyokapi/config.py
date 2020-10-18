# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>


import configparser
import logging
import os
import pathlib

log = logging.getLogger("pyokapi.config")


class _Config:

    def __init__(self):
        self.__pyokapicfg = configparser.ConfigParser()
        self.__okapicfg = configparser.ConfigParser()
        self.load_pyokapi_config()
        self.load_okapi_conf()

    def pyokapicfg(self):
        return self.__pyokapicfg

    def okapicfg(self):
        return self.__okapicfg

    def modulescfg(self, modId):
        modules_dir = os.path.join(self.get_confdir(),
                                   self.get_server(),
                                   "modules")
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

    def get_server(self):
        fname = os.path.join(self.get_confdir(), ".server")
        if os.path.exists(fname):
            with open(fname) as f:
                return f.read()
        else:
            return self.set_server("default")

    def get_servers(self):
        servers = []
        for f in os.listdir(CONFIG.get_confdir()):
            if os.path.exists(os.path.join(CONFIG.get_confdir(), f, "okapi.conf")):
                servers.append(f)
        return servers

    def set_server(self, name):
        fname = os.path.join(self.get_confdir(), ".server")
        with open(fname, "w") as f:
            f.write(name)
            return name
        self.load_okapi_conf()

    def set_okapicfg(self, section, option, value):
        fname = os.path.join(self.get_confdir(),
                             self.get_server(),
                             "okapi.conf")
        self.__okapicfg.set(section, option, value)
        with open(fname, "w") as f:
            self.__okapicfg.write(f)

    def set_pyokapicfg(self, section, option, value):
        fname = os.path.join(self.get_confdir(),
                             "pyokapi.conf")
        self.__okapicfg.set(section, option, value)
        with open(fname, "w") as f:
            self.__okapicfg.write(f)

    def get_confdir(self):
        if "PYOKAPI_CONFDIR" in os.environ:
            confdir = os.environ["PYOKAPI_CONFDIR"]
        else:
            confdir = os.path.join(pathlib.Path.home(), ".pyokapi")
        if not os.path.exists(confdir):
            os.mkdir(confdir)
        return confdir

    def load_pyokapi_config(self):
        fname = os.path.join(self.get_confdir(), "pyokapi.conf")
        if not os.path.exists(fname):
            self.create_pyokapi_conf()
        else:
            log.debug("Load config from %s", fname)
            self.__pyokapicfg.read(fname)
        if not os.path.exists(self.__pyokapicfg["Cache"]["descriptors"]):
            os.makedirs(self.__pyokapicfg["Cache"]
                        ["descriptors"], exist_ok=True)

    def load_okapi_conf(self):
        sdir = os.path.join(self.get_confdir(), self.get_server())
        fname = os.path.join(sdir, "okapi.conf")
        if not os.path.exists(sdir):
            self.create_okapi_conf(self.get_server())
        else:
            log.debug("Load config from %s", fname)
            self.__okapicfg.read(fname)

    def create_pyokapi_conf(self):
        fname = os.path.join(self.get_confdir(), "pyokapi.conf")
        log.debug("Write new config %s", fname)
        self.__pyokapicfg["PullNode"] = {}
        self.__pyokapicfg["PullNode"]["host"] = "folio-registry.aws.indexdata.com"
        self.__pyokapicfg["PullNode"]["port"] = "80"
        self.__pyokapicfg["Cache"] = {}
        self.__pyokapicfg["Cache"]["descriptors"] = os.path.join(self.get_confdir(),
                                                                 "cache",
                                                                 "descriptors")
        self.__pyokapicfg["GitHub"] = {}
        self.__pyokapicfg["GitHub"]["access-token"] = ""
        with open(fname, "w") as f:
            self.__pyokapicfg.write(f)

    def create_okapi_conf(self, name, okapi_host="localhost", okapi_port="9130",
                          db_host="localhost", db_port="5432",
                          db_user="postgres", db_password="postgres"):
        self.set_server(name)
        sdir = os.path.join(self.get_confdir(), self.get_server())
        fname = os.path.join(sdir, "okapi.conf")
        os.mkdir(sdir)
        os.mkdir(os.path.join(sdir, "modules"))
        log.debug("Write new config %s", fname)
        self.__okapicfg["Okapi"] = {}
        self.__okapicfg["Okapi"]["host"] = okapi_host
        self.__okapicfg["Okapi"]["port"] = okapi_port
        self.__okapicfg["Postgres"] = {}
        self.__okapicfg["Postgres"]["host"] = db_host
        self.__okapicfg["Postgres"]["port"] = db_port
        self.__okapicfg["Postgres"]["user"] = db_user
        self.__okapicfg["Postgres"]["password"] = db_password
        with open(fname, "w") as f:
            self.__okapicfg.write(f)
        if not os.path.exists(os.path.join(sdir, "modules")):
            os.mkdir(os.path.join(sdir, "modules"))
        fname = os.path.join(sdir, "modules", "mod-pubsub.conf")
        with open(fname, "w") as f:
            f.write(f"""
[Env]
KAFKA_HOST = {okapi_host}
KAFKA_PORT = 9092
OKAPI_URL = http://{okapi_host}:9130
    """)


CONFIG = _Config()
