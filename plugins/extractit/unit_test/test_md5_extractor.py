import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase

from icon_extractit.actions.md5_extractor import Md5Extractor
from icon_extractit.actions.md5_extractor.schema import Input, Md5ExtractorOutput, Output
from jsonschema import validate
from parameterized import parameterized

from util import Util

parameters = Util.load_parameters("md5_extractor").get("parameters")


class TestMd5Extractor(TestCase):
    def setUp(self) -> None:
        self.action = Md5Extractor()

    @parameterized.expand(parameters)
    def test_extract_md5(self, name: str, string: str, file: Dict[str, Any], expected: List[str]) -> None:
        actual = self.action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.MD5: expected}
        validate(actual, Md5ExtractorOutput.schema)
        self.assertEqual(actual, expected)
