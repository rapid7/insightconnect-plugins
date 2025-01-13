import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate
from komand_twilio.actions.send_sms import SendSms
from komand_twilio.actions.send_sms.schema import Input, Output
from parameterized import parameterized

from utils import MockResponse, Util

STUB_RESPONSE_FILENAME = "send_sms"


class TestSendSms(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(SendSms())

    @patch(
        "requests.sessions.Session.send", return_value=MockResponse(filename=STUB_RESPONSE_FILENAME, status_code=200)
    )
    def test_send_sms(self, mock_requests: MagicMock) -> None:
        response = self.action.run({Input.TO_NUMBER: "000111222", Input.MESSAGE: "ExampleMessage"})
        expected = {Output.MESSAGE_SID: "ExampleMessageSID"}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
        mock_requests.assert_called()

    @parameterized.expand(
        [
            (400, PluginException.Preset.BAD_REQUEST),
            (401, PluginException.Preset.API_KEY),
            (403, PluginException.Preset.UNAUTHORIZED),
            (404, PluginException.Preset.NOT_FOUND),
            (429, PluginException.Preset.RATE_LIMIT),
            (430, PluginException.Preset.UNKNOWN),
            (500, PluginException.Preset.SERVER_ERROR),
        ]
    )
    @patch("requests.sessions.Session.send")
    def test_send_sms_error(
        self,
        status_code: int,
        preset: str,
        mock_requests: MagicMock,
    ) -> None:
        mock_requests.return_value = MockResponse(filename=STUB_RESPONSE_FILENAME, status_code=status_code)
        with self.assertRaises(PluginException) as context:
            self.action.run({})
        self.assertEqual(context.exception.cause, PluginException.causes[preset])
        self.assertEqual(context.exception.assistance, PluginException.assistances[preset])
        mock_requests.assert_called()
