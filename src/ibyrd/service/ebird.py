"""Module to interact with EBird API."""
from io import StringIO
from typing import Any

import pandas as pd
import requests

from ibyrd.util.auth import EBIRD_KEY  # type: ignore


def get_hotspots(
    lat: float, lon: float, fmt: str = "json", dist: int = 10, back: int = 5
) -> Any:
    """Retreive HotStop info for Lat/Lon coordinates."""
    parameters = {"lat": lat, "lng": lon, "fmt": fmt, "dist": dist, "back": back}

    response = requests.get(
        "https://api.ebird.org/v2/ref/hotspot/geo?", params=parameters  # type: ignore
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

    return response


def get_taxonomy_df(response) -> Any:
    """Format eBird Taxonomy response to pandas DataFrame."""
    taxonomy = StringIO(response.text)
    df = pd.read_csv(taxonomy)

    return df


# def get_checklist(subId: str) -> Any:
#     """Retreive eBird checklist information based on a single ID."""
#     header = {"X-eBirdApiToken": EBIRD_KEY}
#     parameters = {"subId": subId}
#     subId = "S90521630"
#     response = requests.get(
#         f"https://api.ebird.org/v2/product/checklist/view/{subId}", headers=header
#     )
#     taxonomy = StringIO(response.text)
#     df = pd.read_csv(taxonomy)


# TODO: def get_ebird_region():
# TODO: def get_species_list():
