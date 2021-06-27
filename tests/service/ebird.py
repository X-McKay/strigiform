"""Unit tests."""
import unittest
from unittest.mock import patch

from service import ebird


class TestEbirdService(unittest.TestCase):
    """
    Test Cases to validate API calls to Ebird
    """

    @patch("ibyrd.service.ebird.get_hotspots.request")
    def test_get_hotspots_invalid_coord(self, mock_request):
        response = ebird.get_hotspots(91, 181, fmt="json")
        self.assertEqual(response.status_code, 400)
