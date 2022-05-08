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
@click.argument("platform")
@click.argument("tenantid")
@click.option("-n", "--node", default=get_node(),
              help="node id", show_default=True)
@click.option("-e", "--edgemodule", multiple=True,
              help="Exclude edge module to deploy, e.g. edge-oai-pmh. Can be repeated")
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

    PLATFORM\tpath to folio platform.
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
    install_platform(kwargs["platform"], kwargs["node"], kwargs["tenantid"],
                     list(kwargs["edgemodule"]),
                     loadSample=kwargs["loadsample"],
                     loadReference=kwargs["loadreference"],
                     **_kwargs)


@platform.command()
@click.argument("platform")
@click.argument("tenantid")
@click.option("-n", "--node", default=get_node(),
              help="node id", show_default=True)
@click.option("-e", "--edgemodule", multiple=True,
              help="Exclude edge module to deploy, e.g. edge-oai-pmh . Can be repeated")
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
    """Upgrade a folio platform.

    PLATFORM\tpath to folio platform.
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
    upgrade_platform(kwargs["platform"], kwargs["node"], kwargs["tenantid"],
                     list(kwargs["edgemodule"]),
                     **_kwargs)