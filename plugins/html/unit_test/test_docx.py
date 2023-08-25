import sys
import os
from unittest import TestCase
from icon_html.actions.docx import Docx
from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


class TestDocx(TestCase):
    def test_docx(self):
        params = {
            "doc": "<!DOCTYPE html><html><body><h1>Rapid7 InsightConnect</h1><p>Convert HTML to DOCX</p></body></html>"
        }

        test_action = Docx()
        result = test_action.run(params)

        self.assertEqual(result["docx"][:10], "UEsDBBQAAg")

    def test_action_empty_string(self):
        params = {"doc": " "}

        test_action = Docx()

        with self.assertRaises(PluginException):
            test_action.run(params)

    def test_bad_input(self):
        params = {"doc": "docx bad input"}

        test_action = Docx()

        with self.assertRaises(PluginException) as context:
            test_action.run(params)
        self.assertEqual(context.exception.cause, "Run: Invalid input.")
