import os
import sys
from jsonschema import validate
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from komand_mimecast.actions import GetAuditEvents
from komand_mimecast.actions.get_audit_events.schema import GetAuditEventsOutput, GetAuditEventsInput

from util import Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestGetAuditEvent(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAuditEvents())

    def test_get_audit_event(self, _mocked_request):
        input_data = Util.load_json("inputs/get_audit_events.json.exp")
        validate(input_data, GetAuditEventsInput.schema)
        actual = self.action.run(input_data)
        expect = Util.load_json("expected/get_audit_events.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, GetAuditEventsOutput.schema)
