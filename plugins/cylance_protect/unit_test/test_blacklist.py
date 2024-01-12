import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_cylance_protect.actions.blacklist.action import Blacklist
from icon_cylance_protect.actions.blacklist.schema import BlacklistInput, BlacklistOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("icon_cylance_protect.util.api.CylanceProtectAPI.generate_token", side_effect=Util.mock_generate_token)
@patch("requests.request", side_effect=Util.mock_request)
class TestBlacklist(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Blacklist())

    @parameterized.expand(
        [
            [
                "valid_create_blacklist",
                {
                    "hash": "232cdf149baf0b1fd8cfddd940f5cbdf4142a7be387e57187b1aaedd238b1327",
                    "blacklist_state": True,
                    "description": "valid",
                },
                {"success": True},
            ],
            [
                "valid_delete_blacklist",
                {
                    "hash": "232cdf149baf0b1fd8cfddd940f5cbdf4142a7be387e57187b1aaedd238b1328",
                    "blacklist_state": False,
                    "description": "valid",
                },
                {"success": True},
            ],
        ]
    )
    def test_integration_blacklist(
        self,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, BlacklistInput.schema)
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
        validate(actual, BlacklistOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_create_blacklist",
                {
                    "hash": "232cdf149baf0b1fd8cfddd940f5cbdf4142a7be387e57187b1aaedd238b1327",
                    "blacklist_state": True,
                    "description": "invalid",
                },
                "The response from the CylancePROTECT API was not in the correct format.",
                "Contact support for help. See log for more details",
                "['error from the api']",
            ],
            [
                "invalid_delete_blacklist",
                {
                    "hash": "232cdf149baf0b1fd8cfddd940f5cbdf4142a7be387e57187b1aaedd238b1329",
                    "blacklist_state": False,
                    "description": "invalid",
                },
                "The response from the CylancePROTECT API was not in the correct format.",
                "Contact support for help. See log for more details",
                "['error from the api']",
            ],
        ]
    )
    def test_integration_create_blacklist_invalid(
        self,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
        _test_name: str,
        input_params: dict,
        cause: str,
        assistance: str,
        data: list,
    ):
        validate(input_params, BlacklistInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)

    @parameterized.expand(
        [
            [
                "not_a_valid_hash",
                {
                    "hash": "not a valid hash",
                    "blacklist_state": True,
                    "description": "",
                },
                "The Cylance API only supports SHA256.",
                "Please enter a SHA256 hash and try again.",
            ],
            [
                "md5_hash_used",
                {
                    "hash": "2e7e0b79e1383359acb1ca14ea4ec88a",
                    "blacklist_state": True,
                    "description": "",
                },
                "The Cylance API only supports SHA256.",
                "Please enter a SHA256 hash and try again.",
            ],
        ]
    )
    def test_integration_blacklist_non_hash(
        self,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
        _test_name: str,
        input_params: dict,
        cause: str,
        assistance: str,
    ):
        validate(input_params, BlacklistInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
