import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_greynoise.connection.connection import Connection
from icon_greynoise.actions.quick_lookup import QuickLookup
from greynoise import GreyNoise
import json
import logging


def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


def mocked_requests_get(*args, **kwargs):
    actual_path = os.path.dirname(os.path.realpath(__file__))
    actual_joined_path = os.path.join(actual_path, "payloads/quick_ip.json")
    get_messages_from_user_payload = read_file_to_string(actual_joined_path)
    return json.loads(get_messages_from_user_payload)


class MockConnection:
    def __init__(self):
        self.server = "test_server"
        self.api_key = "test_api_key"
        self.user_agent = "test_user_agent"
        self.gn_client = GreyNoise(api_key=self.api_key, api_server=self.server, integration_name=self.user_agent)


class TestQuickLookup(TestCase):
    @mock.patch("greynoise.GreyNoise.quick", side_effect=mocked_requests_get)
    def test_quick_lookup(self, mock_get):
        log = logging.getLogger("Test")
        test_quick = QuickLookup()
        test_quick.connection = MockConnection()
        test_quick.logger = log

        working_params = {"ip_address": "1.2.3.4"}
        results = test_quick.run(working_params)
        expected = {
            "code": "0x01",
            "ip": "1.2.3.4",
            "code_message": "IP has been observed by the GreyNoise sensor network",
            "noise": True,
            "riot": False,
        }

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)
