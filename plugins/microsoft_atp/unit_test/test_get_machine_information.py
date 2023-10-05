import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_microsoft_atp.actions.get_machine_information import GetMachineInformation
from komand_microsoft_atp.actions.get_machine_information.schema import Input, Output
from parameterized import parameterized

from util import (
    Util,
    mock_request_200,
    mock_request_201_invalid_json,
    mock_request_401,
    mock_request_403,
    mock_request_404,
    mock_request_500,
    mocked_request,
)


class TestGetMachineInformation(TestCase):
    @classmethod
    @patch("requests.request", side_effect=mock_request_200)
    def setUpClass(cls, mock_get: Mock) -> None:
        cls.action = Util.default_connector(GetMachineInformation())

    @parameterized.expand([("my-hostname",), ("192.168.0.5",)])
    @patch("requests.request", side_effect=mock_request_200)
    def test_get_machine_information(self, input_machine: str, mock_get: Mock) -> None:
        response = self.action.run({Input.MACHINE: input_machine})
        expected = {
            Output.MACHINE: {
                "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Machines",
                "id": "1234",
                "computerDnsName": "my-hostname",
                "firstSeen": "2018-08-02T14:55:03.7791856Z",
                "lastSeen": "2018-08-02T14:55:03.7791856Z",
                "osPlatform": "Windows10",
                "version": "1709",
                "osProcessor": "x64",
                "lastIpAddress": "192.168.0.5",
                "lastExternalIpAddress": "0.0.0.0",
                "osBuild": 18209,
                "healthStatus": "Active",
                "rbacGroupId": 140,
                "rbacGroupName": "ExampleGroup",
                "riskScore": "Low",
                "exposureLevel": "Medium",
                "isAadJoined": True,
                "aadDeviceId": "1111111",
                "machineTags": ["ExampleTag1", "ExampleTag2"],
            }
        }
        self.assertEqual(response, expected)

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_get_machine_information_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run({Input.MACHINE: "my-hostname"})
        self.assertEqual(
            context.exception.cause,
            exception,
        )
