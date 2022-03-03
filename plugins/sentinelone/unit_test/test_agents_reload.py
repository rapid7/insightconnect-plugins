import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.agents_reload import AgentsReload
from komand_sentinelone.actions.agents_reload.schema import Input
from unit_test.util import Util
from unittest import TestCase


class TestAgentsReload(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(AgentsReload())
        Util.mock_response_params = {}

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_with_filter(self, mock_request):
        expected = {"affected": 1}
        for test in ["monitor", "static", "agent", "log"]:
            with self.subTest(f"Running agent with action: {test}"):
                actual = self.action.run({Input.FILTER: '{"ids": ["1000000000000000000"]}', Input.MODULE: test})
                self.assertEqual(expected, actual)
