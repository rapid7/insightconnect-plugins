import unittest
from unittest import TestCase
from unittest.mock import patch, MagicMock
from jsonschema import validate
from icon_jq.actions.run_jq import RunJq


class TestRunJq(TestCase):

    def setUp(self) -> None:
        self.action = RunJq()

    @patch("subprocess.Popen")
    def test_run_jq_action(self, mock_popen):
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
