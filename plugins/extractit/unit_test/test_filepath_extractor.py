import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase

from icon_extractit.actions.filepath_extractor import FilepathExtractor
from icon_extractit.actions.filepath_extractor.schema import FilepathExtractorOutput, Input, Output
from jsonschema import validate
from parameterized import parameterized

from util import Util

parameters = Util.load_parameters("filepath_extractor").get("parameters")


class TestFilepathExtractor(TestCase):
    def setUp(self) -> None:
        self.action = FilepathExtractor()

    @parameterized.expand(parameters)
    def test_extract_filepath(self, name: str, string: str, file: Dict[str, Any], expected: List[str]) -> None:
        actual = self.action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.FILEPATHS: expected}
        validate(actual, FilepathExtractorOutput.schema)
        self.assertEqual(actual, expected)
