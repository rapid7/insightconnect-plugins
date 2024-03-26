import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Callable, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_sonicwall.actions.check_if_address_in_address_group import CheckIfAddressInAddressGroup
from icon_sonicwall.actions.check_if_address_in_address_group.schema import Input, Output
from icon_sonicwall.util.util import Message
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from mock import (
    mock_request_200,
    mock_request_400,
    mock_request_401,
    mock_request_403,
    mock_request_500,
    mock_request_invalid_json,
    mocked_request,
)
from utils import Util

STUB_PAYLOAD = {Input.ADDRESS: "ExampleAddressObject", Input.GROUP: "ExampleGroupName"}


class TestCheckIfAddressInAddressGroup(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(CheckIfAddressInAddressGroup())

    @parameterized.expand(
        [
            (
                STUB_PAYLOAD,
                [{"name": STUB_PAYLOAD.get(Input.ADDRESS, "")}],
            )
        ]
    )
    @patch("requests.request", side_effect=mock_request_200)
    def test_check_if_address_in_address_group(
        self, input_parameters: Dict[str, Any], expected: Dict[str, Any], mock_request: MagicMock
    ) -> None:
        response = self.action.run(input_parameters)
        validate(response, self.action.output.schema)
        self.assertEqual(response, {Output.ADDRESS_OBJECTS: expected, Output.FOUND: True})
        mock_request.assert_called()

    @parameterized.expand(
        [
            (
                mock_request_400,
                Message.ADDRESS_GROUP_NOT_FOUND_CAUSE,
                Message.ADDRESS_GROUP_NOT_FOUND_ASSISTANCE,
            ),
            (
                mock_request_401,
                PluginException.causes[PluginException.Preset.USERNAME_PASSWORD],
                PluginException.assistances[PluginException.Preset.USERNAME_PASSWORD],
            ),
            (
                mock_request_403,
                PluginException.causes[PluginException.Preset.UNAUTHORIZED],
                PluginException.assistances[PluginException.Preset.UNAUTHORIZED],
            ),
            (
                mock_request_500,
                Message.ADDRESS_GROUP_NOT_FOUND_CAUSE,
                Message.ADDRESS_GROUP_NOT_FOUND_ASSISTANCE,
            ),
            (
                mock_request_invalid_json,
                PluginException.causes[PluginException.Preset.INVALID_JSON],
                PluginException.assistances[PluginException.Preset.INVALID_JSON],
            ),
        ]
    )
    def test_check_if_address_in_address_group_exception(
        self, mock_request: Callable, cause: str, assistance: str
    ) -> None:
        mocked_request(mock_request, "request")
        with self.assertRaises(PluginException) as context:
            self.action.run(STUB_PAYLOAD)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
