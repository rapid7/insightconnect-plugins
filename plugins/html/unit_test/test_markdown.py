import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_html.actions.markdown import Markdown
from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


class TestMarkdown(TestCase):
    def test_markdown(self):
        params = {
            "doc": "<!DOCTYPE html><html><body>Rapid7 InsightConnect<p>Convert HTML to Markdown</p></body></html>"
        }

        test_action = Markdown()
        result = test_action.run(params)

        self.assertEqual(
            result,
            {
                "markdown_contents": "Rapid7 InsightConnect\n\nConvert HTML to Markdown\n",
                "markdown_file": "UmFwaWQ3IEluc2lnaHRDb25uZWN0CgpDb252ZXJ0IEhUTUwgdG8gTWFya2Rvd24K",
            },
        )

    def test_html_with_header_tags(self):
        params = {
            "doc": "<!DOCTYPE html><html><body><h1>Rapid7 InsightConnect</h1><p>Convert HTML to Markdown</p></body></html>"
        }

        test_action = Markdown()
        result = test_action.run(params)
        print(result)

        self.assertEqual(
            result["markdown_contents"],
            "Rapid7 InsightConnect\n=====================\n\nConvert HTML to Markdown\n",
        )

        self.assertEqual(
            result["markdown_file"],
            "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cj09PT09PT09PT09PT09PT09PT09PQoKQ29udmVydCBIVE1MIHRvIE1hcmtkb3duCg==",
        )

    def test_markdown_cloud(self):
        params = {"doc": '<!DOCTYPE html><html><iframe src="https://www.google.com"></iframe></html>'}

        os.environ["PLUGIN_RUNTIME_ENVIRONMENT"] = "cloud"
        test_action = Markdown()
        result = test_action.run(params)
        del os.environ["PLUGIN_RUNTIME_ENVIRONMENT"]

        self.assertEqual(result["markdown_file"], "Cg==")
        self.assertEqual(result["markdown_contents"], "\n")


def test_action_empty_string(self):
    params = {"doc": " "}

    test_action = Markdown()

    with self.assertRaises(PluginException) as context:
        test_action.run(params)
    self.assertEqual(context.exception.cause, "Invalid input.")
