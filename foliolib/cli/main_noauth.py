# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import click
from foliolib.helper.okapi import login_supertenant

from .folio import folio
from .server import server

from.orderedGroup import OrderedGroup

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(cls=OrderedGroup, context_settings=CONTEXT_SETTINGS)
def main():
    """Foliolib command line interface
    """


@main.command()
# @click.argument("user", required=True)
@click.argument("user", default="okapi_admin")
@click.argument("password", default="admin")
def loginOkapi(**kwargs):
    """Log into Supertenant with username and password.

    USER\tUsername of supertenant. (default: okapi_admin)

    PASSWORD\tPassword of supertenant user. (default: admin)
    """
    login_supertenant(kwargs["user"], kwargs["password"])


main.add_command(folio)
main.add_command(server)
