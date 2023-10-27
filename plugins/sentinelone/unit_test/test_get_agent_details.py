import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.get_agent_details import GetAgentDetails
from util import Util
from unittest import TestCase
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestGetAgentDetails(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetAgentDetails())

    @parameterized.expand(
        [
            [
                "success_by_id",
                Util.read_file_to_dict("inputs/get_agent_details_by_id.json.inp"),
                Util.read_file_to_dict("expected/get_agent_details_success.json.exp"),
            ],
            [
                "success_by_uuid",
                Util.read_file_to_dict("inputs/get_agent_details_by_uuid.json.inp"),
                Util.read_file_to_dict("expected/get_agent_details_success.json.exp"),
            ],
            [
                "success_by_hostname",
                Util.read_file_to_dict("inputs/get_agent_details_by_hostname.json.inp"),
                Util.read_file_to_dict("expected/get_agent_details_success.json.exp"),
            ],
            [
                "success_by_ip_address",
                Util.read_file_to_dict("inputs/get_agent_details_by_ip_address.json.inp"),
                Util.read_file_to_dict("expected/get_agent_details_success.json.exp"),
            ],
            [
                "success_by_mac_address",
                Util.read_file_to_dict("inputs/get_agent_details_by_mac_address.json.inp"),
                Util.read_file_to_dict("expected/get_agent_details_success.json.exp"),
            ],
            [
                "not_found_operational_state",
                Util.read_file_to_dict("inputs/get_agent_details_not_found_operational_state.json.inp"),
                Util.read_file_to_dict("expected/get_agent_details_not_found.json.exp"),
            ],
            [
                "not_found_operational_state",
                Util.read_file_to_dict("inputs/get_agent_details_not_found_hostname.json.inp"),
                Util.read_file_to_dict("expected/get_agent_details_not_found.json.exp"),
            ],
            [
                "operational_state",
                Util.read_file_to_dict("inputs/get_agent_details_operational_state.json.inp"),
                Util.read_file_to_dict("expected/get_agent_details_success.json.exp"),
            ],
        ]
    )
    def test_get_agent_details(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "multiple_agents",
                Util.read_file_to_dict("inputs/get_agent_details_multiple_agents.json.inp"),
                "Multiple agents found.",
                "Please provide a unique agent identifier so the action can be performed on the intended agent.",
            ],
        ]
    )
    def test_get_agent_details_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
