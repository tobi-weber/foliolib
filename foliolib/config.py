# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>


import configparser
import logging
import os
import pathlib

log = logging.getLogger("foliolib.config")


class Config:
    """Config class is a singleton.
    This class defines the handling of the config files.
    """

    def __new__(cls, *dt, **mp):
        if not hasattr(cls, "_inst"):
            cls._inst = super(Config, cls).__new__(cls)
        else:
            def init_pass(self, *dt, **mp):
                pass
            cls.__init__ = init_pass

        return cls._inst

    def __init__(self):
        self.__foliolibcfg = configparser.ConfigParser()
        self.__okapicfg = configparser.ConfigParser()
        self.load_foliolib_config()
        self.load_okapi_conf()

    def foliolibcfg(self):
        """Get foliolib.conf ConfigParser object.
        Returns:
            ConfigParser: ConfigParser object of foliolib.conf
        """
        return self.__foliolibcfg

    def okapicfg(self):
        """Get okapi.conf ConfigParser object.
        Returns:
            ConfigParser: ConfigParser object of okapi.conf of the current server setted.
        """
        return self.__okapicfg

    def modulescfg(self, modId):
        """Get ConfigParser object of a module config file.

        Returns:
            ConfigParser: ConfigParser object of $MODULENAME.conf for a specific module.
        """
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
        """Get current server name.

        Returns:
            str: Current server name.
        """
        fname = os.path.join(self.get_confdir(), ".server")
        if os.path.exists(fname):
            with open(fname) as f:
                return f.read()
        else:
            return self.set_server("default")

    def get_servers(self):
        """Get all available server configs.

        Returns:
            List: List of available servers.
        """
        servers = []
        for f in os.listdir(self.get_confdir()):
            if os.path.exists(os.path.join(self.get_confdir(), f, "okapi.conf")):
                servers.append(f)
        return servers

    def set_server(self, name: str):
        """Switch to a server.

        Args:
            name (str): Server name
        """
        fname = os.path.join(self.get_confdir(), ".server")
        with open(fname, "w") as f:
            f.write(name)
            return name
        self.load_okapi_conf()

    def set_okapicfg(self, section: str, option: str, value):
        """Set a value in okapi.conf

        Args:
            section (str): Section
            option (str): Option
            value (any): Value
        """
        fname = os.path.join(self.get_confdir(),
                             self.get_server(),
                             "okapi.conf")
        self.__okapicfg.set(section, option, value)
        with open(fname, "w") as f:
            self.__okapicfg.write(f)

    def set_foliolibcfg(self, section: str, option: str, value):
        """Set a value in foliolib.conf

        Args:
            section (str): Section
            option (str): Option
            value (any): Value
        """
        fname = os.path.join(self.get_confdir(),
                             "foliolib.conf")
        self.__okapicfg.set(section, option, value)
        with open(fname, "w") as f:
            self.__okapicfg.write(f)

    def get_confdir(self):
        """Get the configuration directory

        Returns:
            str: Path to configuration directory
        """
        if "FOLIOLIB_CONFDIR" in os.environ:
            confdir = os.environ["FOLIOLIB_CONFDIR"]
        else:
            confdir = os.path.join(pathlib.Path.home(), ".foliolib")
        if not os.path.exists(confdir):
            os.mkdir(confdir)
        return confdir

    def load_foliolib_config(self):
        """Read the foliolib.conf
        """
        fname = os.path.join(self.get_confdir(), "foliolib.conf")
        if not os.path.exists(fname):
            self.create_foliolib_conf()
        else:
            log.debug("Load config from %s", fname)
            self.__foliolibcfg.read(fname)
        if not os.path.exists(self.__foliolibcfg["Cache"]["descriptors"]):
            os.makedirs(self.__foliolibcfg["Cache"]
                        ["descriptors"], exist_ok=True)

    def load_okapi_conf(self):
        """Read the okapi.conf
        """
        sdir = os.path.join(self.get_confdir(), self.get_server())
        fname = os.path.join(sdir, "okapi.conf")
        if not os.path.exists(sdir):
            self.create_okapi_conf(self.get_server())
        else:
            log.debug("Load config from %s", fname)
            self.__okapicfg.read(fname)

    def create_foliolib_conf(self):
        """Create foliolib.conf
        """
        fname = os.path.join(self.get_confdir(), "foliolib.conf")
        log.debug("Write new config %s", fname)
        self.__foliolibcfg["PullNode"] = {}
        self.__foliolibcfg["PullNode"]["host"] = "folio-registry.aws.indexdata.com"
        self.__foliolibcfg["PullNode"]["port"] = "80"
        self.__foliolibcfg["Cache"] = {}
        self.__foliolibcfg["Cache"]["descriptors"] = os.path.join(self.get_confdir(),
                                                                  "cache",
                                                                  "descriptors")
        self.__foliolibcfg["GitHub"] = {}
        self.__foliolibcfg["GitHub"]["access-token"] = ""
        with open(fname, "w") as f:
            self.__foliolibcfg.write(f)

    def create_okapi_conf(self, name: str, okapi_host: str = "localhost", okapi_port: str = "9130",
                          db_host: str = "localhost", db_port: str = "5432",
                          db_user: str = "postgres", db_password: str = "postgres"):
        """Create okapi.conf for given server config name.

        Args:
            name (str): Server name.
            okapi_host (str, optional): Okapi host. Defaults to "localhost".
            okapi_port (str, optional): Okapi port. Defaults to "9130".
            db_host (str, optional): Postgres host. Defaults to "localhost".
            db_port (str, optional): Postgres port. Defaults to "5432".
            db_user (str, optional): Postgres user. Defaults to "postgres".
            db_password (str, optional): Postgres password. Defaults to "postgres".
        """
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
