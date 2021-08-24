"""Test cases for the ebird module."""
import pytest

from ibyrd.service import ebird


@pytest.fixture
def test_get_hotspots_invalid_coord() -> None:
    """Test hotspot functionality."""
    response = ebird.get_hotspots(91, 181, fmt="json")
    assert response.status_code == 400


def test_get_hotspots_valid_coord() -> None:
    """Test hotspot functionality."""
    response = ebird.get_hotspots(47.60, -122.33, fmt="json")
    assert response.status_code == 200


# @pytest.fixture
# class TestEbirdService(unittest.TestCase):
#     """Test Cases to validate API calls to Ebird."""

#     @patch("ibyrd.service.ebird.get_hotspots.request")
#     def test_get_hotspots_invalid_coord(self) -> None:
#         """Test hotspot functionality."""
#         response = ebird.get_hotspots(91, 181, fmt="json")
#         self.assertEqual(response.status_code, 400)
