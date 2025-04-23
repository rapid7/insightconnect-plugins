import unittest
from unittest import TestCase
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from icon_jq.actions.run_jq import RunJq


class TestRunJq(TestCase):

    def setUp(self) -> None:
        self.action = RunJq()

    @patch("subprocess.Popen")
    def test_valid_jq(self, mock_popen):
        mock_process = MagicMock()
        mock_process.communicate.return_value = (b'"Alice"', b"")
        mock_process.returncode = 0
        mock_popen.return_value = mock_process

        input_param = {
            "json_in": {"user": {"name": "Alice", "age": 30}},
            "flags": [],
            "filter": ".user.name",
            "timeout": 1,
        }

        validate(input_param, self.action.input.schema)

        expected = {"json_out": '"Alice"'}

        actual = self.action.run(input_param)
        validate(actual, self.action.output.schema)

        self.assertEqual(expected, actual)

    @patch("subprocess.Popen")
    def test_unsupported_flag(self, mock_popen):

        input_param = {
            "json_in": {"user": {"name": "Alice", "age": 30}},
            "flags": ["--rawfile"],  # Unsupported flag
            "filter": ".user.name",
            "timeout": 1,
        }

        with self.assertRaises(PluginException) as context:
            self.action.run(input_param)

        self.assertIn(
            "The following flag(s) are not supported: ['--rawfile']",
            str(context.exception),
        )
