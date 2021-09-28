import json

import click
from foliolib.helper import get_node
from foliolib.okapi.okapiClient import OkapiClient
from foliolib.okapi.okapiModule import create_okapiModules

from.orderedGroup import OrderedGroup


@click.group(cls=OrderedGroup)
def module():
    """Commands to manage Modules
    """


@module.command()
@click.option("-f", "--full", is_flag=True,
              help="Full MD should be returned")
def lst(**kwargs):
    """List all modules
    """
    mods = OkapiClient().get_modules(**kwargs)
    for e in mods:
        if kwargs["full"]:
            print(json.dumps(e, indent=2)+"\n")
        else:
            k = e["id"].ljust(40)
            v = e["name"]
            print(f"{k}\t{v}")


@module.command()
@click.argument("moduleid", required=True)
def get(**kwargs):
    """Get ModulDescriptor, e.g. mod-users-17.1.0

    MODULEID\tmodule id.
    """
    mod = OkapiClient().get_module(kwargs["moduleid"])
    print(json.dumps(mod, indent=2))


@module.command()
@click.option("-m", "--moduleid", multiple=True, required=True)
@click.option("-f", "--file", multiple=True, type=click.File('r'),
              help="Path to ModulDescriptor")
def add(**kwargs):
    """Add module(s) by name or add a ModulDescriptor(s)
    """
    print(kwargs)
    for m in create_okapiModules(kwargs["moduleid"]):
        print(f"Add module {m.get_modId()}")
        OkapiClient().add_module(m)

    for f in kwargs["file"]:
        d = json.load(f)
        print("Add module descriptor %s" % d["id"])


@module.command()
@click.argument("moduleid", required=True, nargs=-1)
def remove(**kwargs):
    """Remove module(s) by id, e.g. mod-users-17.1.0

    MODULEID\tmodule id. Can be repeated.
    """
    print(kwargs)
    for m in kwargs["moduleid"]:
        print(f"Remove module {m}")
        OkapiClient().remove_module(m)


@module.command()
@click.option("-v", "--verbose", help="increase output verbosity",
              is_flag=True)
def deployed(**kwargs):
    """List deployed modules
    """
    mods = OkapiClient().get_deployed_modules()
    if kwargs["verbose"]:
        for mod in mods:
            print()
            print(json.dumps(mod, indent=2))
    else:
        print("Mod-id\t\t\t\tNode\t\tDocker-URL\t\t\tDocker-Image")
        for e in mods:
            m = e["srvcId"].ljust(30)
            n = e["nodeId"]
            u = e["url"]
            if "dockerImage" in e["descriptor"]:
                d = e["descriptor"]["dockerImage"]
            else:
                d = ""
            print(f"{m}\t{n}\t{u}\t{d}")


@module.command()
@click.argument("moduleid", required=True, nargs=-1)
@click.option("-n", "--node", default=get_node(), help="Node", show_default=True)
def deploy(**kwargs):
    """Deploy module(s) for a node

    MODULEID\tmodule id. Can be repeated.
    """
    print(kwargs)
    for m in kwargs["moduleid"]:
        n = kwargs["node"]
        print(f"Deploy module {m} on node {n}")
        OkapiClient().deploy_module(m, n)


@module.command()
@click.argument("moduleid", required=True, nargs=-1)
def undeploy(**kwargs):
    """Undeploy module(s)

    MODULEID\tmodule id. Can be repeated.
    """
    print(kwargs)
    for m in kwargs["moduleid"]:
        print(f"Undeploy module {m}")
        OkapiClient().undeploy_module(m)
