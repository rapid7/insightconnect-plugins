import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock

from icon_jamf.actions.lock_mobile_devices import LockMobileDevices
from icon_jamf.actions.lock_mobile_devices.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from mock import (
    STUB_CONNECTION,
    STUB_DEVICE_IDS,
    mock_request_201,
    mock_request_400,
    mock_request_403,
    mock_request_404,
    mock_request_500,
    mock_request_505,
    mocked_request,
)
from util import Util


class TestLockMobileDevices(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_action_connector(STUB_CONNECTION, LockMobileDevices())

    @mock.patch("requests.request", side_effect=mock_request_201)
    def test_lock_mobile_devices_ok(self, mocked_post) -> None:
        response = self.action.run({Input.DEVICES_ID: STUB_DEVICE_IDS})
        expected_response = {Output.STATUS: 201}
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
            (mock_request_505, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_lock_mobile_devices_exception(self, mock_request, exception) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.DEVICES_ID: STUB_DEVICE_IDS})
        self.assertEqual(context.exception.cause, exception)
