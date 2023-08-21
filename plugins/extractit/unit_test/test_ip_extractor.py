import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase

from icon_extractit.actions.ip_extractor import IpExtractor
from icon_extractit.actions.ip_extractor.schema import Input, IpExtractorOutput, Output
from jsonschema import validate
from parameterized import parameterized

from util import Util

parameters = Util.load_parameters("ip_extractor").get("parameters")


class TestIpExtractor(TestCase):
    def setUp(self) -> None:
        self.action = IpExtractor()

    @parameterized.expand(parameters)
    def test_extract_ips_from_string(self, name: str, string: str, file: Dict[str, Any], expected: List[str]) -> None:
        actual = self.action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.IP_ADDRS: expected}
        validate(actual, IpExtractorOutput.schema)
        self.assertEqual(actual, expected)
