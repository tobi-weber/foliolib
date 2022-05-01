# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import json

import click
from foliolib.helper.tenant import uninstall_tenant
from foliolib.okapi.okapiClient import OkapiClient
from tabulate import tabulate

from .orderedGroup import OrderedGroup


@click.group(cls=OrderedGroup)
def tenant():
    """Commands to manage tenants.
    """


@tenant.command()
def lst():
    """List tenants.
    """
    tenants = OkapiClient().get_tenants()
    headers = ["id", "Name", "Description"]
    body = [[e["id"], e["name"], e["description"]] for e in tenants]
    print(tabulate(body, headers=headers))


@tenant.command()
@click.argument("tenantid", required=True)
@click.option("-a", "--name", default="", help="tenant name", show_default=True)
@click.option("-d", "--description", default="",
                    help="tenant description long", show_default=True)
def add(**kwargs):
    """Add new tenant.

    TENANTID\ttenant id.
    """
    print("Create tenant: %s" % kwargs["tenantid"])
    print("Name: %s" % kwargs["name"])
    print("Description: %s" % kwargs["description"])
    OkapiClient().create_tenant(kwargs["tenantid"],
                                kwargs["name"],
                                kwargs["description"])


@tenant.command()
@click.argument("tenantid", required=True)
def remove(**kwargs):
    """Remove tenant.

    TENANTID\ttenant id.
    """
    print("Remove tenant: %s" % kwargs["tenantid"])
    OkapiClient().remove_tenant(kwargs["tenantid"])


@tenant.command()
@click.argument("tenantid", required=True)
@click.option("-n", "--name", default="", help="tenant name", show_default=True)
@click.option("-d", "--description", default="",
                    help="tenant description long", show_default=True)
def modify(**kwargs):
    """Modify tenant.

    TENANTID\ttenant id.
    """
    print("Modify tenantid: %s" % kwargs["tenantid"])
    print("Name: %s" % kwargs["name"])
    print("Description: %s" % kwargs["description"])
    OkapiClient().modify_tenant(kwargs["tenantid"],
                                kwargs["name"],
                                kwargs["description"])


@tenant.command()
@click.argument("tenantid", required=True)
@click.argument("moduleid", nargs=-1, required=True)
@click.option("--loadSample",  help="", is_flag=True, default=False)
@click.option("--loadReference",  help="", is_flag=True, default=False)
@click.option("--async", is_flag=True,
              help="Install in the background")
@click.option("--deploy", is_flag=True,
              help="Deploy modules")
@click.option("--ignoreErrors", is_flag=True,
              help="Ignore errors during the install operation")
@click.option("--no-invoke", is_flag=True,
              help="Do not invoke for tenant init/permissions/purge")
@click.option("--no-npmSnapshot", is_flag=True,
              help="Do not include NPM module snapshots")
@click.option("--no-preRelease", is_flag=True,
              help="Pre-releases should not be considered for installation")
@click.option("--simulate", is_flag=True,
              help="Simulate the installation")
def enable(**kwargs):
    """Enable module(s) for a tenant.

    TENANTID\tThe tenant id.
    MODULEID\tOne ore multiple module id(s).
    """
    _kwargs = {}
    if kwargs["async"]:
        _kwargs["async"] = True
    if kwargs["deploy"]:
        _kwargs["deploy"] = True
    if kwargs["ignoreerrors"]:
        _kwargs["ignoreErrors"] = True
    if kwargs["simulate"]:
        _kwargs["simulate"] = True
    if kwargs["no_invoke"]:
        _kwargs["invoke"] = False
    if kwargs["no_npmsnapshot"]:
        _kwargs["npmSnapshot"] = False
    if kwargs["no_prerelease"]:
        _kwargs["preRelease"] = False
    print("Enable module %s for tenant %s" %
          (kwargs["moduleid"], kwargs["tenantid"]))
    OkapiClient().enable_modules(kwargs["moduleid"], kwargs["tenantid"],
                                 loadSample=kwargs["loadsample"],
                                 loadReference=kwargs["loadreference"],
                                 **_kwargs)


@tenant.command()
@click.argument("tenantid", required=True)
@click.argument("modid", nargs=-1, required=True)
@click.option("--async", is_flag=True,
              help="Uninstall in the background")
@click.option("--undeploy", is_flag=True,
              help="Undeploy modules")
@click.option("--ignoreErrors", is_flag=True,
              help="Ignore errors during the uninstall operation")
@click.option("--no-invoke", is_flag=True,
              help="Do not invoke for tenant init/permissions/purge")
@click.option("--purge", is_flag=True,
              help="Modules will also be purged.")
@click.option("--simulate", is_flag=True,
              help="Simulate the installation")
