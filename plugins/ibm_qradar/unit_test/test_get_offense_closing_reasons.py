import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from unittest import TestCase
from jsonschema import validate

from insightconnect_plugin_runtime.exceptions import PluginException
from icon_ibm_qradar.actions.get_offense_closing_reasons.action import GetOffenseClosingReasons
from icon_ibm_qradar.actions.get_offense_closing_reasons.schema import (
    Input,
    GetOffenseClosingReasonsInput,
    GetOffenseClosingReasonsOutput,
)
from helpers.offense import OffensesHelper


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
        validate(action_params, GetOffenseClosingReasonsInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], 10001)
        validate(results.get("data"), GetOffenseClosingReasonsOutput.schema)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_with_fields(self, make_request):
        """To get offense closing reasons with given filed list as output.

        :return: None
        """
        action_params = {Input.FIELDS: "id"}
        validate(action_params, GetOffenseClosingReasonsInput.schema)
        results = self.action.run(action_params)

        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())
        validate(results.get("data"), GetOffenseClosingReasonsOutput.schema)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_with_range(self, make_request):
        """To get offenses closing reasons with given range.

        :return: None
        """
        action_params = {Input.RANGE: "1-2"}
        validate(action_params, GetOffenseClosingReasonsInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(len(results.get("data")["data"]), 1)
        validate(results.get("data"), GetOffenseClosingReasonsOutput.schema)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_with_invalid_range(self, make_request):
        """To get offenses closing reason with given invalid range.

        :return: None
        """
        action_params = {Input.RANGE: "-1-2"}
        validate(action_params, GetOffenseClosingReasonsInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_with_filter(self, make_request):
        """To get offenses closing reasons with given filter.

        :return: None
        """
        action_params = {Input.FILTER: "id=10001"}
        validate(action_params, GetOffenseClosingReasonsInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], 10001)
        validate(results.get("data"), GetOffenseClosingReasonsOutput.schema)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_with_include_delete(self, make_request):
        """To get offenses with Include_delete.

        :return: None
        """
        action_params = {Input.INCLUDE_DELETED: True}
        validate(action_params, GetOffenseClosingReasonsInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], 10001)
        validate(results.get("data"), GetOffenseClosingReasonsOutput.schema)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_with_include_reserve(self, make_request):
        """To get offenses with Include_reserve.

        :return: None
        """
        action_params = {Input.INCLUDE_RESERVED: True}
        validate(action_params, GetOffenseClosingReasonsInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], 10001)
        validate(results.get("data"), GetOffenseClosingReasonsOutput.schema)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_with_multiple_query_params(self, make_request):
        """To get offenses with multiple query prams passed.

        :return: None
        """
        action_params = {"filter": "id=10001", "fields": "id"}
        action_params = {Input.FILTER: "id=10001", Input.FIELDS: "id"}
        validate(action_params, GetOffenseClosingReasonsInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], 10001)
        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())
        validate(results.get("data"), GetOffenseClosingReasonsOutput.schema)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offense_closing_reason_internal_server_error(self, make_request):
        """To test the get offense closing reason by internalServerError."""
        action_params = {Input.FILTER: "internalServerError"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)
