import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_cylance_protect.actions.delete_asset.action import DeleteAsset
from icon_cylance_protect.actions.delete_asset.schema import DeleteAssetInput, DeleteAssetOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_cylance_protect.util.find_helpers import find_in_whitelist, find_agent_by_ip


@patch("icon_cylance_protect.util.api.CylanceProtectAPI.generate_token", side_effect=Util.mock_generate_token)
@patch("requests.request", side_effect=Util.mock_request)
class TestDeleteAsset(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteAsset())

    @parameterized.expand(
        [
            [
                "valid_delete_asset_ip",
                {
                    "agents": ["1.1.1.1"],
                    "whitelist": [],
                },
                {"deleted": ["1.1.1.1"], "not_deleted": [], "success": True},
            ],
            [
                "valid_delete_asset_hostname",
                {
                    "agents": ["hostname"],
                    "whitelist": [],
                },
                {"deleted": ["hostname"], "not_deleted": [], "success": True},
            ],
            [
                "valid_delete_asset_both",
                {
                    "agents": ["hostname", "1.1.1.1"],
                    "whitelist": [],
                },
                {"deleted": ["hostname", "1.1.1.1"], "not_deleted": [], "success": True},
            ],
            [
                "valid_delete_asset_1_invalid",
                {
                    "agents": ["hostname", "invalid_hostname"],
                    "whitelist": [],
                },
                {"deleted": ["hostname"], "not_deleted": ["invalid_hostname"], "success": True},
            ],
        ]
    )
    @patch("icon_cylance_protect.actions.delete_asset.action.find_agent_by_ip", side_effect=Util.mock_find_agent_by_ip)
    def test_integration_delete_asset_invalid(
        self,
        _test_name: str,
        input_params: dict,
        expected: dict,
        _mock_find_agent_by_ip: MagicMock,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
    ):
        validate(input_params, DeleteAssetInput.schema)
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
        validate(actual, DeleteAssetOutput.schema)

    @parameterized.expand(
        [
            [
                "valid_delete_asset_invalid",
                {
                    "agents": ["invalid_hostname"],
                    "whitelist": [],
                },
                "No valid devices to delete.",
                "Be sure that the devices exist in Cylance and are not part of the whitelist.",
            ],
            [
                "valid_delete_asset_invalid_post",
                {
                    "agents": ["invalid_post"],
                    "whitelist": [],
                },
                "One of the devices failed to delete.",
                "A valid agent deletion may have failed, check your Cylance console.",
            ],
        ]
    )
    @patch("icon_cylance_protect.actions.delete_asset.action.find_agent_by_ip", side_effect=Util.mock_find_agent_by_ip)
    def test_integration_delete_asset_invalid(
        self,
        _test_name: str,
        input_params: dict,
        cause: str,
        assistance: str,
        _mock_find_agent_by_ip: MagicMock,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
    ):
        validate(input_params, DeleteAssetInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

    def test_find_in_whitelist(
        self,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
    ):
        dic = {
            "id": "cf9c26cc-6d3d-454a-b242-7e9f565c6cf7",
            "name": "VAGRANT-PC",
            "host_name": "vagrant-pc",
            "os_version": "Microsoft Windows 7 Professional, Service Pack 1",
            "state": "Online",
            "agent_version": "2.0.1540",
            "products": [{"name": "protect", "version": "2.0.1540"}],
            "policy": {"id": "c6f694e8-5ddd-4988-8a6b-3a1d3d2da631", "name": "Default"},
            "last_logged_in_user": "vagrant-pc\\vagrant",
            "update_available": False,
            "background_detection": False,
            "is_safe": True,
            "date_first_registered": "2020-09-14T15:39:14",
            "date_last_modified": "2020-09-14T15:45:53",
            "ip_addresses": ["10.0.2.15"],
            "mac_addresses": ["08-00-27-33-9F-CE"],
        }

        self.assertEqual(find_in_whitelist(dic, ["1.1.1.1", "2.2.2.2"]), [])
        self.assertEqual(find_in_whitelist(dic, []), [])
        self.assertNotEqual(find_in_whitelist(dic, ["1.1.1.1", "2.2.2.2"]), ["1.1.1.1"])
        self.assertEqual(find_in_whitelist(dic, ["10.0.2.15"]), ["10.0.2.15"])
        self.assertEqual(find_in_whitelist(dic, ["08-00-27-33-9F-CE"]), ["08-00-27-33-9F-CE"])
        self.assertEqual(find_in_whitelist(dic, ["vagrant-pc"]), ["vagrant-pc"])
