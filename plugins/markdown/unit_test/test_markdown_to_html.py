import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_markdown.connection.connection import Connection
from komand_markdown.actions.markdown_to_html import MarkdownToHtml
import json
import logging


class TestMarkdownToHtml(TestCase):
    def test_markdown_to_html_valid_markdown(self):
        return

    def test_markdown_to_html_valid_markdown_string(self):
        return

    def test_markdown_to_html_invalid(self):
        return
