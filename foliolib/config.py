# -*- coding: utf-8 -*-
# Copyright (C) 2023 Tobias Weber <tobi-weber@gmx.de>


import configparser
import logging
import os
import pathlib
from typing import Any, Union

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
        self.__foliolibcfg = None
        self.__servercfg = None

    def get_server(self):
        """Get current server name.

        Returns:
            str: Current server name.
        """
        return self._server

    def set_server(self, name: str):
        """Set current server name.

        Args:
            name (str): Server name

        Raises:
            ServerConfigNotFound: Server config not found.
        """
        if name in self.get_servers():
            self._server = name
            self.__foliolibcfg = configparser.ConfigParser()
            self.__servercfg = configparser.ConfigParser()
            self.__load()
        else:
            raise ServerConfigNotFound(name, self.get_servers())

    def foliolibcfg(self):
        """Get foliolib.conf ConfigParser object.

        Returns:
            ConfigParser: ConfigParser object of foliolib.conf
        """
        return self.__foliolibcfg

    def servercfg(self):
        """Get server.conf ConfigParser object.

        Returns:
            ConfigParser: ConfigParser object of server.conf of the current server setted.
        """
        return self.__servercfg

    def modulescfg(self, modId):
        """Get ConfigParser object of a module config file.

        Returns:
            ConfigParser: ConfigParser object of $MODULENAME.conf for a specific module.
        """
        from foliolib.helper import split_modid
        modules_dir = os.path.join(self.get_confdir(),
                                   self.get_server(),
                                   "modules")
        conf_file = None
        name, version = split_modid(modId)
        for f in os.listdir(modules_dir):
            if os.path.splitext(f)[0] == name:
                conf_file = os.path.join(modules_dir, f)
        if conf_file is not None:
            config = configparser.ConfigParser()
            config.read(conf_file)
            return config
        else:
            return None

    def is_kubernetes(self):
        """Is Kubernetes enabled?

        Returns:
            bool: Wether kubernets is enabled.
        """
        return self.__servercfg.get("Kubernetes", "enable", fallback=False)

    def get_kube_config(self):
        kube_config = os.path.join(self.get_confdir(),
                                   self.get_server(), "kube_config")
        kube_config = self.__servercfg.get(
            "Kubernetes", "kube_config", fallback=kube_config)
        if os.path.exists(kube_config):
            return kube_config
        else:
            raise FileNotFoundError("%s not found" % kube_config)

    def get_servers(self):
        """Get all available server configs.

        Returns:
            List: List of available servers.
        """
        servers = []
        for f in os.listdir(self.get_confdir()):
            if os.path.exists(os.path.join(self.get_confdir(), f, "server.conf")):
                servers.append(f)
        return servers

    def get_url(self):
        host = self.servercfg().get("Okapi", "host")
        port = self.servercfg().get("Okapi", "port")
        ssl = self.servercfg().getboolean("Okapi", "ssl", fallback=False)
        if ssl:
            url = f"https://{host}:{port}"
        else:
            url = f"http://{host}:{port}"

        return url

    def set_servercfg(self, section: str, option: str, value: str):
        """Set a value in server.conf

        Args:
            section (str): Section
            option (str): Option
            value (any): Value
        """
        fname = os.path.join(self.get_confdir(),
                             self.get_server(),
                             "server.conf")
        if not section in self.__servercfg:
            self.__servercfg[section] = {}
        self.__servercfg.set(section, option, value)
        with open(fname, "w") as f:
            self.__servercfg.write(f)

    def remove_servercfg(self, section: str, option: str):
        """Remove a option in server.conf

        Args:
            section (str): Section
            option (str): Option
            value (any): Value
        """
        fname = os.path.join(self.get_confdir(),
                             self.get_server(),
                             "server.conf")
        self.__servercfg.remove_option(section, option)
        with open(fname, "w") as f:
            self.__servercfg.write(f)

    def set_foliolibcfg(self, section: str, option: str, value: str):
        """Set a value in foliolib.conf

        Args:
            section (str): Section
            option (str): Option
            value (any): Value
        """
        fname = os.path.join(self.get_confdir(),
                             "foliolib.conf")
        if not section in self.__servercfg:
            self.__foliolibcfg[section] = {}
        self.__foliolibcfg.set(section, option, value)
        with open(fname, "w") as f:
            self.__foliolibcfg.write(f)

    def get_token(self, tenantid: str):
        """Get token for a tenant

        Args:
            tenantid (str): tenant id
        """
        return self.__servercfg.get("Tokens", tenantid, fallback=None)

    def set_token(self, tenantid: str, token: str):
        """Set token for a tenant

        Args:
            tenantid (str): tenant id
            token (str): token
        """
        log.debug("Set token for %s", tenantid)
        self.set_servercfg("Tokens", tenantid, token)

    def del_token(self, tenantid: str):
        """Delete token for a tenant

        Args:
            tenantid (str): tenant id
            token (str): token
        """
        if self.has_token(tenantid):
            log.debug("Remove token for %s", tenantid)
            self.__servercfg.remove_option("Tokens", tenantid)

    def has_token(self, tenantid: str):
        """Delete token for a tenant

        Args:
            tenantid (str): tenant id
            token (str): token
        """
        return self.__servercfg.has_option("Tokens", tenantid)

    def is_foliolib_env(self):
        """Is global env handled by foliolib?

        Returns:
            bool: Wether foliolib env is enabled.
        """
        is_foliolib_env = self.__servercfg.get(
            "Okapi", "foliolibEnv", fallback=False)

        return is_foliolib_env

    def get_env(self, as_dict: bool = False):
        """get global enviroment variables.

        Args:
            as_dict (bool, optional): Defaults to False.

        Returns:
            Union[dict, list]: dict, if as_dict is True, else list with enviroments variables.
        """
        if self.is_foliolib_env():
            if as_dict:
                return {k: v for k, v in self.__servercfg["Env"].items()}
            else:
                return [{"name": k, "value": v}
                        for k, v in self.__servercfg["Env"].items()]
        else:
            if as_dict:
                return {}
            else:
                return []

    def set_env(self, key: str, value: Any):
        """Set enviroment variable.

        Args:
            key (str): Name of the enviroment variable.
            value (Any): Value of the enviroment variable.
        """
        if self.is_foliolib_env():
            self.set_servercfg("Env", key, value)

    def delete_env(self, key: str):
        """Delete enviroment variable.

        Args:
            key (str): Name of the enviroment variable.
        """
        if self.is_foliolib_env():
            self.remove_servercfg("Env", key)

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
        self.__foliolibcfg = configparser.ConfigParser()
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
            self.__foliolibcfg["Cache"]["platforms"] = os.path.join(self.get_confdir(),
                                                                    "cache",
                                                                    "platforms")
            # self.__foliolibcfg["GitHub"] = {}
            # self.__foliolibcfg["GitHub"]["access-token"] = ""
            with open(fpath, "w") as f:
                self.__foliolibcfg.write(f)
        else:
            log.debug("%s already exists.", fpath)

    def create_server_conf(self, name: str, okapi_host: str = "localhost",
                           okapi_port: str = "9130", ssl=False):
        """Create server.conf for given server config name.

        Args:
            name (str): Server name.
            okapi_host (str, optional): Okapi host. Defaults to "localhost".
            okapi_port (str, optional): Okapi port. Defaults to "9130".
            ssl (bool, optional): SSL. Defaults to False.
        """
        self.__servercfg = configparser.ConfigParser()
        sdir = os.path.join(self.get_confdir(), name)
        fpath = os.path.join(sdir, "server.conf")
        if not os.path.exists(fpath):
            os.mkdir(sdir)
            os.mkdir(os.path.join(sdir, "modules"))
            log.debug("Write new config %s", fpath)
            self.__servercfg["Okapi"] = {}
            self.__servercfg["Okapi"]["host"] = okapi_host
            self.__servercfg["Okapi"]["port"] = okapi_port
            self.__servercfg["Okapi"]["ssl"] = str(ssl)
            self.__servercfg["Okapi"]["verify_ssl"] = str(True)
            self.__servercfg["Okapi"]["foliolibenv"] = str(True)
            self.__servercfg["Cli"] = {}
            self.__servercfg["Cli"]["confirm"] = str(True)
            self.__servercfg["Cli"]["loglevel"] = "INFO"
            self.__servercfg["Env"] = {}
            self.__servercfg["Env"]["db_host"] = okapi_host
            self.__servercfg["Env"]["db_port"] = "5432"
            self.__servercfg["Env"]["db_username"] = "folio"
            self.__servercfg["Env"]["db_password"] = "folio"
            self.__servercfg["Env"]["db_database"] = "okapi_modules"
            self.__servercfg["Env"]["db_querytimeout"] = "120000"
            self.__servercfg["Env"]["db_charset"] = "UTF-8"
            self.__servercfg["Env"]["kafka_host"] = okapi_host
            self.__servercfg["Env"]["kafka_port"] = "9092"
            self.__servercfg["Env"]["okapi_url"] = f"http://{okapi_host}:{okapi_port}"
            self.__servercfg["Env"]["replication_factor"] = "1"
            with open(fpath, "w") as f:
                self.__servercfg.write(f)
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
        # Load server.conf
        sdir = os.path.join(self.get_confdir(), self.get_server())
        fpath = os.path.join(sdir, "server.conf")
        log.debug("Load config from %s", fpath)
        self.__servercfg.read(fpath)


def server(name: str, logging_level: str = "INFO"):
    """ Load server config for given name.

    Args:
        name (str): Name of the server config.
        logging_level (str, optional): INFO, WARNING, ERROR or DEBUG. Defaults to "INFO".
    """
    from foliolib import set_logging
    set_logging(level=logging_level)
    Config().set_server(name)
    log.info("Server is %s" % name)
