import sys
import os

sys.path.append(os.path.abspath("../"))
from parameterized import parameterized
from unittest import TestCase
from komand_markdown.actions.markdown_to_txt import MarkdownToTxt
import logging


class TestMarkdownToTxt(TestCase):

    # @parameterized.expand([
    #     ({"markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q="}),
    #     ({"markdown_string": "# Rapid7 InsightConnect"})
    # ])
    def test_markdown_to_txt_valid_markdown(self):
        action = MarkdownToTxt()
        input_params = {"markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q="}
        results = action.run(input_params)

        log = logging.getLogger("Test")
        action.logger = log
        expected = {"txt_string": "Rapid7 InsightConnect\n", "txt": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="}
        self.assertEqual(results, expected)

    def test_markdown_to_txt_valid_markdown_string(self):
        action = MarkdownToTxt()
        input_params = {"markdown_string": "# Rapid7 InsightConnect"}
        results = action.run(input_params)

        log = logging.getLogger("Test")
        action.logger = log
        expected = {"txt_string": "Rapid7 InsightConnect\n", "txt": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="}
        self.assertEqual(results, expected)

    def test_markdown_to_txt_invalid_both(self):
        action = MarkdownToTxt()
        input_params = {"markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=", "markdown_string": "# Rapid7 InsightConnect"}
        results = action.run(input_params)

        log = logging.getLogger("Test")
        action.logger = log

        expected = "Input Error Only one of Markdown or Markdown String can be defined"

        self.assertRaises()
