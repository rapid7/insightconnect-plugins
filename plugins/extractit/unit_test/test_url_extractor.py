from unittest import TestCase
from icon_extractit.actions.url_extractor import UrlExtractor
from icon_extractit.actions.url_extractor.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

parameters = Util.load_parameters("url_extractor").get("parameters")


class TestUrlExtractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_urls(self, name, string, file, keep_original_urls, expected):
        action = UrlExtractor()
        actual = action.run({Input.STR: string, Input.FILE: file, Input.KEEP_ORIGINAL_URLS: keep_original_urls})
        expected = {Output.URLS: expected}
        self.assertEqual(expected, actual)
