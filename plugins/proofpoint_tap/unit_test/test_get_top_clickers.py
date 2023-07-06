import sys
import os

from unittest.mock import patch
from komand_proofpoint_tap.actions.get_top_clickers import GetTopClickers
from test_util import Util
from unittest import TestCase
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestGetTopClickers(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetTopClickers())

    @parameterized.expand(
        [
            [
                "success_empty",
                Util.read_file_to_dict("inputs/get_top_clickers_success_empty.json.inp"),
                Util.read_file_to_dict("expected/get_top_clickers_success_empty.json.exp"),
            ],
            [
                "success",
                Util.read_file_to_dict("inputs/get_top_clickers_success.json.inp"),
                Util.read_file_to_dict("expected/get_top_clickers_success.json.exp"),
            ],
        ]
    )
    def test_get_top_clickers(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)
