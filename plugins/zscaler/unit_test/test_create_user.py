import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.util import Util
from icon_zscaler.actions.create_user import CreateUser
from icon_zscaler.util.constants import Assistance, Cause


@patch("requests.request", side_effect=Util.mock_request)
class TestCreateUser(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateUser())

    @parameterized.expand(
        [
            [
                "valid_user",
                Util.read_file_to_dict("inputs/create_user.json.inp"),
                Util.read_file_to_dict("expected/create_user.json.exp"),
            ],
            [
                "mandatory_fields",
                Util.read_file_to_dict("inputs/create_user_mandatory_fields.json.inp"),
                Util.read_file_to_dict("expected/create_user_mandatory_fields.json.exp"),
            ],
        ]
    )
    def test_create_user(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "bad_department",
                Util.read_file_to_dict("inputs/create_user_bad_department.json.inp"),
                Cause.DEPARTMENT_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
            [
                "bad_group",
                Util.read_file_to_dict("inputs/create_user_bad_group.json.inp"),
                Cause.GROUP_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
        ]
    )
    def test_create_user_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
