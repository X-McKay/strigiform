"""Test cases for the ebird module."""
import unittest
from unittest.mock import patch

import pytest

from ibyrd.service import ebird


@pytest.fixture
class TestEbirdService(unittest.TestCase):
    """Test Cases to validate API calls to Ebird."""

    @patch("ibyrd.service.ebird.get_hotspots.request")
    def test_get_hotspots_invalid_coord(self) -> None:
        """Test hotspot functionality."""
        response = ebird.get_hotspots(91, 181, fmt="json")
        self.assertEqual(response.status_code, 400)
