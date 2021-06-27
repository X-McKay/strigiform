"""Command line functions for ibyrd."""
import argparse
import os
import textwrap

import click
import requests

HOTSPOT_API_URL = "https://api.ebird.org/v2/ref/hotspot/geo?"


@click.command()
def main() -> None:
    """The Al McKay's Birding Projects."""
    click.echo("Hello, Birders!")


def hotspots() -> None:
    """Get user input coordindates and range."""
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

    for result in data:
        click.secho(result["locName"], fg="green")
        click.echo(textwrap.fill(result["latestObsDt"]))
