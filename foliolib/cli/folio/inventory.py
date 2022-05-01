# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import click

from ..orderedGroup import OrderedGroup


@click.group(cls=OrderedGroup)
def inventory():
    """Commands related to inventory.
    """
