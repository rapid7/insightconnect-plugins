import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_intelhub.actions.get_threat_actor_cves import GetThreatActorCves
from komand_rapid7_intelhub.actions.get_threat_actor_cves.schema import Input

from util import STUB_THREAT_ACTOR_UUID, STUB_UNKNOWN_THREAT_ACTOR_UUID, Util


class TestGetThreatActorCves(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetThreatActorCves())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_threat_actor_cves(self, mock_request: MagicMock) -> None:
        input_params = {Input.UUID: STUB_THREAT_ACTOR_UUID, Input.PAGE: 1, Input.PAGE_SIZE: 3}
        validate(input_params, self.action.input.schema)
        response = self.action.run(input_params)
        validate(response, self.action.output.schema)
        self.assertEqual(Util.read_file_to_dict("expected/get_threat_actor_cves.json.exp"), response)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_threat_actor_cves_raise_exception(self, mock_request: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.UUID: STUB_UNKNOWN_THREAT_ACTOR_UUID})
        self.assertEqual("Resource not found", context.exception.cause)
        self.assertEqual(Util.read_file_to_string("payloads/threat_actor_not_found.json.resp"), context.exception.data)