def disable(**kwargs):
    """Disable module(s) for a tenant.

    TENANTID\tThe tenant id.
    MODULEID\tOne ore multiple module id(s).
    """
    _kwargs = {}
    if kwargs["async"]:
        _kwargs["async"] = True
    if kwargs["undeploy"]:
        _kwargs["deploy"] = True
    if kwargs["ignoreerrors"]:
        _kwargs["ignoreErrors"] = True
    if kwargs["purge"]:
        _kwargs["purge"] = True
    if kwargs["simulate"]:
        _kwargs["simulate"] = True
    if kwargs["no_invoke"]:
        _kwargs["invoke"] = False
    print("Disable module %s for tenant %s" %
          (kwargs["modid"], kwargs["tenantid"]))
    OkapiClient().disable_modules(
        kwargs["modid"], kwargs["tenantid"], **_kwargs)


@tenant.command()
@click.argument("tenantid", required=True)
@click.option("--async", is_flag=True,
              help="Upgrade in the background")
@click.option("--ignoreErrors", is_flag=True,
              help="Ignore errors during the uninstall operation")
@click.option("--no-invoke", is_flag=True,
              help="Not invoke for tenant init/permissions/purge")
@click.option("--no-npmSnapshot", is_flag=True,
              help="Do not include NPM module snapshots")
@click.option("--no-preRelease", is_flag=True,
              help="Pre-releases should be considered for installation")
@click.option("--purge", is_flag=True,
              help="Modules will also be purged.")
@click.option("--simulate", is_flag=True,
              help="Simulate the installation")
def upgrade(**kwargs):
    """Upgrade tenant.

    TENANTID\tThe tenant id.
    """
    _kwargs = {}
    if kwargs["async"]:
        _kwargs["async"] = True
    if kwargs["ignoreerrors"]:
        _kwargs["ignoreErrors"] = True
    if kwargs["simulate"]:
        _kwargs["simulate"] = True
    if kwargs["no_invoke"]:
        _kwargs["invoke"] = False
    if kwargs["no_npmsnapshot"]:
        _kwargs["npmSnapshot"] = False
    if kwargs["no_prerelease"]:
        _kwargs["preRelease"] = False
    msg = OkapiClient().upgrade_modules(kwargs["tenantid"], **_kwargs)
    print(json.dumps(msg, indent=2))


@tenant.command()
@click.argument("tenantid", required=True)
@click.option("--full", is_flag=True,
              help="Full MD should be returned")
def modules(**kwargs):
    """List modules of a tenant.

    TENANTID\tThe tenant id.
    """
    _kwargs = {}
    if kwargs["full"]:
        _kwargs["full"] = kwargs["full"]
    mods = OkapiClient().get_tenant_modules(kwargs["tenantid"],
                                            **_kwargs)
    for e in mods:
        print(e["id"])


@tenant.command()
@click.argument("tenantid", required=True)
@click.option("-i", "--interface")
@click.option("-f", "--full", is_flag=True,
              help="Full MD should be returned")
def interfaces(**kwargs):
    """List interface(s).

    TENANTID\tThe tenant id.
    """
    if kwargs["interface"]:
        inf = OkapiClient().get_tenant_interface(kwargs["interface"],
                                                 kwargs["tenantid"])
        print("Interface is in module %s" % inf[0]["id"])
        # print(inf)
    else:
        _kwargs = {}
        if kwargs["full"]:
            _kwargs["full"] = kwargs["full"]
        interfaces = OkapiClient().get_tenant_interfaces(kwargs["tenantid"],
                                                         **_kwargs)
        for e in sorted(interfaces, key=lambda e: e["id"]):
            k = e["id"]
            n = e["version"]
            print(f"{k} {n}")
            if "handlers" in e:
                for handler in e["handlers"]:
                    try:
                        p = ", ".join(handler["permissionsRequired"])
                    except:
                        p = ""
                    print("\t%s %s" %
                          ((", ".join(handler["methods"])),
                           handler["pathPattern"]
                           )
                          )
                    #print("\t\t%s" % p)


@tenant.command()
@click.argument("tenantid")
@click.option("--async", is_flag=True,
              help="Uninstall in the background")
@click.option("--undeploy", is_flag=True,
              help="Undeploy modules")
@click.option("--ignoreErrors", is_flag=True,
              help="Ignore errors during the uninstall operation")
@click.option("--no-invoke", is_flag=True,
              help="Do not invoke for tenant init/permissions/purge")
@click.option("--purge", is_flag=True,
              help="Modules will also be purged.")
@click.option("--simulate", is_flag=True,
              help="Simulate the installation")
def uninstall(**kwargs):
    """Disable all modules of a tenant.

    TENANTID\ttenant id
    """
    _kwargs = {}
    if kwargs["async"]:
        _kwargs["async"] = True
    if kwargs["undeploy"]:
        _kwargs["deploy"] = True
    if kwargs["ignoreerrors"]:
        _kwargs["ignoreErrors"] = True
    if kwargs["purge"]:
        _kwargs["purge"] = True
    if kwargs["simulate"]:
        _kwargs["simulate"] = True
    if kwargs["no_invoke"]:
        _kwargs["invoke"] = False
    print("Disable all modules for tenant %s" % kwargs["tenantid"])
    uninstall_tenant(kwargs["tenantid"], **_kwargs)
