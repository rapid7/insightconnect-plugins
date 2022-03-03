import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.agents_action import AgentsAction
from komand_sentinelone.actions.agents_action.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unittest import TestCase


class TestAgentsAction(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(AgentsAction())
        Util.mock_response_params = {}

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_with_filter(self, mock_request):
        expected = {"affected": 1}
        for test in [
            "abort-scan",
            "connect",
            "decommission",
            "disconnect",
            "fetch-logs",
            "initiate-scan",
            "restart-machine",
            "shutdown",
            "uninstall",
        ]:
            with self.subTest(f"Running agent with action: {test}"):
                actual = self.action.run({Input.FILTER: '{"ids": ["1000000000000000000"]}', Input.ACTION: test})
                self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_fail_when_wrong_action(self, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.FILTER: '{"ids": ["1000000000000000000"]}', Input.ACTION: "wrong_action"})

        self.assertEqual(error.exception.cause, "API call failed: This is some error text")
        self.assertEqual(error.exception.assistance, "")
