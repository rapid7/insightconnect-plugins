import sys
import os

sys.path.append(os.path.abspath("../"))
from parameterized import parameterized
from unittest import TestCase
from komand_markdown.actions.markdown_to_html import MarkdownToHtml
from insightconnect_plugin_runtime.exceptions import PluginException


class TestMarkdownToHtml(TestCase):
    expected_result = {
        "html_string": '<h1 id="rapid7-insightconnect">Rapid7 InsightConnect</h1>\n',
        "html": "PGgxIGlkPSJyYXBpZDctaW5zaWdodGNvbm5lY3QiPlJhcGlkNyBJbnNpZ2h0Q29ubmVjdDwvaDE+Cg==",
    }
    expected_error = "Input error"

    def setUp(self) -> None:
        self.action = MarkdownToHtml()

    @parameterized.expand(
        [
            ({"markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q="}, expected_result),
            ({"markdown_string": "# Rapid7 InsightConnect"}, expected_result),
        ]
    )
    def test_markdown_to_html_valid_markdown(self, input_params, expected):
        results = self.action.run(input_params)
        self.assertEqual(results, expected)

    @parameterized.expand(
        [
            (
                {"markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=", "markdown_string": "# Rapid7 InsightConnect"},
                expected_error,
            ),
            ({"markdown": "", "markdown_string": ""}, expected_error),
        ]
    )
    def test_markdown_to_html_invalid(self, input_params, exception):
        with self.assertRaises(PluginException) as context:
            self.action.run(input_params)
        self.assertEqual(context.exception.cause, exception)
