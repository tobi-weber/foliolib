# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>


class FoliolibError(Exception):
    pass


class ConfigError(FoliolibError):
    pass


class ServerConfigNotFound(ConfigError):

    def __init__(self, name=None, servers=None):
        msg = "Server config not found\n"
        if name is not None:
            msg += f"Config {name} not found. "
        if servers is None:
            msg = "You have to create a server!"
        else:
            msg += "Available servers:\n\t"
            msg += "\n\t".join(sorted(servers))
            msg += "\nEnable a server config with 'foliolib server enable SERVER'"
            msg += "\nor create a server config with 'foliolib server create -h'"
            self.msg = msg

    def __str__(self):
        return self.msg
