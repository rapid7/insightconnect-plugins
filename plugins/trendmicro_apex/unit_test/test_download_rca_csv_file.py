import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_trendmicro_apex.actions.download_rca_csv_file import DownloadRcaCsvFile
from icon_trendmicro_apex.actions.download_rca_csv_file.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


@patch("icon_trendmicro_apex.connection.connection.create_jwt_token", side_effect="abcgdgd")
class TestDownloadRcaCsvFile(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(DownloadRcaCsvFile())
        self.params = {
            Input.AGENT_GUID: "1234567-1234-1234-1234-123456789",
            Input.HOST_IP: "192.168.0.1",
            Input.HOST_NAME: "TEST-123",
            Input.SCAN_SUMMARY_GUID: "1234567-1234-1234-1234-123456789",
            Input.SERVER_GUID: ["1234567-1234-1234-1234-123456780"],
            Input.TASK_TYPE: "CMEF",
        }

    @patch("requests.request", side_effect=mock_request_200)
    def test_download_rca_csv_file(self, mock_put, mock_token):
        mocked_request(mock_put)
        response = self.action.run(self.params)
        expected = {
            Output.API_RESPONSE: {
                "Data": {
                    "Code": 0,
                    "CodeType": 1,
                    "Data": {
                        "content": [
                            {
                                "content": {"csv": "test"},
                                "message": "TMSL_S_SUCCESS",
                                "statusCode": 0,
                            }
                        ],
                        "hasMore": False,
                        "serverGuid": "test",
                        "serverName": "Apex One as a Service",
                        "taskId": "test",
                    },
                    "Message": "OK",
                    "TimeZone": -4,
                },
                "FeatureCtrl": {"mode": "0"},
                "Meta": {"errorCode": 0, "errorMessgae": "Success", "result": 1},
                "PermissionCtrl": {"permission": "255"},
                "SystemCtrl": {"TmcmSoDist_Role": "none"},
            }
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
