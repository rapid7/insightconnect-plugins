import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.get_submitted_info.action import GetSubmittedInfo
from icon_joe_sandbox.actions.get_submitted_info.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request, MagicMock


class TestGetSubmittedInfo(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(GetSubmittedInfo())
        self.params = {Input.SUBMISSION_ID: "12345"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_get_submitted_info(self, mock_get) -> None:
        mocked_request(mock_get)
        response = self.action.run(self.params)
        expected = {
            Output.SUBMISSION_INFO: {
                "submission_info": {
                    "analyses": [
                        {
                            "analysisid": "1111",
                            "classification": "",
                            "comments": "",
                            "detection": "clean",
                            "duration": 595,
                            "encrypted": False,
                            "filename": "test.csv",
                            "has_malwareconfig": False,
                            "md5": "df7761075b3e745e58ae6c9607721d04",
                            "runs": [
                                {
                                    "detection": "clean",
                                    "error": None,
                                    "score": 0,
                                    "sigma": False,
                                    "suricata": False,
                                    "system": "w10x64_21h1_office",
                                    "yara": False,
                                },
                                {
                                    "detection": "clean",
                                    "error": None,
                                    "score": 0,
                                    "sigma": False,
                                    "suricata": False,
                                    "system": "w7x64_office",
                                    "yara": False,
                                },
                            ],
                            "score": 0,
                            "scriptname": "default.jbs",
                            "sha1": "111",
                            "sha256": "1111",
                            "status": "finished",
                            "tags": [],
                            "threatname": "",
                            "time": "2025-02-04T15:44:08+01:00",
                            "webid": "1111",
                        }
                    ],
                    "most_relevant_analysis": {
                        "detection": "clean",
                        "score": 0,
                        "webid": "1111",
                    },
                    "name": "test.csv",
                    "status": "finished",
                    "submission_id": "12345",
                    "time": "2025-02-04T15:44:06+01:00",
                },
                "most_relevant_analysis": {
                    "webid": "running",
                    "detection": "running",
                    "score": "running",
                },
            }
        }

        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
