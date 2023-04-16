# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import json

import click
from foliolib.config import Config
from foliolib.helper import get_node
from foliolib.okapi.kubeClient import KubeClient
from foliolib.okapi.okapiClient import OkapiClient
from foliolib.okapi.okapiModule import create_okapiModules
from tabulate import tabulate

from .orderedGroup import OrderedGroup


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
    if kwargs["full"]:
        for e in mods:
            print(json.dumps(e, indent=2)+"\n")
    else:
        headers = ["id", "name"]
        body = [[e["id"], e["name"]] for e in mods]
        print(tabulate(body, headers=headers))


@module.command()
@click.argument("moduleid", required=True)
def get(**kwargs):
    """Get ModulDescriptor. e.g. mod-users-17.1.0

    MODULEID\tmodule id.
    """
    mod = OkapiClient().get_module(kwargs["moduleid"])
    print(json.dumps(mod, indent=2))


@module.command()
@click.argument("moduleid", required=True, nargs=-1)
def add(**kwargs):
    """Add module(s) by id. e.g. mod-users-17.1.0

    MODULEID\tmodule id. Can be repeated.
    """
    for m in create_okapiModules(kwargs["moduleid"]):
        print(f"Add module {m.get_id()}")
        OkapiClient().add_module(m)


@module.command()
@click.option("-f", "--file", multiple=True, type=click.File('r'),
              help="Path to ModulDescriptor")
def addMD(**kwargs):
    """Add ModulDescriptor(s)
    """
    for f in kwargs["file"]:
        m = json.load(f)
        print("Add module descriptor %s" % m["id"])
        OkapiClient().add_module(m)


@module.command()
@click.argument("moduleid", required=True, nargs=-1)
def remove(**kwargs):
    """Remove module(s), e.g. mod-users-17.1.0

    MODULEID\tmodule id. Can be repeated.
    """
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
        okapi_mods = [m for m in mods if "descriptor" in m]
        kube_mods = [m for m in mods if m["instId"].startswith("kube_")]
        if okapi_mods:
            headers = ["Module id", "Node id", "Docker URL", "Docker Image"]
            body = []
            for e in mods:
                l = [e["srvcId"], e["nodeId"], e["url"]]
                if "dockerImage" in e["descriptor"]:
                    l.append(e["descriptor"]["dockerImage"])
                else:
                    l.append("")
                body.append(l)
            print(tabulate(body, headers=headers))
        if okapi_mods and kube_mods:
            print("")
        if kube_mods:
            headers = ["Module id", "Kubernetes URL"]
            body = [[e["srvcId"], e["url"]] for e in mods]
            print(tabulate(body, headers=headers))


@module.command()
@click.argument("moduleid", required=True, nargs=-1)
@click.option("-n", "--node", default=get_node(), help="Node", show_default=True)
def deploy(**kwargs):
    """Deploy module(s) for a node.

    MODULEID\tmodule id. Can be repeated.
    """
    for m in kwargs["moduleid"]:
        n = kwargs["node"]
        print(f"Deploy module {m} on node {n}")
        OkapiClient().deploy_module(m, n)


@module.command()
@click.argument("moduleid", required=True, nargs=-1)
def undeploy(**kwargs):
    """Undeploy module(s).

    MODULEID\tmodule id. Can be repeated.
    """
    for m in kwargs["moduleid"]:
        print(f"Undeploy module {m}")
        OkapiClient().undeploy_module(m)


if Config().is_kubernetes():
    @module.command()
    @click.argument("moduleid", nargs=-1)
    def redeploy(**kwargs):
        """Redeploy module(s).

        MODULEID\tmodule id. Can be repeated.
        """
        modIds = kwargs["moduleid"]
        if not modIds:
            modIds = [module["id"] for module in OkapiClient().get_modules()
                      if "launchDescriptor" in OkapiClient().get_module(module["id"])]

        for modId in modIds:
            print("Redeploy %s" % modId)
            KubeClient().patch(modId)
