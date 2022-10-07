import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_markdown.actions.markdown_to_html import MarkdownToHtml
import logging


class TestMarkdownToHtml(TestCase):
    def test_markdown_to_html_valid_markdown(self):
        action = MarkdownToHtml()
        input_params = {"markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q="}
        results = action.run(input_params)

        log = logging.getLogger("Test")
        action.logger = log
        expected = {}
        self.assertEqual(results, expected)

    def test_markdown_to_html_valid_markdown_string(self):
        action = MarkdownToHtml()
        input_params = {"markdown_string": "# Rapid7 InsightConnect"}
        results = action.run(input_params)

        log = logging.getLogger("Test")
        action.logger = log
        expected = {}
        self.assertEqual(results, expected)

    def test_markdown_to_html_invalid(self):
        action = MarkdownToHtml()
        input_params = {"markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=", "markdown_string": "# Rapid7 InsightConnect"}
        results = action.run(input_params)

        log = logging.getLogger("Test")
        action.logger = log

        expected = "Input Error Only one of Markdown or Markdown String can be defined"

        self.assertRaises()
