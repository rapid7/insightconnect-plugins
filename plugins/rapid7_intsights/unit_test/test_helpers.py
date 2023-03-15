import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from parameterized import parameterized
from icon_rapid7_intsights.util.helpers import clean, convert_dict_keys_to_camel_case, to_camel_case


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
            [
                "to_be_cleaned_with_boolean",
                {
                    "bool": False,
                    "key": "value",
                    "next": {"key_in_value": [], "request_i": "123", "none": None},
                    "team": {"id": 0, "name": "John"},
                    "empty_string": "",
                },
                {"bool": False, "key": "value", "next": {"request_i": "123"}, "team": {"name": "John"}},
            ],
            [
                "iocs_empty",
                {"iocs": [], "nextOffset": None},
                {"iocs": []},
            ],
            [
                "iocs_list",
                {"iocs": [{"key": "value"}], "nextOffset": "example"},
                {"iocs": [{"key": "value"}], "nextOffset": "example"},
            ],
        ]
    )
    def test_clean(self, test_name, input_params, expected):
        actual = clean(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["snake1", "camel_case_string", "camelCaseString"],
            ["snake2", "my_new_camel", "myNewCamel"],
            ["snake3", "my0_snake", "my0Snake"],
            ["single_word", "word", "word"],
            ["word_with_digit1", "word1", "word1"],
            ["word_with_digit1", "word1", "word1"],
            ["word_capitalized1", "wordABC", "wordAbc"],
            ["word_capitalized2", "word9ABC9", "word9Abc9"],
            ["camel_case", "myCamelCase", "myCamelCase"],
            ["pascal_case", "PascalCase", "pascalCase"],
            ["empty", "", ""],
        ]
    )
    def test_to_camel_case(self, test_name, string_to_modify, expected):
        actual = to_camel_case(string_to_modify)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["dict_to_camel1", {"snake_key": 4}, {"snakeKey": 4}],
            ["dict_to_camel2", {"camelCase": 4}, {"camelCase": 4}],
            ["dict_to_camel3", {"PascalCase": 4}, {"pascalCase": 4}],
            ["list_to_camel1", [{"snake_key": 4}], [{"snakeKey": 4}]],
            ["list_to_camel2", [{"camelCase": 4}], [{"camelCase": 4}]],
            ["list_to_camel3", [{"PascalCase": 4}], [{"pascalCase": 4}]],
        ]
    )
    def test_convert_dict_keys_to_camel_case(self, test_name, to_modify, expected):
        actual = convert_dict_keys_to_camel_case(to_modify)
        self.assertEqual(actual, expected)
