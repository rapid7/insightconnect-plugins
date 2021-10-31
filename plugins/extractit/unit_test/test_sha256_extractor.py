from unittest import TestCase
from icon_extractit.actions.sha256_extractor import Sha256Extractor
from icon_extractit.actions.sha256_extractor.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

parameters = Util.load_parameters("sha256_extractor").get("parameters")


class TestSha256Extractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_sha256(self, name, string, file, expected):
        action = Sha256Extractor()
        actual = action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.SHA256: expected}
        self.assertEqual(actual, expected)
