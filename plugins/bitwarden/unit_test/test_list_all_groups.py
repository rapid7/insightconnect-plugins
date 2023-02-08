import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_bitwarden.actions.listAllGroups import ListAllGroups
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mock_request)
class TestListAllGroups(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListAllGroups())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("expected/list_all_groups.json.exp"),
            ]
        ]
    )
    def test_list_all_groups(self, mock_request, test_name, expected):
        actual = self.action.run()
        self.assertEqual(actual, expected)
