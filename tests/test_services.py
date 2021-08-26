"""Test cases for the ebird module."""
import pytest
import requests
from click.testing import CliRunner

from ibyrd.service import ebird


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_get_hotspots_valid_coord(runner: CliRunner) -> None:
    """Test hotspot functionality."""
    function_response = ebird.get_hotspots(47.60, -122.33, fmt="json")

    parameters = {"lat": 47.60, "lng": -122.33, "fmt": "json", "dist": 10, "back": 5}
    response = requests.get(
        "https://api.ebird.org/v2/ref/hotspot/geo?", params=parameters  # type: ignore
    )

    locations = []
    for result in response.json():
        locations.append(str(result["locName"]))

    assert function_response == locations


def test_taxonomy_api_call(runner: CliRunner) -> None:
    """Test API call to get taxonomy from ebird."""
    response = ebird.get_taxonomy()

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200

    # Validate response content type header
    assert response.headers["Content-Type"] == "application/json"


# def test_get_hotspots_invalid_coord(runner: CliRunner) -> None:
#     """Test hotspot functionality."""
#     response = ebird.get_hotspots(91, 181, fmt="json")
#     assert response.status_code == 400

# @pytest.fixture
# class TestEbirdService(unittest.TestCase):
#     """Test Cases to validate API calls to Ebird."""

#     @patch("ibyrd.service.ebird.get_hotspots.request")
#     def test_get_hotspots_invalid_coord(self) -> None:
#         """Test hotspot functionality."""
#         response = ebird.get_hotspots(91, 181, fmt="json")
#         self.assertEqual(response.status_code, 400)
