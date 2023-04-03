import sys
import os
import json

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_ivanti_service_manager.actions.add_note.schema import Input
from unit_test.util import Util
from unit_test.mock import mock_request
from icon_ivanti_service_manager.actions.add_note import AddNote


class TestAddNote(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.params = {
            "category": "category",
            "notes": "notes",
            "source": "source",
            "summary": "summary",
            "incident_number_good": 12345,
            "incident_number_bad": 54321,
        }

    def setUp(self) -> None:
        self.action = Util.default_connector((AddNote()))
        self.connection = self.action.connection

    @patch("requests.Session.request", side_effect=mock_request)
    def test_add_note_success(self, _mock_req):
        actual = self.action.run(
            {
                Input.CATEGORY: self.params.get("category"),
                Input.NOTES: self.params.get("notes"),
                Input.SOURCE: self.params.get("source"),
                Input.SUMMARY: self.params.get("summary"),
                Input.INCIDENT_NUMBER: self.params.get("incident_number_good"),
            }
        )
        expected = json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/expected_add_note_good.json.resp")
            )
        )
        self.assertEqual(actual, expected)
