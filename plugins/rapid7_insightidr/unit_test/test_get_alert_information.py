import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_insightidr.actions.get_alert_information import GetAlertInformation
from komand_rapid7_insightidr.actions.get_alert_information.schema import (
    GetAlertInformationInput,
    GetAlertInformationOutput,
    Input,
)
from parameterized import parameterized

from util import Util


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestGetAlertInformation(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAlertInformation())

    @parameterized.expand(Util.load_parameters("get_alert_information").get("parameters"))
    def test_get_alert_information(self, mock_request: MagicMock, alert_rrn: str, expected: dict) -> None:
        test_input = {Input.ALERT_RRN: alert_rrn}
        validate(test_input, GetAlertInformationInput.schema)
        actual = self.action.run(test_input)
        self.assertCountEqual(actual, expected)
        validate(actual, GetAlertInformationOutput.schema)

    @parameterized.expand(Util.load_parameters("get_alert_information_not_found").get("parameters"))
    def test_get_alert_information_bad(
        self, mock_request: MagicMock, alert_rrn: str, cause: str, assistance: str
    ) -> None:
        test_input = {Input.ALERT_RRN: alert_rrn}
        validate(test_input, GetAlertInformationInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
