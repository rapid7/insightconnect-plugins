import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from icon_rapid7_intsights.actions.get_indicator_by_value.action import GetIndicatorByValue
from icon_rapid7_intsights.connection.schema import Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class TestConnection(TestCase):
    @patch("requests.request", side_effect=Util.mock_request)
    def test_connection_should_success_when_good_credentials(self, mock_request) -> None:
        action = Util.default_connector(GetIndicatorByValue())
        self.assertEqual(action.connection.test(), {"success": True})

    @patch("requests.request", side_effect=Util.mock_request)
    def test_connection_should_success_when_credentials(self, mock_request) -> None:
        action = Util.default_connector(
            GetIndicatorByValue(),
            {Input.API_KEY: {"secretKey": "api_key"}, Input.ACCOUNT_ID: "account_id"},
        )

        self.assertEqual("https://api.intsights.com", action.connection.client.url)
        self.assertEqual("api_key", action.connection.client.api_key)
        self.assertEqual("account_id", action.connection.client.account_id)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_connection_should_fail_when_wrong_credentials(self, mock_request) -> None:
        action = Util.default_connector(
            GetIndicatorByValue(), {Input.API_KEY: {"secretKey": "wrong"}, Input.ACCOUNT_ID: "wrong"}
        )
        with self.assertRaises(ConnectionTestException) as error:
            action.connection.test()

        self.assertEqual("Invalid username or password provided.", error.exception.cause)
        self.assertEqual("Verify your username and password are correct.", error.exception.assistance)
