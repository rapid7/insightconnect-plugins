import os
import sys
from unittest.mock import patch

from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ibm_qradar.actions.get_offense_note_by_id import GetOffenseNoteById
from unit_test.helpers.offense_note import OffenseNotesHelper

sys.path.append(os.path.abspath("../"))


class TestGetOffenseNotesById(TestCase):
    """Test case class for action: Get offense notes By ID."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = OffenseNotesHelper.default_connector(GetOffenseNoteById())

    @patch("requests.get", side_effect=OffenseNotesHelper.mock_request)
    def test_get_offense_notes_by_id(self, make_request):
        """To get the offense notes.

        :return: None
        """
        action_params = {"offense_id": "33", "note_id": "34"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")

    @patch("requests.get", side_effect=OffenseNotesHelper.mock_request)
    def test_get_offense_notes_by_id_with_fields(self, make_request):
        """To Get offense notes By Id with field list given.

        :return: None
        """
        action_params = {"offense_id": "33", "note_id": "34", "fields": "id"}
        results = self.action.run(action_params)

        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())

    @patch("requests.get", side_effect=OffenseNotesHelper.mock_request)
    def test_get_offense_notes_by_id_with_filter(self, make_request):
        """To Get offense notes By Id with given filter.

        :return: None
        """
        action_params = {"offense_id": "33", "note_id": "34", "filter": "id=10001"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")

    @patch("requests.get", side_effect=OffenseNotesHelper.mock_request)
    def test_with_internal_server_error(self, make_request):
        """To test the Get offense notes By Id by ID with internalServerError."""
        action_params = {
            "offense_id": "33",
            "note_id": "33",
            "fields": "internalServerError",
        }
        with self.assertRaises(PluginException):
            self.action.run(action_params)
