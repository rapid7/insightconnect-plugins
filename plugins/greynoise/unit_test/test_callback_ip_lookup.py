import json
import logging
import os
from unittest import TestCase, mock

from icon_greynoise.actions.callback_ip_lookup import CallbackIpLookup

from util import MockConnection, read_file_to_string


def callback_response(*_args, **_kwargs):
    return json.loads(read_file_to_string(os.path.join(os.path.dirname(__file__), "payloads/callback_ip.json")))


class TestCallbackIpLookup(TestCase):
    @mock.patch("greynoise.GreyNoise.callback_ip", side_effect=callback_response)
    def test_callback_ip_lookup(self, mock_get):
        log = logging.getLogger("Test")
        action = CallbackIpLookup()
        action.connection = MockConnection()
        action.logger = log

        results = action.run({"ip_address": "198.51.100.42", "source_workspace": "GreyNoise"})

        self.assertEqual(callback_response(), results)
        self.assertNotIn("message", results)
        self.assertEqual(mock_get.call_args.args[0], "198.51.100.42")
        self.assertEqual(mock_get.call_args.kwargs["source_workspace"], "GreyNoise")

    @mock.patch("greynoise.GreyNoise.callback_ip", return_value={"ip": "198.51.100.42", "active_files": None})
    def test_callback_ip_lookup_omits_null_arrays(self, _mock_get):
        action = CallbackIpLookup()
        action.connection = MockConnection()
        action.logger = logging.getLogger("Test")

        results = action.run({"ip_address": "198.51.100.42"})

        self.assertEqual({"ip": "198.51.100.42"}, results)
