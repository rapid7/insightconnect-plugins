import os
import sys
from unittest.mock import patch

from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import (
    PluginException,
    ConnectionTestException,
)

from icon_ibm_qradar.actions.start_ariel_search import StartArielSearch
from unit_test.helpers.ariel_search import ArielSearchHelper

sys.path.append(os.path.abspath("../"))


class TestStartArielSearch(TestCase):
    """Test case class for action: Start ariel search."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = ArielSearchHelper.default_connector(StartArielSearch())

    @patch("requests.post", side_effect=ArielSearchHelper.mock_request)
    def test_start_ariel_search(self, make_request):
        """To test the ariel search.

        :return: None
        """
        action_params = {"aql": "Select * from events"}
        results = self.action.run(action_params)

        self.assertEqual(results.get("data")["cursor_id"], "test_cursor_id")

    @patch("requests.post", side_effect=ArielSearchHelper.mock_request)
    def test_start_ariel_search_wrong_host_url(self, make_request):
        """To test the ariel search with wrong host_url.

        :return: None
        """
        action_params = {"aql": "Select * from events"}

        action = ArielSearchHelper.default_connector(
            StartArielSearch(),
            {
                "host_url": "http://wrong",
                "credentials": {"username": "user1", "password": "password"},
            },
        )

        with self.assertRaises(PluginException):
            action.run(params=action_params)

    @patch("requests.post", side_effect=ArielSearchHelper.mock_request)
    def test_start_ariel_search_wrong_aql(self, make_request):
        """To test the ariel search with wrong aql.

        :return: None
        """
        action_params = {"aql": "wrong"}

        with self.assertRaises(PluginException):
            self.action.run(params=action_params)

    @patch("requests.post", side_effect=ArielSearchHelper.mock_request)
    def test_start_ariel_search_wrong_username(self, make_request):
        """To test the ariel search with wrong username.

        :return: None
        """
        action_params = {"aql": "Select * from events"}

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
