import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_microsoft_atp.actions.update_alert import UpdateAlert
from komand_microsoft_atp.actions.update_alert.schema import Input, Output
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


class TestUpdateAlert(TestCase):
    @classmethod
    @patch("requests.request", side_effect=mock_request_200)
    def setUpClass(cls, mock_get: Mock) -> None:
        cls.action = Util.default_connector(UpdateAlert())

    @patch("requests.request", side_effect=mock_request_200)
    def test_update_alert(self, mock_get: Mock) -> None:
        response = self.action.run(
            {
                Input.ALERT_ID: "da637292082891366787_322129023",
                Input.ALERT_FIELDS: {"status": "Resolved", "classification": "FalsePositive"},
            }
        )
        self.assertIn(Output.ALERT, response)
        self.assertEqual(response[Output.ALERT]["id"], "da637292082891366787_322129023")
        self.assertEqual(response[Output.ALERT]["status"], "Resolved")
        self.assertEqual(response[Output.ALERT]["classification"], "FalsePositive")

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_update_alert_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run(
                {
                    Input.ALERT_ID: "da637292082891366787_322129023",
                    Input.ALERT_FIELDS: {"status": "Resolved"},
                }
            )
        self.assertEqual(context.exception.cause, exception)
