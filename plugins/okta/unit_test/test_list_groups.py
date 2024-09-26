import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate
from komand_okta.actions.list_groups import ListGroups
from parameterized import parameterized

from util import Util


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
    def test_list_groups(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, self.action.output.schema)
        self.assertEqual(actual, expected)
