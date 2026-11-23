import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from icon_vpndetection.actions.lookup_ip import LookupIp
from util import API_KEY, Util


@patch("requests.request", side_effect=Util.mock_request)
class TestLookupIp(TestCase):
    @parameterized.expand(
        [
            ["tor_exit_keyless", "", "185.220.101.1", "expected/lookup_keyless.json.exp"],
            ["vpn_keyed", API_KEY, "188.42.45.201", "expected/lookup_keyed.json.exp"],
            ["bogon", "", "10.0.0.1", "expected/lookup_bogon.json.exp"],
            ["address_with_spaces", "", " 185.220.101.1 ", "expected/lookup_keyless.json.exp"],
        ]
    )
    def test_lookup_ip(self, mock_request: Mock, _name: str, api_key: str, address: str, expected: str) -> None:
        action = Util.default_connector(LookupIp(), api_key)
        actual = action.run({"address": address})
        self.assertEqual(Util.read_file_to_dict(expected), actual)
        validate(actual, action.output.schema)

    def test_key_sent_as_bearer_header_not_in_url(self, mock_request: Mock) -> None:
        Util.default_connector(LookupIp(), API_KEY).run({"address": "188.42.45.201"})
        args, kwargs = mock_request.call_args
        self.assertEqual(f"Bearer {API_KEY}", kwargs["headers"]["Authorization"])
        self.assertEqual("https://api.vpndetection.io/188.42.45.201", args[1])

    def test_no_key_sends_no_authorization(self, mock_request: Mock) -> None:
        Util.default_connector(LookupIp()).run({"address": "185.220.101.1"})
        _, kwargs = mock_request.call_args
        self.assertNotIn("Authorization", kwargs["headers"])

    def test_keyless_answer_is_partial(self, mock_request: Mock) -> None:
        actual = Util.default_connector(LookupIp()).run({"address": "185.220.101.1"})
        self.assertTrue(actual["partial"])
        self.assertTrue(actual["is_tor"])
        self.assertNotIn("is_hosting", actual)

    @parameterized.expand(
        [
            ["invalid_address", "", "not-an-ip", "'not-an-ip' is not a valid IP address."],
            ["invalid_key", "wrong-key", "185.220.101.1", PluginException.causes[PluginException.Preset.API_KEY]],
            ["rate_limited", "", "198.51.100.7", PluginException.causes[PluginException.Preset.RATE_LIMIT]],
            ["server_error", "", "198.51.100.8", PluginException.causes[PluginException.Preset.SERVER_ERROR]],
            ["not_json", "", "198.51.100.9", PluginException.causes[PluginException.Preset.INVALID_JSON]],
        ]
    )
    def test_lookup_ip_error(self, mock_request: Mock, _name: str, api_key: str, address: str, cause: str) -> None:
        action = Util.default_connector(LookupIp(), api_key)
        with self.assertRaises(PluginException) as context:
            action.run({"address": address})
        self.assertEqual(cause, context.exception.cause)

    def test_invalid_address_makes_no_request(self, mock_request: Mock) -> None:
        with self.assertRaises(PluginException):
            Util.default_connector(LookupIp()).run({"address": "999.1.1.1"})
        mock_request.assert_not_called()
