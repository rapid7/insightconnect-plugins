import sys

sys.path.append("../")

from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_basename.actions.basename import Basename
from komand_basename.actions.basename.schema import Input


class TestBasename(TestCase):
    def test_basename(self):
        action = Basename()
        expected = {"basename": "text.txt"}
        result = action.run({Input.PATH: "example/text.txt"})
        self.assertEqual(result, expected)

    def test_basename_failure(self):
        action = Basename()
        cause = "Unable to find basename."
        assistance = "Not able to retrieve basename of example/."
        with self.assertRaises(PluginException) as error:
            action.run({Input.PATH: "example/"})
        self.assertEqual(cause, error.exception.cause)
        self.assertEqual(assistance, error.exception.assistance)
