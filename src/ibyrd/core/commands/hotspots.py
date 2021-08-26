"""Cli interface for retreiving birding hotspots."""
import textwrap

import click
import requests

from ibyrd.commons.config import HOTSPOT_API_URL


def clean_echo_results(data) -> None:
    """Function to print location infomation to terminal."""
    for result in data:
        click.secho(result["locName"], fg="green")
        try:
            click.echo(textwrap.fill(result["latestObsDt"]))
        except KeyError:
            click.secho("No recent Observations", fg="red")


def hotspot_cmd(lat: float, lon: float, fmt: str, miles: int) -> None:
    """Get user input coordindates and range."""
    parameters = {"lat": lat, "lng": lon, "fmt": fmt, "dist": miles}

    with requests.get(HOTSPOT_API_URL, params=parameters) as response:
        response.raise_for_status()
        data = response.json()

    clean_echo_results(data)
