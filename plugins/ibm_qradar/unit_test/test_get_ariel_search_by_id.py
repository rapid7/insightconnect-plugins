"""Test cases for get ariel search by id end point action."""
import os
import sys
from unittest import TestCase
from unittest.mock import patch

import requests
from insightconnect_plugin_runtime.exceptions import PluginException, ClientException

from icon_ibm_qradar.actions.get_ariel_search_by_id import GetArielSearchById
from unit_test.helper import Helper

sys.path.append(os.path.abspath("../"))


class TestGetArielSearchById(TestCase):
    """Unit Test class for Test cases of action : get ariel search by id."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = Helper.default_connector(GetArielSearchById())

    @patch("requests.request", side_effect=Helper.mock_request)
    def test_get_ariel_search_by_id(self, make_request):
        """To Test the get serial search by id."""
        action_params = {"search_id": "search_id"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["cursor_id"], "test_cursor_id")

    @patch("requests.request", side_effect=Helper.mock_request)
    def test_get_ariel_search_by_id_with_poll_interval(self, make_request):
        """To Test the get serial search by id."""
        action_params = {"search_id": "search_id", "poll_interval": 1}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["cursor_id"], "test_cursor_id")

    @patch("requests.request", side_effect=Helper.mock_request)
    def test_get_ariel_search_by_wrong_id(self, make_request):
        """To Test the get serial search by id."""
        action_params = {"search_id": "wrong"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.request", side_effect=Helper.mock_request)
    def test_get_ariel_search_by_id_with_empty_searchid(self, make_request):
        """To Test the get serial search by id."""
        action_params = {"search_id": ""}
        with self.assertRaises(ClientException):
            self.action.run(action_params)

    @patch("requests.request", side_effect=Helper.mock_request)
    def test_get_ariel_search_by_id_wrong_hostname(self, make_request):
        """To test the get ariel search with wrong hostname.

        :return: None
        """
        action_params = {"search_id": "search_id"}

        action = Helper.default_connector(
            GetArielSearchById(),
            {"hostname": "wrong", "username": "username", "password": "password"},
        )

        with self.assertRaises(requests.exceptions.ConnectionError):
            action.run(action_params)

    @patch("requests.request", side_effect=Helper.mock_request)
    def test_get_ariel_search_by_id_with_internal_server_error(self, make_request):
        """To Test the get serial search by id with internalServerError."""
        action_params = {"search_id": "internalServerError"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)
