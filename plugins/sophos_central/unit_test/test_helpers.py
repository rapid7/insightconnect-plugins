import os
import sys

from unittest import TestCase
from parameterized import parameterized
from icon_sophos_central.util.helpers import clean

sys.path.append(os.path.abspath("../"))


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
        ]
    )
    def test_clean(self, test_name, input_params, expected):
        actual = clean(input_params)
        self.assertEqual(actual, expected)
