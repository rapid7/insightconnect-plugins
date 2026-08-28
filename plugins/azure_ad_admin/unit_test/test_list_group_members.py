import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_azure_ad_admin.actions.list_group_members import ListGroupMembers
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mocked_requests)
class TestListGroupMembers(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request: MagicMock) -> None:
        cls.action = Util.default_connector(ListGroupMembers())

    @parameterized.expand(
        [
            [
                "pagination_two_pages",
                Util.read_file_to_dict("inputs/list_group_members_pagination.json.inp"),
                Util.read_file_to_dict("expected/list_group_members_pagination.json.exp"),
            ],
            [
                "single_page",
                Util.read_file_to_dict("inputs/list_group_members_single_page.json.inp"),
                Util.read_file_to_dict("expected/list_group_members_single_page.json.exp"),
            ],
        ]
    )
    def test_list_group_members(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        # Regression coverage for SOAR-21944: the "pagination_two_pages" case exercises a
        # group whose members span two @odata.nextLink pages, so the action must follow
        # every page and return all members (previously it returned only the first page
        # of 100 while still reporting the true @odata.count).
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
