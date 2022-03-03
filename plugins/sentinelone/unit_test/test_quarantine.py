import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.quarantine import Quarantine
from komand_sentinelone.actions.quarantine.schema import Input
from unit_test.util import Util
from unittest import TestCase


class TestQuarantine(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(Quarantine())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    @patch("requests.get", side_effect=Util.mocked_requests_get)
    def test_should_success(self, mock_request, mock_get):
        expected = {"response": {"data": {"affected": 1}}}
        actual = self.action.run({Input.AGENT: "hostname123", Input.CASE_SENSITIVE: True, Input.QUARANTINE_STATE: True})
        self.assertEqual(expected, actual)
