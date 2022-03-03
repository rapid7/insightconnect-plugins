import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.agents_summary import AgentsSummary
from komand_sentinelone.actions.agents_summary.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unittest import TestCase


class TestAgentsSummary(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(AgentsSummary())
        Util.mock_response_params = {}

    def setUp(self) -> None:
        self.action.connection.api_version = "2.1"

    def test_should_fail_when_wrong_api_version(self):
        self.action.connection.api_version = "2.0"
        with self.assertRaises(PluginException) as error:
            self.action.run()

        self.assertEqual(error.exception.cause, "Endpoint not found.")
        self.assertEqual(
            error.exception.assistance,
            "This action is not supported in SentinelOne API v2.0. Verify that your SentinelOne console supports SentinelOne API v2.1 and try again.",
        )

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_when_no_inputs(self, mock_request):
        expected = {"decommissioned": 1, "infected": 1, "online": 1, "out_of_date": 1, "total": 1, "up_to_date": 1}
        actual = self.action.run()
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_when_site_ids_input(self, mock_request):
        expected = {"decommissioned": 1, "infected": 1, "online": 1, "out_of_date": 1, "total": 1, "up_to_date": 1}
        actual = self.action.run({Input.SITE_IDS: ["500000000001"]})
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_when_account_ids_inputs(self, mock_request):
        expected = {"decommissioned": 1, "infected": 1, "online": 1, "out_of_date": 1, "total": 1, "up_to_date": 1}
        actual = self.action.run({Input.ACCOUNT_IDS: ["500000000001"]})
        self.assertEqual(expected, actual)
