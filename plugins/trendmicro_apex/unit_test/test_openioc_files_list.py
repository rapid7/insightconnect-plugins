import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_trendmicro_apex.actions.openioc_files_list import OpeniocFilesList
from icon_trendmicro_apex.actions.openioc_files_list.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


@patch("icon_trendmicro_apex.connection.connection.create_jwt_token", side_effect="abcgdgd")
class TestOpeniocFilesList(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(OpeniocFilesList())
        self.params = {
            Input.FILE_HASH_ID_LIST: [],
            Input.FUZZY_MATCH_STRING: "Rapid7 InsightConnect",
            Input.PAGE_NUMBER: 1,
            Input.PAGE_SIZE: 10,
            Input.SORTING_COLUMN: "FileAddedDateTime",
            Input.SORTING_DIRECTION: "Descending",
        }

    @patch("requests.request", side_effect=mock_request_200)
    def test_openioc_files_list(self, mock_get, mock_token):
        mocked_request(mock_get)
        response = self.action.run(self.params)
        expected = {
            Output.DATA: {
                "FilingCabinet": [
                    {
                        "ExtractingStatus": 999,
                        "FileAddedDatetime": "05/10/2020 15:58:41",
                        "FileHashID": "cd9b739b7c6e488080412e9a831e9260a468564f",
                        "FileName": "file.txt",
                        "ShortDesc": "Cryptolocker Detection (EXPERIMENTAL)",
                        "UploadedBy": "Integration Lab",
                        "UploadedFrom": 1,
                    },
                    {
                        "ExtractingStatus": 1,
                        "FileAddedDatetime": "05/10/2020 12:28:18",
                        "FileHashID": "2a99370fd6218b6b8e0c3413f11eb504a4a60225",
                        "FileName": "openioc1",
                        "ShortDesc": "SHELLDC.DLL (BACKDOOR)",
                        "UploadedBy": "Integration Lab",
                        "UploadedFrom": 1,
                    },
                    {
                        "ExtractingStatus": 1,
                        "FileAddedDatetime": "05/10/2020 10:39:17",
                        "FileHashID": "fc3f17bd9068c2588c4c475d2d08a0e7f04f434d",
                        "FileName": "cryptolocker2.ioc",
                        "ShortDesc": "Cryptolocker Detection (EXPERIMENTAL)",
                        "UploadedBy": "Integration Lab",
                        "UploadedFrom": 1,
                    },
                ],
                "TotalIOCCount": 3,
            },
            Output.FEATURE_CTRL: {"mode": "0"},
            Output.META: {"ErrorCode": 0, "Result": 1},
            Output.PERMISSION_CTRL: {"permission": "255"},
            Output.SYSTEM_CTRL: {"TmcmSoDist_Role": "none"},
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
