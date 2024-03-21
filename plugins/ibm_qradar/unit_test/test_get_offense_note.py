import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from unittest import TestCase
from jsonschema import validate

from insightconnect_plugin_runtime.exceptions import PluginException
from icon_ibm_qradar.actions.get_offense_note.action import GetOffenseNote
from icon_ibm_qradar.actions.get_offense_note.schema import Input, GetOffenseNoteInput, GetOffenseNoteOutput
from helpers.offense_note import OffenseNotesHelper


class TestGetOffenseNote(TestCase):
    """Test case class for action: Get offense notes."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = OffenseNotesHelper.default_connector(GetOffenseNote())

    @patch("requests.request", side_effect=OffenseNotesHelper.mock_request)
    def test_get_offense_notes(self, make_request):
        """To get the offense notes.

        :return: None
        """
        action_params = {Input.OFFENSE_ID: 33}
        validate(action_params, GetOffenseNoteInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], 10001)
        validate(results.get("data"), GetOffenseNoteOutput.schema)

    @patch("requests.request", side_effect=OffenseNotesHelper.mock_request)
    def test_get_offense_notes_with_fields(self, make_request):
        """To get offense notes with field list given.

        :return: None
        """
        action_params = {Input.OFFENSE_ID: 33, Input.FIELDS: "id"}
        validate(action_params, GetOffenseNoteInput.schema)
        results = self.action.run(action_params)

        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())
        validate(results.get("data"), GetOffenseNoteOutput.schema)

    @patch("requests.request", side_effect=OffenseNotesHelper.mock_request)
    def test_get_offense_notes_with_filter(self, make_request):
        """To get offense notes with given filter.

        :return: None
        """
        action_params = {Input.OFFENSE_ID: 33, Input.FILTER: "id=10001"}
        validate(action_params, GetOffenseNoteInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], 10001)
        validate(results.get("data"), GetOffenseNoteOutput.schema)

    @patch("requests.request", side_effect=OffenseNotesHelper.mock_request)
    def test_with_internal_server_error(self, make_request):
        """To test the get offense notes by ID with internalServerError."""
        action_params = {Input.OFFENSE_ID: 33, Input.FILTER: "internalServerError"}
        validate(action_params, GetOffenseNoteInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(action_params)
