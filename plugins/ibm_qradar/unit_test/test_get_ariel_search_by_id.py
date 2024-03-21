import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from jsonschema import validate

from insightconnect_plugin_runtime.exceptions import PluginException
from icon_ibm_qradar.actions.get_ariel_search_by_id.action import GetArielSearchById
from icon_ibm_qradar.actions.get_ariel_search_by_id.schema import (
    Input,
    GetArielSearchByIdInput,
    GetArielSearchByIdOutput,
)
from helpers.ariel_search import ArielSearchHelper


class TestGetArielSearchById(TestCase):
    """Unit Test class for Test cases of action: Get ariel search by ID."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = ArielSearchHelper.default_connector(GetArielSearchById())

    @patch("requests.get", side_effect=ArielSearchHelper.mock_request)
    def test_get_ariel_search_by_id(self, make_request):
        """To test the get ariel search by ID."""
        action_params = {Input.SEARCH_ID: "search_id"}
        validate(action_params, GetArielSearchByIdInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["cursor_id"], "test_cursor_id")
        validate(results.get("data"), GetArielSearchByIdOutput.schema)

    @patch("requests.get", side_effect=ArielSearchHelper.mock_request)
    def test_get_ariel_search_by_id_with_poll_interval(self, make_request):
        """To test the get ariel search by ID."""
        action_params = {Input.SEARCH_ID: "search_id", Input.POLL_INTERVAL: 1}
        validate(action_params, GetArielSearchByIdInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["cursor_id"], "test_cursor_id")
        validate(results.get("data"), GetArielSearchByIdOutput.schema)

    @patch("requests.get", side_effect=ArielSearchHelper.mock_request)
    def test_get_ariel_search_by_wrong_id(self, make_request):
        """To test the get ariel search by ID."""
        action_params = {Input.SEARCH_ID: "wrong"}
        validate(action_params, GetArielSearchByIdInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.get", side_effect=ArielSearchHelper.mock_request)
    def test_get_ariel_search_by_id_wrong_host_url(self, make_request):
        """To test the get ariel search with wrong host_url.

        :return: None
        """
        action_params = {Input.SEARCH_ID: "search_id"}
        validate(action_params, GetArielSearchByIdInput.schema)
        action = ArielSearchHelper.default_connector(
            GetArielSearchById(),
            {
                "host_url": "http://wrong",
                "credentials": {"username": "user1", "password": "password"},
            },
        )

        with self.assertRaises(PluginException):
            action.run(action_params)

    @patch("requests.get", side_effect=ArielSearchHelper.mock_request)
    def test_get_ariel_search_by_id_with_internal_server_error(self, make_request):
        """To test the get ariel search by ID with internalServerError."""
        action_params = {Input.SEARCH_ID: "internalServerError"}
        validate(action_params, GetArielSearchByIdInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.get", side_effect=ArielSearchHelper.mock_request)
    def test_get_ariel_search_by_id_with_forbidden(self, make_request):
        """To test the get ariel search by ID with forbidden."""
        action_params = {Input.SEARCH_ID: "checkforbidden"}
        validate(action_params, GetArielSearchByIdInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.get", side_effect=ArielSearchHelper.mock_request)
    def test_get_ariel_search_by_id_with_rate_limit(self, make_request):
        """To test the get ariel search by ID with rate limit."""
        action_params = {Input.SEARCH_ID: "checkratelimit"}
        validate(action_params, GetArielSearchByIdInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(action_params)
