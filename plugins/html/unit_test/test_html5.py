from unittest import TestCase
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_html.actions.html5 import Html5


class TestHtml5(TestCase):
    def test_run(self):
        params = {"doc": "<p>That's a failure</p>"}

        test_action = Html5()
        result = test_action.run(params)

        self.assertEqual(
            result,
            {
                "html5_contents": "<p>\nThat’s a failure\n</p>\n",
                "html5_file": "PHA+ClRoYXTigJlzIGEgZmFpbHVyZQo8L3A+Cg==",
            },
        )

    def test_action_empty_string(self):
        params = {"doc": " "}

        test_action = Html5()

        with self.assertRaises(PluginException) as context:
            test_action.run(params)
        self.assertEqual(context.exception.cause, "Run: Invalid input.")
