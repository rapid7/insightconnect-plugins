import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_microsoft_atp.actions.search_machines import SearchMachines
from komand_microsoft_atp.actions.search_machines.schema import Input, Output
from parameterized import parameterized

from util import (
    Util,
    mock_request_200,
    mock_request_201_invalid_json,
    mock_request_401,
    mock_request_403,
    mock_request_404,
    mock_request_500,
    mocked_request,
)


class TestSearchMachines(TestCase):
    @classmethod
    @patch("requests.request", side_effect=mock_request_200)
    def setUpClass(cls, mock_get: Mock) -> None:
        cls.action = Util.default_connector(SearchMachines())

    @patch("requests.request", side_effect=mock_request_200)
    def test_search_machines_with_results(self, mock_get: Mock) -> None:
        response = self.action.run({Input.FILTER: "osPlatform eq 'Windows10'", Input.LIMIT: 50})
        self.assertEqual(len(response[Output.MACHINES]), 2)
        self.assertEqual(response[Output.MACHINES][0]["id"], "abc123def456")
        self.assertEqual(response[Output.MACHINES][0]["osPlatform"], "Windows10")
        self.assertEqual(response[Output.MACHINES][1]["id"], "def789ghi012")

    @patch("requests.request", side_effect=mock_request_200)
    def test_search_machines_empty_results(self, mock_get: Mock) -> None:
        response = self.action.run({Input.FILTER: "noResults eq 'true'"})
        self.assertEqual(response[Output.MACHINES], [])

    @patch("requests.request", side_effect=mock_request_200)
    def test_search_machines_default_limit(self, mock_get: Mock) -> None:
        response = self.action.run({Input.FILTER: "osPlatform eq 'Windows10'"})
        self.assertIsInstance(response[Output.MACHINES], list)

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_search_machines_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run({Input.FILTER: "osPlatform eq 'Windows10'"})
        self.assertEqual(
            context.exception.cause,
            exception,
        )
