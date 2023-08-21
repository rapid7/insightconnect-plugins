import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase

from icon_extractit.actions.sha256_extractor import Sha256Extractor
from icon_extractit.actions.sha256_extractor.schema import Input, Output, Sha256ExtractorOutput
from jsonschema import validate
from parameterized import parameterized

from util import Util

parameters = Util.load_parameters("sha256_extractor").get("parameters")


class TestSha256Extractor(TestCase):
    def setUp(self) -> None:
        self.action = Sha256Extractor()

    @parameterized.expand(parameters)
    def test_extract_sha256(self, name: str, string: str, file: Dict[str, Any], expected: List[str]) -> None:
        actual = self.action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.SHA256: expected}
        validate(actual, Sha256ExtractorOutput.schema)
        self.assertEqual(actual, expected)
