"""Cli interface for retreiving birding hotspots."""
import textwrap

import click
import requests

from strigiform.util.config import EBIRD_HOTSPOT_URL


def clean_echo_results(data) -> None:
    """Function to print location infomation to terminal."""
    for result in data:
        click.secho(result["locName"], fg="green")
        try:
            click.echo(textwrap.fill(result["latestObsDt"]))
        except KeyError:
            click.secho("No recent Observations", fg="red")


def hotspot_cmd(
    lat: float = 40.71, lon: float = -73.95, fmt: str = "json", miles: int = 3
) -> None:
    """Get user input coordindates and range."""
    parameters = {"lat": lat, "lng": lon, "fmt": fmt, "dist": miles}

    if (abs(lat) > 90) or (abs(lon) > 180) or (miles <= 0) or (miles > 30):
        raise ValueError
        exit

    with requests.get(EBIRD_HOTSPOT_URL, params=parameters) as response:
        response.raise_for_status()
        data = response.json()

    clean_echo_results(data)
