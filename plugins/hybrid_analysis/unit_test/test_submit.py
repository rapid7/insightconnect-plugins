import os
import sys
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from icon_hybrid_analysis.actions.submit import Submit
from icon_hybrid_analysis.actions.submit.schema import Input
from util import Util


class TestSubmit(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Submit())

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_submit(self, mocked_request):
        actual = self.action.run(
            {
                Input.CUSTOM_CMD_LINE: "",
                Input.DOCUMENT_PASSWORD: "",
                Input.ENVIRONMENT_ID: 300,
                Input.EXPERIMENTAL_ANTI_EVASION: True,
                Input.FILE: {"content": "dGVzdHNkcXdlZWRxd2Vxd2Vxd2V3cQ==", "filename": "test.py"},
                Input.HYBRID_ANALYSIS: True,
                Input.SCRIPT_LOGGING: False,
                Input.SUBMIT_NAME: "",
            }
        )
        expected = {
            "environment_id": 300,
            "job_id": "61dc30161eec83532833b25b",
            "sha256": "2d7a962a8bbb24be8404db6116517e93aafcdff3d7d437d3ad8576ae1e0d37bb",
            "submission_id": "61dd5f51c19799191f7ab29f",
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_submit_with_custom_cmd_line(self, mocked_request):
        actual = self.action.run(
            {
                Input.CUSTOM_CMD_LINE: "unzip test.zip",
                Input.DOCUMENT_PASSWORD: "",
                Input.ENVIRONMENT_ID: 300,
                Input.EXPERIMENTAL_ANTI_EVASION: True,
                Input.FILE: {"content": "dGVzdHNkcXdlZWRxd2Vxd2Vxd2V3cQ==", "filename": "test.zip"},
                Input.HYBRID_ANALYSIS: True,
                Input.SCRIPT_LOGGING: False,
                Input.SUBMIT_NAME: "",
            }
        )
        expected = {
            "environment_id": 300,
            "job_id": "61dc30161eec83532833b25b",
            "sha256": "2d7a962a8bbb24be8404db6116517e93aafcdff3d7d437d3ad8576ae1e0d37bb",
            "submission_id": "61dd5f51c19799191f7ab29f",
        }
        self.assertEqual(actual, expected)
