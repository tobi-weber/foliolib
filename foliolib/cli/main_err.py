import click

from .server import server

from.orderedGroup import OrderedGroup

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(cls=OrderedGroup, context_settings=CONTEXT_SETTINGS)
def main():
    """Foliolib command line interface
    """


main.add_command(server)
