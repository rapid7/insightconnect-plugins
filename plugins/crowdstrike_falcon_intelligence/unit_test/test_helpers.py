import os
import sys
from unittest import TestCase

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from icon_crowdstrike_falcon_intelligence.util.helpers import (
    clean_dict,
    camel_to_snake_case,
    snake_to_camel_case,
    convert_dict_keys_case,
    split_utc_date_time,
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
            ["snake1", "my_snake_string", "mySnakeString"],
            ["snake2", "my_second_snake_case_string", "mySecondSnakeCaseString"],
            ["empty", "", ""],
        ]
    )
    def test_snake_to_camel_case(self, test_name, string_to_modify, expected):
        actual = snake_to_camel_case(string_to_modify)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["camel1", "camelCaseString", "camel_case_string"],
            ["camel2", "MyNewCamel", "my_new_camel"],
            ["empty", "", ""],
        ]
    )
    def test_camel_to_snake_case(self, test_name, string_to_modify, expected):
        actual = camel_to_snake_case(string_to_modify)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["dict_to_camel", {"snake_key": 4}, "camel_case", {"snakeKey": 4}],
            ["list_to_camel", [{"snake_key": 4}], "camel_case", [{"snakeKey": 4}]],
            ["dict_to_snake", {"CamelCase": 4}, "snake_case", {"camel_case": 4}],
            ["list_to_snake", [{"camelCase": 4}], "snake_case", [{"camel_case": 4}]],
        ]
    )
    def test_convert_dict_keys_case(self, test_name, to_modify, case_type, expected):
        actual = convert_dict_keys_case(to_modify, case_type)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["utc_date_time", "2022-11-01T12:33:21+02:00", ("2022-11-01", "12:33")],
            ["incorrect_date_time_no_T", "2022-11-0112:33:21+02:00", (None, None)],
            ["incorrect_date_time_no_timezone", "2022-11-01T12:33:21", (None, None)],
            ["incorrect_date_time_random", "random_date", (None, None)],
        ]
    )
    def test_split_utc_date_time(self, test_name, utc_date_time, expected):
        actual = split_utc_date_time(utc_date_time)
        self.assertEqual(actual, expected)
