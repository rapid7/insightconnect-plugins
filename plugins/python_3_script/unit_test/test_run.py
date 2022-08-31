import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from icon_python_3_script.actions.run import Run


@patch.object(Run, "_exec_python_function", side_effect=Util.mock_exec_python_function)
class TestRun(TestCase):
    @parameterized.expand(
        [
            [
                Util.read_file_to_dict(f"inputs/connection_with_credentials.json.inp"),
                Util.read_file_to_dict(f"inputs/run_with_credentials.json.inp"),
                Util.read_file_to_dict(f"payloads/run_with_credentials.json.exp"),
            ],
            [
                Util.read_file_to_dict(f"inputs/connection_no_credentials.json.inp"),
                Util.read_file_to_dict(f"inputs/run_no_credentials.json.inp"),
                Util.read_file_to_dict(f"payloads/run_no_credentials.json.exp"),
            ],
        ]
    )
    def test_run(self, mock_exec_python_function, connection_params, action_params, expected):
        action = Util.default_connector(Run(), connection_params)
        actual = action.run(params=action_params)

        self.assertEqual(actual, expected)

    def test_run_return_none(self, mock_exec_python_function):
        params = Util.read_file_to_dict(f"inputs/run.bad.json.inp")
        action = Util.default_connector(Run())
        with self.assertRaises(PluginException) as e:
            action.run(params=params)

        self.assertEqual(e.exception.cause, "Output type was None")
        self.assertEqual(e.exception.assistance, "Ensure that output has a non-None data type")
