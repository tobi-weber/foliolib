# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import logging
from collections import UserDict

from foliolib import folio
from foliolib.folio import FolioService
from foliolib.folio.api.configuration import Config as ConfigApi

log = logging.getLogger("foliolib.folio.config")


class ConfigEntry(UserDict):

    def __init__(self, module, configName,
                 code, description, value,
                 default=True, enabled=True):
        entry = {
            "module": module,
            "configName": configName,
            "code": code,
            "description": description,
            "default": default,
            "enabled": enabled,
            "value": value
        }
        super().__init__(entry)


class EMailEntry(ConfigEntry):

    def __init__(self, code, description, value):
        super().__init__("SMTP_SERVER", "email",
                         code, description, value)


class FolioHostEntry(ConfigEntry):

    def __init__(self, folio_host):
        super().__init__("USERSBL", "resetPassword",
                         "FOLIO_HOST", "Folio UI application host",
                         folio_host)


class Config(FolioService):

    def __init__(self, tenant: str) -> None:
        """
        Args:
            tenant (str): Tenant id
        """
        super().__init__(tenant)
        self._config = ConfigApi(tenant)

    def get_entries(self, module=None):
        if module is None:
            return self._config.get_entries()["configs"]
        else:
            return self._config.get_entries(query=f"module={module}")["configs"]

    def get_entry(self, module, configName, code):
        query = f"module={module} and configName={configName} and code={code}"
        entries = self._config.get_entries(query=query)["configs"]
        if len(entries):
            return entries[0]
        else:
            return None

    def set_entry(self, entry: ConfigEntry):
        _entry = self.get_entry(entry["module"],
                                entry["configName"],
                                entry["code"])
        if _entry is None:
            self._config.set_entry(entry.data)
        else:
            # for k, v in entry.data.items():
            #    _entry[k] = v
            self._config.modify_entry(_entry["id"], entry.data)

    def delete_entry(self, module, configName, code):
        entry = self.get_entry(module, configName, code)
        if entry is None:
            log.error("Entry does not exist. (%s, %s, %s)" %
                      (module, configName, code))
        else:
            self._config.delete_entry(entry["id"])

    def set_email(self, smtp_host: str, smtp_port: str, email_from: str,
                  username: str, password: str, ssl: bool = False,
                  smtp_login_option: str = None, start_tls: str = None,
                  trust_all: bool = None, auth_methods: str = None):
        """Set email configuration for a tenant.
        AUTH_METHODS	authentication methods	'CRAM-MD5 LOGIN PLAIN'

        Args:
            smtp_host (str): The host of the smtp server.
            smtp_port (str): The port of the smtp server.
            email_from (str): The 'from' property of the email.
            username (str): The username for the login.
            password (str): The password for the login.
            ssl (bool, optional): sslOnConnect mode for the connection. Defaults to False.
            smtp_login_option (str, optional): The login mode for the connection. Examples are DISABLED, OPTIONAL or REQUIRED Defaults to DISABLED.
            start_tls (str, optional):TLS security mode for the connection. Examples are NONE, OPTIONAL or REQUIRED Defaults to NONE.
            trust_all (bool, optional): trust all certificates on ssl connect.
            auth_methods (str, optional): Authentication methods. Example is 'CRAM-MD5 LOGIN PLAIN'.
        """
        self.set_entry(
            EMailEntry("EMAIL_SMTP_HOST",
                       "server smtp host",
                       smtp_host))
        self.set_entry(
            EMailEntry("EMAIL_SMTP_PORT",
                       "server smtp port",
                       smtp_port))
        self.set_entry(
            EMailEntry("EMAIL_FROM",
                       "smtp from",
                       email_from))

        self.set_entry(
            EMailEntry("EMAIL_USERNAME",
                       "smtp username",
                       username))
        self.set_entry(
            EMailEntry("EMAIL_PASSWORD",
                       "smtp password",
                       password))
        self.set_entry(
            EMailEntry("EMAIL_SMTP_SSL",
                       "sslOnConnect for the connection",
                       ssl))
        if smtp_login_option is not None:
            self.set_entry(
                EMailEntry("EMAIL_SMTP_LOGIN_OPTION",
                           "login mode for the connection",
                           smtp_login_option))
        if start_tls is not None:
            self.set_entry(
                EMailEntry("EMAIL_START_TLS_OPTIONS",
                           "TLS security for the connection",
                           start_tls))
        if trust_all is not None:
            self.set_entry(
                EMailEntry("EMAIL_TRUST_ALL",
                           "trust all certificates on ssl connect",
                           trust_all))
        if auth_methods is not None:
            self.set_entry(
                EMailEntry("AUTH_METHODS",
                           "authentication method",
                           auth_methods))

    def get_folio_host(self):
        return self.get_entries("USERSBL")

    def set_folio_host(self, folio_host):
        self.set_entry(FolioHostEntry(folio_host))
