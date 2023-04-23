# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import os
import shutil

import click
from foliolib.config import Config
from foliolib.helper import database

from .orderedGroup import OrderedGroup


def __save_current_server(name):
    fname = os.path.join(Config().get_confdir(), ".server")
    with open(fname, "w") as f:
        f.write(name)


@click.group(cls=OrderedGroup)
def server():
    """Commands to manage foliolib server configs.
    """


@server.command()
def active():
    """Show active server
    """
    print(f"Active server is {Config().get_server()} - {Config().get_url()}")


@server.command()
def lst():
    """List available server configs
    """
    print(f"Active server is {Config().get_server()}")
    for srv in Config().get_servers():
        print(srv)


@server.command()
@click.argument("name")
def enable(**kwargs):
    """Enable server config

    NAME\tserver name.
    """
    name = kwargs["name"]
    if name in Config().get_servers():
        print("Load configs for server %s." % name)
        config = Config()
        config.set_server(name)
        __save_current_server(name)
        print("Loaded config: %s - %s:%s" % (Config().get_server(),
                                             Config().servercfg().get("Okapi", "host"),
                                             Config().servercfg().get("Okapi", "port")))
    else:
        print("Config for server %s does not exist." % name)


@server.command()
@click.argument("name")
@click.option("-H", "--host", default="localhost", help="okapi host", show_default=True)
@click.option("-p", "--port", default="9130", help="", show_default=True)
@click.option("-s", "--ssl", is_flag=True,
              help="")
def create(**kwargs):
    """Create new server config

    NAME\tserver name.
    """
    name = kwargs["name"]
    if not name in Config().get_servers():
        print(f"Create configs for server %s." % name)
        Config().create_foliolib_conf()
        Config().create_server_conf(name, okapi_host=kwargs["host"],
                                    okapi_port=kwargs["port"],
                                    ssl=kwargs["ssl"])
        Config().set_server(name)
        __save_current_server(name)
    else:
        print("Config for server %s exist already." % kwargs["name"])


@server.command()
@click.argument("name")
def delete(**kwargs):
    """Delete a server config

    NAME\tserver name.
    """
    print(f"Delete configs for server %s" % kwargs["name"])
    confdir = os.path.join(Config().get_confdir(), kwargs["name"])
    if os.path.exists(confdir):
        print(f"Delete {confdir}")
        shutil.rmtree(confdir)
    else:
        print(f"Config for %s does not exist" % kwargs["name"])
