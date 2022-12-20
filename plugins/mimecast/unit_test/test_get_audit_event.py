import os
import sys
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from komand_mimecast.actions import GetAuditEvents

from unit_test.util import Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestGetAuditEvent(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAuditEvents())

    def test_get_audit_event(self, mocked_request):
        actual = self.action.run(Util.load_json("inputs/get_audit_events.json.exp"))
        expect = Util.load_json("expected/get_audit_events.json.exp")
        self.assertEqual(expect, actual)
