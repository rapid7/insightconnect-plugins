import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_sentinelone.actions.agents_summary import AgentsSummary
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestAgentsSummary(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(AgentsSummary())

    def setUp(self) -> None:
        self.action.connection.client.api_version = "2.1"

    @parameterized.expand(
        [
            [
                "site_id",
                Util.read_file_to_dict("inputs/get_agents_summary_site_id.json.inp"),
                Util.read_file_to_dict("expected/get_agents_summary.json.exp"),
            ],
            [
                "site_ids",
                Util.read_file_to_dict("inputs/get_agents_summary_site_ids.json.inp"),
                Util.read_file_to_dict("expected/get_agents_summary.json.exp"),
            ],
            [
                "account_id",
                Util.read_file_to_dict("inputs/get_agents_summary_account_id.json.inp"),
                Util.read_file_to_dict("expected/get_agents_summary.json.exp"),
            ],
            [
                "account_ids",
                Util.read_file_to_dict("inputs/get_agents_summary_account_ids.json.inp"),
                Util.read_file_to_dict("expected/get_agents_summary.json.exp"),
            ],
            [
                "site_and_account_ids",
                Util.read_file_to_dict("inputs/get_agents_summary_site_and_account_ids.json.inp"),
                Util.read_file_to_dict("expected/get_agents_summary.json.exp"),
            ],
            [
                "all",
                Util.read_file_to_dict("inputs/get_agents_summary.json.inp"),
                Util.read_file_to_dict("expected/get_agents_summary.json.exp"),
            ],
        ]
    )
    def test_agents_summary(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "invalid_api_version",
                Util.read_file_to_dict("inputs/get_agents_summary_site_id.json.inp"),
                "Endpoint not found.",
                "This action is not supported in SentinelOne API v2.0. Verify that your SentinelOne console supports "
                "SentinelOne API v2.1 and try again.",
            ],
        ]
    )
    def test_agents_summary_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        self.action.connection.client.api_version = "2.0"
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
