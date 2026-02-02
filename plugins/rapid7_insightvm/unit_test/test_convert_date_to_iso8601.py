import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightvm.util.util import convert_date_to_iso8601
from parameterized import parameterized


class TestCreateException(TestCase):
    @parameterized.expand(
        [
            ["20 11 2022", "20 11 2022", "2022-11-20T00:00:00.000000Z"],
            ["Jul 1 2022", "Jul 1 2022", "2022-07-01T00:00:00.000000Z"],
            ["10.12.2022", "10.12.2022", "2022-10-12T00:00:00.000000Z"],
            ["02-05-2022", "02-05-2022", "2022-02-05T00:00:00.000000Z"],
            ["January 10 2022", "January 10 2022", "2022-01-10T00:00:00.000000Z"],
            ["2022-11-20T00:00:00Z", "2022-11-20T00:00:00Z", "2022-11-20T00:00:00.000000Z"],
            ["2022-11-20T00:00:00.123Z", "2022-11-20T00:00:00.123Z", "2022-11-20T00:00:00.123000Z"],
            ["2022-11-20 12:34:56", "2022-11-20 12:34:56", "2022-11-20T12:34:56.000000Z"],
            ["2022-11-20 12:34:56.123", "2022-11-20 12:34:56.123", "2022-11-20T12:34:56.123000Z"],
            ["02-05-2022 12:34:56", "02-05-2022 12:34:56", "2022-02-05T12:34:56.000000Z"],
        ]
    )
    def test_convert_date_to_iso8601(self, name, date, expected) -> None:
        actual = convert_date_to_iso8601(date)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_date_format_1",
                "2222-2222-2222",
                "The provided date format 2222-2222-2222 is not supported.",
                "Please provide the date in a different format e.g. 2022-01-01T00:00:00Z and try again.",
            ],
            [
                "invalid_date_format_2",
                "",
                "The provided date format  is not supported.",
                "Please provide the date in a different format e.g. 2022-01-01T00:00:00Z and try again.",
            ],
        ]
    )
    def test_convert_date_to_iso8601_bad(self, name, date, cause, assistance) -> None:
        with self.assertRaises(PluginException) as e:
            convert_date_to_iso8601(date)
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
