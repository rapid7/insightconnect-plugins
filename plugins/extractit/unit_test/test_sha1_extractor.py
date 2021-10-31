from unittest import TestCase
from icon_extractit.actions.sha1_extractor import Sha1Extractor
from icon_extractit.actions.sha1_extractor.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

parameters = Util.load_parameters("sha1_extractor").get("parameters")


class TestSha1Extractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_sha1(self, name, string, file, expected):
        action = Sha1Extractor()
        actual = action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.SHA1: expected}
        self.assertEqual(actual, expected)
