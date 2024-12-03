import logging
from unittest import TestCase, mock

from icon_greynoise.actions.community_lookup import CommunityLookup

from unit_test.util import MockConnection, mocked_requests_get


class TestCommunityLookup(TestCase):
    @mock.patch("greynoise.GreyNoise.ip", side_effect=mocked_requests_get)
    def test_community_lookup(self, mock_get):
        log = logging.getLogger("Test")
        test_community = CommunityLookup()
        test_community.connection = MockConnection()
        test_community.logger = log

        working_params = {"ip_address": "community_lookup"}
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
