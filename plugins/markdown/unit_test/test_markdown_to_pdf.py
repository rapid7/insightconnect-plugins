import sys
import os

sys.path.append(os.path.abspath("../"))
from parameterized import parameterized
from unittest import TestCase
from komand_markdown.actions.markdown_to_pdf import MarkdownToPdf
from insightconnect_plugin_runtime.exceptions import PluginException


class TestMarkdownToPdf(TestCase):

    expected_result = {
        "pdf_string": "%PDF-1.4\n%\u00e2\u00e3\n1 0 obj\n<<\n/Title ()\n/Creator()",
        "pdf": "JVBERi0xLjQKJcOiw6MKMSAwIG9iago8PAovVGl0bGUgKCkKL0NyZWF0b3IgKO+/v",
    }
    expected_error = "Input error"

    def setUp(self) -> None:
        self.action = MarkdownToPdf()

    @parameterized.expand(
        [
            ({"markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q="}, expected_result),
            ({"markdown_string": "# Rapid7 InsightConnect"}, expected_result),
        ]
    )
    def test_markdown_to_pdf_valid(self, input_params, expected):
        results = self.action.run(input_params)
        self.assertEqual(results, expected)

    @parameterized.expand(
        [
            ({"markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=", "markdown_string": "# Rapid7 InsightConnect"}),
            ({"markdown": "", "markdown_string": ""}),
        ]
    )
    def test_markdown_to_pdf_invalid(self, input_params, exception):
        with self.assertRaises(PluginException) as context:
            self.action.run(input_params)
        self.assertEqual(context.exception.cause, exception)
