# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import click
from foliolib.helper.okapi import login_supertenant

from .folio import folio
from .orderedGroup import OrderedGroup
from .server import server

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(cls=OrderedGroup, context_settings=CONTEXT_SETTINGS)
def main():
    """Foliolib command line interface
    """


@main.command()
# @click.argument("user", required=True)
@click.option("-u", "--user", required=True,
              help="username for the supertenant")
@click.option("-p", "--password", required=True,
              help="password of the user for the supertenant")
def loginOkapi(**kwargs):
    """Log into Supertenant with username and password.
    """
    login_supertenant(kwargs["user"], kwargs["password"])


main.add_command(folio)
main.add_command(server)
