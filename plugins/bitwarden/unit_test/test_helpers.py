import sys
import os
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_bitwarden.util.helpers import clean_dict, switch_member_status_and_type
from icon_bitwarden.util.constants import ValueType

sys.path.append(os.path.abspath("../"))


class TestHelpers(TestCase):
    @parameterized.expand(
        [
            ["-1_to_-1-Revoked", {"status": -1}, {"status": "-1-Revoked"}],
            ["0_to_0-Invited", {"status": 0}, {"status": "0-Invited"}],
            ["1_to_1-Accepted", {"status": 1}, {"status": "1-Accepted"}],
            ["2_to_2-Confirmed", {"status": 2}, {"status": "2-Confirmed"}],
            ["0_to_0-Owner", {"type": 0}, {"type": "0-Owner"}],
            ["1_to_1-Admin", {"type": 1}, {"type": "1-Admin"}],
            ["2_to_2-User", {"type": 2}, {"type": "2-User"}],
            ["3_to_3-Manager", {"type": 3}, {"type": "3-Manager"}],
            ["both_keys_1", {"status": -1, "type": 0}, {"status": "-1-Revoked", "type": "0-Owner"}],
            ["both_keys_2", {"status": 0, "type": 1}, {"status": "0-Invited", "type": "1-Admin"}],
            ["keys_string", {"status": "0-Invited", "type": "0-Owner"}, {"status": "0-Invited", "type": "0-Owner"}],
            ["no_key", {}, {}],
        ]
    )
    def test_switch_status_and_type_to_string(self, test_name, input_params, expected):
        actual = switch_member_status_and_type(input_params, ValueType.STRING)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["-1-Revoked_to_-1", {"status": "-1-Revoked"}, {"status": -1}],
            ["0-Invited_to_0", {"status": "0-Invited"}, {"status": 0}],
            ["1-Accepted_to_1", {"status": "1-Accepted"}, {"status": 1}],
            ["2-Confirmed_to_2", {"status": "2-Confirmed"}, {"status": 2}],
            ["0-Owner_to_0", {"type": "0-Owner"}, {"type": 0}],
            ["1-Admin_to_1", {"type": "1-Admin"}, {"type": 1}],
            ["2-User_to_2", {"type": "2-User"}, {"type": 2}],
            ["3-Manager_to_ 3", {"type": "3-Manager"}, {"type": 3}],
            ["both_keys_1", {"status": "-1-Revoked", "type": "0-Owner"}, {"status": -1, "type": 0}],
            ["both_keys_2", {"status": "0-Invited", "type": "1-Admin"}, {"status": 0, "type": 1}],
            ["keys_integer", {"status": 0, "type": 0}, {"status": 0, "type": 0}],
            ["no_key", {}, {}],
        ]
    )
    def test_switch_status_and_type_to_integer(self, test_name, input_params, expected):
        actual = switch_member_status_and_type(input_params, ValueType.INTEGER)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["empty_dict", {}, {}],
            [
                "clean_dict",
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "id": "908"},
                    "id": 2,
                },
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "id": "908"},
                    "id": 2,
                },
            ],
            [
                "to_be_cleaned",
                {
                    "key": "value",
                    "next": {"key_in_value": [], "request_i": "123", "none": None},
                    "team": {"id": 1234, "name": "John"},
                    "empty_string": "",
                },
                {"key": "value", "next": {"request_i": "123"}, "team": {"id": 1234, "name": "John"}},
            ],
        ]
    )
    def test_clean_dict(self, test_name, input_params, expected):
        actual = clean_dict(input_params)
        self.assertEqual(actual, expected)
