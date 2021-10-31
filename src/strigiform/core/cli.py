"""strigiform CLI functionality."""
import functools
import os
from subprocess import SubprocessError

import click
from botocore.exceptions import ClientError
from click_help_colors import HelpColorsCommand
from click_help_colors import HelpColorsGroup

from strigiform.core.commands._helpers import CliColors
from strigiform.core.commands.hotspots import hotspot_cmd
from strigiform.core.commands.launch import launch_app_cmd
from strigiform.core.commands.test import nox_cmd
from strigiform.core.commands.vault import launch_vault_cmd


click.option = functools.partial(click.option, show_default=True)


@click.group(
    name="strigiform",
    cls=HelpColorsGroup,
    help_headers_color=CliColors.USAGE.value,
    help_options_color=CliColors.OPTIONS.value,
)
@click.version_option("0.0.0", prog_name="strigiform")
def main():
    """Command line interface for strigiform - python tools for Ebird and birding in general."""
    click.echo("Hello, Birders!")


@main.command(cls=HelpColorsCommand, help_options_color="blue")
@click.argument("root_dir", type=click.Path(), default=os.curdir)
def test(root_dir: str):
    """Runs the Nox testing suite for the entire project."""
    nox_cmd(root_dir)


@main.command(cls=HelpColorsCommand, help_options_color=CliColors.OPTIONS.value)
@click.option(
    "--lat",
    help="Latitude, distance north or south of the equator in degrees",
    type=float,
    default=40.71,
)
@click.option(
    "--lon",
    help="Longitude, distance east or west of the meridian in degrees",
    type=float,
    default=-73.95,
)
@click.option("--fmt", help="Format of output (default json)", type=str, default="json")
@click.option(
    "--miles", help="Search radius from provided Lat and Lon ", type=int, default=3
)
def hotspots(lat: float, lon: float, fmt: str, miles: int):
    """Searches Ebird for hotspots for birding."""
    hotspot_cmd(lat, lon, fmt, miles)


@main.command(cls=HelpColorsCommand, help_options_color="blue")
def launch():
    """Launches strigiform webapp."""
    launch_app_cmd()


@main.command(cls=HelpColorsCommand, help_options_color="blue")
def vault():
    """Launches Hashicorp Vault."""
    try:
        launch_vault_cmd()
    except SubprocessError:
        click.secho(
            """Failed to start Vault...
        Vault server may be running already?
            You can verify by running 'vault status'. \n""",
            fg="yellow",
        )


if __name__ == "__main__":
    try:
        main(prog_name="strigiform")
    except ClientError:
        click.secho("Command failed... please debug. \n", fg="yellow")
