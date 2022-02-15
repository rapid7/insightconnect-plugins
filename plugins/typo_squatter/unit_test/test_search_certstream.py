import sys
import os
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from komand_typo_squatter.triggers.search_certstream import SearchCertstream
from komand_typo_squatter.triggers.search_certstream.schema import Input, Output
from unit_test.util import Util

sys.path.append(os.path.abspath("../"))


class MockTrigger:
    actual = None
    message = None

    @staticmethod
    def send(params):
        MockTrigger.actual = params

    @staticmethod
    def listen_for_events(callback, url):
        return callback(MockTrigger.message, "")


@patch("certstream.listen_for_events", side_effect=MockTrigger.listen_for_events)
@patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
class TestSearchCertstream(TestCase):
    @parameterized.expand(Util.load_parameters("search_certstream_parameters").get("parameters"))
    def test_search_certstream(self, mock_send, mock_response, name, query, domain, distance, message, expected):
        action_params = {Input.QUERY: query, Input.DOMAIN: domain, Input.LEVENSHTEIN: distance}
        MockTrigger.message = message
        action = SearchCertstream()
        action.run(action_params)
        self.assertEqual(MockTrigger.actual, expected)
