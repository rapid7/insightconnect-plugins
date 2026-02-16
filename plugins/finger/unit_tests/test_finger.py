import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_finger.actions.finger import Finger
from komand_finger.actions.finger.schema import Input


class TestFinger(unittest.TestCase):
    def setUp(self):
        self.action = Finger()

    def test_run_success(self):
        params = {Input.USER: "user", Input.HOST: "host"}
        output = self.action.run(params)
        expected_output = {"found": True, "status": "Success"}
        self.assertEqual(output, expected_output)

    def test_run_invalid_input_exception(self):
        with self.assertRaises(PluginException):
            params = {Input.USER: "invalid/user", Input.HOST: "invalid/host"}
            self.action.run(params)

    @patch("insightconnect_plugin_runtime.helper")
    def test_run_exec_error(self, mock):
        mock.exec_command.side_effect = Exception("exec error")
        with self.assertRaises(PluginException):
            params = {Input.USER: "user", Input.HOST: "host"}
            self.action.run(params)

    def test_validate_input(self):
        self.assertTrue(self.action.validate_input("valid_user-1.2"))
        self.assertFalse(self.action.validate_input("invalid user!"))

    def test_found_error(self):
        result, msg = self.action.found("error in stdout", "error in stderr", ["error"])
        self.assertFalse(result)
        self.assertEqual(msg, "error")

    def test_found_success(self):
        result, msg = self.action.found("all good", "no error", ["notfound"])
        self.assertTrue(result)
        self.assertEqual(msg, "Success")


if __name__ == "__main__":
    unittest.main()
