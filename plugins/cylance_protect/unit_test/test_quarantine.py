import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_cylance_protect.actions.quarantine.action import Quarantine
from icon_cylance_protect.actions.quarantine.schema import QuarantineInput, QuarantineOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("icon_cylance_protect.util.api.CylanceProtectAPI.generate_token", side_effect=Util.mock_generate_token)
@patch("requests.request", side_effect=Util.mock_request)
class TestQuarantine(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Quarantine())

    @parameterized.expand(
        [
            [
                "valid_quarantine_ip",
                {"agent": "1.1.1.1", "whitelist": []},
                {
                    "lockdown_details": {
                        "status": "COMPLETE",
                        "data": {
                            "id": "1ABC234D5EFA6789BCDE0F1ABCDE23F5",
                            "hostname": "Example-Hostname",
                            "tenant_id": "1abc234d5efa6789bcde0f1abcde23f5",
                            "connection_status": "locked",
                            "optics_device_version": "2.4.2100.1015",
                            "password": "unlock-pa22-w0rd",
                            "lockdown_expiration": "2020-07-11T21:15:29Z",
                            "lockdown_initiated": "2020-07-08T21:15:29Z",
                        },
                    }
                },
            ],
            [
                "valid_quarantine_hostnme",
                {"agent": "hostname", "whitelist": []},
                {
                    "lockdown_details": {
                        "status": "COMPLETE",
                        "data": {
                            "id": "1ABC234D5EFA6789BCDE0F1ABCDE23F5",
                            "hostname": "Example-Hostname",
                            "tenant_id": "1abc234d5efa6789bcde0f1abcde23f5",
                            "connection_status": "locked",
                            "optics_device_version": "2.4.2100.1015",
                            "password": "unlock-pa22-w0rd",
                            "lockdown_expiration": "2020-07-11T21:15:29Z",
                            "lockdown_initiated": "2020-07-08T21:15:29Z",
                        },
                    }
                },
            ],
            [
                "valid_quarantine_mac",
                {"agent": "00-60-26-26-D5-19", "whitelist": []},
                {
                    "lockdown_details": {
                        "status": "COMPLETE",
                        "data": {
                            "id": "1ABC234D5EFA6789BCDE0F1ABCDE23F5",
                            "hostname": "Example-Hostname",
                            "tenant_id": "1abc234d5efa6789bcde0f1abcde23f5",
                            "connection_status": "locked",
                            "optics_device_version": "2.4.2100.1015",
                            "password": "unlock-pa22-w0rd",
                            "lockdown_expiration": "2020-07-11T21:15:29Z",
                            "lockdown_initiated": "2020-07-08T21:15:29Z",
                        },
                    }
                },
            ],
        ]
    )
    @patch("icon_cylance_protect.actions.quarantine.action.find_agent_by_ip", side_effect=Util.mock_find_agent_by_ip)
    def test_integration_quarantine_valid(
        self,
        _test_name: str,
        input_params: dict,
        expected: dict,
        _mock_find_agent_by_ip: MagicMock,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
    ):
        validate(input_params, QuarantineInput.schema)
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
        validate(actual, QuarantineOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_quarantine_not_found",
                {"agent": "1.1.1.2", "whitelist": []},
                "Agent not found.",
                "Unable to find an agent with IP: 1.1.1.2, please ensure that the IP address is correct.",
            ],
            [
                "invalid_quarantine_in_both",
                {"agent": "1.1.1.1", "whitelist": ["1.1.1.1"]},
                "Agent found in the whitelist.",
                "If you would like to block this host, remove '1.1.1.1' from the whitelist.",
            ],
        ]
    )
    @patch("icon_cylance_protect.actions.quarantine.action.find_agent_by_ip", side_effect=Util.mock_find_agent_by_ip)
    def test_integration_get_agent_details_invalid(
        self,
        _test_name: str,
        input_params: dict,
        cause: str,
        assistance: str,
        _mock_find_agent_by_ip: MagicMock,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
    ):
        validate(input_params, QuarantineInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
