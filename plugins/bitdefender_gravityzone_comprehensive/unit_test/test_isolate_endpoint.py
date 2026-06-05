import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_bitdefender_gravityzone_comprehensive.actions.isolate_endpoint import IsolateEndpoint
from komand_bitdefender_gravityzone_comprehensive.actions.isolate_endpoint.schema import Input
from util import Util


class TestIsolateEndpoint(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(IsolateEndpoint())

    @patch("requests.Session.post", side_effect=Util.mocked_requests)
    def test_isolate_endpoint_success(self, mock_post):
        """Test successful endpoint isolation."""
        test_input = {
            Input.ENDPOINT_ID: "5a4f2c3b6e9d1a0012345678",
        }
        result = self.action.run(test_input)

        self.assertTrue(result["success"])

    @patch("requests.Session.post", side_effect=Util.mocked_requests)
    def test_isolate_endpoint_invalid_id(self, mock_post):
        """Test isolation with an invalid endpoint ID raises PluginException."""
        test_input = {
            Input.ENDPOINT_ID: "invalid_endpoint_id_000000",
        }
        with self.assertRaises(PluginException) as context:
            self.action.run(test_input)

        self.assertIn("Endpoint not found", str(context.exception.cause))

    def test_isolate_endpoint_empty_id(self):
        """Test isolation with empty endpoint ID raises PluginException."""
        test_input = {
            Input.ENDPOINT_ID: "",
        }
        with self.assertRaises(PluginException) as context:
            self.action.run(test_input)

        self.assertIn("Missing required input", str(context.exception.cause))

    def test_isolate_endpoint_whitespace_id(self):
        """Test isolation with whitespace-only endpoint ID raises PluginException."""
        test_input = {
            Input.ENDPOINT_ID: "   ",
        }
        with self.assertRaises(PluginException) as context:
            self.action.run(test_input)

        self.assertIn("Missing required input", str(context.exception.cause))
