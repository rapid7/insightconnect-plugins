from unittest import TestCase
from icon_extractit.actions.date_extractor import DateExtractor
from icon_extractit.actions.date_extractor.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

parameters = Util.load_parameters("date_extractor").get("parameters")


class TestDateExtractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_dates(self, name, string, file, expected):
        action = DateExtractor()
        actual = action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.DATES: expected}
        self.assertEqual(actual, expected)
