import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from jsonschema.validators import validate

from insightconnect_plugin_runtime.exceptions import PluginException

from util import Util
from icon_sophos_central.actions.get_agent_details import GetAgentDetails


@patch("requests.request", side_effect=Util.mock_request)
class TestGetAgentDetails(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAgentDetails())

    @parameterized.expand(
        [
            [
                "found_on_second_page",
                Util.read_file_to_dict("inputs/get_agent_details.json.inp"),
                Util.read_file_to_dict("expected/get_agent_details.json.exp"),
            ]
        ]
    )
    def test_get_agent_details(self, mock_request, test_name: str, input_params: dict, expected: dict) -> None:
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
        validate(actual, self.action.output.schema)

    def test_get_agent_details_paginates_with_page_from_key(self, mock_request) -> None:
        self.action.run(Util.read_file_to_dict("inputs/get_agent_details.json.inp"))

        second_call_params = mock_request.call_args_list[-1].kwargs["params"]
        self.assertEqual(second_call_params.get("pageFromKey"), "exampleKey")
        self.assertNotIn("pageKey", second_call_params)
        self.assertTrue(second_call_params.get("pageTotal"))

    @parameterized.expand(
        [
            [
                "agent_not_found",
                Util.read_file_to_dict("inputs/get_agent_details_not_found.json.inp"),
            ]
        ]
    )
    def test_get_agent_details_raise_exception(self, mock_request, test_name: str, input_params: dict) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)

        self.assertEqual(error.exception.preset, PluginException.Preset.NOT_FOUND)
