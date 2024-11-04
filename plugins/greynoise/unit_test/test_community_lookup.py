import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_greynoise.connection.connection import Connection
from icon_greynoise.actions.community_lookup import CommunityLookup
from greynoise import GreyNoise
import json
import logging


def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


def mocked_requests_get(*args, **kwargs):
    actual_path = os.path.dirname(os.path.realpath(__file__))
    actual_joined_path = os.path.join(actual_path, "payloads/community_ip.json")
    get_messages_from_user_payload = read_file_to_string(actual_joined_path)
    return json.loads(get_messages_from_user_payload)


class MockConnection:
    def __init__(self):
        self.server = "test_server"
        self.api_key = "test_api_key"
        self.user_agent = "test_user_agent"


class TestCommunityLookup(TestCase):
    @mock.patch("greynoise.GreyNoise.ip", side_effect=mocked_requests_get)
    def test_community_lookup(self, mock_get):
        log = logging.getLogger("Test")
        test_community = CommunityLookup()
        test_community.connection = MockConnection()
        test_community.logger = log

        working_params = {"ip_address": "1.2.3.4"}
        results = test_community.run(working_params)
        expected = {
            "ip": "1.2.3.4",
            "noise": False,
            "riot": True,
            "classification": "benign",
            "name": "Acme, Inc",
            "link": "https://viz.greynoise.io/ip/1.2.3.4",
            "last_seen": "2020-01-01T00:00:00+00:00",
            "message": "Success",
        }

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)
