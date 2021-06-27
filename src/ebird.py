"""Module to interact with EBird API."""
import requests


def get_hotspots(lat: float, lon: float, fmt: str):
    """Retreive HotStop info for Lat/Lon coordinates."""
    parameters = {"lat": lat, "lng": lon, "fmt": fmt}

    response = requests.get(
        "https://api.ebird.org/v2/ref/hotspot/geo?", params=parameters
    )
    return response.json()
