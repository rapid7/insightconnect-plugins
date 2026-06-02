import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_microsoft_atp.actions.get_related_machines import GetRelatedMachines
from komand_microsoft_atp.actions.get_related_machines.schema import Input, Output
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


class TestGetRelatedMachines(TestCase):
    @classmethod
    @patch("requests.request", side_effect=mock_request_200)
    def setUpClass(cls, mock_get: Mock) -> None:
        cls.action = Util.default_connector(GetRelatedMachines())

    @patch("requests.request", side_effect=mock_request_200)
    def test_get_related_machines_domain(self, mock_get: Mock) -> None:
        response = self.action.run({Input.INDICATOR: "example.com"})
        self.assertIn(Output.MACHINES, response)
        self.assertEqual(len(response[Output.MACHINES]), 2)
        self.assertEqual(response[Output.MACHINES][0]["id"], "related-machine-1")

    @patch("requests.request", side_effect=mock_request_200)
    def test_get_related_machines_sha1(self, mock_get: Mock) -> None:
        response = self.action.run({Input.INDICATOR: "da39a3ee5e6b4b0d3255bfef95601890afd80709"})
        self.assertIn(Output.MACHINES, response)
        self.assertEqual(len(response[Output.MACHINES]), 2)

    @patch("requests.request", side_effect=mock_request_200)
    def test_get_related_machines_user(self, mock_get: Mock) -> None:
        response = self.action.run({Input.INDICATOR: "DOMAIN\\username"})
        self.assertIn(Output.MACHINES, response)
        self.assertEqual(len(response[Output.MACHINES]), 2)

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_get_related_machines_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run({Input.INDICATOR: "example.com"})
        self.assertEqual(context.exception.cause, exception)
