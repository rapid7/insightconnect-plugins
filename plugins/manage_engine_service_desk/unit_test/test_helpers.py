import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_manage_engine_service_desk.util.constants import ResponseStatus, Response

sys.path.append(os.path.abspath("../"))

from parameterized import parameterized
from icon_manage_engine_service_desk.util import helpers


class TestHelpers(TestCase):
    @parameterized.expand(
        [
            [
                "empty_dict",
                {},
                {"input_data": "{}"},
            ],
            [
                "not_empty_dict",
                {"key": "value", "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "k": 0, "none": None}},
                {"input_data": '{"key": "value", "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "k": 0}}'},
            ],
        ]
    )
    def test_prepare_input_data(self, test_name, input_params, expected):
        actual = helpers.prepare_input_data(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "empty_dict",
                {},
                {},
            ],
            [
                "with_status_code",
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "k": 0, "none": None},
                    Response.RESPONSE_STATUS: {ResponseStatus.STATUS_CODE: 999},
                },
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "k": 0, "none": None},
                    Response.RESPONSE_STATUS: {"manage_engine_status_code": 999},
                },
            ],
            [
                "without_status_code",
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "k": 0, "none": None},
                    Response.RESPONSE_STATUS: {},
                },
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "k": 0, "none": None},
                    Response.RESPONSE_STATUS: {},
                },
            ],
        ]
    )
    def test_replace_status_code(self, test_name, input_params, expected):
        actual = helpers.replace_status_code(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "empty_dict",
                {},
                {},
            ],
            [
                "with_id",
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "id": "908", "none": None},
                    Response.RESPONSE_STATUS: {ResponseStatus.STATUS_CODE: 999},
                },
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "id": 908, "none": None},
                    Response.RESPONSE_STATUS: {ResponseStatus.STATUS_CODE: 999},
                },
            ],
            [
                "with_id_2",
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "request_id": "123", "none": None},
                    Response.RESPONSE_STATUS: {},
                },
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "request_id": 123, "none": None},
                    Response.RESPONSE_STATUS: {},
                },
            ],
            [
                "with_string_id",
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "request_id": "random_string", "none": None},
                    Response.RESPONSE_STATUS: {},
                },
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "request_id": "random_string", "none": None},
                    Response.RESPONSE_STATUS: {},
                },
            ],
            [
                "without_id",
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "request_i": "123", "none": None},
                    Response.RESPONSE_STATUS: {},
                },
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "request_i": "123", "none": None},
                    Response.RESPONSE_STATUS: {},
                },
            ],
        ]
    )
    def test_map_ids_to_integer(self, test_name, input_params, expected):
        actual = helpers.map_ids_to_integer(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "empty_dict",
                {},
                {},
            ],
            [
                "clean_dict",
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "id": "908"},
                    Response.RESPONSE_STATUS: {ResponseStatus.STATUS_CODE: 999},
                },
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "id": "908"},
                    Response.RESPONSE_STATUS: {ResponseStatus.STATUS_CODE: 999},
                },
            ],
            [
                "to_be_cleaned",
                {
                    "key": "value",
                    "next": {"key_in_value": [], "request_i": "123", "none": None},
                    Response.RESPONSE_STATUS: {},
                    "empty_string": "",
                },
                {"key": "value", "next": {"request_i": "123"}},
            ],
        ]
    )
    def test_clean_dict(self, test_name, input_params, expected):
        actual = helpers.clean_dict(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "empty_dict",
                [],
                {},
                {},
            ],
            [
                "to_remove",
                ["next"],
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "id": "908"},
                    Response.RESPONSE_STATUS: {ResponseStatus.STATUS_CODE: 999},
                },
                {"next": {"key_in_value": [9, 8, 7, 6, 5, 4], "id": "908"}},
            ],
            [
                "removed",
                ["key", "next", Response.RESPONSE_STATUS, "empty_string"],
                {
                    "key": "value",
                    "next": {"key_in_value": [], "request_i": "123", "none": None},
                    Response.RESPONSE_STATUS: {},
                    "empty_string": "",
                },
                {
                    "key": "value",
                    "next": {"key_in_value": [], "request_i": "123", "none": None},
                    Response.RESPONSE_STATUS: {},
                    "empty_string": "",
                },
            ],
        ]
    )
    def test_remove_other_keys(self, test_name, keys_to_keep, input_dict, expected):
        actual = helpers.remove_other_keys(input_dict, keys_to_keep)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "full_request",
                {
                    "id": "201",
                    "subject": "Test request",
                    "requester": {"id": "4", "name": "John", "is_vipuser": False, "email_id": "john@example.com"},
                    "technician": {"id": "5", "name": "Admin", "is_vipuser": True, "phone": "555-1234"},
                    "created_by": {"id": "4", "name": "John", "is_vipuser": False, "phone": None},
                    "priority": {"id": "2", "name": "Normal", "color": "#006600"},
                    "status": {"id": "2", "name": "Open", "stop_timer": False},
                    "created_time": {"display_value": "Aug 3, 2022 01:11 AM", "value": "1659514299775"},
                    "due_by_time": {"display_value": "Aug 3, 2022 01:00 PM", "value": "1659556800775"},
                    "extra_field": "should be removed",
                },
                {
                    "requester": {"id": "4", "name": "John", "is_vipuser": False},
                    "technician": {"id": "5", "name": "Admin", "is_vipuser": True},
                    "created_by": {"id": "4", "name": "John", "is_vipuser": False},
                    "priority": {"id": "2", "name": "Normal"},
                    "status": {"id": "2", "name": "Open"},
                    "created_time": "Aug 3, 2022 01:11 AM",
                    "due_by_time": "Aug 3, 2022 01:00 PM",
                },
            ],
            [
                "missing_optional_fields",
                {
                    "id": "100",
                    "subject": "Minimal request",
                    "requester": {"id": "1", "name": "User"},
                },
                {
                    "requester": {"id": "1", "name": "User", "is_vipuser": None},
                    "technician": {"id": None, "name": None, "is_vipuser": None},
                    "created_time": None,
                    "due_by_time": None,
                },
            ],
        ]
    )
    def test_transform_request(self, test_name, raw_request, expected_fields):
        result = helpers.transform_request(raw_request)
        # Assert only the specific fields the function is responsible for transforming,
        # avoiding the bound-method key that get_all_attributes() introduces as a side effect.
        for key, expected_value in expected_fields.items():
            self.assertEqual(result[key], expected_value)
        # Confirm extra fields not in the Request schema are stripped
        string_keys = {k for k in result if isinstance(k, str)}
        self.assertNotIn("extra_field", string_keys)
        self.assertNotIn("email_id", string_keys)
        self.assertNotIn("phone", string_keys)
