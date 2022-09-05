import os
import sys
from unittest import TestCase

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from icon_connectwise.util.helpers import clean_dict, iso8601_to_utc_date


class TestUpdateTicket(TestCase):
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
                "empty_string",
                "",
                "",
            ],
            [
                "iso_date",
                "2022-09-23T01:00:00+02:00",
                "2022-09-23T01:00:00Z"
            ],
            [
                "utc_date",
                "2022-09-01T08:51:01Z",
                "2022-09-01T08:51:01Z",
            ],
            [
                "random_string",
                "hello:worldT1-00",
                "hello:worldT1-00",
            ],
        ]
    )
    def test_iso8601_to_utc_date(self, test_name, date_string, expected):
        actual = iso8601_to_utc_date(date_string)
        self.assertEqual(actual, expected)
