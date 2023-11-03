import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_sentinelone.actions.move_between_sites import MoveBetweenSites
from util import Util
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestMoveBetweenSites(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(MoveBetweenSites())

    @parameterized.expand(
        [
            [
                "move_between_sites_minimum",
                Util.read_file_to_dict("inputs/move_between_sites_minimum.json.inp"),
                Util.read_file_to_dict("expected/move_between_sites_minimum.json.exp"),
            ],
            [
                "move_between_sites_data",
                Util.read_file_to_dict("inputs/move_between_sites_data.json.inp"),
                Util.read_file_to_dict("expected/move_between_sites_data.json.exp"),
            ],
        ]
    )
    def test_agents_action(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)
