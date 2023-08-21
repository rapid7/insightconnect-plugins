import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase

from icon_extractit.actions.mac_extractor import MacExtractor
from icon_extractit.actions.mac_extractor.schema import Input, MacExtractorOutput, Output
from jsonschema import validate
from parameterized import parameterized

from util import Util

parameters = Util.load_parameters("mac_extractor").get("parameters")


class TestMacExtractor(TestCase):
    def setUp(self) -> None:
        self.action = MacExtractor()

    @parameterized.expand(parameters)
    def test_extract_mac_addresses(self, name: str, string: str, file: Dict[str, Any], expected: List[str]) -> None:
        actual = self.action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.MAC_ADDRS: expected}
        validate(actual, MacExtractorOutput.schema)
        self.assertEqual(actual, expected)
