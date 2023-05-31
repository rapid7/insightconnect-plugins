import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_duo_admin.actions.get_users import GetUsers
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mock_request)
class TestGetUsers(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetUsers())

    @parameterized.expand(
        [
            [
                "user_list",
                Util.read_file_to_dict("expected/get_users.json.exp"),
            ],
        ]
    )
    def test_get_users(self, mock_request, test_name, expected):
        actual = self.action.run()
        self.assertEqual(actual, expected)
