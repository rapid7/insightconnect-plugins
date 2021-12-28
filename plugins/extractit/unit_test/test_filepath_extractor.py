from unittest import TestCase
from icon_extractit.actions.filepath_extractor import FilepathExtractor
from icon_extractit.actions.filepath_extractor.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

parameters = Util.load_parameters("filepath_extractor").get("parameters")


class TestFilepathExtractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_filepath(self, name, string, file, expected):
        action = FilepathExtractor()
        actual = action.run({Input.STR: string, Input.FILE: file})
        expected = {Output.FILEPATHS: expected}
        self.assertEqual(actual, expected)
