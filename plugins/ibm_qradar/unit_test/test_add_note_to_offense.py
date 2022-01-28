import os
import sys
from unittest.mock import patch

from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ibm_qradar.actions.add_notes_to_offense import AddNotesToOffense
from unit_test.helpers.offense_note import OffenseNotesHelper

sys.path.append(os.path.abspath("../"))


class TestAddNoteToOffense(TestCase):
    """Test case class for action: Add notes to offense."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = OffenseNotesHelper.default_connector(AddNotesToOffense())

    @patch("requests.post", side_effect=OffenseNotesHelper.mock_request)
    def test_add_note_to_offense(self, make_request):
        """To get the offense notes.

        :return: None
        """
        action_params = {"offense_id": "33", "note_text": "Hello"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")

    @patch("requests.post", side_effect=OffenseNotesHelper.mock_request)
    def test_add_note_to_offense_with_fields(self, make_request):
        """To Add notes to offense with field list given.

        :return: None
        """
        action_params = {"offense_id": "33", "fields": "id", "note_text": "Hello"}
        results = self.action.run(action_params)

        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())

    @patch("requests.post", side_effect=OffenseNotesHelper.mock_request)
    def test_add_note_to_offense_with_filter(self, make_request):
        """To Add notes to offense with given filter.

        :return: None
        """
        action_params = {"offense_id": "33", "filter": "id=10001", "note_text": "Hello"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")

    @patch("requests.post", side_effect=OffenseNotesHelper.mock_request)
    def test_with_internal_server_error(self, make_request):
        """To test the Add notes to offense by ID with internalServerError."""
        action_params = {
            "offense_id": "33",
            "note_text": "Hello",
            "fields": "internalServerError",
        }
        with self.assertRaises(PluginException):
            self.action.run(action_params)
