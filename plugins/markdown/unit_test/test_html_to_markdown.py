import sys
import os

sys.path.append(os.path.abspath("../"))
from parameterized import parameterized
from unittest import TestCase
from icon_markdown.actions.html_to_markdown import HtmlToMarkdown
from icon_markdown.actions.html_to_markdown.schema import Output, Input
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


class TestHtmlToMarkdown(TestCase):
    expected_result_header = {
        Output.MARKDOWN_STRING: "# Rapid7\n",
        Output.MARKDOWN: "IyBSYXBpZDcK",
    }
    expected_result_bold = {Output.MARKDOWN_STRING: "", Output.MARKDOWN: ""}
    expected_error = "Input error"

    def setUp(self) -> None:
        self.action = HtmlToMarkdown()

    @parameterized.expand(
        [
            ({Input.HTML: "PGgxPlJhcGlkNzwvaDE+"}, expected_result_header),
            ({Input.HTML_STRING: "<h1>Rapid7</h1>"}, expected_result_header),
        ]
    )
    def test_html_to_markdown_valid(self, input_params, expected):
        results = self.action.run(input_params)
        validate(results, self.action.output.schema)
        self.assertEqual(results, expected)

    @parameterized.expand(
        [
            (
                {
                    Input.HTML: "PGgxPlJhcGlkNzwvaDE+",
                    Input.HTML_STRING: "<h1>Rapid7</h1>",
                },
                expected_error,
            ),
            ({Input.HTML: "", Input.HTML_STRING: ""}, expected_error),
        ]
    )
    def test_html_to_markdown_invalid(self, input_params, exception):
        with self.assertRaises(PluginException) as context:
            self.action.run(input_params)
        self.assertEqual(context.exception.cause, exception)
