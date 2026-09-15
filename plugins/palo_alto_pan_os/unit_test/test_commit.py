import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import patch, MagicMock

from jsonschema import validate
from komand_palo_alto_pan_os.actions.commit import Commit
from komand_palo_alto_pan_os.actions.commit.schema import CommitInput, CommitOutput, Input
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
@patch("requests.get", side_effect=Util.mocked_requests)
class TestCommit(TestCase):
    @parameterized.expand(
        [
            [
                "no_changes",
                "",
                "<commit></commit>",
                {
                    "response": {
                        "@status": "success",
                        "@code": "19",
                        "result": {"msg": "There are no changes to commit."},
                    }
                },
            ],
            [
                "partial",
                "partial",
                "<commit><partial><admin><member>admin-name</member></admin></partial></commit>",
                {
                    "response": {
                        "@status": "success",
                        "@code": "19",
                        "result": {"msg": {"line": "Commit job enqueued with jobid 10"}, "job": "10"},
                    }
                },
            ],
        ]
    )
    def test_commit(
        self,
        mock_get: MagicMock,
        mock_get2: MagicMock,
        name: str,
        commit_action: str,
        cmd: str,
        expected: dict,
    ) -> None:
        action = Util.default_connector(Commit())
        input_data = {Input.ACTION: commit_action, Input.CMD: cmd}
        validate(input_data, CommitInput.schema)
        actual = action.run(input_data)
        self.assertEqual(actual, expected)
        validate(actual, CommitOutput.schema)

    @parameterized.expand(
        [
            # PAN-OS documents a plain commit of the candidate configuration as no action at all, so
            # the key has to be absent from the querystring rather than blank
            ["blank_action", {Input.CMD: "<commit></commit>"}, None, "<commit></commit>"],
            ["empty_action", {Input.ACTION: "", Input.CMD: "<commit></commit>"}, None, "<commit></commit>"],
            ["blank_cmd", {}, None, "<commit></commit>"],
            ["empty_cmd", {Input.ACTION: "", Input.CMD: ""}, None, "<commit></commit>"],
            # 'all' is a Panorama commit-all selector. Published workflows hold it because it used to
            # be the default, so it is dropped when the command is not a commit-all
            [
                "all_action_on_a_firewall_commit",
                {Input.ACTION: "all", Input.CMD: "<commit></commit>"},
                None,
                "<commit></commit>",
            ],
            ["all_action_with_no_cmd", {Input.ACTION: "all"}, None, "<commit></commit>"],
            [
                "partial_action",
                {
                    Input.ACTION: "partial",
                    Input.CMD: "<commit><partial><admin><member>admin-name</member></admin></partial></commit>",
                },
                "partial",
                "<commit><partial><admin><member>admin-name</member></admin></partial></commit>",
            ],
            # A commit-all command is not turned into a Panorama commit-all on its own: the action has
            # to say so, so that the action given is always the action sent
            [
                "commit_all_cmd_without_action",
                {
                    Input.CMD: "<commit-all><shared-policy><device-group><entry name='dg1'/></device-group></shared-policy></commit-all>"
                },
                None,
                "<commit-all><shared-policy><device-group><entry name='dg1'/></device-group></shared-policy></commit-all>",
            ],
            [
                "commit_all_cmd_with_action",
                {
                    Input.ACTION: "all",
                    Input.CMD: " <commit-all><shared-policy><device-group><entry name='dg1'/></device-group></shared-policy></commit-all>",
                },
                "all",
                " <commit-all><shared-policy><device-group><entry name='dg1'/></device-group></shared-policy></commit-all>",
            ],
        ]
    )
    def test_commit_querystring(
        self,
        mock_get: MagicMock,
        mock_get2: MagicMock,
        name: str,
        input_data: dict,
        expected_action: str,
        expected_cmd: str,
    ) -> None:
        action = Util.default_connector(Commit())
        validate(input_data, CommitInput.schema)
        actual = action.run(input_data)
        validate(actual, CommitOutput.schema)

        self.assertEqual(len(Util.calls), 1)
        self.assertEqual(Util.calls[0].get("type"), "commit")
        self.assertEqual(Util.calls[0].get("cmd"), expected_cmd)
        if expected_action is None:
            self.assertNotIn("action", Util.calls[0])
        else:
            self.assertEqual(Util.calls[0].get("action"), expected_action)
