import os
import sys

sys.path.append(os.path.abspath("../"))
from typing import Any, Callable, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_azure_compute.actions.availability_set_vm import AvailabilitySetVm
from icon_azure_compute.actions.availability_set_vm.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from mock import (
    STUB_AVAILABILITY_SET_NAME,
    STUB_RESOURCE_GROUP_NAME,
    STUB_SUBSCRIPTION_ID,
    mock_request_200,
    mock_request_500,
    mocked_request,
)
from utils import Util

STUB_INPUT_PARAMETERS = {
    Input.SUBSCRIPTIONID: STUB_SUBSCRIPTION_ID,
    Input.RESOURCEGROUP: STUB_RESOURCE_GROUP_NAME,
    Input.AVAILABILITYSET: STUB_AVAILABILITY_SET_NAME,
}


class TestAvailabilitySetVm(TestCase):
    @patch("requests.post", side_effect=mock_request_200)
    def setUp(self, mock_requests: MagicMock) -> None:
        self.action = Util.default_connector(AvailabilitySetVm())

    @patch("requests.get", side_effect=mock_request_200)
    def test_availability_set_vm(self, mock_request: MagicMock) -> None:
        response = self.action.run(STUB_INPUT_PARAMETERS)
        expected = {
            Output.VALUE: [
                {
                    "maxDataDiskCount": 2,
                    "memoryInMB": 4096,
                    "name": "ExampleName",
                    "numberOfCores": 4,
                    "osDiskSizeInMB": 120000,
                    "resourceDiskSizeInMB": 60000,
                }
            ]
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
        mock_request.assert_called_once()

    @parameterized.expand(
        [
            (
                {**STUB_INPUT_PARAMETERS, Input.RESOURCEGROUP: "Exception"},
                mock_request_500,
                PluginException.causes[PluginException.Preset.UNKNOWN],
                PluginException.assistances[PluginException.Preset.UNKNOWN],
            ),
            (
                {**STUB_INPUT_PARAMETERS, Input.RESOURCEGROUP: "InvalidJSON"},
                mock_request_200,
                PluginException.causes[PluginException.Preset.INVALID_JSON],
                PluginException.assistances[PluginException.Preset.INVALID_JSON],
            ),
        ]
    )
    def test_availability_set_vm_exception(
        self, input_parameters: Dict[str, Any], request: Callable, cause: str, assistance: str
    ) -> None:
        mocked_request(request, "get")
        with self.assertRaises(PluginException) as context:
            self.action.run(input_parameters)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
