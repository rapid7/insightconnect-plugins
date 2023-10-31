import sys
import os

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.name_available import NameAvailable
from util import Util
from unittest import TestCase


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestNameAvailable(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(NameAvailable())

    @parameterized.expand(
        [
            [
                "name_available",
                Util.read_file_to_dict("inputs/name_available.json.inp"),
                Util.read_file_to_dict("expected/name_available.json.exp"),
            ],
            [
                "name_not_available",
                Util.read_file_to_dict("inputs/name_not_available.json.inp"),
                Util.read_file_to_dict("expected/name_not_available.json.exp"),
            ],
        ]
    )
    def test_name_available(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
