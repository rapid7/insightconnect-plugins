import json
import logging
import os
from unittest import TestCase, mock

from icon_greynoise.actions.timeline_lookup import TimelineLookup

from util import MockConnection, read_file_to_string


def timeline_response(*_args, **_kwargs):
    return json.loads(read_file_to_string(os.path.join(os.path.dirname(__file__), "payloads/timeline_ip.json")))


class TestTimelineLookup(TestCase):
    @mock.patch("greynoise.GreyNoise.timelinedaily", side_effect=timeline_response)
    def test_timeline_lookup(self, mock_get):
        log = logging.getLogger("Test")
        test_timeline = TimelineLookup()
        test_timeline.connection = MockConnection()
        test_timeline.logger = log

        working_params = {"ip_address": "100.29.192.92", "days": 1}
        results = test_timeline.run(working_params)
        expected = timeline_response()
        expected["ip"] = expected["metadata"]["ip"]

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)
        self.assertEqual(mock_get.call_args.args[0], "100.29.192.92")
        self.assertEqual(mock_get.call_args.kwargs["days"], 1)
