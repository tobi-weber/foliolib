# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import click

from .orderedGroup import OrderedGroup
from .server import server

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(cls=OrderedGroup, context_settings=CONTEXT_SETTINGS)
def err():
    """Foliolib command line interface
    """


err.add_command(server)
