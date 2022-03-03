import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.create_ioc_threat import CreateIocThreat
from komand_sentinelone.actions.create_ioc_threat.schema import Input
from unit_test.util import Util
from unittest import TestCase


class TestCreateIocThreat(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(CreateIocThreat())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_when_blacklist(self, mock_request):
        expected = {"affected": 1}
        actual = self.action.run(
            {Input.AGENTID: "1000000000000000000", Input.HASH: "3395856ce81f2b7382dee72602f798b642f14140"}
        )
        self.assertEqual(expected, actual)
