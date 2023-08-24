import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase

from icon_extractit.actions.extract_all import ExtractAll
from icon_extractit.actions.extract_all.schema import ExtractAllOutput, Input, Output
from jsonschema import validate
from parameterized import parameterized

from util import Util

parameters = Util.load_parameters("extract_all").get("parameters")


class TestIocExtractor(TestCase):
    def setUp(self) -> None:
        self.action = ExtractAll()

    @parameterized.expand(parameters)
    def test_extract_all(
        self, name: str, date_format: str, string: str, file: Dict[str, Any], expected: List[str]
    ) -> None:
        actual = self.action.run({Input.DATE_FORMAT: date_format, Input.STR: string, Input.FILE: file})
        expected = {Output.INDICATORS: expected}
        validate(actual, ExtractAllOutput.schema)
        self.assertEqual(actual, expected)
