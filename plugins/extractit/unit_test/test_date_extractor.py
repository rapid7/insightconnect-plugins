from unittest import TestCase
from icon_extractit.actions.date_extractor import DateExtractor
from icon_extractit.actions.date_extractor.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from parameterized import parameterized

positive_parameters = Util.load_parameters("date_extractor_positive").get("parameters")
negative_parameters = Util.load_parameters("date_extractor_negative").get("parameters")
error_parameters = Util.load_parameters("date_extractor_error").get("parameters")


class TestDateExtractor(TestCase):
    @parameterized.expand(positive_parameters)
    def test_extract_dates_positive(self, name, date_format, string, file, expected):
        action = DateExtractor()
        actual = action.run({Input.DATE_FORMAT: date_format, Input.STR: string, Input.FILE: file})
        expected = {Output.DATES: expected}
        self.assertEqual(actual, expected)

    @parameterized.expand(negative_parameters)
    def test_extract_dates_negative(self, name, date_format, string, file, expected):
        action = DateExtractor()
        actual = action.run({Input.DATE_FORMAT: date_format, Input.STR: string, Input.FILE: file})
        expected = {Output.DATES: expected}
        self.assertEqual(actual, expected)

    @parameterized.expand(error_parameters)
    def test_extract_dates_error(self, name, date_format, string, file, expected):
        with self.assertRaises(PluginException):
            action = DateExtractor()
            actual = action.run({Input.DATE_FORMAT: date_format, Input.STR: string, Input.FILE: file})
