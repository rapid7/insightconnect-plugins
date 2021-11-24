from unittest import TestCase
from icon_extractit.actions.mac_extractor import MacExtractor
from icon_extractit.actions.mac_extractor.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

parameters = Util.load_parameters("mac_extractor").get("parameters")


class TestMacExtractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_mac_addresses(self, name, string, file, expected):
        action = MacExtractor()
        actual = action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.MAC_ADDRS: expected}
        self.assertEqual(actual, expected)
