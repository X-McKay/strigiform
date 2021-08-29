"""Module to interact with EBird API."""
import os
from typing import Any

import requests

from ibyrd.commons import config
from ibyrd.commons.api import api_extract


ebird_key = os.getenv("EBIRD_KEY")


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


def get_taxonomy(
    category: str = config.DEFAULT_TAXONOMY_CATEGORY,
    fmt: str = config.DEFAULT_TAXONOMY_FORMAT,
    save: bool = False,
    path: str = "./data/taxonomy",
):
    """Function to request the latest taxonomy data from the eBird API.

    :param str category:
        Optional specification related to the granularity of taxonomy
    :param str fmt:
        Format output should be returned in
    :param bool save:
        Option to save option to file
    :param str path:
        Path to save output if relevant
    :return:
        API response
    """
    params = {"cat": category, "fmt": fmt}

    return api_extract(config.EBIRD_TAXONOMY_URL, params, save, path)


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
