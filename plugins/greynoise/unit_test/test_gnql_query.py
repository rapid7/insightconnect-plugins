import logging
from unittest import TestCase, mock

from icon_greynoise.actions.gnql_query import GnqlQuery

from util import MockConnection, mocked_requests_get


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
            "data": [
                {
                    "ip": "1.2.3.4",
                    "internet_scanner_intelligence": {
                        "found": True,
                        "classification": "benign",
                        "actor": "Acme Inc",
                    },
                    "business_service_intelligence": {"found": False, "trust_level": ""},
                }
            ],
            "request_metadata": {
                "complete": True,
                "count": 1,
                "message": "ok",
                "query": "query",
                "adjusted_query": "query",
                "scroll": "token",
                "restricted_fields": [],
            },
        }

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)
