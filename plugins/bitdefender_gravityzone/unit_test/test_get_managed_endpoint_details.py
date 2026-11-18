import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_bitdefender_gravityzone.actions.get_managed_endpoint_details import GetManagedEndpointDetails
from icon_bitdefender_gravityzone.actions.get_managed_endpoint_details.schema import Input, Output
from util import NETWORK_URL, Util


@patch("requests.Session.send")
class TestGetManagedEndpointDetails(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetManagedEndpointDetails())

    def test_returns_endpoint_details(self, mock_send):
        mock_send.return_value = Util.payload_response("get_managed_endpoint_details.json.resp")

        result = self.action.run(
            {
                Input.ENDPOINT_ID: " 5a4f2c3b6e9d1a0012345678 ",
                Input.INCLUDE_SCAN_LOGS: True,
                Input.INCLUDE_LAST_LOGGED_USERS: False,
            }
        )

        self.action.output.validate(result)
        expected = Util.read_file_to_dict("get_managed_endpoint_details.json.resp")["result"]
        self.assertEqual({Output.ENDPOINT_DETAILS: expected}, result)
        payload = Util.sent_payload(mock_send)
        self.assertEqual(NETWORK_URL, Util.sent_request(mock_send).url)
        self.assertEqual("getManagedEndpointDetails", payload["method"])
        self.assertEqual(
            {
                "endpointId": "5a4f2c3b6e9d1a0012345678",
                "options": {"includeScanLogs": True, "includeLastLoggedUsers": False},
            },
            payload["params"],
        )

    def test_options_default_to_false(self, mock_send):
        mock_send.return_value = Util.payload_response("get_managed_endpoint_details.json.resp")

        self.action.run({Input.ENDPOINT_ID: "5a4f2c3b6e9d1a0012345678"})

        self.assertEqual(
            {"includeScanLogs": False, "includeLastLoggedUsers": False},
            Util.sent_payload(mock_send)["params"]["options"],
        )

    def test_empty_result(self, mock_send):
        mock_send.return_value = Util.rpc_result(None)

        result = self.action.run({Input.ENDPOINT_ID: "5a4f2c3b6e9d1a0012345678"})

        self.assertEqual({Output.ENDPOINT_DETAILS: {}}, result)

    def test_unknown_endpoint(self, mock_send):
        mock_send.return_value = Util.rpc_error(-32002, "Resource not found", "The endpoint was not found")

        with self.assertRaises(PluginException) as context:
            self.action.run({Input.ENDPOINT_ID: "5a4f2c3b6e9d1a0012345678"})

        self.assertEqual("GravityZone API error -32002: Resource not found.", context.exception.cause)
        self.assertIn("The endpoint was not found", context.exception.data)

    def test_empty_endpoint_id(self, mock_send):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.ENDPOINT_ID: "  "})

        self.assertEqual("The endpoint ID is empty.", context.exception.cause)
        mock_send.assert_not_called()
