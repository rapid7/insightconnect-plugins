import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from komand_ssh.actions.run import Run
from komand_ssh.actions.run.schema import Input, Output
from komand_ssh.util.constants import DEFAULT_ENCODING, MAX_COMMAND_ARG_BYTES

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

    @patch("paramiko.SSHClient.connect", return_value=None)
    @patch("paramiko.SSHClient.exec_command")
    def test_run_large_command_sent_via_stdin(self, mock_exec: MagicMock, mock_connect: MagicMock) -> None:
        streams = Util.mock_execute_command("/bin/sh -s")
        mock_exec.return_value = streams
        large_command = "A" * MAX_COMMAND_ARG_BYTES
        params = {Input.HOST: "example.com", Input.COMMAND: large_command}

        response = self.action.run(params)

        expected = {Output.RESULTS: {"stdout": "/home/vagrant", "stderr": "", "all_output": "/home/vagrant"}}
        self.assertEqual(response, expected)
        mock_exec.assert_called_with("/bin/sh -s")

        # The command itself must reach the remote shell over stdin, and the write side must be closed
        stdin = streams[0]
        stdin.write.assert_called_once_with(large_command.encode(DEFAULT_ENCODING))
        stdin.flush.assert_called_once()
        stdin.channel.shutdown_write.assert_called_once()

    @patch("paramiko.SSHClient.connect", return_value=None)
    @patch("paramiko.SSHClient.exec_command", side_effect=Util.mock_execute_command)
    def test_run_does_not_raise_on_nonzero_exit_status(self, mock_exec: MagicMock, mock_connect: MagicMock) -> None:
        # Exit status is logged, not raised: $success semantics are unchanged by this fix.
        mock_exec.side_effect = lambda command: Util.mock_execute_command(command, exit_status=7)
        response = self.action.run(STUB_PARAMETERS)
        self.assertEqual(response[Output.RESULTS]["stdout"], "/home/vagrant")
