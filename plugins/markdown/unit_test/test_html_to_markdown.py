import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_markdown.connection.connection import Connection
from komand_markdown.actions.html_to_markdown import HtmlToMarkdown
import json
import logging


class TestHtmlToMarkdown(TestCase):
    def test_html_to_markdown_valid_markdown(self):
        return

    def test_html_to_markdown_valid_markdown_string(self):
        return

    def test_html_to_markdown_invalid(self):
        return
