import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_cylance_protect.actions.update_agent.action import UpdateAgent
from icon_cylance_protect.actions.update_agent.schema import UpdateAgentInput, UpdateAgentOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("icon_cylance_protect.util.api.CylanceProtectAPI.generate_token", side_effect=Util.mock_generate_token)
@patch("requests.request", side_effect=Util.mock_request)
class TestUpdateAgent(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateAgent())

    @parameterized.expand(
        [
            [
                "valid_update_agent",
                {"agent": "hostname", "policy": "", "zones": [], "remove_zones": []},
                {"success": True},
            ],
            [
                "valid_update_agent_add_zone",
                {"agent": "hostname", "policy": "", "zones": ["zone_to_be_added"], "remove_zones": []},
                {"success": True},
            ],
            [
                "valid_update_agent_remove_zone",
                {"agent": "hostname", "policy": "", "zones": [], "remove_zones": ["zone_to_be_removed"]},
                {"success": True},
            ],
            [
                "valid_update_agent_both_zone",
                {
                    "agent": "hostname",
                    "policy": "",
                    "zones": ["zone_to_be_added"],
                    "remove_zones": ["zone_to_be_added"],
                },
                {"success": True},
            ],
            [
                "valid_update_agent_policy",
                {
                    "agent": "hostname",
                    "policy": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                    "zones": [],
                    "remove_zones": [],
                },
                {"success": True},
            ],
        ]
    )
    def test_integration_search_threats_valid(
        self,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, UpdateAgentInput.schema)
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
        validate(actual, UpdateAgentOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_update_agent_bad_hostname",
                {"agent": "invalid_hostname", "policy": "", "zones": [], "remove_zones": []},
                "Not found.",
                "The request was made for a resource that doesn't exist.",
            ],
            [
                "invalid_update_agent_bad_olicy",
                {"agent": "bad_hostname", "policy": "bad", "zones": [], "remove_zones": []},
                "The response from the CylancePROTECT API was not in the correct format.",
                "Contact support for help. See log for more details",
            ],
        ]
    )
    def test_integration_search_threats_invalid(
        self,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
        _test_name: str,
        input_params: dict,
        cause: str,
        assistance: str,
    ):
        validate(input_params, UpdateAgentInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
