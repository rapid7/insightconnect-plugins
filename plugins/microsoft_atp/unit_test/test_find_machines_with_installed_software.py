import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_microsoft_atp.actions.find_machines_with_installed_software import FindMachinesWithInstalledSoftware
from komand_microsoft_atp.actions.find_machines_with_installed_software.schema import Input, Output
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


class TestFindMachinesWithInstalledSoftware(TestCase):
    @classmethod
    @patch("requests.request", side_effect=mock_request_200)
    def setUpClass(cls, mock_get: Mock) -> None:
        cls.action = Util.default_connector(FindMachinesWithInstalledSoftware())

    @patch("requests.request", side_effect=mock_request_200)
    def test_find_machines_with_installed_software(self, mock_get: Mock) -> None:
        response = self.action.run({Input.SOFTWARE: "microsoft-_-windows_10"})
        self.assertIn(Output.MACHINES, response)
        self.assertEqual(len(response[Output.MACHINES]), 2)
        self.assertEqual(response[Output.MACHINES][0]["id"], "abc123")
        self.assertEqual(response[Output.MACHINES][1]["computerDnsName"], "desktop-02")

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_500, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_find_machines_with_installed_software_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run({Input.SOFTWARE: "microsoft-_-windows_10"})
        self.assertEqual(context.exception.cause, exception)
