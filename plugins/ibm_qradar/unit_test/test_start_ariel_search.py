import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from unittest import TestCase
from jsonschema import validate

from insightconnect_plugin_runtime.exceptions import (
    PluginException,
    ConnectionTestException,
)

from icon_ibm_qradar.actions.start_ariel_search.action import StartArielSearch
from icon_ibm_qradar.actions.start_ariel_search.schema import Input, StartArielSearchInput, StartArielSearchOutput
from helpers.ariel_search import ArielSearchHelper


class TestStartArielSearch(TestCase):
    """Test case class for action: Start ariel search."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = ArielSearchHelper.default_connector(StartArielSearch())

    @patch("requests.request", side_effect=ArielSearchHelper.mock_request)
    def test_start_ariel_search(self, make_request):
        """To test the ariel search.

        :return: None
        """
        action_params = {Input.AQL: "Select * from events"}
        validate(action_params, StartArielSearchInput.schema)
        results = self.action.run(action_params)

        self.assertEqual(results.get("data")["cursor_id"], "test_cursor_id")
        validate(results.get("data"), StartArielSearchOutput.schema)

    @patch("requests.request", side_effect=ArielSearchHelper.mock_request)
    def test_start_ariel_search_wrong_host_url(self, make_request):
        """To test the ariel search with wrong host_url.

        :return: None
        """
        action_params = {Input.AQL: "Select * from events"}
        validate(action_params, StartArielSearchInput.schema)
        action = ArielSearchHelper.default_connector(
            StartArielSearch(),
            {
                "host_url": "http://wrong",
                "credentials": {"username": "user1", "password": "password"},
            },
        )

        with self.assertRaises(PluginException):
            action.run(params=action_params)

    @patch("requests.request", side_effect=ArielSearchHelper.mock_request)
    def test_start_ariel_search_wrong_aql(self, make_request):
        """To test the ariel search with wrong aql.

        :return: None
        """
        action_params = {Input.AQL: "wrong"}
        validate(action_params, StartArielSearchInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(params=action_params)

    @patch("requests.request", side_effect=ArielSearchHelper.mock_request)
    def test_start_ariel_search_wrong_username(self, make_request):
        """To test the ariel search with wrong username.

        :return: None
        """
        action_params = {Input.AQL: "Select * from events"}
        validate(action_params, StartArielSearchInput.schema)
        action = ArielSearchHelper.default_connector(
            StartArielSearch(),
            {
                "host_url": "http://host_url",
                "credentials": {"username": "wrong", "password": "password"},
            },
        )

        with self.assertRaises(ConnectionTestException) as err:
            action.run(params=action_params)
            self.assertEqual(ConnectionTestException.Preset.USERNAME_PASSWORD, err.exception.preset)
