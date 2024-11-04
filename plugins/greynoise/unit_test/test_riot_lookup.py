import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_greynoise.connection.connection import Connection
from icon_greynoise.actions.riot_lookup import RiotLookup
from greynoise import GreyNoise
import json
import logging


def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


def mocked_requests_get(*args, **kwargs):
    actual_path = os.path.dirname(os.path.realpath(__file__))
    actual_joined_path = os.path.join(actual_path, "payloads/riot_ip.json")
    get_messages_from_user_payload = read_file_to_string(actual_joined_path)
    return json.loads(get_messages_from_user_payload)


class MockConnection:
    def __init__(self):
        self.server = "test_server"
        self.api_key = "test_api_key"
        self.user_agent = "test_user_agent"
        self.gn_client = GreyNoise(api_key=self.api_key, api_server=self.server, integration_name=self.user_agent)


class TestRiotLookup(TestCase):
    @mock.patch("greynoise.GreyNoise.riot", side_effect=mocked_requests_get)
    def test_riot_lookup(self, mock_get):
        log = logging.getLogger("Test")
        test_riot = RiotLookup()
        test_riot.connection = MockConnection()
        test_riot.logger = log

        working_params = {"ip_address": "1.2.3.4"}
        results = test_riot.run(working_params)
        expected = {
            "ip": "1.2.3.4",
            "riot": True,
            "category": "public_dns",
            "name": "Acme Inc",
            "description": "description",
            "explanation": "explanation",
            "last_updated": "2024-11-04T17:10:58Z",
            "reference": "reference",
            "trust_level": "1",
            "viz_url": "https://viz.greynoise.io/ip/1.2.3.4",
        }

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)
