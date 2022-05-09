# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>


import configparser
import logging
import os
import pathlib

from foliolib.exceptions import ServerConfigNotFound

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
        self._server = None
        self.__foliolibcfg = configparser.ConfigParser()
        self.__okapicfg = configparser.ConfigParser()

    def get_server(self):
        """Get current server name.

        Returns:
            str: Current server name.
        """
        return self._server

    def set_server(self, name):
        """Set current server name.

        Args:
            name (str): Server name

        Raises:
            ServerConfigNotFound: Server config not found.
        """
        if name in self.get_servers():
            self._server = name
            self.__load()
        else:
            raise ServerConfigNotFound(name, self.get_servers())

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
        if conf_file is not None:
            config.read(conf_file)
            return config
        else:
            return None

    def is_kubernetes(self):
        """Is Kubernets enabled?

        Returns:
            bool: Wether kubernets is enabled.
        """
        #print(self.__okapicfg.get("Kubernetes", "enable", fallback=False))
        return self.__okapicfg.get("Kubernetes", "enable", fallback=False)

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

    def get_url(self):
        host = self.okapicfg().get("Okapi", "host")
        port = self.okapicfg().get("Okapi", "port")

        try:
            ssl = self.okapicfg().get("Okapi", "ssl")
        except configparser.NoOptionError:
            ssl = False
        if ssl:
            url = f"https://{host}:{port}"
        else:
            url = f"http://{host}:{port}"

        return url

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
        if not section in self.__okapicfg:
            self.__okapicfg[section] = {}
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
        if not section in self.__okapicfg:
            self.__foliolibcfg[section] = {}
        self.__foliolibcfg.set(section, option, value)
        with open(fname, "w") as f:
            self.__foliolibcfg.write(f)

    def get_token(self, tenantid: str):
        """Get token for a tenant

        Args:
            tenantid (str): tenant id
        """
        return self.__okapicfg.get("Tokens", tenantid, fallback=None)

    def set_token(self, tenantid: str, token: str):
        """Set token for a tenant

        Args:
            tenantid (str): tenant id
            token (str): token
        """
        log.debug("Set token for %s", tenantid)
        self.set_okapicfg("Tokens", tenantid, token)

    def del_token(self, tenantid: str):
        """Delete token for a tenant

        Args:
            tenantid (str): tenant id
            token (str): token
        """
        if self.has_token(tenantid):
            log.debug("Remove token for %s", tenantid)
            self.__okapicfg.remove_option("Tokens", tenantid)

    def has_token(self, tenantid: str):
        """Delete token for a tenant

        Args:
            tenantid (str): tenant id
            token (str): token
        """
        return self.__okapicfg.has_option("Tokens", tenantid)

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

    def create_foliolib_conf(self):
        """Create foliolib.conf
        """
        fpath = os.path.join(self.get_confdir(), "foliolib.conf")
        if not os.path.exists(fpath):
            log.debug("Write new config %s", fpath)
            self.__foliolibcfg["PullNode"] = {}
            self.__foliolibcfg["PullNode"]["host"] = "folio-registry.dev.folio.org"
            self.__foliolibcfg["PullNode"]["port"] = "443"
            self.__foliolibcfg["PullNode"]["ssl"] = str(True)
            self.__foliolibcfg["Cache"] = {}
            self.__foliolibcfg["Cache"]["descriptors"] = os.path.join(self.get_confdir(),
                                                                      "cache",
                                                                      "descriptors")
            self.__foliolibcfg["GitHub"] = {}
            self.__foliolibcfg["GitHub"]["access-token"] = ""
            with open(fpath, "w") as f:
                self.__foliolibcfg.write(f)
        else:
            log.debug("%s already exists.", fpath)

    def create_okapi_conf(self, name: str, okapi_host: str = "localhost",
                          okapi_port: str = "9130", ssl=False,
                          db_host: str = "localhost", db_port: str = "5432",
                          db_user: str = "postgres", db_password: str = "postgres"):
        """Create okapi.conf for given server config name.

        Args:
            name (str): Server name.
            okapi_host (str, optional): Okapi host. Defaults to "localhost".
            okapi_port (str, optional): Okapi port. Defaults to "9130".
            ssl (bool, optional): SSL. Defaults to False.
            db_host (str, optional): Postgres host. Defaults to "localhost".
            db_port (str, optional): Postgres port. Defaults to "5432".
            db_user (str, optional): Postgres user. Defaults to "postgres".
            db_password (str, optional): Postgres password. Defaults to "postgres".
        """
        sdir = os.path.join(self.get_confdir(), name)
        fpath = os.path.join(sdir, "okapi.conf")
        if not os.path.exists(fpath):
            os.mkdir(sdir)
            os.mkdir(os.path.join(sdir, "modules"))
            log.debug("Write new config %s", fpath)
            self.__okapicfg["Okapi"] = {}
            self.__okapicfg["Okapi"]["host"] = okapi_host
            self.__okapicfg["Okapi"]["port"] = okapi_port
            self.__okapicfg["Okapi"]["ssl"] = str(ssl)
            self.__okapicfg["Postgres"] = {}
            self.__okapicfg["Postgres"]["host"] = db_host
            self.__okapicfg["Postgres"]["port"] = db_port
            self.__okapicfg["Postgres"]["user"] = db_user
            self.__okapicfg["Postgres"]["password"] = db_password
            self.__okapicfg["Tokens"] = {}
            with open(fpath, "w") as f:
                self.__okapicfg.write(f)
            if not os.path.exists(os.path.join(sdir, "modules")):
                os.mkdir(os.path.join(sdir, "modules"))
        else:
            log.debug("%s already exists.", fpath)

    def __load(self):
        # Load foliolib.conf
        fpath = os.path.join(self.get_confdir(), "foliolib.conf")
        log.debug("Load config from %s", fpath)
        self.__foliolibcfg.read(fpath)
        if not os.path.exists(self.__foliolibcfg["Cache"]["descriptors"]):
            os.makedirs(self.__foliolibcfg["Cache"]
                        ["descriptors"], exist_ok=True)
        # Load okapi.conf
        sdir = os.path.join(self.get_confdir(), self.get_server())
        fpath = os.path.join(sdir, "okapi.conf")
        log.debug("Load config from %s", fpath)
        self.__okapicfg.read(fpath)


def server(name, logging_level="INFO"):
    from foliolib import set_logging
    set_logging(level=logging_level)
    Config().set_server(name)
    print("Server is %s" % name)
