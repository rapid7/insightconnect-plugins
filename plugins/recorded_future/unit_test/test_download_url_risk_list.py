import os
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException


from typing import Any, Dict

from jsonschema import validate
from komand_recorded_future.actions.download_url_risk_list import DownloadUrlRiskList
from komand_recorded_future.connection.schema import Input
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestDownloadURLRiskList(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DownloadUrlRiskList())

    @parameterized.expand(
        [
            [
                Util.read_file_to_dict("inputs/url_risk_list.json.resp"),
                Util.read_file_to_dict("expected/url_risk_list.json.resp"),
            ],
        ]
    )
    def test_download_url_risk_list(
        self, mock_request: MagicMock, input_parameters: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_parameters)
        validate(actual, self.action.output.schema)
        self.assertEqual(expected, actual)
        self.assertFalse(os.path.exists("risk_list.gzip"))

    @parameterized.expand(
        [
            [
                "bad_api_key",
                Util.read_file_to_dict("inputs/url_risk_list.json.resp"),
                PluginException.causes.get(PluginException.Preset.API_KEY),
                PluginException.assistances.get(PluginException.Preset.API_KEY),
            ],
            [
                "unauthorized",
                Util.read_file_to_dict("inputs/url_risk_list.json.resp"),
                PluginException.causes.get(PluginException.Preset.UNAUTHORIZED),
                PluginException.assistances.get(PluginException.Preset.UNAUTHORIZED),
            ],
            [
                "unknown",
                Util.read_file_to_dict("inputs/url_risk_list.json.resp"),
                PluginException.causes.get(PluginException.Preset.UNKNOWN),
                PluginException.assistances.get(PluginException.Preset.UNKNOWN),
            ],
            [
                "server_error",
                Util.read_file_to_dict("inputs/url_risk_list.json.resp"),
                PluginException.causes.get(PluginException.Preset.SERVER_ERROR),
                PluginException.assistances.get(PluginException.Preset.SERVER_ERROR),
            ],
        ]
    )
    def test_download_url_risk_list_raise_exception(
        self, mock_request: MagicMock, token: str, input_parameters: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        action = Util.default_connector(DownloadUrlRiskList(), {Input.API_KEY: {"secretKey": token}})
        with self.assertRaises(PluginException) as error:
            action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
