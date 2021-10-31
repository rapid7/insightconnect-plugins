from unittest import TestCase
from icon_extractit.actions.domain_extractor import DomainExtractor
from icon_extractit.actions.domain_extractor.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

parameters = Util.load_parameters("domain_extractor").get("parameters")


class TestDomainExtractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_domains(self, name, string, file, include_subdomains, expected):
        action = DomainExtractor()
        actual = action.run({Input.STR: string, Input.FILE: file, Input.SUBDOMAIN: include_subdomains})
        expected = {Output.DOMAINS: expected}
        self.assertEqual(actual, expected)
