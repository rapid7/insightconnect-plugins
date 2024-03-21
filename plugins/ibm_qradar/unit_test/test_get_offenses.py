import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from unittest import TestCase
from jsonschema import validate

from insightconnect_plugin_runtime.exceptions import PluginException
from icon_ibm_qradar.actions.get_offenses.action import GetOffenses
from icon_ibm_qradar.actions.get_offenses.schema import Input, GetOffensesInput, GetOffensesOutput
from helpers.offense import OffensesHelper


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
        validate(action_params, GetOffensesInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], 10001)
        validate(results.get("data"), GetOffensesOutput.schema)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offenses_with_fields(self, make_request):
        """To get offenses with given filed list as output.

        :return: None
        """
        action_params = {Input.FIELDS: "id2"}
        validate(action_params, GetOffensesInput.schema)
        results = self.action.run(action_params)

        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())
        validate(results.get("data"), GetOffensesOutput.schema)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offenses_with_range(self, make_request):
        """To get offenses with given range.

        :return: None
        """
        action_params = {Input.RANGE: "1-2"}
        validate(action_params, GetOffensesInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(len(results.get("data")["data"]), 1)
        validate(results.get("data"), GetOffensesOutput.schema)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offenses_with_invalid_range(self, make_request):
        """To get offenses with given invalid range.

        :return: None
        """
        action_params = {Input.RANGE: "-1-2"}
        validate(action_params, GetOffensesInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offenses_with_filter(self, make_request):
        """To get offenses with given filters.

        :return: None
        """
        action_params = {Input.FILTER: "id=10001"}
        validate(action_params, GetOffensesInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], 10001)
        validate(results.get("data"), GetOffensesOutput.schema)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offenses_with_sort(self, make_request):
        """To get offenses with given sort options.

        :return: None
        """
        action_params = {Input.SORT: "+id"}
        validate(action_params, GetOffensesInput.schema)
        results = self.action.run(action_params)
        self.assertTrue(results.get("data")["data"][0]["id"] < results.get("data")["data"][1]["id"])
        validate(results.get("data"), GetOffensesOutput.schema)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offenses_with_multiple_query_params(self, make_request):
        """To get offenses with multiple query prams passed.

        :return: None
        """
        action_params = {Input.FILTER: "id=10001", Input.FIELDS: "id"}
        validate(action_params, GetOffensesInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], 10001)
        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())
        validate(results.get("data"), GetOffensesOutput.schema)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_with_internal_server_error(self, make_request):
        """To test the get offense with internalServerError."""
        action_params = {Input.FILTER: "internalServerError"}
        validate(action_params, GetOffensesInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(action_params)
