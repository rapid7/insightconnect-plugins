import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase

from icon_extractit.actions.ioc_extractor import IocExtractor
from icon_extractit.actions.ioc_extractor.schema import Input, IocExtractorOutput, Output
from jsonschema import validate
from parameterized import parameterized

from util import Util

parameters = Util.load_parameters("ioc_extractor").get("parameters")


class TestIocExtractor(TestCase):
    def setUp(self) -> None:
        self.action = IocExtractor()

    @parameterized.expand(parameters)
    def test_extract_iocs(self, name: str, string: str, file: Dict[str, Any], expected: List[str]) -> None:
        actual = self.action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.IOCS: expected}
        validate(actual, IocExtractorOutput.schema)
        self.assertEqual(actual, expected)
