import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import Mock, patch

from komand_sentinelone.actions.quarantine import Quarantine
from komand_sentinelone.actions.quarantine.schema import Input

from util import Util


class TestQuarantine(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request: Mock) -> None:
        cls.action = Util.default_connector(Quarantine())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    @patch("requests.get", side_effect=Util.mocked_requests_get)
    def test_should_success(self, mock_request: Mock, mock_get: Mock) -> None:
        expected = {"response": {"data": {"affected": 1}}}
        actual = self.action.run({Input.AGENT: "hostname123", Input.CASE_SENSITIVE: True, Input.QUARANTINE_STATE: True})
        self.assertEqual(expected, actual)
