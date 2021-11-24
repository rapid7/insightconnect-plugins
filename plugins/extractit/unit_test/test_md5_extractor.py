from unittest import TestCase
from icon_extractit.actions.md5_extractor import Md5Extractor
from icon_extractit.actions.md5_extractor.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

parameters = Util.load_parameters("md5_extractor").get("parameters")


class TestMd5Extractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_md5(self, name, string, file, expected):
        action = Md5Extractor()
        actual = action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.MD5: expected}
        self.assertEqual(actual, expected)
