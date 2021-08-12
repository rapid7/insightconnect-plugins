from unittest import TestCase
from icon_extractit.actions.date_extractor import DateExtractor
from icon_extractit.actions.date_extractor.schema import Input, Output


class TestDateExtractor(TestCase):
    def test_extract_dates_from_string(self):
        action = DateExtractor()
        actual = action.run(
            {
                Input.STR: "05/12/1982 is an example date",
            }
        )
        expected = {Output.DATES: ["1982-12-05T00:00:00Z"]}
        self.assertEqual(actual, expected)

    def test_extract_dates_from_file(self):
        action = DateExtractor()
        actual = action.run(
            {
                Input.FILE: "MDUvMTIvMTk4MiBpcyBhbiBleGFtcGxlIGRhdGU=",
            }
        )
        expected = {Output.DATES: ["1982-12-05T00:00:00Z"]}
        self.assertEqual(actual, expected)
