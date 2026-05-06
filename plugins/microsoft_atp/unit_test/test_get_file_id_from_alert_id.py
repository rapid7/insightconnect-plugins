import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_microsoft_atp.actions.get_file_id_from_alert_id import GetFileIdFromAlertId
from komand_microsoft_atp.actions.get_file_id_from_alert_id.schema import Input, Output
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


class TestGetFileIdFromAlertId(TestCase):
    @classmethod
    @patch("requests.request", side_effect=mock_request_200)
    def setUpClass(cls, mock_get: Mock) -> None:
        cls.action = Util.default_connector(GetFileIdFromAlertId())

    @patch("requests.request", side_effect=mock_request_200)
    def test_get_file_id_from_alert_id(self, mock_get: Mock) -> None:
        response = self.action.run({Input.ALERT_ID: "da637292082891366787_322129023"})
        self.assertIn(Output.FILE_LIST, response)
        self.assertEqual(len(response[Output.FILE_LIST]), 1)
        self.assertEqual(response[Output.FILE_LIST][0]["sha1"], "abc123sha1")

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_get_file_id_from_alert_id_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run({Input.ALERT_ID: "da637292082891366787_322129023"})
        self.assertEqual(context.exception.cause, exception)
