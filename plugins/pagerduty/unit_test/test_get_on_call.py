import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_pagerduty.actions.get_on_call import GetOnCall
from unittest.mock import patch, MagicMock, call
from parameterized import parameterized
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.Session.request", side_effect=Util.mock_request)
class TestGetOnCall(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetOnCall())

    @parameterized.expand(
        [
            [
                "missing_params_invalid",
                {},
                "Missing required paramaters",
                "Please ensure a valid 'schedule_id' is provided",
            ]
        ]
    )
    def test_missing_params_invalid(
        self, mock_request: MagicMock, test_name: str, input_params: dict, cause: str, assistance: str
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

    @parameterized.expand([["no_uers_from_schedule_invalid", {"schedule_id": "no_users"}, {"users": []}]])
    def test_no_uers_from_schedule_invalid(
        self, mock_request: MagicMock, test_name: str, input_params: dict, expected: dict
    ):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "no_user_id_from_user_invalid",
                {"schedule_id": "user_missing_id"},
                Util.read_file_to_dict("expected/test_user_missing_id.json.exp"),
            ]
        ]
    )
    @patch("logging.Logger.warning")
    def test_no_user_id_from_user_invalid(
        self, test_name: str, input_params: dict, expected: dict, mocked_warn: MagicMock, mock_request: MagicMock
    ):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

        if mocked_warn.called:
            log_call = call("User ID not available: 'id'")
            self.assertIn(log_call, mocked_warn.call_args_list)

    @parameterized.expand(
        [
            [
                "test_a_deleted_user_invalid",
                {"schedule_id": "user_has_been_deleted"},
                Util.read_file_to_dict("expected/test_deleted_user.json.exp"),
            ]
        ]
    )
    @patch("logging.Logger.warning")
    def test_no_user_id_from_user_invalid(
        self, test_name: str, input_params: dict, expected: dict, mocked_warn: MagicMock, mock_request: MagicMock
    ):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

        if mocked_warn.called:
            log_call = call("The following user P9FKCQ7 is part of the schedule but has been deleted")
            self.assertIn(log_call, mocked_warn.call_args_list)

    @parameterized.expand([["test_cannot_find_user_invalid", {"schedule_id": "test_cannot_find_user"}, {"users": []}]])
    @patch("logging.Logger.warning")
    def test_no_user_id_from_user_invalid(
        self, test_name: str, input_params: dict, expected: dict, mocked_warn: MagicMock, mock_request: MagicMock
    ):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

        if mocked_warn.called:
            log_call = call("No information was found for the user - PYGDZB9")
            self.assertIn(log_call, mocked_warn.call_args_list)

    @parameterized.expand(
        [
            [
                "test_valid_on_call",
                {"schedule_id": "test_valid_on_call"},
                Util.read_file_to_dict("expected/test_valid_on_call.json.exp"),
            ]
        ]
    )
    def test_valid_on_call(self, mock_request: MagicMock, test_name: str, input_params: dict, expected: dict):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
