import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_html.actions.epub import Epub


class TestEpub(TestCase):
    def test_epub(self):

        params = {"doc": "<!DOCTYPE html><html><body><h1>Rapid7 InsightConnect</h1><p>Convert HTML to EPUB</p></body></html>"}

        test_action = Epub()
        result = test_action.run(params)

        self.assertEqual(
            result['epub'][:10],
              "UEsDBBQAAg"
        )

    def test_action_empty_string(self):
        params = {"doc": " "}

        test_action = Epub()

        with self.assertRaises(PluginException) as context:
            test_action.run(params)
        self.assertEqual(context.exception.cause, "Run: Invalid input.")