from unittest import TestCase
from icon_extractit.actions.cve_extractor import CveExtractor
from icon_extractit.actions.cve_extractor.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

parameters = Util.load_parameters("cve_extractor").get("parameters")


class TestIocExtractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_cves(self, name, string, file, expected):
        action = CveExtractor()
        actual = action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.CVES: expected}
        self.assertEqual(actual, expected)
