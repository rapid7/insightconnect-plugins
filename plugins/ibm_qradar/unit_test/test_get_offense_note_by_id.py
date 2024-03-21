import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from unittest import TestCase
from jsonschema import validate

from insightconnect_plugin_runtime.exceptions import PluginException
from icon_ibm_qradar.actions.get_offense_note_by_id.action import GetOffenseNoteById
from icon_ibm_qradar.actions.get_offense_note_by_id.schema import (
    Input,
    GetOffenseNoteByIdInput,
    GetOffenseNoteByIdOutput,
)
from helpers.offense_note import OffenseNotesHelper


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
        action_params = {Input.OFFENSE_ID: 33, Input.NOTE_ID: 34}
        validate(action_params, GetOffenseNoteByIdInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], 10001)
        validate(results.get("data")["data"][0], GetOffenseNoteByIdOutput.schema)

    @patch("requests.get", side_effect=OffenseNotesHelper.mock_request)
    def test_get_offense_notes_by_id_with_fields(self, make_request):
        """To Get offense notes By Id with field list given.

        :return: None
        """
        action_params = {Input.OFFENSE_ID: 33, Input.NOTE_ID: 34, Input.FIELDS: "id"}
        validate(action_params, GetOffenseNoteByIdInput.schema)
        results = self.action.run(action_params)

        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())
        validate(results.get("data")["data"][0], GetOffenseNoteByIdOutput.schema)

    @patch("requests.get", side_effect=OffenseNotesHelper.mock_request)
    def test_get_offense_notes_by_id_with_filter(self, make_request):
        """To Get offense notes By Id with given filter.

        :return: None
        """
        action_params = {Input.OFFENSE_ID: 33, Input.NOTE_ID: 34, Input.FILTER: "id=10001"}
        validate(action_params, GetOffenseNoteByIdInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], 10001)
        validate(results.get("data")["data"][0], GetOffenseNoteByIdOutput.schema)

    @patch("requests.get", side_effect=OffenseNotesHelper.mock_request)
    def test_with_internal_server_error(self, make_request):
        """To test the Get offense notes By Id by ID with internalServerError."""
        action_params = {Input.OFFENSE_ID: 33, Input.NOTE_ID: 34, Input.FIELDS: "internalServerError"}
        validate(action_params, GetOffenseNoteByIdInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(action_params)
