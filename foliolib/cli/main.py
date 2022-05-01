# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import click

from .folio import folio
from .module import module
from .okapi import okapi
from .platform import platform
from .server import server
from .tenant import tenant

from.orderedGroup import OrderedGroup

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(cls=OrderedGroup, context_settings=CONTEXT_SETTINGS)
def main():
    """Foliolib command line interface
    """


main.add_command(okapi)
main.add_command(module)
main.add_command(tenant)
main.add_command(platform)
main.add_command(folio)
main.add_command(server)
