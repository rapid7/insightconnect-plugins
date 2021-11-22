from unittest import TestCase
from icon_extractit.actions.sha512_extractor import Sha512Extractor
from icon_extractit.actions.sha512_extractor.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

parameters = Util.load_parameters("sha512_extractor").get("parameters")


class TestSha512Extractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_sha512(self, name, string, file, expected):
        action = Sha512Extractor()
        actual = action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.SHA512: expected}
        self.assertEqual(actual, expected)
