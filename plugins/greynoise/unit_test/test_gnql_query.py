import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_greynoise.connection.connection import Connection
from icon_greynoise.actions.gnql_query import GnqlQuery
from greynoise import GreyNoise
import json
import logging


def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


def mocked_requests_get(*args, **kwargs):
    actual_path = os.path.dirname(os.path.realpath(__file__))
    actual_joined_path = os.path.join(actual_path, "payloads/gnql_query.json")
    get_messages_from_user_payload = read_file_to_string(actual_joined_path)
    return json.loads(get_messages_from_user_payload)


class MockConnection:
    def __init__(self):
        self.server = "test_server"
        self.api_key = "test_api_key"
        self.user_agent = "test_user_agent"
        self.gn_client = GreyNoise(api_key=self.api_key, api_server=self.server, integration_name=self.user_agent)


class TestGnqlQuery(TestCase):
    @mock.patch("greynoise.GreyNoise.query", side_effect=mocked_requests_get)
    def test_gnql_query(self, mock_get):
        log = logging.getLogger("Test")
        test_gnql = GnqlQuery()
        test_gnql.connection = MockConnection()
        test_gnql.logger = log

        working_params = {"query": "last_seen:1d"}
        results = test_gnql.run(working_params)
        expected = {
            "complete": True,
            "count": 1,
            "data": [
                {
                    "ip": "1.2.3.4",
                    "first_seen": "2019-07-29",
                    "last_seen": "2024-11-04",
                    "seen": True,
                    "tags": ["Acme Inc"],
                    "actor": "Acme Inc",
                    "spoofable": False,
                    "classification": "benign",
                    "cve": ["CVE-2021-38645"],
                    "bot": False,
                    "vpn": False,
                    "vpn_service": "",
                    "metadata": {
                        "asn": "AS12345",
                        "city": "Berlin",
                        "country": "Germany",
                        "country_code": "DE",
                        "organization": "Acme Inc",
                        "category": "hosting",
                        "tor": False,
                        "rdns": "",
                        "os": "Linux 2.2.x-3.x (barebone)",
                        "sensor_count": 352,
                        "sensor_hits": 799,
                        "region": "Berlin",
                        "destination_countries": ["Australia"],
                        "destination_country_codes": ["AU"],
                        "source_country": "Germany",
                        "source_country_code": "DE",
                    },
                    "raw_data": {
                        "scan": [{"port": 50050, "protocol": "TCP"}],
                        "web": {"paths": ["/favicon.ico"], "useragents": ["Microsoft WinRM Client"]},
                        "ja3": [{"fingerprint": "12345", "port": 22}],
                        "hassh": [{"fingerprint": "12345", "port": 22}],
                    },
                }
            ],
            "message": "ok",
            "query": "query",
            "scroll": "token",
        }

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)
