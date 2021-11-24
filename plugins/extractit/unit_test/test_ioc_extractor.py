from unittest import TestCase
from icon_extractit.actions.ioc_extractor import IocExtractor
from icon_extractit.actions.ioc_extractor.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

parameters = Util.load_parameters("ioc_extractor").get("parameters")


class TestIocExtractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_iocs(self, name, string, file, expected):
        action = IocExtractor()
        actual = action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.IOCS: expected}
        self.assertEqual(actual, expected)
