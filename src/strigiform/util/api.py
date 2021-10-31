"""Common functions used to interact with APIs."""
import json
import os
from urllib.parse import urlencode

import requests

from strigiform.util import config


_ebird_api_defaults = {
    "lat": config.DEFAULT_LAT,
    "lng": config.DEFAULT_LNG,
    "dist": config.DEFAULT_DIST,
    "back": config.DEFAULT_BACK,
    "fmt": config.DEFAULT_FORMAT,
    "cat": config.DEFAULT_TAXONOMY_CATEGORY,
    "locale": config.DEFAULT_LOCALE,
    "hotspot": config.DEFAULT_HOTSPOTS_ONLY,
    "includeProvivsional": config.DEFAULT_PROVISIONAL,
    "maxResults": config.DEFAULT_MAX_OBSERVATIONS,
    "r": config.DEFAULT_MAX_LOCATIONS,
    "rank": config.DEFAULT_RANK,
}


def ebird_auth():
    """Return header with eBird token."""
    ebird_key = os.getenv("EBIRD_KEY")
    header = {"X-eBirdApiToken": ebird_key}
    return header


# TODO: Fix fetch of request parameters
def filter_parameters(params):
    """Filter out any parameter which matches the eBird API default value.

    :param dict params:
        a dict contains the GET parameters for the request that
        will be sent to the eBird API.
    :returns:
        A copy of the params dictionary with only the parameters
        that are not set to a default value.
    :rtype:
        dict
    """
    filtered = {}

    defaults = _ebird_api_defaults.copy()

    for key, value in params.items():
        if key in defaults:
            if value != defaults[key]:
                filtered[key] = value
            else:
                filtered[key] = value

    print("Filtered params:", filtered)
    return filtered


def get_api_response(url, params=None, headers=None):
    """Get response from an API.

    :param str url:
        API URL destination of the request.
    :param dict params:
        parameters used in the API request.
    :param dict headers:
        request headers.
    :return:
        the output/response received from the API.
    :rtype:
        str
    :raises:
        URLError if a connection with the URL occurs.
    :raises:
        HTTPError if the API requests returns an error.
    """
    if params:
        url += "?" + urlencode(params, doseq=True)

    if url.lower().startswith("http") is True:
        if headers:
            response = requests.get(url, params, headers=ebird_auth())
        else:
            response = requests.get(url, params)
    else:
        raise ValueError from None

    return response.text


def get_json(response):
    """Decode the JSON records from the response.

    :param http.client.HTTPResponse response:
        response from the API.
    :return:
        returns a results decoded to json.
    :rtype:
        list
    """
    return json.loads(response)


def api_extract(
    url=None,
    params=None,
    save: bool = False,
    save_fmt: str = config.DEFAULT_SAVE_FORMAT,
    path: str = "./data/temp",
):
    """Get clean API output.

    :param list response:
        Decoded response from the API.
    :param dict params:
        Dictionary with request parameters
    :param bool save:
        Option to save output to a preconfigured location. Default values is false
    :param str path:
        Save path for output if relevant
    :return:
        API response
    """
    headers = ebird_auth()

    filtered = filter_parameters(params)

    if "fmt" in params:
        if params["fmt"] == "csv":
            print("returning csv...")
            api_response = get_api_response(url, filtered, headers)
        else:
            print("returning json...")
            # api_response = get_json(get_api_response(url, filtered, headers))
            api_response = get_api_response(url, filtered, headers)

    api_response = get_api_response(url, filtered, headers)

    if save is True:
        if save_fmt == "json":
            with open(f"{path}.json", "w+") as f:
                json.dump(api_response, f)
        else:
            with open(f"{path}.csv", "w") as f:
                f.write(api_response)

    return api_response
