import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_markdown.actions.html_to_markdown import HtmlToMarkdown
import logging


class TestHtmlToMarkdown(TestCase):
    def test_html_to_markdown_valid_markdown(self):
        action = HtmlToMarkdown()
        input_params = {}
        results = action.run(input_params)

        log = logging.getLogger("Test")
        action.logger = log
        expected = {}
        self.assertEqual(results, expected)

    def test_html_to_markdown_valid_markdown_string(self):
        action = HtmlToMarkdown()
        input_params = {}
        results = action.run(input_params)

        log = logging.getLogger("Test")
        action.logger = log
        expected = {}
        self.assertEqual(results, expected)

    def test_html_to_markdown_invalid(self):
        action = HtmlToMarkdown()
        input_params = {}
        results = action.run(input_params)

        log = logging.getLogger("Test")
        action.logger = log

        expected = "Input Error Only one of Markdown or Markdown String can be defined"

        self.assertRaises()
