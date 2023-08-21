import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase

from icon_extractit.actions.uuid_extractor import UuidExtractor
from icon_extractit.actions.uuid_extractor.schema import Input, Output, UuidExtractorOutput
from jsonschema import validate
from parameterized import parameterized

from util import Util

parameters = Util.load_parameters("uuid_extractor").get("parameters")


class TestIocExtractor(TestCase):
    def setUp(self) -> None:
        self.action = UuidExtractor()

    @parameterized.expand(parameters)
    def test_extract_uuid(self, name: str, string: str, file: Dict[str, Any], expected: List[str]) -> None:
        actual = self.action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.UUIDS: expected}
        validate(actual, UuidExtractorOutput.schema)
        self.assertEqual(actual, expected)
