# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import click
from foliolib.cli.folio.config import config
from foliolib.cli.folio.inventory import inventory
from foliolib.folio.users import Users
from foliolib.helper.folio import create_superuser

from ..orderedGroup import OrderedGroup


@click.group(cls=OrderedGroup)
def folio():
    """Commands to manage Folio.
    """


@folio.command()
@click.argument("tenantid")
@click.option("-u", "--user", default="folio_admin", help=" ", show_default=True)
@click.option("-p", "--password", default="admin", help=" ", show_default=True)
def login(**kwargs):
    """Log into a tenant

    TENANTID\tThe tenant id.
    """
    print("Login %s with %s:%s" % (kwargs["tenantid"],
                                   kwargs["user"],
                                   kwargs["password"]))

    Users(kwargs["tenantid"]).login(kwargs["user"], kwargs["password"])


@folio.command()
@click.argument("tenantid")
@click.option("-u", "--user", default="folio_admin", help=" ", show_default=True)
@click.option("-p", "--password", default="admin", help=" ", show_default=True)
def superuser(**kwargs):
    """Create superuser for a tenant.

    TENANTID\tThe tenant id.
    """
    print("Create superuser %s:%s for tenant %s" % (kwargs["user"],
                                                    kwargs["password"],
                                                    kwargs["tenantid"]))
    create_superuser(kwargs["tenantid"],
                     kwargs["user"], kwargs["password"])


folio.add_command(inventory)
folio.add_command(config)
