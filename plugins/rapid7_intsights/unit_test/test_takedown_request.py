import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from util import Util
from icon_rapid7_intsights.actions.takedown_request import TakedownRequest
from icon_rapid7_intsights.actions.takedown_request.schema import (
    Input,
    Output,
    TakedownRequestInput,
    TakedownRequestOutput,
)
from jsonschema import validate
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mock_request)
class TestTakedownRequest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(TakedownRequest())

    def test_takedown_request_valid(self, mock_request):
        input_params = {Input.ALERT_ID: "valid_id", Input.TARGET: "Domain"}
        validate(input_params, TakedownRequestInput.schema)
        actual = self.action.run(input_params)
        expected = {Output.STATUS: True}
        self.assertEqual(expected, actual)
        validate(actual, TakedownRequestOutput.schema)

    def test_takedown_request_invalid_400(self, mock_request):
        input_params = {Input.ALERT_ID: "invalid_id_400", Input.TARGET: "Domain"}
        validate(input_params, TakedownRequestInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, "The status for the alert was not changed by this request")
        self.assertEqual(error.exception.assistance, "This alert may already be in the process of a takedown request")
        self.assertEqual(error.exception.data, "StatusNotChanged")

    def test_takedown_request_invalid_403(self, mock_request):
        input_params = {Input.ALERT_ID: "invalid_id_403", Input.TARGET: "Domain"}
        validate(input_params, TakedownRequestInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, "A takedown cannot be made to this alert")
        self.assertEqual(error.exception.assistance, "Please ensure that a takedown request is allowed for this alert")
        self.assertEqual(error.exception.data, "CantRequestTakedownForAlert")
