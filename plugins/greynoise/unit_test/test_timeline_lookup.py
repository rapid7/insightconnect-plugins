import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_greynoise.connection.connection import Connection
from icon_greynoise.actions.timeline_lookup import TimelineLookup
from greynoise import GreyNoise
import json
import logging


def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


def mocked_requests_get(*args, **kwargs):
    actual_path = os.path.dirname(os.path.realpath(__file__))
    actual_joined_path = os.path.join(actual_path, "payloads/timeline_ip.json")
    get_messages_from_user_payload = read_file_to_string(actual_joined_path)
    return json.loads(get_messages_from_user_payload)


class MockConnection:
    def __init__(self):
        self.server = "test_server"
        self.api_key = "test_api_key"
        self.user_agent = "test_user_agent"
        self.gn_client = GreyNoise(api_key=self.api_key, api_server=self.server, integration_name=self.user_agent)


class TestTimelineLookup(TestCase):
    @mock.patch("greynoise.GreyNoise.timelinedaily", side_effect=mocked_requests_get)
    def test_timeline_lookup(self, mock_get):
        log = logging.getLogger("Test")
        test_timeline = TimelineLookup()
        test_timeline.connection = MockConnection()
        test_timeline.logger = log

        working_params = {"ip_address": "1.2.3.4"}
        results = test_timeline.run(working_params)
        expected = [
            {
                "activity": [
                    {
                        "asn": "AS12345",
                        "category": "hosting",
                        "city": "Berlin",
                        "classification": "benign",
                        "country": "Germany",
                        "country_code": "DE",
                        "destinations": [{"country": "South Africa", "country_code": "ZA"}],
                        "hassh_fingerprints": [],
                        "http_paths": ["/favicon.ico"],
                        "http_user_agents": ["Mozilla/5.0"],
                        "ja3_fingerprints": ["04b3f524166caafd433b6864250945be"],
                        "organization": "Alpha Strike Labs GmbH",
                        "protocols": [{"port": 80, "transport_protocol": "TCP"}],
                        "rdns": "",
                        "region": "Berlin",
                        "spoofable": True,
                        "tags": [
                            {
                                "category": "actor",
                                "description": "description.",
                                "intention": "benign",
                                "name": "Acme, Inc.",
                            }
                        ],
                        "timestamp": "2024-11-03T00:00:00Z",
                        "tor": False,
                        "vpn": False,
                        "vpn_service": "",
                    }
                ],
                "ip": "1.2.3.4",
                "metadata": {
                    "end_time": "2024-11-04T19:13:35.892189739Z",
                    "ip": "1.2.3.4",
                    "limit": 50,
                    "next_cursor": "",
                    "start_time": "2024-11-03T00:00:00Z",
                },
            }
        ]

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)
