import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_palo_alto_pan_os.actions.get_policy import GetPolicy
from komand_palo_alto_pan_os.actions.get_policy.schema import GetPolicyInput, GetPolicyOutput, Input
from parameterized import parameterized

from util import Util


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
    def test_get_policy(
        self,
        mock_get: MagicMock,
        name: str,
        policy_name: str,
        device_name: str,
        virtual_system: str,
        expected: dict,
    ) -> None:
        action = Util.default_connector(GetPolicy())
        input_data = {
            Input.POLICY_NAME: policy_name,
            Input.DEVICE_NAME: device_name,
            Input.VIRTUAL_SYSTEM: virtual_system,
        }
        validate(input_data, GetPolicyInput.schema)
        actual = action.run(input_data)
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
    def test_get_policy_bad(
        self,
        mock_get: MagicMock,
        name: str,
        policy_name: str,
        device_name: str,
        virtual_system: str,
        cause: str,
        assistance: str,
    ) -> None:
        action = Util.default_connector(GetPolicy())
        input_data = {
            Input.POLICY_NAME: policy_name,
            Input.DEVICE_NAME: device_name,
            Input.VIRTUAL_SYSTEM: virtual_system,
        }
        validate(input_data, GetPolicyInput.schema)
        with self.assertRaises(PluginException) as e:
            actual = action.run(input_data)
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
