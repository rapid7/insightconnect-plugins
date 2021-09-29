from unittest import TestCase
from icon_extractit.actions.uuid_extractor import UuidExtractor
from icon_extractit.actions.uuid_extractor.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

parameters = Util.load_parameters("uuid_extractor").get("parameters")


class TestIocExtractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_uuid(self, name, string, file, expected):
        action = UuidExtractor()
        actual = action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.UUIDS: expected}
        self.assertEqual(actual, expected)
