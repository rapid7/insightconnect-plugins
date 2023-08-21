import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase

from icon_extractit.actions.sha512_extractor import Sha512Extractor
from icon_extractit.actions.sha512_extractor.schema import Input, Output, Sha512ExtractorOutput
from jsonschema import validate
from parameterized import parameterized

from util import Util

parameters = Util.load_parameters("sha512_extractor").get("parameters")


class TestSha512Extractor(TestCase):
    def setUp(self) -> None:
        self.action = Sha512Extractor()

    @parameterized.expand(parameters)
    def test_extract_sha512(self, name: str, string: str, file: Dict[str, Any], expected: List[str]) -> None:
        actual = self.action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.SHA512: expected}
        validate(actual, Sha512ExtractorOutput.schema)
        self.assertEqual(actual, expected)
