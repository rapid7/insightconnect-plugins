import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any
from unittest import TestCase
from unittest.mock import MagicMock, patch

from komand_duo_admin.actions.get_users import GetUsers
from jsonschema.validators import validate
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
@patch("komand_duo_admin.util.api.isinstance", return_value=True)
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
    def test_get_users(
        self, mock_request_instance: MagicMock, mock_request: MagicMock, test_name: str, expected: dict[str, Any]
    ) -> None:
        actual = self.action.run()
        self.assertEqual(actual, expected)
        validate(actual, self.action.output.schema)
        self.assertEqual([call.kwargs["params"]["offset"] for call in mock_request.call_args_list], ["0", "300"])

    @patch(
        "komand_duo_admin.util.api.DuoAdminAPI.get_users",
        return_value={"response": [{"user_id": "ABCABC", "username": "Example 1"}], "metadata": {"next_offset": 0}},
    )
    def test_get_users_non_advancing_offset(
        self, mock_get_users: MagicMock, mock_request_instance: MagicMock, mock_request: MagicMock
    ) -> None:
        actual = self.action.run()
        self.assertEqual(actual, {"users": [{"userId": "ABCABC", "username": "Example 1"}]})
        self.assertEqual(mock_get_users.call_count, 1)
