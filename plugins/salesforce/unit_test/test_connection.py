import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from komand_salesforce.actions.simple_search import SimpleSearch
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestConnection(TestCase):
    @parameterized.expand(
        [
            [
                "valid_credentials",
                Util.read_file_to_dict("inputs/connection_valid.json.inp"),
                Util.read_file_to_string("expected/connection_valid.txt.exp"),
            ]
        ]
    )
    def test_connection(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: str
    ) -> None:
        self.action = Util.default_connector(SimpleSearch(), input_params)
        token, url = self.action.connection.api._get_token(
            self.action.connection.api._client_id,
            self.action.connection.api._client_secret,
            self.action.connection.api._username,
            self.action.connection.api._password,
            self.action.connection.api._security_token,
            self.action.connection.api._oauth_url,
        )
        self.assertEqual(token, expected)

    @parameterized.expand(
        [
            [
                "invalid_credentials",
                Util.read_file_to_dict("inputs/connection_invalid.json.inp"),
                PluginException.causes[PluginException.Preset.INVALID_CREDENTIALS],
                PluginException.assistances[PluginException.Preset.INVALID_CREDENTIALS],
            ],
            [
                "salesforce_server_error",
                Util.read_file_to_dict("inputs/connection_server_error.json.inp"),
                PluginException.causes[PluginException.Preset.UNKNOWN],
                PluginException.assistances[PluginException.Preset.UNKNOWN],
            ],
        ]
    )
    def test_connection_raise_exception(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action = Util.default_connector(SimpleSearch(), input_params)
            self.action.connection.api._get_token(
                self.action.connection.api._client_id,
                self.action.connection.api._client_secret,
                self.action.connection.api._username,
                self.action.connection.api._password,
                self.action.connection.api._security_token,
                self.action.connection.api._oauth_url,
            )

        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
