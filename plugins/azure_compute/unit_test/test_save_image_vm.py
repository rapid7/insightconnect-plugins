import os
import sys

sys.path.append(os.path.abspath("../"))
from typing import Any, Callable, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_azure_compute.actions.save_image_vm import SaveImageVm
from icon_azure_compute.actions.save_image_vm.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from mock import (
    STUB_RESOURCE_GROUP_NAME,
    STUB_SUBSCRIPTION_ID,
    STUB_VM_NAME,
    mock_request_200,
    mock_request_202,
    mock_request_500,
    mocked_request,
)
from utils import Util

STUB_INPUT_PARAMETERS = {
    Input.SUBSCRIPTIONID: STUB_SUBSCRIPTION_ID,
    Input.RESOURCEGROUP: STUB_RESOURCE_GROUP_NAME,
    Input.VM: STUB_VM_NAME,
}


class TestSaveImageVm(TestCase):
    @patch("requests.post", side_effect=mock_request_200)
    def setUp(self, mock_requests: MagicMock) -> None:
        self.action = Util.default_connector(SaveImageVm())

    @patch("requests.post", side_effect=mock_request_202)
    def test_save_image_vm(self, mock_request: MagicMock) -> None:
        response = self.action.run(STUB_INPUT_PARAMETERS)
        expected = {Output.STATUS_CODE: 202}
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
        ]
    )
    def test_save_image_vm_exception(
        self, input_parameters: Dict[str, Any], request: Callable, cause: str, assistance: str
    ) -> None:
        mocked_request(request, "post")
        with self.assertRaises(PluginException) as context:
            self.action.run(input_parameters)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
