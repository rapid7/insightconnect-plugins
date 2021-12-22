"""Test cases for action : start ariel search."""
import os
import sys
from unittest.mock import patch

import requests
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import (
    PluginException,
    ClientException,
    ConnectionTestException,
)

from icon_ibm_qradar.actions.start_ariel_search import StartArielSearch
from unit_test.helper import Helper

sys.path.append(os.path.abspath("../"))


class TestStartArielSearch(TestCase):
    """Test case class for action : Start ariel search."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = Helper.default_connector(StartArielSearch())

    @patch("requests.request", side_effect=Helper.mock_request)
    def test_start_ariel_search(self, make_request):
        """To test the ariel search.

        :return: None
        """
        action_params = {"AQL": "Select * from events"}
        results = self.action.run(action_params)

        self.assertEqual(results.get("data")["cursor_id"], "test_cursor_id")

    @patch("requests.request", side_effect=Helper.mock_request)
    def test_start_ariel_search_wrong_hostname(self, make_request):
        """To test the ariel search with wrong hostname.

        :return: None
        """
        action_params = {"AQL": "Select * from events"}

        action = Helper.default_connector(
            StartArielSearch(),
            {"hostname": "wrong", "username": "username", "password": "password"},
        )

        with self.assertRaises(requests.exceptions.ConnectionError):
            action.run(params=action_params)

    @patch("requests.request", side_effect=Helper.mock_request)
    def test_start_ariel_search_wrong_aql(self, make_request):
        """To test the ariel search with wrong aql.

        :return: None
        """
        action_params = {"AQL": "wrong"}

        with self.assertRaises(PluginException):
            self.action.run(params=action_params)

    @patch("requests.request", side_effect=Helper.mock_request)
    def test_start_ariel_search_empty_aql(self, make_request):
        """To test the ariel search with empty aql.

        :return: None
        """
        action_params = {"AQL": ""}

        with self.assertRaises(ClientException):
            self.action.run(params=action_params)

    @patch("requests.request", side_effect=Helper.mock_request)
    def test_start_ariel_search_wrong_username(self, make_request):
        """To test the ariel search with wrong username.

        :return: None
        """
        action_params = {"AQL": "Select * from events"}

        action = Helper.default_connector(
            StartArielSearch(),
            {"hostname": "hostname", "username": "wrong", "password": "password"},
        )

        with self.assertRaises(ConnectionTestException) as err:
            action.run(params=action_params)
            self.assertEqual(ConnectionTestException.Preset.USERNAME_PASSWORD, err.exception.preset)
