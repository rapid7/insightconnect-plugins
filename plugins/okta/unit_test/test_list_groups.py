import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_okta.actions.list_groups import ListGroups
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mock_request)
class TestListGroups(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListGroups())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/list_groups.json.inp"),
                Util.read_file_to_dict("expected/list_groups.json.exp"),
            ],
            [
                "with_query",
                Util.read_file_to_dict("inputs/list_groups_with_query.json.inp"),
                Util.read_file_to_dict("expected/list_groups_with_query.json.exp"),
            ],
            [
                "empty",
                Util.read_file_to_dict("inputs/list_groups_empty.json.inp"),
                Util.read_file_to_dict("expected/list_groups_empty.json.exp"),
            ],
        ]
    )
    def test_list_groups(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
