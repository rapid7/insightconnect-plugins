import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_pagerduty.actions.send_resolve_event import SendResolveEvent
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.Session.request", side_effect=Util.mock_request)
class TestSendResolveEvent(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SendResolveEvent())

    @parameterized.expand(
        [
            [
                "test_resolve_valid",
                {"incident_id": "valid_id", "email": "test@example.com"},
                Util.read_file_to_dict("expected/test_resolve_valid.json.exp"),
            ]
        ]
    )
    def test_send_resolve_event(self, mock_request: MagicMock, test_name: str, input_params: dict, expected: dict):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "api_error_invalid",
                {"incident_id": "invalid_id", "email": "test@example.com"},
                "Invalid or unreachable endpoint provided.",
                "Verify the endpoint/URL/hostname configured in your plugin connection is correct.",
            ]
        ]
    )
    def test_api_error_invalid(
        self, mock_request: MagicMock, test_name: str, input_params: dict, cause: str, assistance: str
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
