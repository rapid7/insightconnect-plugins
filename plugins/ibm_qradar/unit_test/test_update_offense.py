import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from unittest import TestCase
from jsonschema import validate

from insightconnect_plugin_runtime.exceptions import PluginException
from icon_ibm_qradar.actions.update_offense.action import UpdateOffense
from icon_ibm_qradar.actions.update_offense.schema import Input, UpdateOffenseInput, UpdateOffenseOutput
from helpers.offense import UpdateOffenseHelper


class TestGetOffense(TestCase):
    """Test case class for action: get offense."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = UpdateOffenseHelper.default_connector(UpdateOffense())

    @patch("requests.request", side_effect=UpdateOffenseHelper.mock_request)
    def test_update_offense(self, make_request):
        """To update the offense with multiple params.

        :return: None
        """
        action_params = {
            Input.OFFENSE_ID: 1,
            Input.PROTECTED: True,
            Input.ASSIGNED_TO: "assigned_to:",
            Input.FOLLOW_UP: True,
        }
        validate(action_params, UpdateOffenseInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"]["id"], 10001)
        validate(results.get("data"), UpdateOffenseOutput.schema)

    @patch("requests.request", side_effect=UpdateOffenseHelper.mock_request)
    def test_update_offenses_with_fields(self, make_request):
        """To update offenses with given field list as output.

        :return: None
        """
        action_params = {Input.OFFENSE_ID: 1, Input.FIELDS: "id"}
        validate(action_params, UpdateOffenseInput.schema)
        results = self.action.run(action_params)

        self.assertEqual(len(results.get("data")["data"].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"].keys())
        validate(results.get("data"), UpdateOffenseOutput.schema)

    @patch("requests.request", side_effect=UpdateOffenseHelper.mock_request)
    def test_close_offense(self, make_request):
        """To update offenses with given closed status.

        :return: None
        """
        action_params = {Input.OFFENSE_ID: 1, Input.STATUS: "Closed", Input.CLOSING_REASON_ID: "1"}
        validate(action_params, UpdateOffenseInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"]["status"], "CLOSED")
        validate(results.get("data"), UpdateOffenseOutput.schema)

    @patch("requests.request", side_effect=UpdateOffenseHelper.mock_request)
    def test_close_offense_without_closing_reason(self, make_request):
        """To update offenses with given closed status without closing ID .

        :return: None
        """
        action_params = {Input.OFFENSE_ID: 1, Input.STATUS: "Closed", Input.FIELDS: "id"}
        validate(action_params, UpdateOffenseInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.request", side_effect=UpdateOffenseHelper.mock_request)
    def test_open_offense_with_closing_reason(self, make_request):
        """To update offenses with given closed status without closing ID .

        :return: None
        """
        action_params = {
            Input.OFFENSE_ID: 1,
            Input.FIELDS: "id",
            Input.STATUS: "Open",
            Input.CLOSING_REASON_ID: "1",
        }
        validate(action_params, UpdateOffenseInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.request", side_effect=UpdateOffenseHelper.mock_request)
    def test_with_internal_server_error(self, make_request):
        """To test the update offense with internalServerError."""
        action_params = {Input.OFFENSE_ID: 1, Input.FIELDS: "internalServerError"}
        validate(action_params, UpdateOffenseInput.schema)
        with self.assertRaises(PluginException):
            print(self.action.run(action_params))
