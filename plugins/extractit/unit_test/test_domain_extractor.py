import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase

from icon_extractit.actions.domain_extractor import DomainExtractor
from icon_extractit.actions.domain_extractor.schema import DomainExtractorOutput, Input, Output
from jsonschema import validate
from parameterized import parameterized

from util import Util

parameters = Util.load_parameters("domain_extractor").get("parameters")


class TestDomainExtractor(TestCase):
    def setUp(self) -> None:
        self.action = DomainExtractor()

    @parameterized.expand(parameters)
    def test_extract_domains(
        self, name: str, string: str, file: Dict[str, Any], include_subdomains: bool, expected: List[str]
    ) -> None:
        actual = self.action.run({Input.STR: string, Input.FILE: file, Input.SUBDOMAIN: include_subdomains})
        expected = {Output.DOMAINS: expected}
        validate(actual, DomainExtractorOutput.schema)
        self.assertEqual(actual, expected)
