import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase

from icon_extractit.actions.date_extractor import DateExtractor
from icon_extractit.actions.date_extractor.schema import DateExtractorOutput, Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from util import Util

positive_parameters = Util.load_parameters("date_extractor_positive").get("parameters")
negative_parameters = Util.load_parameters("date_extractor_negative").get("parameters")
error_parameters = Util.load_parameters("date_extractor_error").get("parameters")


class TestDateExtractor(TestCase):
    def setUp(self) -> None:
        self.action = DateExtractor()

    @parameterized.expand(positive_parameters)
    def test_extract_dates_positive(
        self, name: str, date_format: str, string: str, file: Dict[str, Any], expected: List[str]
    ) -> None:
        actual = self.action.run({Input.DATE_FORMAT: date_format, Input.STR: string, Input.FILE: file})
        expected = {Output.DATES: expected}
        validate(actual, DateExtractorOutput.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(negative_parameters)
    def test_extract_dates_negative(
        self, name: str, date_format: str, string: str, file: Dict[str, Any], expected: List[str]
    ) -> None:
        actual = self.action.run({Input.DATE_FORMAT: date_format, Input.STR: string, Input.FILE: file})
        expected = {Output.DATES: expected}
        validate(actual, DateExtractorOutput.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(error_parameters)
    def test_extract_dates_error(
        self, name: str, date_format: str, string: str, file: Dict[str, Any], expected: List[str]
    ) -> None:
        with self.assertRaises(PluginException):
            self.action.run({Input.DATE_FORMAT: date_format, Input.STR: string, Input.FILE: file})
