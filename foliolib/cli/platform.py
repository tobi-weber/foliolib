# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import click
from foliolib.helper import get_node
from foliolib.helper.platform import install_platform, upgrade_platform

from .orderedGroup import OrderedGroup


@click.group(cls=OrderedGroup)
def platform():
    """Commands to manage Folio platforms.
    """


@platform.command()
@click.argument("tenantid")
@click.option("-p", "--platform", default="R1-2023-GA",
              help="Platform version (e.g. R1-2023 or path to platform directory or platform tgz file")
@click.option("-n", "--node", default=get_node(),
              help="node id", show_default=True)
@click.option("-a", "--deployAsync",  help="", is_flag=True)
@click.option("--loadSample",  help="", is_flag=True)
@click.option("--loadReference",  help="", is_flag=True)
@click.option(
    "--ignoreErrors", is_flag=True, help="Ignore errors during the install operation")
@click.option(
    "--no-invoke", is_flag=True, help="Not invoke for tenant init/permissions/purge")
@click.option(
    "--no-npmSnapshot", is_flag=True, help="Not include NPM module snapshots")
@click.option(
    "--no-preRelease", is_flag=True, help="Pre-releases should be considered for installation")
@click.option(
    "--simulate", is_flag=True, help="Simulate the installation")
def install(**kwargs):
    """Install a folio platform.
    This can be called multiple times, to setup different tenants.

    TENANTID\ttenant id.
    """
    _kwargs = {}
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
    install_platform(kwargs["platform"], kwargs["tenantid"], kwargs["node"],
                     loadSample=kwargs["loadsample"],
                     loadReference=kwargs["loadreference"],
                     deploy_async=kwargs["deployasync"],
                     **_kwargs)


@platform.command()
@click.option("-t", "--tenant", default="ALL",
              help="Tenant id to upgrade. Default all tenants will be upgraded, except the supertenant")
@click.option("-p", "--platform", required=True,
              help="Path to platform directory, tgz file, zip file or platform version")
@click.option("-n", "--node", default=get_node(),
              help="node id", show_default=True)
@click.option("-a", "--deployAsync",  help="", is_flag=True)
@click.option("-e", "--exclude",  help="Exclude module from upgrade, e.g. mod-authtoken",
              multiple=True)
@click.option(
    "--ignoreErrors", is_flag=True, help="Ignore errors during the install operation")
@click.option(
    "--no-invoke", is_flag=True, help="Not invoke for tenant init/permissions/purge")
@click.option(
    "--no-npmSnapshot", is_flag=True, help="Not include NPM module snapshots")
@click.option(
    "--no-preRelease", is_flag=True, help="Pre-releases should be considered for installation")
@click.option(
    "--simulate", is_flag=True, help="Simulate the installation")
def upgrade(**kwargs):
    """Upgrade folio tenants.
    It is recommended to unsecure okapi before upgrading.
    It may be necessary to update okapi before.
    """
    _kwargs = {}
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
    upgrade_platform(kwargs["platform"], kwargs["tenant"], kwargs["node"],
                     deploy_async=kwargs["deployasync"],
                     exclude=kwargs["exclude"], **_kwargs)
