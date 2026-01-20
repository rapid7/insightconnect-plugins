import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized
from util import Util
from icon_connectwise.util.helpers import clean_dict, iso8601_to_utc_date, rename_keys


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
            ["iso_date", "2022-09-23T01:00:00+02:00", "2022-09-23T01:00:00Z"],
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

    @parameterized.expand(
        [
            [
                "invalid_iso_format",
                "2022-09-01T08:51:01+XY",
                "Invalid date format",
            ]
        ]
    )
    def test_iso8601_to_utc_date_raise_exception(self, test_name, date_string, cause):
        with self.assertRaises(PluginException) as error:
            iso8601_to_utc_date(date_string)
        self.assertEqual(error.exception.cause, cause)

    @parameterized.expand(
        [
            [
                "empty_dict",
                {},
                "xyz",
                "zyx",
                {},
            ],
            [
                "list_of_dicts",
                Util.read_file_to_dict("responses/create_ticket_few_parameters.json.resp"),
                "_info",
                "info",
                Util.read_file_to_dict("expected/create_ticket_few_parameters.json.exp").get("ticket"),
            ],
            [
                "list_of_dicts_2",
                Util.read_file_to_dict("responses/get_ticket_notes_many_parameters.json.resp"),
                "_info",
                "info",
                Util.read_file_to_dict("expected/get_ticket_notes_many_parameters.json.exp").get("ticket_notes"),
            ],
            ["nothing_to_rename", {"key": "repl"}, "replace", "replaced", {"key": "repl"}],
        ]
    )
    def test_rename_keys(self, test_name, response, rename_from, rename_to, expected):
        actual = rename_keys(response, rename_from, rename_to)
        self.assertEqual(actual, expected)
