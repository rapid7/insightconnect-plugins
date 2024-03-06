import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.get_analysis_info import GetAnalysisInfo
from icon_joe_sandbox.actions.get_analysis_info.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request, MagicMock


class TestGetAnalysisInfo(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(GetAnalysisInfo())
        self.params = {Input.WEBID: "abc"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_get_analysis_info(self, mock_get: MagicMock) -> None:
        mocked_request(mock_get)
        response = self.action.run()

        expected = {
            Output.ANALYSIS: {
                "analysis": {
                    "webid": "3675753",
                    "time": "2024-03-01T11:46:34+01:00",
                    "runs": [
                        {
                            "detection": "clean",
                            "system": "w10x64_office",
                            "yara": False,
                            "sigma": False,
                            "snort": False,
                            "score": 0,
                        }
                    ],
                    "tags": [],
                    "encrypted": False,
                    "analysisid": "3675753",
                    "duration": 253,
                    "filename": "http://conor",
                    "scriptname": "browseurl.jbs",
                    "status": "finished",
                    "score": 0,
                    "detection": "clean",
                    "has_malwareconfig": False,
                }
            }
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
