import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.mark_as_threat import MarkAsThreat
from komand_sentinelone.actions.mark_as_threat.schema import Input
from unit_test.util import Util
from unittest import TestCase


class TestMarkAsThreat(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(MarkAsThreat())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_with_target_scope(self, mock_request):
        expected = {"affected": 1}
        for test in ["group", "site", "tenant"]:
            with self.subTest(f"Running agent with action: {test}"):
                actual = self.action.run({Input.THREAT_ID: "1000000000000000000", Input.TARGET_SCOPE: test})
                self.assertEqual(expected, actual)
