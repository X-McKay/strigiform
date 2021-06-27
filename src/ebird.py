"""Module to interact with EBird API."""
import requests


def get_hotspots(lat: float, lon: float, fmt: str):
    """Retreive HotStop info for Lat/Lon coordinates."""
    parameters = {"lat": lat, "lng": lon, "fmt": fmt}

    response = requests.get(
        f"https://api.ebird.org/v2/ref/hotspot/geo?", params=parameters
    )
    return response.json()


# curl --location --request GET 'https://api.ebird.org/v2/ref/taxonomy/ebird?species=thagul,kumgul1' \
# --header 'X-eBirdApiToken: {{x-ebirdapitoken}}'

locations = []
for result in data:
    locations.append(str(result["locName"]))
