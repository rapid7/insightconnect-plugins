import sys
import os
from unittest import TestCase
from komand_palo_alto_pan_os.actions.op import Op
from komand_palo_alto_pan_os.actions.op.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestOp(TestCase):
    @parameterized.expand(
        [
            [
                "show_job",
                "<show><jobs><id>1</id></jobs></show>",
                {
                    "response": {
                        "@status": "success",
                        "result": {
                            "job": {
                                "tenq": "2021/12/22 10:41:44",
                                "id": "1",
                                "type": "Commit",
                                "status": "FIN",
                                "stoppable": "no",
                                "result": "OK",
                                "tfin": "10:42:22",
                                "progress": "100",
                                "details": {"line": "Configuration committed successfully"},
                                "warnings": None,
                            }
                        },
                    }
                },
            ],
            [
                "show_commit_locks",
                "<show><commit-locks/></show>",
                {"response": {"@status": "success", "result": {"commit-locks": None}}},
            ],
        ]
    )
    def test_op(self, mock_get, name, cmd, expected):
        action = Util.default_connector(Op())
        actual = action.run({Input.CMD: cmd})
        self.assertEqual(actual, expected)
