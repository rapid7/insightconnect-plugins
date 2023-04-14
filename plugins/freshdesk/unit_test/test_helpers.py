import os
import sys
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from parameterized import parameterized

from icon_freshdesk.util.constants import Ticket, TextCase
from unit_test.util import Util

sys.path.append(os.path.abspath("../"))

from icon_freshdesk.util.helpers import (
    clean_dict,
    create_attachments_form,
    add_keys_prefix,
    replace_ticket_fields_name_to_id,
    replace_ticket_fields_id_to_name,
    camel_to_snake_case,
    snake_to_camel_case,
    convert_dict_keys_case,
)


class TestHelpers(TestCase):
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
                    "team": {"id": 0, "name": "John"},
                    "empty_string": "",
                },
                {"key": "value", "next": {"request_i": "123"}, "team": {"name": "John"}},
            ],
        ]
    )
    def test_clean_dict(self, test_name, input_params, expected):
        actual = clean_dict(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "many_attachments",
                [
                    {"name": "create.txt", "content": "aGVsbG8gd29ybGQ="},
                    {"name": "unit.png", "content": "ZGZmZmRnZmRiZGpuaXVoZmRpeWVyd2ZnaWhyZmdk="},
                    {"name": "world.py", "content": "aGVsbyB1bml0IHRzdHk="},
                ],
                [
                    ("attachments[]", ("create.txt", b"hello world", "text/plain")),
                    ("attachments[]", ("unit.png", b"dfffdgfdbdjniuhfdiyerwfgihrfgd", "image/png")),
                    ("attachments[]", ("world.py", b"helo unit tsty", "text/x-python")),
                ],
            ],
            [
                "empty",
                [],
                [],
            ],
        ]
    )
    def test_create_attachment_form(self, test_name, attachments, expected):
        actual = create_attachments_form(attachments)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "empty_dict",
                {},
                "abc",
                {},
            ],
            [
                "dict",
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "id": "908"},
                    "id": 2,
                },
                "abc_",
                {
                    "abc_key": "value",
                    "abc_next": {"key_in_value": [9, 8, 7, 6, 5, 4], "id": "908"},
                    "abc_id": 2,
                },
            ],
        ]
    )
    def test_add_keys_prefix(self, test_name, dict_to_modify, prefix, expected):
        actual = add_keys_prefix(dict_to_modify, prefix)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "ticket_fields",
                Util.read_file_to_dict("responses/get_ticket_by_id.json.resp"),
                Ticket.FIELDS_TO_NAME_ID_CONVERSION,
                Util.read_file_to_dict("responses/get_ticket_fields.json.resp"),
                Util.read_file_to_dict("expected/get_ticket_by_id.json.exp").get("ticket"),
            ],
            [
                "ticket_fields_2",
                Util.read_file_to_dict("responses/create_ticket_few_parameters.json.resp"),
                Ticket.FIELDS_TO_NAME_ID_CONVERSION,
                Util.read_file_to_dict("responses/get_ticket_fields.json.resp"),
                Util.read_file_to_dict("expected/create_ticket_few_parameters.json.exp").get("ticket"),
            ],
        ]
    )
    def test_replace_ticket_fields_id_to_name(
        self, test_name, dict_to_modify, fields_to_update, all_ticket_fields, expected
    ):
        actual = clean(
            convert_dict_keys_case(
                replace_ticket_fields_id_to_name(dict_to_modify, fields_to_update, all_ticket_fields),
                TextCase.CAMEL_CASE,
            )
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "ticket_fields",
                Util.read_file_to_dict("expected/get_ticket_by_id.json.exp").get("ticket"),
                Ticket.FIELDS_TO_NAME_ID_CONVERSION,
                Util.read_file_to_dict("responses/get_ticket_fields.json.resp"),
                Util.read_file_to_dict("responses/get_ticket_by_id.json.resp"),
            ],
            [
                "ticket_fields_2",
                Util.read_file_to_dict("expected/create_ticket_few_parameters.json.exp").get("ticket"),
                Ticket.FIELDS_TO_NAME_ID_CONVERSION,
                Util.read_file_to_dict("responses/get_ticket_fields.json.resp"),
                Util.read_file_to_dict("responses/create_ticket_few_parameters.json.resp"),
            ],
        ]
    )
    def test_replace_ticket_fields_name_to_id(
        self, test_name, dict_to_modify, fields_to_update, all_ticket_fields, expected
    ):
        actual = replace_ticket_fields_name_to_id(dict_to_modify, fields_to_update, all_ticket_fields)
        self.assertEqual(actual, clean(convert_dict_keys_case(expected, TextCase.CAMEL_CASE)))

    @parameterized.expand(
        [
            ["snake1", "my_snake_string", "mySnakeString"],
            ["snake2", "my_second_snake_case_string", "mySecondSnakeCaseString"],
            ["empty", "", ""],
        ]
    )
    def test_camel_to_snake_case(self, test_name, string_to_modify, expected):
        actual = snake_to_camel_case(string_to_modify)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["camel1", "camelCaseString", "camel_case_string"],
            ["camel2", "MyNewCamel", "my_new_camel"],
            ["empty", "", ""],
        ]
    )
    def test_camel_snake_case(self, test_name, string_to_modify, expected):
        actual = camel_to_snake_case(string_to_modify)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["dict_to_camel", {"snake_key": 4}, TextCase.CAMEL_CASE, {"snakeKey": 4}],
            ["list_to_camel", [{"snake_key": 4}], TextCase.CAMEL_CASE, [{"snakeKey": 4}]],
            ["dict_to_snake", {"CamelCase": 4}, TextCase.SNAKE_CASE, {"camel_case": 4}],
            ["list_to_snake", [{"camelCase": 4}], TextCase.SNAKE_CASE, [{"camel_case": 4}]],
        ]
    )
    def test_convert_dict_keys_case(self, test_name, to_modify, case_type, expected):
        actual = convert_dict_keys_case(to_modify, case_type)
        self.assertEqual(actual, expected)
