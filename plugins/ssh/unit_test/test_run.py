import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_ssh.actions.run import Run
from komand_ssh.actions.run.schema import Output
from unittest.mock import patch
from util import Util


class TestRun(TestCase):
    def setUp(self):
        self.action = Run()
        self.params = {
            "host": "example.com",
            "command": "ls -l",
        }
        self.action.connection = Util.default_connector()

    def mock_execute_command(self):
        file1 = open("./ssh/unit_test/results", "r")
        return file1, file1, file1

    @patch("paramiko.SSHClient.set_missing_host_key_policy", return_value=None)
    @patch("paramiko.SSHClient.load_system_host_keys", return_value=None)
    @patch("paramiko.SSHClient.connect", return_value=None)
    @patch("paramiko.SSHClient.exec_command", side_effect=mock_execute_command)
    def test_run(self, mock_key_policy, mock_host_keys, mock_connect, mock_exec):
        expected = {Output.RESULTS: {"stdout": "/home/vagrant", "stderr": "", "all_output": "/home/vagrant"}}
        actual = self.action.run(self.params)
        self.assertEqual(actual, expected)
