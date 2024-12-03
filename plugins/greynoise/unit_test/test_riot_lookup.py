import logging
from unittest import TestCase, mock

from icon_greynoise.actions.riot_lookup import RiotLookup

from unit_test.util import MockConnection, mocked_requests_get


class TestRiotLookup(TestCase):
    @mock.patch("greynoise.GreyNoise.riot", side_effect=mocked_requests_get)
    def test_riot_lookup(self, mock_get):
        log = logging.getLogger("Test")
        test_riot = RiotLookup()
        test_riot.connection = MockConnection()
        test_riot.logger = log

        working_params = {"ip_address": "riot_lookup"}
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
