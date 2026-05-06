import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_microsoft_atp.actions.blacklist import Blacklist
from komand_microsoft_atp.actions.blacklist.schema import Input, Output
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


class TestBlacklist(TestCase):
    @classmethod
    @patch("requests.request", side_effect=mock_request_200)
    def setUpClass(cls, mock_get: Mock) -> None:
        cls.action = Util.default_connector(Blacklist())

    @patch("requests.request", side_effect=mock_request_200)
    def test_blacklist_create_indicator(self, mock_get: Mock) -> None:
        response = self.action.run(
            {
                Input.INDICATOR: "220e7d15b011d7fac48f2bd61114db1022197f7f",
                Input.INDICATOR_STATE: True,
                Input.ACTION: "AlertAndBlock",
                Input.SEVERITY: "High",
            }
        )
        self.assertIn(Output.INDICATOR_ACTION_RESPONSE, response)
        self.assertEqual(response[Output.INDICATOR_ACTION_RESPONSE]["indicatorType"], "FileSha1")
        self.assertEqual(response[Output.INDICATOR_ACTION_RESPONSE]["action"], "AlertAndBlock")

    @patch("requests.request", side_effect=mock_request_200)
    def test_blacklist_delete_indicator(self, mock_get: Mock) -> None:
        response = self.action.run(
            {
                Input.INDICATOR: "220e7d15b011d7fac48f2bd61114db1022197f7f",
                Input.INDICATOR_STATE: False,
            }
        )
        self.assertIn(Output.INDICATOR_ACTION_RESPONSE, response)

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_blacklist_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run(
                {
                    Input.INDICATOR: "220e7d15b011d7fac48f2bd61114db1022197f7f",
                    Input.INDICATOR_STATE: True,
                    Input.ACTION: "AlertAndBlock",
                    Input.SEVERITY: "High",
                }
            )
        self.assertEqual(context.exception.cause, exception)
