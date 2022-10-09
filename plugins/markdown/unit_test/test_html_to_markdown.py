import sys
import os

sys.path.append(os.path.abspath("../"))
from parameterized import parameterized
from unittest import TestCase
from komand_markdown.actions.html_to_markdown import HtmlToMarkdown
from insightconnect_plugin_runtime.exceptions import PluginException

class TestHtmlToMarkdown(TestCase):
    expected_result = {"markdown_string": "# Rapid7\n", "markdown": "IyBSYXBpZDcK"}
    expected_error = "Input error"

    def setUp(self) -> None:
        self.action = HtmlToMarkdown()

    @parameterized.expand(
        [({"html": "PGgxPlJhcGlkNzwvaDE+"}, expected_result), ({"html_string": "<h1>Rapid7</h1>"}, expected_result)]
    )
    def test_html_to_markdown_valid(self, input_params, expected):
        results = self.action.run(input_params)
        self.assertEqual(results, expected)

    @parameterized.expand([
        ({"html": "PGgxPlJhcGlkNzwvaDE+", "html_string": "<h1>Rapid7</h1>"}, expected_error),
        ({"html": "", "html_string": ""}, expected_error)
    ])
    def test_html_to_markdown_invalid(self, input_params, exception):
        with self.assertRaises(PluginException) as context:
            self.action.run(input_params)
        self.assertEqual(context.exception.cause, exception)