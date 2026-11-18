import json
import logging
import os
from unittest import TestCase, mock

from icon_greynoise.actions.community_lookup import CommunityLookup

from util import MockConnection, read_file_to_string


def community_response(*_args, **_kwargs):
    return json.loads(read_file_to_string(os.path.join(os.path.dirname(__file__), "payloads/community_ip.json")))


class TestCommunityLookup(TestCase):
    @mock.patch("greynoise.GreyNoise.request", side_effect=community_response)
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
        self.assertEqual(mock_get.call_args.args[0], "v3/community/1.2.3.4")
