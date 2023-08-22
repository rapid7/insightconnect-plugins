import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from icon_freshservice.actions.list_all_groups import ListAllGroups
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mocked_requests)
class TestListAllGroups(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListAllGroups())

    @parameterized.expand(Util.load_parameters("list_all_groups").get("parameters"))
    def test_list_all_groups(self, mock_request, name, expected):
        actual = self.action.run()
        self.assertEqual(actual, expected)
