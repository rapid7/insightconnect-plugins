import logging
from unittest import TestCase, mock

from icon_greynoise.actions.similar_lookup import SimilarLookup

from unit_test.util import MockConnection, mocked_requests_get


class TestSimilarLookup(TestCase):
    @mock.patch("greynoise.GreyNoise.similar", side_effect=mocked_requests_get)
    def test_similar_lookup(self, mock_get):
        log = logging.getLogger("Test")
        test_similar = SimilarLookup()
        test_similar.connection = MockConnection()
        test_similar.logger = log

        working_params = {"ip_address": "similar_lookup"}
        results = test_similar.run(working_params)
        expected = {
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

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)
