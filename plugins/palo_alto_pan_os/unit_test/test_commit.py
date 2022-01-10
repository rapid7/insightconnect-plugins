import sys
import os
from unittest import TestCase
from komand_palo_alto_pan_os.actions.commit import Commit
from komand_palo_alto_pan_os.actions.commit.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
@patch("requests.get", side_effect=Util.mocked_requests)
class TestCommit(TestCase):
    @parameterized.expand(
        [
            [
                "no_changes",
                None,
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
    def test_commit(self, mock_get, mock_get2, name, commit_action, cmd, expected):
        action = Util.default_connector(Commit())
        actual = action.run({Input.ACTION: commit_action, Input.CMD: cmd})
        self.assertEqual(actual, expected)
