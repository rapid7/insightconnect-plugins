import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from komand_sentinelone.actions.create_ioc_threat import CreateIocThreat
from komand_sentinelone.actions.create_ioc_threat.schema import Input

from util import Util


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
