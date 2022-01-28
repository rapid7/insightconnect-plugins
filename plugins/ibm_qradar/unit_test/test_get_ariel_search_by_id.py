import os
import sys
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ibm_qradar.actions.get_ariel_search_by_id import GetArielSearchById
from unit_test.helpers.ariel_search import ArielSearchHelper

sys.path.append(os.path.abspath("../"))


class TestGetArielSearchById(TestCase):
    """Unit Test class for Test cases of action: Get ariel search by ID."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = ArielSearchHelper.default_connector(GetArielSearchById())

    @patch("requests.get", side_effect=ArielSearchHelper.mock_request)
    def test_get_ariel_search_by_id(self, make_request):
        """To test the get ariel search by ID."""
        action_params = {"search_id": "search_id"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["cursor_id"], "test_cursor_id")

    @patch("requests.get", side_effect=ArielSearchHelper.mock_request)
    def test_get_ariel_search_by_id_with_poll_interval(self, make_request):
        """To test the get ariel search by ID."""
        action_params = {"search_id": "search_id", "poll_interval": 1}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["cursor_id"], "test_cursor_id")

    @patch("requests.get", side_effect=ArielSearchHelper.mock_request)
    def test_get_ariel_search_by_wrong_id(self, make_request):
        """To test the get ariel search by ID."""
        action_params = {"search_id": "wrong"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.get", side_effect=ArielSearchHelper.mock_request)
    def test_get_ariel_search_by_id_wrong_host_url(self, make_request):
        """To test the get ariel search with wrong host_url.

        :return: None
        """
        action_params = {"search_id": "search_id"}

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
        action_params = {"search_id": "internalServerError"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.get", side_effect=ArielSearchHelper.mock_request)
    def test_get_ariel_search_by_id_with_forbidden(self, make_request):
        """To test the get ariel search by ID with forbidden."""
        action_params = {"search_id": "checkforbidden"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.get", side_effect=ArielSearchHelper.mock_request)
    def test_get_ariel_search_by_id_with_rate_limit(self, make_request):
        """To test the get ariel search by ID with rate limit."""
        action_params = {"search_id": "checkratelimit"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)
