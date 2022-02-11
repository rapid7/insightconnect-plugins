import sys
import os
from unittest import TestCase
from unittest.mock import patch

from komand.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from komand_python_3_script.actions.run import Run


class TestRun(TestCase):
    @patch.object(Run, "_exec_python_function", side_effect=Util.mock_exec_python_function)
    def test_run(self, mock_exec_python_function):
        params = Util.read_file_to_dict(f"inputs/run.json.resp")
        action = Util.default_connector(Run())
        actual = action.run(params=params)

        expected = Util.read_file_to_dict(f"payloads/run.json.resp")
        self.assertEqual(actual, expected)

    @patch.object(Run, "_exec_python_function", side_effect=Util.mock_exec_python_function)
    def test_run_return_none(self, mock_exec_python_function):
        params = Util.read_file_to_dict(f"inputs/run.bad.json.resp")
        action = Util.default_connector(Run())
        with self.assertRaises(PluginException) as e:
            action.run(params=params)

        self.assertEqual(e.exception.cause, "Output type was None")
        self.assertEqual(e.exception.assistance, "Ensure that output has a non-None data type")
