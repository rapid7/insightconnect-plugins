from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_recorded_future.actions.list_url_risk_rules import ListUrlRiskRules
from komand_recorded_future.connection.schema import Input
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestListUrlRiskRules(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListUrlRiskRules())

    @parameterized.expand(
        [
            [
                Util.read_file_to_dict("expected/list_url_risk_rules.json.resp"),
            ],
        ]
    )
    def test_list_url_risk_rules(self, mock_request: MagicMock, expected: Dict[str, Any]) -> None:
        actual = self.action.run({})
        validate(actual, self.action.output.schema)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "bad_api_key",
                {},
                PluginException.causes.get(PluginException.Preset.API_KEY),
                PluginException.assistances.get(PluginException.Preset.API_KEY),
            ],
            [
                "unauthorized",
                {},
                PluginException.causes.get(PluginException.Preset.UNAUTHORIZED),
                PluginException.assistances.get(PluginException.Preset.UNAUTHORIZED),
            ],
            [
                "unknown",
                {},
                PluginException.causes.get(PluginException.Preset.UNKNOWN),
                PluginException.assistances.get(PluginException.Preset.UNKNOWN),
            ],
            [
                "server_error",
                {},
                PluginException.causes.get(PluginException.Preset.SERVER_ERROR),
                PluginException.assistances.get(PluginException.Preset.SERVER_ERROR),
            ],
        ]
    )
    def test_list_url_risk_rules_raise_exception(
        self, mock_request: MagicMock, token: str, input_parameters: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        action = Util.default_connector(ListUrlRiskRules(), {Input.API_KEY: {"secretKey": token}})
        with self.assertRaises(PluginException) as error:
            action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
