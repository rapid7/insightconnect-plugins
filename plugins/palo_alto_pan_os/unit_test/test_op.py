import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import patch, MagicMock

from jsonschema import validate
from komand_palo_alto_pan_os.actions.op import Op
from komand_palo_alto_pan_os.actions.op.schema import Input, OpInput, OpOutput
from parameterized import parameterized

from util import Util


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
    def test_op(
        self,
        mock_get: MagicMock,
        name: str,
        cmd: str,
        expected: dict,
    ) -> None:
        action = Util.default_connector(Op())
        input_data = {Input.CMD: cmd}
        validate(input_data, OpInput.schema)
        actual = action.run(input_data)
        self.assertEqual(actual, expected)
        validate(actual, OpOutput.schema)
