import logging
from unittest import TestCase, mock

from icon_greynoise.actions.gnql_query import GnqlQuery

from .util import MockConnection, mocked_requests_get


class TestGnqlQuery(TestCase):
    @mock.patch("greynoise.GreyNoise.query", side_effect=mocked_requests_get)
    def test_gnql_query(self, mock_get):
        log = logging.getLogger("Test")
        test_gnql = GnqlQuery()
        test_gnql.connection = MockConnection()
        test_gnql.logger = log

        working_params = {"query": "gnql_query"}
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
