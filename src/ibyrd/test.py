"""Unit tests."""
import requests

import ebird

test = ebird.get_hotspots(40.71, -73.95, fmt="json")
print(test)
