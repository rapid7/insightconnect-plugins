import os
import sys
from unittest.mock import patch

from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ibm_qradar.actions.get_offenses import GetOffenses
from unit_test.helpers.offense import OffensesHelper

sys.path.append(os.path.abspath("../"))


class TestGetOffense(TestCase):
    """Test case class for action: get offense."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = OffensesHelper.default_connector(GetOffenses())

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense(self, make_request):
        """To get the offense.

        :return: None
        """
        action_params = {}
        results = self.action.run(action_params)
        print(results.get("data"))
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offenses_with_fields(self, make_request):
        """To get offenses with given filed list as output.

        :return: None
        """
        action_params = {"fields": "id2"}
        results = self.action.run(action_params)

        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offenses_with_range(self, make_request):
        """To get offenses with given range.

        :return: None
        """
        action_params = {"range": "1-2"}
        results = self.action.run(action_params)
        self.assertEqual(len(results.get("data")["data"]), 1)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offenses_with_invalid_range(self, make_request):
        """To get offenses with given invalid range.

        :return: None
        """
        action_params = {"range": "-1-2"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offenses_with_filter(self, make_request):
        """To get offenses with given filters.

        :return: None
        """
        action_params = {"filter": "id=10001"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offenses_with_sort(self, make_request):
        """To get offenses with given sort options.

        :return: None
        """
        action_params = {"sort": "+id"}
        results = self.action.run(action_params)
        print(results.get("data")["data"])
        self.assertTrue(results.get("data")["data"][0]["id"] < results.get("data")["data"][1]["id"])

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offenses_with_multiple_query_params(self, make_request):
        """To get offenses with multiple query prams passed.

        :return: None
        """
        action_params = {"filter": "id=10001", "fields": "id"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")
        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_with_internal_server_error(self, make_request):
        """To test the get offense with internalServerError."""
        action_params = {"filter": "internalServerError"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)
