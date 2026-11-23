import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_bitdefender_gravityzone.actions.isolate_endpoint import IsolateEndpoint
from icon_bitdefender_gravityzone.actions.isolate_endpoint.schema import Input, Output
from util import INCIDENTS_URL, Util

ENDPOINT_ID = "5a4f2c3b6e9d1a0012345678"


@patch("requests.Session.send")
class TestIsolateEndpoint(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(IsolateEndpoint())

    def test_isolate_endpoint(self, mock_send):
        mock_send.return_value = Util.rpc_result(True)

        result = self.action.run({Input.ENDPOINT_ID: f" {ENDPOINT_ID} "})

        self.action.output.validate(result)
        self.assertEqual({Output.SUCCESS: True}, result)
        payload = Util.sent_payload(mock_send)
        self.assertEqual(INCIDENTS_URL, Util.sent_request(mock_send).url)
        self.assertEqual("createIsolateEndpointTask", payload["method"])
        self.assertEqual({"endpointId": ENDPOINT_ID}, payload["params"])

    def test_result_other_than_true_raises(self, mock_send):
        cases = [
            ("false", Util.rpc_result(False), "createIsolateEndpointTask returned false"),
            ("task ID list", Util.rpc_result(["652feab6b9684f3ba80685d5"]), 'returned ["652feab6b9684f3ba80685d5"]'),
            ("string true", Util.rpc_result("true"), 'returned "true"'),
            ("number one", Util.rpc_result(1), "returned 1"),
            ("missing result", Util.response(body={"id": "1", "jsonrpc": "2.0"}), "returned null"),
        ]
        for name, response, expected_data in cases:
            with self.subTest(name):
                mock_send.return_value = response

                with self.assertRaises(PluginException) as context:
                    self.action.run({Input.ENDPOINT_ID: ENDPOINT_ID})

                self.assertEqual(
                    "GravityZone did not confirm that the isolation task was created.", context.exception.cause
                )
                self.assertIn("managed endpoint that supports this action", context.exception.assistance)
                self.assertIn(expected_data, context.exception.data)

    def test_missing_incidents_permission(self, mock_send):
        mock_send.return_value = Util.rpc_error(
            -32001, "Authorization error", "API Key is not allowed to access the selected API: Incidents"
        )

        with self.assertRaises(PluginException) as context:
            self.action.run({Input.ENDPOINT_ID: ENDPOINT_ID})

        self.assertEqual("GravityZone API error -32001: Authorization error.", context.exception.cause)
        self.assertIn("Incidents API", context.exception.assistance)
        self.assertIn("selected API: Incidents", context.exception.data)

    def test_empty_endpoint_id(self, mock_send):
        for endpoint_id in ["", "   ", None]:
            with self.subTest(endpoint_id=endpoint_id):
                with self.assertRaises(PluginException) as context:
                    self.action.run({Input.ENDPOINT_ID: endpoint_id})

                self.assertEqual("The endpoint ID is empty.", context.exception.cause)
        mock_send.assert_not_called()
