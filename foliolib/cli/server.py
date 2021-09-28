import os
import shutil

import click
from foliolib.config import Config

from .orderedGroup import OrderedGroup


@click.group(cls=OrderedGroup)
def server():
    """Commands to manage foliolib server configs.
    """


@server.command()
def active():
    """List available server configs
    """
    print(f"Active server is {Config().get_server()}")


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
    if kwargs["name"] in Config().get_servers():
        print("Load configs for server %s." % kwargs["name"])
        Config().set_server(kwargs["name"])
        Config().load_okapi_conf()
        print("Loaded config: %s - %s:%s" % (Config().get_server(),
                                             Config().okapicfg().get("Okapi", "host"),
                                             Config().okapicfg().get("Okapi", "port")))
    else:
        print("Config for server %s does not exist." % kwargs["name"])


@server.command()
@click.argument("name")
@click.argument("host")
@click.option("-p", "--port", default="9130", help="", show_default=True)
def create(**kwargs):
    """Create new server config

    NAME\tserver name.
    HOST\thostname or ip of the okapi server.
    """
    if not kwargs["name"] in Config().get_servers():
        print(f"Create configs for server %s." % kwargs["name"])
        Config().create_okapi_conf(kwargs["name"], okapi_host=kwargs["host"],
                                   okapi_port=kwargs["port"], db_host=kwargs["host"])
    else:
        print("Config for server %s exist already." % kwargs["name"])


@server.command()
@click.argument("name")
def delete(**kwargs):
    """Delete a server config

    NAME\tserver name.
    """
    print(f"Del configs for server %s" % kwargs["name"])
    confdir = os.path.join(Config().get_confdir(), kwargs["name"])
    if os.path.exists(confdir):
        print(f"Del {confdir}")
        shutil.rmtree(confdir)
    else:
        print(f"Config for %s does not exist" % kwargs["name"])
    Config().set_server("default")
