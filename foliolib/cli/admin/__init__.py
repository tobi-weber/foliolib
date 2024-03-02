# -*- coding: utf-8 -*-
# Copyright (C) 2024 Tobias Weber <tobi-weber@gmx.de>

import click
from foliolib.helper.okapi import login_supertenant

from ..folio import folio
from ..orderedGroup import OrderedGroup
from ..server import server
from .module import module
from .okapi import okapi
from .platform import platform
from .tenant import tenant

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(cls=OrderedGroup, context_settings=CONTEXT_SETTINGS)
def admin():
    """Foliolib command line interface
    """


admin.add_command(okapi)
admin.add_command(module)
admin.add_command(tenant)
admin.add_command(platform)
admin.add_command(folio)
admin.add_command(server)


@click.group(cls=OrderedGroup, context_settings=CONTEXT_SETTINGS)
def noauth():
    """Foliolib command line interface
    """


@noauth.command()
@click.option("-u", "--user", required=True,
              help="username for the supertenant")
@click.option("-p", "--password", required=True,
              help="password of the user for the supertenant")
def loginOkapi(**kwargs):
    """Log into Supertenant with username and password.
    """
    login_supertenant(kwargs["user"], kwargs["password"])


noauth.add_command(folio)
noauth.add_command(server)
