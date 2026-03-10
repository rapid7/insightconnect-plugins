import sys
import os

sys.path.append(os.path.abspath("../"))
from parameterized import parameterized
from unittest import TestCase
from icon_markdown.actions.markdown_to_txt import MarkdownToTxt
from icon_markdown.actions.markdown_to_txt.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


class TestMarkdownToTxt(TestCase):
    expected_result = {
        Output.TXT_STRING: "Rapid7 InsightConnect\n",
        Output.TXT: "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
    }
    expected_error = "Input Error"

    def setUp(self) -> None:
        self.action = MarkdownToTxt()

    @parameterized.expand(
        [
            ({Input.MARKDOWN: "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q="}, expected_result),
            (
                {Input.MARKDOWN_STRING: "# Rapid7 InsightConnect", "markdown": ""},
                expected_result,
            ),
        ]
    )
    def test_markdown_to_txt_valid(self, input_params, expected):
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
    def test_markdown_to_txt_invalid(self, input_params, exception):
        with self.assertRaises(PluginException) as context:
            self.action.run(input_params)
        self.assertEqual(context.exception.cause, exception)
