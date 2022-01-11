import sys
import os
from unittest import TestCase
from komand_palo_alto_pan_os.actions.get_policy import GetPolicy
from komand_palo_alto_pan_os.actions.get_policy.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from komand.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestGetPolicy(TestCase):
    @parameterized.expand(
        [
            [
                "success",
                "Test Policy",
                "localhost.localdomain",
                "vsys1",
                {
                    "to": ["any"],
                    "from": ["any"],
                    "source": ["any"],
                    "destination": ["any"],
                    "source_user": ["Joe Smith"],
                    "category": ["adult", "abused-drugs"],
                    "application": ["any"],
                    "service": ["application-default", "any"],
                    "hip_profiles": ["any"],
                    "action": "drop",
                },
            ]
        ]
    )
    def test_get_policy(self, mock_get, name, policy_name, device_name, virtual_system, expected):
        action = Util.default_connector(GetPolicy())
        actual = action.run(
            {Input.POLICY_NAME: policy_name, Input.DEVICE_NAME: device_name, Input.VIRTUAL_SYSTEM: virtual_system}
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_policy_name",
                "Invalid Policy",
                "localhost.localdomain",
                "vsys1",
                "PAN OS returned an unexpected response.",
                "Could not find policy 'Invalid Policy'. Check the name, virtual system name, and device name.\ndevice name: localhost.localdomain\nvirtual system: vsys1",
            ]
        ]
    )
    def test_get_policy_bad(self, mock_get, name, policy_name, device_name, virtual_system, cause, assistance):
        action = Util.default_connector(GetPolicy())
        with self.assertRaises(PluginException) as e:
            action.run(
                {Input.POLICY_NAME: policy_name, Input.DEVICE_NAME: device_name, Input.VIRTUAL_SYSTEM: virtual_system}
            )
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
