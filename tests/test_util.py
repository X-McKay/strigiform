"""Test cases for the config module."""
import os
import unittest

import mock

from strigiform.util import api
from strigiform.util import config


class TestApiUtil(unittest.TestCase):
    """Class for testing api utilities."""

    def _mock_response(
        self,
        status=200,
        content="CONTENT",
        json_data=None,
        text="TEXT",
        raise_for_status=None,
    ):
        """Helper function for mock responses."""
        mock_resp = mock.Mock()
        # mock raise_for_status call w/optional error
        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        # set status code and content
        mock_resp.status_code = status
        mock_resp.content = content
        mock_resp.text = text
        # add json data if provided
        if json_data:
            mock_resp.json = mock.Mock(return_value=json_data)
        return mock_resp

    @mock.patch("requests.get")
    def test_api_response(self, mock_get):
        """Test generic api response function."""
        mock_resp = self._mock_response(text="Passerformes")
        mock_get.return_value = mock_resp
        result = api.get_api_response(url="https://www.fakeurl.com")
        self.assertEqual(result, "Passerformes")


def test_ebird_auth():
    """Testing api key extraction."""
    os.environ["EBIRD_KEY"] = "123ABC"
    auth_response = api.ebird_auth()
    assert auth_response["X-eBirdApiToken"] == "123ABC"


def test_postgres_config():
    """Test extraction of db params."""
    postgres_params = config.db_config(filename="./tests/mock_database.ini")
    assert type(postgres_params) == dict


def test_postgres_engine_str():
    """Test generation of sqlalchemy engine string."""
    connenction_string = config.db_engine_str(filename="./tests/mock_database.ini")
    assert type(connenction_string) == str
