"""Module to interact with EBird API."""
from io import StringIO
from typing import Any

import pandas as pd
import requests

from ibyrd.util.auth import EBIRD_KEY


def get_hotspots(
    lat: float, lon: float, fmt: str = "json", dist: int = 10, back: int = 5
) -> Any:
    """Retreive HotStop info for Lat/Lon coordinates."""
    parameters = {"lat": lat, "lng": lon, "fmt": fmt, "dist": dist, "back": back}

    response = requests.get(
        "https://api.ebird.org/v2/ref/hotspot/geo?", params=parameters
    )

    locations = []
    for result in response.json():
        locations.append(str(result["locName"]))

    return locations


def get_taxonomy(fmt: str = "csv") -> Any:
    """Retreive eBird Taxonomy."""
    header = {"X-eBirdApiToken": EBIRD_KEY}

    response = requests.get(
        "https://api.ebird.org/v2/ref/taxonomy/ebird?", headers=header
    )
    taxonomy = StringIO(response.text)
    df = pd.read_csv(taxonomy)

    return df
