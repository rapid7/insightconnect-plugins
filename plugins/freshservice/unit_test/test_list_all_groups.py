import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_freshservice.actions.list_all_groups import ListAllGroups
from util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests)
class TestListAllGroups(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListAllGroups())

    @parameterized.expand(Util.load_parameters("list_all_groups").get("parameters"))
    def test_list_all_groups(self, mock_request, name, expected):
        actual = self.action.run()
        self.assertEqual(actual, expected)
