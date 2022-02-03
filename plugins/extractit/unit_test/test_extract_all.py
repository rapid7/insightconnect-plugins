from unittest import TestCase
from icon_extractit.actions.extract_all import ExtractAll
from icon_extractit.actions.extract_all.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

parameters = Util.load_parameters("extract_all").get("parameters")


class TestIocExtractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_all(self, name, date_format, string, file, expected):
        action = ExtractAll()
        actual = action.run({Input.DATE_FORMAT: date_format, Input.STR: string, Input.FILE: file})
        expected = {Output.INDICATORS: expected}
        self.assertEqual(actual, expected)
