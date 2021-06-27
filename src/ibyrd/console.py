"""Command line functions for ibyrd."""
import argparse
import textwrap

import click
import requests

from . import __version__
# from birding import ebird

HOTSPOT_API_URL = "https://api.ebird.org/v2/ref/hotspot/geo?"


@click.command()
@click.version_option(version=__version__)
def main():
    """The Al McKay's Birding Projects."""
    click.echo("Hello, Birders!")


def hotspots():

    parser = argparse.ArgumentParser()
    parser.add_argument("--lat", type=float, default=40.71)
    parser.add_argument("--lon", type=float, default=-73.95)
    parser.add_argument("--fmt", type=str, default="json")
    parser.add_argument("--miles", type=int, default=3)
    args = parser.parse_args()

    parameters = {"lat": args.lat, "lng": args.lon, "fmt": args.fmt, "dist": args.miles}

    with requests.get(HOTSPOT_API_URL, params=parameters) as response:
        response.raise_for_status()
        data = response.json()

    locations = []
    latest_observation = []

    for result in data:
        # locations.append(str(result["locName"]))
        # latest_observation.append(str(result["latestObsDt"]))
        click.secho(result["locName"], fg="green")
        click.echo(textwrap.fill(result["latestObsDt"]))
