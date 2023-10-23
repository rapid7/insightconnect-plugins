import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_pagerduty.actions.send_acknowledge_event import SendAcknowledgeEvent
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.Session.request", side_effect=Util.mock_request)
class TestSendAcknowledgeEvent(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SendAcknowledgeEvent())

    @parameterized.expand(
        [
            [
                "test_acknowledge_valid",
                {"incident_id": "valid_id", "email": "test@example.com"},
                Util.read_file_to_dict("expected/test_acknowledge_valid.json.exp"),
            ]
        ]
    )
    def test_send_acknowledge_event(self, _mock_request: MagicMock, _test_name: str, input_params: dict, expected: dict):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "api_error_invalid",
                {"incident_id": "invalid_id", "email": "test@example.com"},
                "Invalid or unreachable endpoint provided.",
                "Verify the URLs or endpoints in your configuration are correct.",
            ]
        ]
    )
    def test_api_error_invalid(
        self, _mock_request: MagicMock, _test_name: str, input_params: dict, cause: str, assistance: str
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
