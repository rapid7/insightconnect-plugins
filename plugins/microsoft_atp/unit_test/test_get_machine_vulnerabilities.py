import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_microsoft_atp.actions.get_machine_vulnerabilities import GetMachineVulnerabilities
from komand_microsoft_atp.actions.get_machine_vulnerabilities.schema import Input, Output
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


class TestGetMachineVulnerabilities(TestCase):
    @classmethod
    @patch("requests.request", side_effect=mock_request_200)
    def setUpClass(cls, mock_get: Mock) -> None:
        cls.action = Util.default_connector(GetMachineVulnerabilities())

    @patch("requests.request", side_effect=mock_request_200)
    def test_get_machine_vulnerabilities(self, mock_get: Mock) -> None:
        response = self.action.run({Input.MACHINE: "my-hostname"})
        self.assertIn(Output.VULNERABILITIES, response)
        self.assertEqual(len(response[Output.VULNERABILITIES]), 1)
        self.assertEqual(response[Output.VULNERABILITIES][0]["id"], "CVE-2021-12345")
        self.assertEqual(response[Output.VULNERABILITIES][0]["severity"], "High")

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_get_machine_vulnerabilities_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run({Input.MACHINE: "my-hostname"})
        self.assertEqual(context.exception.cause, exception)
