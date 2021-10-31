"""Module to interact with EBird API."""
import json
import os

from strigiform.util import config
from strigiform.util import logger
from strigiform.util.api import api_extract

logger = logger.logger_init(name=__name__)


ebird_key = os.getenv("EBIRD_KEY")


def get_taxonomy(
    cat: str = config.DEFAULT_TAXONOMY_CATEGORY,
    fmt: str = config.DEFAULT_TAXONOMY_FORMAT,
    save: bool = False,
    save_fmt: str = config.DEFAULT_TAXONOMY_SAVE_FORMAT,
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
    params = {"cat": cat, "fmt": fmt}

    return api_extract(config.EBIRD_TAXONOMY_URL, params, save, save_fmt, path)


def get_hotspots(
    lat: float = config.DEFAULT_LAT,
    lng: float = config.DEFAULT_LNG,
    fmt: str = config.DEFAULT_FORMAT,
    dist: int = config.DEFAULT_DIST,
    back: int = config.DEFAULT_BACK,
    loc_only: bool = True,
    save: bool = False,
    path: str = "./data/hotspots",
):
    """Function to extract eBird hotspots according provided parameters.

    :param params: request parameters for hotspot api request, defaults to None
    :type params: dict, optional
    :param save: Option to save output, defaults to False
    :type save: bool, optional
    :param path: Location of output if save is set to True, defaults to './data/hotspots'
    :type path: str, optional
    :return: Dict of eBird hotspots
    :rtype: dict
    """
    params = {"lat": lat, "lng": lng, "fmt": fmt, "dist": dist, "back": back}

    response = api_extract(config.EBIRD_HOTSPOT_URL, params, save, path)

    if loc_only is True:
        hotspots = []
        for result in json.loads(response):
            hotspots.append(str(result["locName"]))
    else:
        hotspots = response

    return hotspots


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
