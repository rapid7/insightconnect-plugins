import sys
import os

sys.path.append(os.path.abspath("../"))
from parameterized import parameterized
from unittest import TestCase
from icon_markdown.actions.markdown_to_html import MarkdownToHtml
from icon_markdown.actions.markdown_to_html.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


class TestMarkdownToHtml(TestCase):
    expected_result = {
        Output.HTML_STRING: '<h1 id="rapid7-insightconnect">Rapid7 InsightConnect</h1>\n',
        Output.HTML: "PGgxIGlkPSJyYXBpZDctaW5zaWdodGNvbm5lY3QiPlJhcGlkNyBJbnNpZ2h0Q29ubmVjdDwvaDE+Cg==",
    }
    expected_error = "Input error"

    def setUp(self) -> None:
        self.action = MarkdownToHtml()

    @parameterized.expand(
        [
            ({Input.MARKDOWN: "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q="}, expected_result),
            ({Input.MARKDOWN_STRING: "# Rapid7 InsightConnect"}, expected_result),
        ]
    )
    def test_markdown_to_html_valid_markdown(self, input_params, expected):
        results = self.action.run(input_params)
        validate(results, self.action.output.schema)
        self.assertEqual(results, expected)

    @parameterized.expand(
        [
            (
                {
                    Input.MARKDOWN: "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=",
                    Input.MARKDOWN_STRING: "# Rapid7 InsightConnect",
                },
                expected_error,
            ),
            ({Input.MARKDOWN: "", Input.MARKDOWN_STRING: ""}, expected_error),
        ]
    )
    def test_markdown_to_html_invalid(self, input_params, exception):
        with self.assertRaises(PluginException) as context:
            self.action.run(input_params)
        self.assertEqual(context.exception.cause, exception)
