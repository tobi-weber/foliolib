# -*- coding: utf-8 -*-
# Copyright (C) 2024 Tobias Weber <tobi-weber@gmx.de>

import click
from foliolib.helper import jprint
from foliolib.helper.folio import create_superuser
from foliolib.helper.tenant import uninstall_tenant
from foliolib.okapi.okapiClient import OkapiClient
from tabulate import tabulate

from ..confirm import confirm
from ..orderedGroup import OrderedGroup


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
@click.option("-t", "--tenantid", required=True)
@click.option("-a", "--name", default="", help="tenant name", show_default=True)
@click.option("-d", "--description", default="",
                    help="tenant description long", show_default=True)
@confirm
def add(**kwargs):
    """Add new tenant.
    """
    print("Create tenant: %s" % kwargs["tenantid"])
    print("Name: %s" % kwargs["name"])
    print("Description: %s" % kwargs["description"])
    OkapiClient().create_tenant(kwargs["tenantid"],
                                kwargs["name"],
                                kwargs["description"])


@tenant.command()
@click.option("-t", "--tenantid", required=True)
@confirm
def remove(**kwargs):
    """Remove tenant.
    """
    print("Remove tenant: %s" % kwargs["tenantid"])
    OkapiClient().remove_tenant(kwargs["tenantid"])


@tenant.command()
@click.option("-t", "--tenantid", required=True)
@click.option("-n", "--name", default="", help="tenant name", show_default=True)
@click.option("-d", "--description", default="",
                    help="tenant description long", show_default=True)
@confirm
def modify(**kwargs):
    """Modify tenant.
    """
    print("Modify tenantid: %s" % kwargs["tenantid"])
    print("Name: %s" % kwargs["name"])
    print("Description: %s" % kwargs["description"])
    OkapiClient().modify_tenant(kwargs["tenantid"],
                                kwargs["name"],
                                kwargs["description"])


@tenant.command()
@click.option("-t", "--tenantid", required=True)
@click.option("-u", "--user", default="folio_admin", help=" ", show_default=True)
@click.option("-p", "--password", default="admin", help=" ", show_default=True)
@confirm
def superuser(**kwargs):
    """Create superuser for a tenant.

    TENANTID\tThe tenant id.
    """
    print("Create superuser %s:%s for tenant %s" % (kwargs["user"],
                                                    kwargs["password"],
                                                    kwargs["tenantid"]))
    create_superuser(kwargs["tenantid"],
                     kwargs["user"], kwargs["password"])


@tenant.command()
@click.option("-t", "--tenantid", required=True,
              help="If tenantid  is 'all', the action will be executed on all tenants.")
@click.option("-m", "--module", multiple=True, required=True)
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
@confirm
def enable(**kwargs):
    """Enable module(s) for a tenant.
    """
    _kwargs = {}
    tenantid = kwargs["tenantid"]
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

    def do(tid):
        print("Enable module %s for tenant %s" %
              (kwargs["module"], tid))
        msg = OkapiClient().enable_modules(tid, kwargs["module"],
                                           loadSample=kwargs["loadsample"],
                                           loadReference=kwargs["loadreference"],
                                           **_kwargs)
        jprint(msg)

    if tenantid.upper() == "ALL":
        tenants = OkapiClient().get_tenants()
        for tenant in tenants:
            if tenant["id"] != "supertenant":
                do(tenant["id"])
    else:
        do(tenantid)


@tenant.command()
@click.option("-t", "--tenantid", required=True,
              help="If tenantid  is 'all', the action will be executed on all tenants.")
@click.option("-m", "--module", multiple=True, required=True)
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
@confirm
def disable(**kwargs):
    """Disable module(s) for a tenant.
    """
    _kwargs = {}
    tenantid = kwargs["tenantid"]
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

    def do(tid):
        try:
            for modid in kwargs["module"]:
                print("Disable module %s for tenant %s" %
                      (modid, tid))
                msg = OkapiClient().disable_modules([modid], tid, **_kwargs)
                jprint(msg)
        except Exception as e:
            print(e)
            if not kwargs["ignoreerrors"]:
                raise

    if tenantid.upper() == "ALL":
        tenants = OkapiClient().get_tenants()
        for tenant in tenants:
            if tenant["id"] != "supertenant":
                do(tenant["id"])
    else:
        do(tenantid)


@tenant.command()
@click.option("-t", "--tenantid", required=True,
              help="If tenantid  is 'all', the action will be executed on all tenants.")
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
@click.option("--simulate", is_flag=True,
              help="Simulate the installation")
@click.option(
    "--purge", is_flag=True, help="Disabled modules will also be purged.")
@confirm
def upgrade(**kwargs):
    """Upgrade tenant.
    """
    _kwargs = {}
    tenantid = kwargs["tenantid"]
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
    if kwargs["purge"]:
        _kwargs["purge"] = True

    def do(tid):
        print("Upgrade tenant %s" % tid)
        try:
            msg = OkapiClient().upgrade_modules(tid, **_kwargs)
            jprint(msg)
        except Exception as e:
            print(e)
            if not kwargs["ignoreerrors"]:
                raise

    if tenantid.upper() == "ALL":
        tenants = OkapiClient().get_tenants()
        for tenant in tenants:
            if tenant["id"] != "supertenant":
                do(tenant["id"])
    else:
        do(tenantid)


@tenant.command()
@click.option("-t", "--tenantid", required=True,
              help="If tenantid  is 'all', the action will be executed on all tenants.")
@click.option("-m", "--module", multiple=True, required=True)
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
@click.option("--simulate", is_flag=True,
              help="Simulate the installation")
@click.option(
    "--purge", is_flag=True, help="Disabled modules will also be purged.")
@confirm
def upgrademodule(**kwargs):
    """Upgrade tenant.
    """
    _kwargs = {}
    tenantid = kwargs["tenantid"]
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
    modules = kwargs["module"]
    if kwargs["purge"]:
        _kwargs["purge"] = True

    def do(tid):
        print("Upgrade modules %s for tenant %s" % (str(modules), tid))
        msg = OkapiClient().upgrade_modules(tid, modules=modules, **_kwargs)
        jprint(msg)

    if tenantid.upper() == "ALL":
        tenants = OkapiClient().get_tenants()
        for tenant in tenants:
            if tenant["id"] != "supertenant":
                do(tenant["id"])
    else:
        do(tenantid)


@tenant.command()
@click.option("-t", "--tenantid", required=True)
@click.option("--full", is_flag=True,
              help="Full MD should be returned")
def modules(**kwargs):
    """List modules of a tenant.
    """
    _kwargs = {}
    if kwargs["full"]:
        _kwargs["full"] = kwargs["full"]
    mods = OkapiClient().get_tenant_modules(kwargs["tenantid"],
                                            **_kwargs)
    for e in mods:
        if kwargs["full"]:
            jprint(e)
        else:
            print(e["id"])


@tenant.command()
@click.option("-t", "--tenantid", required=True)
@click.option("-i", "--interface")
@click.option("-f", "--full", is_flag=True,
              help="Full MD should be returned")
def interfaces(**kwargs):
    """List interface(s).
    """
    if kwargs["interface"]:
        inf = OkapiClient().get_tenant_interface(kwargs["tenantid"],
                                                 kwargs["interface"])
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
                    # print("\t\t%s" % p)


@tenant.command()
@click.option("-t", "--tenantid", required=True)
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
@confirm
def uninstall(**kwargs):
    """Disable all modules of a tenant.
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
