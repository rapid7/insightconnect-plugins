import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.search_analysis import SearchAnalysis
from icon_joe_sandbox.actions.search_analysis.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestSearchAnalysis(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(SearchAnalysis())
        self.params = {Input.QUERY: "query"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_search_analysis(self, mock_get):
        mocked_request(mock_get)
        response = self.action.run()

        expected = {
            Output.ANALYSES: [
                {
                    "webid": "1",
                    "time": "2024-02-29T12:50:03+01:00",
                    "runs": [
                        {
                            "detection": "clean",
                            "error": None,
                            "system": "w10x64_office",
                            "yara": False,
                            "sigma": False,
                            "snort": False,
                            "score": 0,
                        }
                    ],
                    "tags": [],
                    "encrypted": False,
                    "analysisid": "3673217",
                    "duration": 397,
                    "md5": "",
                    "sha1": "",
                    "sha256": "",
                    "filename": "https://www.google.com",
                    "scriptname": "browseurl.jbs",
                    "status": "finished",
                    "comments": "",
                    "classification": "",
                    "threatname": "",
                    "score": 0,
                    "detection": "clean",
                    "has_malwareconfig": False,
                }
            ]
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
