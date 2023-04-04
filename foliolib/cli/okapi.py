# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import click
from foliolib.config import Config
from foliolib.helper.okapi import (clean_okapi, secure_supertenant,
                                   unsecure_supertenant)
from foliolib.okapi.okapiClient import OkapiClient
from tabulate import tabulate

from .orderedGroup import OrderedGroup


@click.group(cls=OrderedGroup)
def okapi():
    """Commands to manage Okapi.
    """


@okapi.command()
def version():
    """Get Okapi version.
    """
    print(OkapiClient().version())


@okapi.command()
@click.option("-s", "--serviceId", help="")
@click.option("-i", "--instanceId", help="requires serviceId")
def health(**kwargs):
    """Get health.
    """
    res = OkapiClient().health(kwargs["serviceid"], kwargs["instanceid"])
    if isinstance(res, dict):
        res = [res]

    headers = ["Service ID", "Message", "Install ID", "Status"]
    body = [[e["srvcId"], e["healthMessage"], e["instId"], e["healthStatus"]]
            for e in sorted(res, key=lambda x: x["srvcId"])]
    print(tabulate(body, headers=headers))


@okapi.command()
def nodes():
    """List Nodes.
    """
    body = []
    for e in OkapiClient().get_nodes():
        l = [e["nodeId"], e["url"]]
        if "nodeName" in e:
            l.append(e["nodeName"])
        body.append(l)
    headers = ["NodeID", "URL"]
    if len(body) == 3:
        headers = ["NodeID", "URL", "NodeName"]
    print(tabulate(body, headers=headers))


@okapi.command()
def env():
    """List Okapi enviroment variables.
    """
    ev = OkapiClient().get_env()
    if not ev:
        print("No entries in okapi enviroment!")
    headers = ["Name", "Value", "Description"]
    body = []
    for e in ev:
        l = [e["name"], e["value"]]
        if "description" in e:
            l.append(e["description"])
        else:
            l.append("")
        body.append(l)
    print(tabulate(body, headers=headers))


@okapi.command()
@click.option("-n", "--name", help="")
@click.option("-v", "--value", help="")
@click.option("-d", "--description", help="")
def add_env(**kwargs):
    """Add global enviroment variable.
    """
    print("Add global enviroment variable:")
    print(f"\tname: {kwargs['name']}")
    print(f"\tvalue: {kwargs['value']}")
    print(f"\tdescription: {kwargs['description']}")
    OkapiClient().set_env(kwargs["name"], kwargs["value"],
                          description=kwargs["description"])


@okapi.command()
@click.argument("name", required=True, nargs=-1)
# @click.option("-n", "--name", help="")
def del_env(**kwargs):
    """Remove global enviroment variable.
    """
    print("Remove global enviroment variable:")
    print(f"\tname: {kwargs['name']}")
    # OkapiClient().delete_env(kwargs['name'])
    for name in kwargs["name"]:
        OkapiClient().delete_env(name)


@okapi.command()
@click.option("-u", "--user", default="okapi_admin", help=" ", show_default=True)
@click.option("-p", "--password", default="admin", help=" ", show_default=True)
def secure(**kwargs):
    """Secure Okapi installation.
    """
    print(f"Create supertenant user {kwargs['user']}:{kwargs['password']}")
    secure_supertenant(kwargs["user"], kwargs["password"])


@okapi.command()
def unsecure():
    """Unsecure Okapi installation.
    """
    print("Remove supertenant user")
    unsecure_supertenant()


@okapi.command()
def clean():
    """Undeploy and remove not enabled modules in a tenant.
    """
    clean_okapi()
