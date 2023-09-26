import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_carbon_black_cloud.actions.get_agent_details import GetAgentDetails
from icon_carbon_black_cloud.actions.get_agent_details.schema import GetAgentDetailsOutput, Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from util import (
    Util,
    mock_request_200,
    mock_request_400,
    mock_request_401,
    mock_request_403,
    mock_request_404,
    mock_request_409,
    mock_request_503,
    mocked_request,
)

STUB_AGENT_ID = "192.168.0.1"


class TestGetAgentDetails(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetAgentDetails())
        self.payload = {Input.AGENT: STUB_AGENT_ID}

    @patch("requests.post", side_effect=mock_request_200)
    def test_get_agent_details(self, mocked_post: MagicMock) -> None:
        response = self.action.run(self.payload)
        expected = {
            Output.AGENT: {
                "activation_code_expiry_time": "2022-07-11T06:53:06.190Z",
                "ad_group_id": 0,
                "av_ave_version": "8.3.64.172",
                "av_engine": "4.15.1.560-ave.8.3.64.172:avpack.8.5.2.64:vdf.8.19.20.4:vdfdate.20220711",
                "av_master": False,
                "av_pack_version": "8.5.2.64",
                "av_product_version": "4.15.1.560",
                "av_status": ["AV_ACTIVE", "ONDEMAND_SCAN_DISABLED"],
                "av_vdf_version": "8.19.20.4",
                "current_sensor_policy_name": "CB-policy",
                "deployment_type": "ENDPOINT",
                "device_meta_data_item_list": [
                    {"key_name": "OS_MAJOR_VERSION", "key_value": "Windows 10", "position": 0},
                    {"key_name": "SUBNET", "key_value": "198.18.127", "position": 0},
                ],
                "device_owner_id": 854220,
                "email": "vagrant",
                "id": 5765373,
                "last_contact_time": "2022-07-11T22:04:42.993Z",
                "last_device_policy_changed_time": "2022-07-04T13:22:15.870Z",
                "last_device_policy_requested_time": "2022-07-04T13:46:25.278Z",
                "last_external_ip_address": "162.111.555.333",
                "last_internal_ip_address": "198.18.127.111",
                "last_location": "OFFSITE",
                "last_policy_updated_time": "2022-05-18T09:33:54.616Z",
                "last_reported_time": "2022-07-11T22:04:43.063Z",
                "last_shutdown_time": "2022-07-04T06:58:55.867Z",
                "login_user_name": "CARBONBLACK\\testuser",
                "mac_address": "fa163e92d344",
                "name": "carbonblack",
                "organization_id": 1105,
                "organization_name": "cb-internal-alliances.com",
                "os": "WINDOWS",
                "os_version": "Windows 10 x64",
                "passive_mode": False,
                "policy_id": 87816,
                "policy_name": "CB-policy",
                "policy_override": True,
                "quarantined": False,
                "registered_time": "2022-07-04T06:53:06.220Z",
                "sensor_kit_type": "WINDOWS",
                "sensor_out_of_date": False,
                "sensor_pending_update": False,
                "sensor_states": [
                    "ACTIVE",
                    "LIVE_RESPONSE_NOT_RUNNING",
                    "LIVE_RESPONSE_NOT_KILLED",
                    "LIVE_RESPONSE_ENABLED",
                ],
                "sensor_version": "3.8.0.627",
                "status": "REGISTERED",
                "target_priority": "MEDIUM",
                "uninstall_code": "R6VERVN2",
                "virtual_machine": False,
                "virtualization_provider": "OTHER",
                "vulnerability_score": 0.0,
            }
        }
        validate(response, GetAgentDetailsOutput.schema)
        self.assertEqual(response, expected)
        mocked_post.assert_called_once()

    @parameterized.expand(
        [
            (mock_request_400, "400 Bad Request"),
            (mock_request_401, "Authentication Error"),
            (mock_request_403, "The specified object cannot be accessed or changed."),
            (mock_request_404, "The object referenced in the request cannot be found."),
            (mock_request_409, "Either the name you chose already exists, or there is an unacceptable character used."),
            (mock_request_503, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_get_agent_details_exception(self, mock_request: MagicMock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.payload)
        self.assertEqual(
            context.exception.cause,
            exception,
        )
