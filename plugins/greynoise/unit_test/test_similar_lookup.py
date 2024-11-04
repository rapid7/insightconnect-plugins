import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_greynoise.connection.connection import Connection
from icon_greynoise.actions.similar_lookup import SimilarLookup
from greynoise import GreyNoise
import json
import logging


def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


def mocked_requests_get(*args, **kwargs):
    actual_path = os.path.dirname(os.path.realpath(__file__))
    actual_joined_path = os.path.join(actual_path, "payloads/similar_ip.json")
    get_messages_from_user_payload = read_file_to_string(actual_joined_path)
    return json.loads(get_messages_from_user_payload)


class MockConnection:
    def __init__(self):
        self.server = "test_server"
        self.api_key = "test_api_key"
        self.user_agent = "test_user_agent"
        self.gn_client = GreyNoise(api_key=self.api_key, api_server=self.server, integration_name=self.user_agent)


class TestSimilarLookup(TestCase):
    @mock.patch("greynoise.GreyNoise.similar", side_effect=mocked_requests_get)
    def test_similar_lookup(self, mock_get):
        log = logging.getLogger("Test")
        test_similar = SimilarLookup()
        test_similar.connection = MockConnection()
        test_similar.logger = log

        working_params = {"ip_address": "1.2.3.4"}
        results = test_similar.run(working_params)
        expected = [
            {
                "ip": {
                    "actor": "Acme Inc",
                    "asn": "AS12345",
                    "city": "Berlin",
                    "classification": "benign",
                    "country": "Germany",
                    "country_code": "DE",
                    "first_seen": "2019-07-29",
                    "ip": "1.2.3.4",
                    "last_seen": "2024-11-04",
                    "organization": "Acme Inc",
                },
                "similar_ips": [
                    {
                        "actor": "Alpha Strike Labs",
                        "asn": "AS12345",
                        "city": "Berlin",
                        "classification": "benign",
                        "country": "Germany",
                        "country_code": "DE",
                        "features": ["hassh_fp", "mass_scan_bool", "os", "ports", "useragents", "web_paths"],
                        "first_seen": "2019-07-11",
                        "ip": "2.3.4.5",
                        "last_seen": "2024-11-04",
                        "organization": "Acme Inc",
                        "score": 0.98933446,
                    }
                ],
                "total": 1,
            }
        ]

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)
