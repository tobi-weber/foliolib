# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import click
from foliolib.cli.folio.config import config
from foliolib.cli.folio.inventory import inventory
from foliolib.cli.folio.user import user
from foliolib.folio.usersImpl import UsersImpl

from ..orderedGroup import OrderedGroup
from ..server import server

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(cls=OrderedGroup, context_settings=CONTEXT_SETTINGS)
def folio():
    """Commands to manage Folio.
    """


@folio.command()
@click.option("-t", "--tenantid", required=True)
@click.option("-u", "--user", default="folio_admin", help=" ", show_default=True)
@click.option("-p", "--password", default="admin", help=" ", show_default=True)
def login(**kwargs):
    """Log into a tenant

    TENANTID\tThe tenant id.
    """
    print("Login %s with %s:%s" % (kwargs["tenantid"],
                                   kwargs["user"],
                                   kwargs["password"]))

    UsersImpl(kwargs["tenantid"]).login(kwargs["user"], kwargs["password"])


folio.add_command(inventory)
folio.add_command(config)
folio.add_command(user)
folio.add_command(server)
