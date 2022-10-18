import sys
import os

sys.path.append(os.path.abspath("../"))
from parameterized import parameterized
from unittest import TestCase
from komand_markdown.actions.markdown_to_pdf import MarkdownToPdf
from insightconnect_plugin_runtime.exceptions import PluginException


class TestMarkdownToPdf(TestCase):
    # TODO - Import the expected results from a json file
    expected_error = "Input error"

    def setUp(self) -> None:
        self.action = MarkdownToPdf()

    # TODO - Write parameterized test for valid inputs

    @parameterized.expand(
        [
            (
                {"markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=", "markdown_string": "# Rapid7 InsightConnect"},
                expected_error,
            ),
            ({"markdown": "", "markdown_string": ""}, expected_error),
        ]
    )
    def test_markdown_to_pdf_invalid(self, input_params, exception):
        with self.assertRaises(PluginException) as context:
            self.action.run(input_params)
        self.assertEqual(context.exception.cause, exception)
