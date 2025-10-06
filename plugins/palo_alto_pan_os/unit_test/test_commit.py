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
