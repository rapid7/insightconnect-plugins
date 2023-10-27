import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.search_agents import SearchAgents
from util import Util
from unittest import TestCase
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestSearchAgents(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(SearchAgents())

    @parameterized.expand(
        [
            [
                "all",
                Util.read_file_to_dict("inputs/search_agents_all.json.inp"),
                Util.read_file_to_dict("expected/search_agents_all.json.exp"),
            ],
            [
                "all_active",
                Util.read_file_to_dict("inputs/search_agents_all_active.json.inp"),
                Util.read_file_to_dict("expected/search_agents_all_active.json.exp"),
            ],
            [
                "empty",
                Util.read_file_to_dict("inputs/search_agents_empty.json.inp"),
                Util.read_file_to_dict("expected/search_agents_empty.json.exp"),
            ],
            [
                "single_agent",
                Util.read_file_to_dict("inputs/search_agents_single.json.inp"),
                Util.read_file_to_dict("expected/search_agents_single.json.exp"),
            ],
            [
                "multiple_agents",
                Util.read_file_to_dict("inputs/search_agents_multiple.json.inp"),
                Util.read_file_to_dict("expected/search_agents_multiple.json.exp"),
            ],
        ]
    )
    def test_search_agents(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(expected, actual)
