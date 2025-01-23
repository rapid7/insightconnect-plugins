import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from komand_ssh.actions.run import Run
from komand_ssh.actions.run.schema import Input, Output

from util import Util

STUB_PARAMETERS = {Input.HOST: "example.com", Input.COMMAND: "ls -l"}


class TestRun(TestCase):
    def setUp(self):
        self.action = Util.default_connector(Run())

    @patch("paramiko.SSHClient.connect", return_value=None)
    @patch("paramiko.SSHClient.exec_command", side_effect=Util.mock_execute_command)
    def test_run(self, mock_connect: MagicMock, mock_exec: MagicMock) -> None:
        response = self.action.run(STUB_PARAMETERS)
        expected = {Output.RESULTS: {"stdout": "/home/vagrant", "stderr": "", "all_output": "/home/vagrant"}}
        self.assertEqual(response, expected)
        mock_connect.assert_called()
        mock_exec.assert_called()
