import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_extractit.actions.url_extractor import UrlExtractor
from icon_extractit.actions.url_extractor.schema import Input, Output
from unit_test.util import Util
from icon_extractit.util.extractor import remove_extracted_urls_from_links
from parameterized import parameterized

parameters = Util.load_parameters("url_extractor").get("parameters", {})


class TestUrlExtractor(TestCase):
    @parameterized.expand(parameters)
    def test_extract_urls(self, name, string, file, keep_original_urls, expected):
        action = UrlExtractor()
        actual = action.run({Input.STR: string, Input.FILE: file, Input.KEEP_ORIGINAL_URLS: keep_original_urls})
        expected = {Output.URLS: expected}
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            (
                [
                    "https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital",
                    "http://example.com/?url=http://example.com",
                    "http://example3.com/?url=http://example.com",
                    "http://example.com",
                    "https://example.com/api?url=http://example2.com/QWekqjwekj23$!@412kj4?q=Test+test==&amp",
                    "http://example2.com/QWekqjwekj23$!@412kj4?q=Test+test==&amp",
                ],
                [
                    "https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital",
                    "http://example.com/?url=http://example.com",
                    "http://example3.com/?url=http://example.com",
                    "https://example.com/api?url=http://example2.com/QWekqjwekj23$!@412kj4?q=Test+test==&amp",
                ],
            )
        ]
    )
    def test_remove_extracted_urls_from_links(self, input_list_of_urls, expected):
        self.assertEqual(expected, remove_extracted_urls_from_links(input_list_of_urls))
