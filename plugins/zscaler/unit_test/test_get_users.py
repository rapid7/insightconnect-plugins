import sys
import os
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.util import Util
from icon_zscaler.actions.get_users import GetUsers

sys.path.append(os.path.abspath("../"))


@patch("requests.request", side_effect=Util.mock_request)
class TestGetUsers(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetUsers())

    @parameterized.expand(
        [
            [
                "existing_users",
                Util.read_file_to_dict("inputs/get_users.json.inp"),
                Util.read_file_to_dict("expected/get_users.json.exp"),
            ],
            [
                "no_params",
                Util.read_file_to_dict("inputs/get_users_empty.json.inp"),
                Util.read_file_to_dict("expected/get_users.json.exp"),
            ],
            [
                "not_found_user",
                Util.read_file_to_dict("inputs/get_users_not_found.json.inp"),
                Util.read_file_to_dict("expected/get_users_not_found.json.exp"),
            ],
        ]
    )
    def test_get_users(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
