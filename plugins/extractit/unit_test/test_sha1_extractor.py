import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase

from icon_extractit.actions.sha1_extractor import Sha1Extractor
from icon_extractit.actions.sha1_extractor.schema import Input, Output, Sha1ExtractorOutput
from jsonschema import validate
from parameterized import parameterized

from util import Util

parameters = Util.load_parameters("sha1_extractor").get("parameters")


class TestSha1Extractor(TestCase):
    def setUp(self) -> None:
        self.action = Sha1Extractor()

    @parameterized.expand(parameters)
    def test_extract_sha1(self, name: str, string: str, file: Dict[str, Any], expected: List[str]) -> None:
        actual = self.action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.SHA1: expected}
        validate(actual, Sha1ExtractorOutput.schema)
        self.assertEqual(actual, expected)
