import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from util import Util
from icon_rapid7_intsights.actions.get_indicator_by_value.action import GetIndicatorByValue
from icon_rapid7_intsights.connection.schema import Input, ConnectionSchema
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from jsonschema import validate


class TestConnection(TestCase):
    @patch("requests.request", side_effect=Util.mock_request)
    def test_connection_should_success_when_good_credentials(self, mock_request) -> None:
        action = Util.default_connector(GetIndicatorByValue())
        self.assertEqual(action.connection.test(), {"success": True})

    @patch("requests.request", side_effect=Util.mock_request)
    def test_connection_should_success_when_credentials(self, mock_request) -> None:
        input_params = {Input.API_KEY: {"secretKey": "api_key"}, Input.ACCOUNT_ID: "account_id"}
        validate(input_params, ConnectionSchema.schema)
        action = Util.default_connector(
            GetIndicatorByValue(),
            input_params,
        )

        self.assertEqual("https://api.intsights.com", action.connection.client.url)
        self.assertEqual("api_key", action.connection.client.api_key)
        self.assertEqual("account_id", action.connection.client.account_id)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_connection_should_fail_when_wrong_credentials(self, mock_request) -> None:
        input_params = {Input.API_KEY: {"secretKey": "wrong"}, Input.ACCOUNT_ID: "wrong"}
        validate(input_params, ConnectionSchema.schema)
        action = Util.default_connector(GetIndicatorByValue(), input_params)
        with self.assertRaises(ConnectionTestException) as error:
            action.connection.test()

        self.assertEqual("Invalid API key provided.", error.exception.cause)
        self.assertEqual("Verify your API key configured in your connection is correct.", error.exception.assistance)
