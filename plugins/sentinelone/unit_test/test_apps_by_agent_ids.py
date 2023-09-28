import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.apps_by_agent_ids import AppsByAgentIds
from util import Util
from unittest import TestCase
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.post", side_effect=Util.mocked_requests_get)
@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestAppsByAgentIds(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(AppsByAgentIds())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/apps_by_agent_ids_success.json.inp"),
                Util.read_file_to_dict("expected/apps_by_agent_ids_success.json.exp"),
            ],
        ]
    )
    def test_apps_by_agent_ids(self, mock_request, mock_post, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "empty_input",
                Util.read_file_to_dict("inputs/apps_by_agent_ids_empty_input.json.inp"),
                "Input validation error.",
                "Please provide valid 'Agent IDs' input.",
            ],
        ]
    )
    def test_apps_by_agent_ids_raise_exception(
        self, mock_request, mock_post, test_name, input_params, cause, assistance
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
