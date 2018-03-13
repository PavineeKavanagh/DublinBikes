# -*- coding: utf-8 -*-

"""Console script for dublinbikes."""

import click


@click.command()
def main(args=None):
    """Console script for dublinbikes."""
    click.echo("Replace this message by putting your code into "
               "dublinbikes.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
