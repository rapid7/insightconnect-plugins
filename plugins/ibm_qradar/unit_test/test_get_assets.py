import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from unittest import TestCase
from jsonschema import validate

from insightconnect_plugin_runtime.exceptions import PluginException
from icon_ibm_qradar.actions.get_assets.action import GetAssets
from icon_ibm_qradar.actions.get_assets.schema import Input, GetAssetsInput, GetAssetsOutput
from helpers.assets import AsstesHelper


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
        validate(action_params, GetAssetsInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], 10001)
        validate(results.get("data"), GetAssetsOutput.schema)

    @patch("requests.get", side_effect=AsstesHelper.mock_request)
    def test_get_assets_with_fields(self, make_request):
        """To get assets with given filed list as output.

        :return: None
        """
        action_params = {Input.FIELDS: "id"}
        validate(action_params, GetAssetsInput.schema)
        results = self.action.run(action_params)

        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())
        validate(results.get("data"), GetAssetsOutput.schema)

    @patch("requests.get", side_effect=AsstesHelper.mock_request)
    def test_get_assets_with_range(self, make_request):
        """To get assets with given range.

        :return: None
        """
        action_params = {Input.RANGE: "1-2"}
        validate(action_params, GetAssetsInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(len(results.get("data")["data"]), 1)
        validate(results.get("data"), GetAssetsOutput.schema)

    @patch("requests.get", side_effect=AsstesHelper.mock_request)
    def test_get_assets_with_invalid_range(self, make_request):
        """To get assets with given invalid range.

        :return: None
        """
        action_params = {Input.RANGE: "-1-2"}
        validate(action_params, GetAssetsInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.get", side_effect=AsstesHelper.mock_request)
    def test_get_assets_with_filter(self, make_request):
        """To get assets with given filter.

        :return: None
        """
        action_params = {Input.FILTER: "id=10001"}
        validate(action_params, GetAssetsInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], 10001)
        validate(results.get("data"), GetAssetsOutput.schema)

    @patch("requests.get", side_effect=AsstesHelper.mock_request)
    def test_get_assets_with_multiple_query_params_given(self, make_request):
        """To get assets with multiple option given.

        :return: None
        """
        action_params = {Input.FILTER: "id=10001", Input.FIELDS: "id"}
        validate(action_params, GetAssetsInput.schema)
        results = self.action.run(action_params)
        self.assertEqual(results.get("data")["data"][0]["id"], 10001)
        self.assertEqual(len(results.get("data")["data"][0].keys()), 1)
        self.assertTrue("id" in results.get("data")["data"][0].keys())
        validate(results.get("data"), GetAssetsOutput.schema)

    @patch("requests.get", side_effect=AsstesHelper.mock_request)
    def test_with_internal_server_error(self, make_request):
        """To test the get assets by ID with internalServerError."""
        action_params = {"filter": "internalServerError"}
        validate(action_params, GetAssetsInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(action_params)
