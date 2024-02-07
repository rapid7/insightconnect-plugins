import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_trendmicro_apex.actions.get_rca_object import GetRcaObject
from icon_trendmicro_apex.actions.get_rca_object.schema import Input, Output
from jsonschema import validate
from unit_test.mock import Util, mock_request_200, mocked_request


class TestGetRcaObject(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(GetRcaObject())
        self.params = {
            Input.TASK_ID: "9BD2204C-0554-45C8-9C62-799284928AFA",
            Input.TASK_TYPE: "CMEF",
            Input.CONTENT_ID: 8,
            Input.LIMIT: "1",
        }

    @patch("requests.request", side_effect=mock_request_200)
    def test_get_rca_object(self, mock_get, mock_token):
        mocked_request(mock_get)
        response = self.action.run(self.params)

        expected = {
            Output.DATA: {
                "Code": 0,
                "CodeType": 1,
                "Data": {
                    "content": [
                        {
                            "content": {
                                "agentServerMeta": [
                                    {
                                        "agentGuid": "626dcf14-b0c3-4b00-bc76-71cf5713ab2e",
                                        "ip": "198.51.100.100",
                                        "isCriteriaExceedMaxMetaCount": [False],
                                        "isEnable": True,
                                        "isImportant": False,
                                        "isOnline": True,
                                        "isolateStatus": 4,
                                        "machineGuid": "3E4EC062-A620-4DE6-9DA9-395DD98EC1D8",
                                        "machineName": "TREND-MICRO-TES",
                                        "machineOS": "Windows 10",
                                        "machineType": "Desktop",
                                        "minFirstSeen": 1589061887,
                                        "productType": 15,
                                        "serverGuid": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
                                        "serverMeta": [
                                            {
                                                "criteriaNo": 0,
                                                "firstSeen": 1589061887,
                                                "lastSeen": 1589131161,
                                                "metaHashId": "-1666102285318829169",
                                                "metaValue": "notepad.exe",
                                                "sweepingType": 7,
                                            }
                                        ],
                                        "serverMode": 1,
                                        "serverName": "Apex One as a Service",
                                        "userGuid": "6AC1B3DCF-CE52-8279-EE9E-E101FD504E3",
                                        "userName": "TREND-MICRO-TES\\vagrant",
                                    }
                                ]
                            },
                            "message": "TMSL_S_SUCCESS",
                            "statusCode": 0,
                        }
                    ],
                    "hasMore": False,
                    "lastContentId": '[\r\n  {\r\n    "serverGuid": "C22E1795-BF95-45BB-BC82-486B0F5161BE",\r\n    "lastContentId": 48,\r\n    "hasMore": false,\r\n    "totalProgress": 0,\r\n    "currentProgress": 0\r\n  }\r\n]',
                    "serverGuid": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
                    "serverName": "Apex One as a Service",
                    "taskId": "B44BE9AE-80A9-4048-A4CE-064D90CB6D4C",
                },
                "Message": "OK",
                "TimeZone": -4,
            },
            Output.META: {"errorCode": 0, "errorMessgae": "Success", "result": 1},
            Output.SYSTEMCTRL: {"TmcmSoDist_Role": "none"},
            Output.FEATURECTRL: {"mode": "0"},
            Output.PERMISSIONCTRL: {"permission": "255"},
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
