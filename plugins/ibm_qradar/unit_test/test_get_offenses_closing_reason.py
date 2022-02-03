import os
import sys
from unittest.mock import patch

from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ibm_qradar.actions.get_offense_closing_reasons import GetOffenseClosingReasons
from unit_test.helpers.offense import OffensesHelper

sys.path.append(os.path.abspath("/"))


class TestGetOffenseClosingReason(TestCase):
    """Test case class for action: Get Offense closing reasons."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = OffensesHelper.default_connector(GetOffenseClosingReasons())

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason(self, make_request):
        """To get the offense closing reasons.

        :return: None
        """
        action_params = {}
        results = self.action.run(action_params)
        print(results.get("data"))
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_with_fields(self, make_request):
        """To get offense closing reasons with given filed list as output.

        :return: None
        """
        action_params = {"fields": "id"}
        results = self.action.run(action_params)

        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_with_range(self, make_request):
        """To get offenses closing reasons with given range.

        :return: None
        """
        action_params = {"range": "1-2"}
        results = self.action.run(action_params)
        self.assertEqual(len(results.get("data")["data"]), 1)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_with_invalid_range(self, make_request):
        """To get offenses closing reason with given invalid range.

        :return: None
        """
        action_params = {"range": "-1-2"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_with_filter(self, make_request):
        """To get offenses closing reasons with given filter.

        :return: None
        """
        action_params = {"filter": "id=10001"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_with_include_delete(self, make_request):
        """To get offenses with Include_delete.

        :return: None
        """
        action_params = {"Include_delete": "true"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_with_include_reserve(self, make_request):
        """To get offenses with Include_reserve.

        :return: None
        """
        action_params = {"Include_reserve": "true"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_with_multiple_query_params(self, make_request):
        """To get offenses with multiple query prams passed.

        :return: None
        """
        action_params = {"filter": "id=10001", "fields": "id"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")
        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_internal_server_error(self, make_request):
        """To test the get offense closing reason by internalServerError."""
        action_params = {"filter": "internalServerError"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)
