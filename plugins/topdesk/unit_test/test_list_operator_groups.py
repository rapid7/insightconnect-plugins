import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_topdesk.actions.listOperatorGroups import ListOperatorGroups
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mock_request)
class TestListOperatorGroups(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListOperatorGroups())

    @parameterized.expand(
        [
            [
                "default_params",
                Util.read_file_to_dict("inputs/list_operator_groups_default_params.json.inp"),
                Util.read_file_to_dict("expected/list_operator_groups_all_fields.json.exp"),
            ],
            [
                "with_query",
                Util.read_file_to_dict("inputs/list_operator_groups_with_query.json.inp"),
                Util.read_file_to_dict("expected/list_operator_groups_all_fields.json.exp"),
            ],
            [
                "with_query_and_fields",
                Util.read_file_to_dict("inputs/list_operator_groups_with_query_and_fields.json.inp"),
                Util.read_file_to_dict("expected/list_operator_groups_selected_fields.json.exp"),
            ],
            [
                "empty",
                Util.read_file_to_dict("inputs/list_operator_groups_empty.json.inp"),
                Util.read_file_to_dict("expected/list_operator_groups_empty.json.exp"),
            ],
        ]
    )
    def test_list_operator_groups(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
