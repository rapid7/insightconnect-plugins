import sys
import os

sys.path.append(os.path.abspath("../"))
from parameterized import parameterized
from unittest import TestCase
from komand_markdown.actions.markdown_to_txt import MarkdownToTxt
from insightconnect_plugin_runtime.exceptions import PluginException


class TestMarkdownToTxt(TestCase):
    expected_result = {"txt_string": "Rapid7 InsightConnect\n", "txt": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="}
    expected_error = "Input Error"

    def setUp(self) -> None:
        self.action = MarkdownToTxt()

    @parameterized.expand(
        [
            ({"markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q="}, expected_result),
            ({"markdown_string": "# Rapid7 InsightConnect"}, expected_result),
        ]
    )
    def test_markdown_to_txt_valid(self, input_params, expected):
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
    def test_markdown_to_txt_invalid(self, input_params, exception):
        with self.assertRaises(PluginException) as context:
            self.action.run(input_params)
        self.assertEqual(context.exception.cause, exception)
