import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_intelhub.actions.get_threat_actor import GetThreatActor
from komand_rapid7_intelhub.actions.get_threat_actor.schema import Input, Output
from parameterized import parameterized

from util import STUB_THREAT_ACTOR_UUID, STUB_UNKNOWN_THREAT_ACTOR_UUID, STUB_UNLICENSED_CONNECTION, Util


class TestGetThreatActor(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetThreatActor())

    @parameterized.expand(
        [
            ["found", STUB_THREAT_ACTOR_UUID, Util.read_file_to_dict("expected/get_threat_actor.json.exp")],
            ["not_found", STUB_UNKNOWN_THREAT_ACTOR_UUID, {Output.THREAT_ACTOR: {}, Output.FOUND: False}],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_threat_actor(self, _name: str, uuid: str, expected: dict, mock_request: MagicMock) -> None:
        input_params = {Input.UUID: uuid}
        validate(input_params, self.action.input.schema)
        response = self.action.run(input_params)
        validate(response, self.action.output.schema)
        self.assertEqual(expected, response)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_threat_actor_raise_exception(self, mock_request: MagicMock) -> None:
        # A missing license must not be reported as a threat actor that was not found
        action = Util.default_connector(GetThreatActor(), STUB_UNLICENSED_CONNECTION)
        with self.assertRaises(PluginException) as context:
            action.run({Input.UUID: STUB_THREAT_ACTOR_UUID})
        self.assertEqual("Product license not found.", context.exception.cause)
