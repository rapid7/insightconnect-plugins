import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase

from icon_extractit.actions.cve_extractor import CveExtractor
from icon_extractit.actions.cve_extractor.schema import CveExtractorOutput, Input, Output
from jsonschema import validate
from parameterized import parameterized

from util import Util

parameters = Util.load_parameters("cve_extractor").get("parameters")


class TestIocExtractor(TestCase):
    def setUp(self) -> None:
        self.action = CveExtractor()

    @parameterized.expand(parameters)
    def test_extract_cves(self, name: str, string: str, file: Dict[str, Any], expected: List[str]) -> None:
        actual = self.action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.CVES: expected}
        validate(actual, CveExtractorOutput.schema)
        self.assertEqual(actual, expected)
