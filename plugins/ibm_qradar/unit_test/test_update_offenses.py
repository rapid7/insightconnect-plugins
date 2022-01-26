import os
import sys
from unittest.mock import patch

from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ibm_qradar.actions.update_offense import UpdateOffense
from unit_test.helpers.offense import UpdateOffenseHelper

sys.path.append(os.path.abspath("../"))


class TestGetOffense(TestCase):
    """Test case class for action: get offense."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = UpdateOffenseHelper.default_connector(UpdateOffense())

    @patch("requests.post", side_effect=UpdateOffenseHelper.mock_request)
    def test_update_offense(self, make_request):
        """To update the offense with multiple params.

        :return: None
        """
        action_params = {
            "offense_id": 1,
            "protected": True,
            "assigned_to:": "assigned_to:",
            "follow_up": True,
        }
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"]["id"], "10001")

    @patch("requests.post", side_effect=UpdateOffenseHelper.mock_request)
    def test_update_offenses_with_fields(self, make_request):
        """To update offenses with given field list as output.

        :return: None
        """
        action_params = {"offense_id": 1, "fields": "id"}
        results = self.action.run(action_params)

        self.assertEqual(len(results.get("data")["data"].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"].keys())

    @patch("requests.post", side_effect=UpdateOffenseHelper.mock_request)
    def test_close_offense(self, make_request):
        """To update offenses with given closed status.

        :return: None
        """
        action_params = {"offense_id": 1, "status": "CLOSED", "closing_reason_id": "1"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"]["status"], "CLOSED")

    @patch("requests.post", side_effect=UpdateOffenseHelper.mock_request)
    def test_close_offense_without_closing_reason(self, make_request):
        """To update offenses with given closed status without closing ID .

        :return: None
        """
        action_params = {
            "offense_id": 1,
            "fields": "id",
            "status": "CLOSED",
        }
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.post", side_effect=UpdateOffenseHelper.mock_request)
    def test_open_offense_with_closing_reason(self, make_request):
        """To update offenses with given closed status without closing ID .

        :return: None
        """
        action_params = {
            "offense_id": 1,
            "fields": "id",
            "status": "OPEN",
            "closing_reason_id": "1",
        }
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.post", side_effect=UpdateOffenseHelper.mock_request)
    def test_with_internal_server_error(self, make_request):
        """To test the update offense with internalServerError."""
        action_params = {"offense_id": 1, "fields": "internalServerError"}
        with self.assertRaises(PluginException):
            print(self.action.run(action_params))
