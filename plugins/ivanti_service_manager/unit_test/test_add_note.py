import sys
import os
import json

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.payload_stubs import STUB_ADD_NOTE_PARAMETERS
from unit_test.util import Util
from unit_test.mock import mock_request
from icon_ivanti_service_manager.actions.add_note import AddNote


@patch("requests.Session.request", side_effect=mock_request)
class TestAddNote(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector((AddNote()))
        self.connection = self.action.connection

    def test_add_note_success(self, _mock_req):
        actual = self.action.run(
            STUB_ADD_NOTE_PARAMETERS
        )
        expected = json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/expected_add_note_good.json.resp")
            )
        )
        self.assertEqual(actual, expected)
