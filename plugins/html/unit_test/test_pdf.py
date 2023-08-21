import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_html.actions.pdf import Pdf


class TestPdf(TestCase):
    def test_pdf(self):

        params = {"doc": "<!DOCTYPE html><html><body><h1>Rapid7 InsightConnect</h1><p>Convert HTML to PDF</p></body></html>"}

        test_action = Pdf()
        result = test_action.run(params)

        self.assertEqual(
            result['pdf'][:15],
                 "JVBERi0xLjUKJdDUxdgK"
        )

    def test_action_empty_string(self):
        params = {"doc": " "}

        test_action = Pdf()

        with self.assertRaises(PluginException) as context:
            test_action.run(params)
        self.assertEqual(context.exception.cause, "Run: Invalid input.")
