import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_topdesk.actions.listOperators import ListOperators
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mock_request)
class TestListOperators(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListOperators())

    @parameterized.expand(
        [
            [
                "default_params",
                Util.read_file_to_dict("inputs/list_operators_default_params.json.inp"),
                Util.read_file_to_dict("expected/list_operators_all_fields.json.exp"),
            ],
            [
                "with_query",
                Util.read_file_to_dict("inputs/list_operators_with_query.json.inp"),
                Util.read_file_to_dict("expected/list_operators_all_fields.json.exp"),
            ],
            [
                "with_query_and_fields",
                Util.read_file_to_dict("inputs/list_operators_with_query_and_fields.json.inp"),
                Util.read_file_to_dict("expected/list_operators_selected_fields.json.exp"),
            ],
            [
                "empty",
                Util.read_file_to_dict("inputs/list_operators_empty.json.inp"),
                Util.read_file_to_dict("expected/list_operators_empty.json.exp"),
            ],
        ]
    )
    def test_list_operators(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
