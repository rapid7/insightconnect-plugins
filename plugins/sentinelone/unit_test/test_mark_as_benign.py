import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from komand_sentinelone.actions.mark_as_benign import MarkAsBenign
from komand_sentinelone.actions.mark_as_benign.schema import Input

from util import Util


class TestMarkAsBenign(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(MarkAsBenign())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_with_target_scope(self, mock_request):
        expected = {"affected": 1}
        for test in ["group", "site", "tenant"]:
            with self.subTest(f"Running agent with action: {test}"):
                actual = self.action.run({Input.THREAT_ID: "1000000000000000000", Input.TARGET_SCOPE: test})
                self.assertEqual(expected, actual)
