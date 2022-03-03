import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.blacklist_by_content_hash import BlacklistByContentHash
from komand_sentinelone.actions.blacklist_by_content_hash.schema import Input
from unit_test.util import Util
from unittest import TestCase


class TestBlacklistByContentHash(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(BlacklistByContentHash())

    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def test_should_success_when_hash(self, mock_request):
        expected = {"affected": 1}
        actual = self.action.run({Input.HASH: "3395856ce81f2b7382dee72602f798b642f14140"})
        self.assertEqual(expected, actual)
