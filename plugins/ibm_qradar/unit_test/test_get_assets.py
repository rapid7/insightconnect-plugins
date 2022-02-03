import os
import sys
from unittest.mock import patch

from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ibm_qradar.actions.get_assets import GetAssets
from unit_test.helpers.assets import AsstesHelper

sys.path.append(os.path.abspath("../"))


class TestGetAssets(TestCase):
    """Test case class for action: Get assets."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = AsstesHelper.default_connector(GetAssets())

    @patch("requests.get", side_effect=AsstesHelper.mock_request)
    def test_get_assets(self, make_request):
        """To get the assets.

        :return: None
        """
        action_params = {}
        results = self.action.run(action_params)
        print(results.get("data"))
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")

    @patch("requests.get", side_effect=AsstesHelper.mock_request)
    def test_get_assets_with_fields(self, make_request):
        """To get assets with given filed list as output.

        :return: None
        """
        action_params = {"fields": "id"}
        results = self.action.run(action_params)

        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())

    @patch("requests.get", side_effect=AsstesHelper.mock_request)
    def test_get_assets_with_range(self, make_request):
        """To get assets with given range.

        :return: None
        """
        action_params = {"range": "1-2"}
        results = self.action.run(action_params)
        self.assertEqual(len(results.get("data")["data"]), 1)

    @patch("requests.get", side_effect=AsstesHelper.mock_request)
    def test_get_assets_with_invalid_range(self, make_request):
        """To get assets with given invalid range.

        :return: None
        """
        action_params = {"range": "-1-2"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.get", side_effect=AsstesHelper.mock_request)
    def test_get_assets_with_filter(self, make_request):
        """To get assets with given filter.

        :return: None
        """
        action_params = {"filter": "id=10001"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")

    @patch("requests.get", side_effect=AsstesHelper.mock_request)
    def test_get_assets_with_multiple_query_params_given(self, make_request):
        """To get assets with multiple option given.

        :return: None
        """
        action_params = {"filter": "id=10001", "fields": "id"}
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], "10001")
        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())

    @patch("requests.get", side_effect=AsstesHelper.mock_request)
    def test_with_internal_server_error(self, make_request):
        """To test the get assets by ID with internalServerError."""
        action_params = {"filter": "internalServerError"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)
