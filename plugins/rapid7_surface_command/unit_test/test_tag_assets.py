import logging
import os
import sys
from unittest import TestCase
from unittest.mock import Mock, patch

sys.path.append(os.path.abspath("../"))

from icon_rapid7_surface_command.util.api_connection import ApiConnection
from insightconnect_plugin_runtime.exceptions import PluginException


OBJECT_IDS = [
    "11111111-1111-1111-1111-111111111111",
    "22222222-2222-2222-2222-222222222222",
]
TAGS = ["env:prod", "team:security"]


class TestTagAssets(TestCase):
    def setUp(self):
        self.logger = logging.getLogger("test")
        self.logger.addHandler(logging.NullHandler())
        self.connection = ApiConnection("not_an_api_key", "us", self.logger)

    # ------------------------------------------------------------------
    # Success paths – one per operation type
    # ------------------------------------------------------------------

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_add_success(self, mock_request):
        mock_request.return_value = Mock(status_code=204)

        result = self.connection.tag_assets(OBJECT_IDS, TAGS, "add")

        self.assertEqual(result["success_count"], 2)
        self.assertEqual(result["failure_count"], 0)
        self.assertEqual(result["failures"], [])
        self.assertEqual(mock_request.call_count, 2)

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_set_uses_put(self, mock_request):
        mock_request.return_value = Mock(status_code=204)

        result = self.connection.tag_assets(OBJECT_IDS, TAGS, "set")

        self.assertEqual(result["success_count"], 2)
        self.assertEqual(result["failure_count"], 0)
        for call_args in mock_request.call_args_list:
            self.assertEqual(call_args[1]["_request"].method, "PUT")

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_remove_uses_delete(self, mock_request):
        mock_request.return_value = Mock(status_code=204)

        result = self.connection.tag_assets(OBJECT_IDS, TAGS, "remove")

        self.assertEqual(result["success_count"], 2)
        self.assertEqual(result["failure_count"], 0)
        for call_args in mock_request.call_args_list:
            self.assertEqual(call_args[1]["_request"].method, "DELETE")

    # ------------------------------------------------------------------
    # Failure paths
    # ------------------------------------------------------------------

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_partial_failure(self, mock_request):
        """First asset succeeds, second raises PluginException."""
        mock_request.side_effect = [
            Mock(status_code=204),
            PluginException(cause="Not found", assistance="Check object ID"),
        ]

        result = self.connection.tag_assets(OBJECT_IDS, TAGS, "add")

        self.assertEqual(result["success_count"], 1)
        self.assertEqual(result["failure_count"], 1)
        self.assertEqual(len(result["failures"]), 1)
        self.assertEqual(result["failures"][0]["object_id"], OBJECT_IDS[1])
        self.assertEqual(result["failures"][0]["error"], "Not found")

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_all_fail(self, mock_request):
        mock_request.side_effect = PluginException(
            cause="Unauthorized", assistance="Check API key"
        )

        result = self.connection.tag_assets(OBJECT_IDS, TAGS, "add")

        self.assertEqual(result["success_count"], 0)
        self.assertEqual(result["failure_count"], 2)
        self.assertEqual(len(result["failures"]), 2)
        for failure in result["failures"]:
            self.assertIn("object_id", failure)
            self.assertEqual(failure["error"], "Unauthorized")

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_unexpected_exception(self, mock_request):
        """Non-PluginException errors are caught and recorded per-asset."""
        mock_request.side_effect = RuntimeError("connection reset")

        result = self.connection.tag_assets(
            ["33333333-3333-3333-3333-333333333333"], TAGS, "add"
        )

        self.assertEqual(result["success_count"], 0)
        self.assertEqual(result["failure_count"], 1)
        self.assertIn("connection reset", result["failures"][0]["error"])

    # ------------------------------------------------------------------
    # Edge cases
    # ------------------------------------------------------------------

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_empty_object_ids(self, mock_request):
        result = self.connection.tag_assets([], TAGS, "add")

        self.assertEqual(result["success_count"], 0)
        self.assertEqual(result["failure_count"], 0)
        self.assertEqual(result["failures"], [])
        mock_request.assert_not_called()

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_correct_url_format(self, mock_request):
        """Verify the URL constructed for each object follows the API spec."""
        mock_request.return_value = Mock(status_code=204)
        single_id = "44444444-4444-4444-4444-444444444444"

        self.connection.tag_assets([single_id], TAGS, "add")

        call_args = mock_request.call_args
        request_obj = call_args[1]["_request"]
        expected_url = f"https://us.api.insight.rapid7.com/surface/graph-api/objects/id/{single_id}/tags"
        self.assertEqual(request_obj.url, expected_url)

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_sends_tags_as_json_body(self, mock_request):
        """Tags list must be sent as the request JSON body."""
        mock_request.return_value = Mock(status_code=204)

        self.connection.tag_assets(
            ["55555555-5555-5555-5555-555555555555"], TAGS, "add"
        )

        call_args = mock_request.call_args
        request_obj = call_args[1]["_request"]
        self.assertEqual(request_obj.json, TAGS)

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_region_reflected_in_url(self, mock_request):
        """Base URL should honour the region set at construction time."""
        mock_request.return_value = Mock(status_code=204)
        eu_connection = ApiConnection("key", "eu", self.logger)

        eu_connection.tag_assets(["66666666-6666-6666-6666-666666666666"], TAGS, "set")

        call_args = mock_request.call_args
        request_obj = call_args[1]["_request"]
        self.assertIn("eu.api.insight.rapid7.com", request_obj.url)
