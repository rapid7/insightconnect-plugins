from unittest import TestCase
from icon_extractit.actions.ip_extractor import IpExtractor
from icon_extractit.actions.ip_extractor.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

parameters = Util.load_parameters("ip_extractor").get("parameters")


class TestIpExtractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_ips_from_string(self, name, string, file, expected):
        action = IpExtractor()
        actual = action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.IP_ADDRS: expected}
        self.assertEqual(actual, expected)
