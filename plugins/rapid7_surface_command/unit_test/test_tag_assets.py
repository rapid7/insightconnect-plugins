import logging
import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

sys.path.append(os.path.abspath("../"))

from icon_rapid7_surface_command.actions.tag_assets.action import TagAssets
from icon_rapid7_surface_command.actions.tag_assets.schema import Input, Output
from icon_rapid7_surface_command.util.api_connection import (
    ApiConnection,
    NON_RETRYABLE_STATUS_CODES,
    RETRYABLE_STATUS_CODES,
)
from insightconnect_plugin_runtime.exceptions import PluginException

OBJECT_IDS = [
    "11111111-1111-1111-1111-111111111111",
    "22222222-2222-2222-2222-222222222222",
]
TAGS = ["env:prod", "team:security"]


def _plugin_exception_with_status(status_code: int, cause: str = "API error") -> PluginException:
    """Build a PluginException whose .data is a mock Response with a status code.

    Uses spec=Response so that isinstance(exc.data, Response) returns True,
    matching the behaviour of real responses from make_request.
    """
    from requests import Response as RequestsResponse

    mock_response = Mock(spec=RequestsResponse)
    mock_response.status_code = status_code
    mock_response.headers = {}
    exc = PluginException(cause=cause, assistance="See docs")
    exc.data = mock_response
    return exc


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
        """One asset succeeds, one fails — verified by URL matching, not call order."""
        fail_id = OBJECT_IDS[1]

        def side_effect(*args, **kwargs):
            request = kwargs["_request"]
            if fail_id in request.url:
                raise PluginException(cause="Not found", assistance="Check object ID")
            return Mock(status_code=204)

        mock_request.side_effect = side_effect

        result = self.connection.tag_assets(OBJECT_IDS, TAGS, "add", max_retries=0)

        self.assertEqual(result["success_count"], 1)
        self.assertEqual(result["failure_count"], 1)
        self.assertEqual(len(result["failures"]), 1)
        self.assertEqual(result["failures"][0]["object_id"], fail_id)
        self.assertEqual(result["failures"][0]["error"], "Not found")

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_all_fail(self, mock_request):
        mock_request.side_effect = PluginException(cause="Unauthorized", assistance="Check API key")

        result = self.connection.tag_assets(OBJECT_IDS, TAGS, "add", max_retries=0)

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

        result = self.connection.tag_assets(["33333333-3333-3333-3333-333333333333"], TAGS, "add", max_retries=0)

        self.assertEqual(result["success_count"], 0)
        self.assertEqual(result["failure_count"], 1)
        self.assertIn("connection reset", result["failures"][0]["error"])

    @patch("icon_rapid7_surface_command.util.api_connection.time")
    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_retries_unexpected_exception_then_succeeds(self, mock_request, mock_time):
        """A generic exception is retried with backoff; success on the second attempt is recorded."""
        mock_request.side_effect = [RuntimeError("connection reset"), Mock(status_code=204)]

        result = self.connection.tag_assets(["33333333-3333-3333-3333-333333333333"], TAGS, "add", max_retries=1)

        self.assertEqual(result["success_count"], 1)
        self.assertEqual(result["failure_count"], 0)
        self.assertEqual(mock_request.call_count, 2)
        mock_time.sleep.assert_called_once_with(1.0)  # 2**0 = 1s for attempt 0

    # ------------------------------------------------------------------
    # Retry behaviour
    # ------------------------------------------------------------------

    @patch("icon_rapid7_surface_command.util.api_connection.time")
    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_retries_on_transient_error(self, mock_request, mock_time):
        """A transient 503 is retried; success on the second attempt is recorded."""
        transient_exc = _plugin_exception_with_status(503, cause="Service unavailable")
        mock_request.side_effect = [transient_exc, Mock(status_code=204)]

        result = self.connection.tag_assets(["44444444-4444-4444-4444-444444444444"], TAGS, "add", max_retries=1)

        self.assertEqual(result["success_count"], 1)
        self.assertEqual(result["failure_count"], 0)
        self.assertEqual(mock_request.call_count, 2)
        mock_time.sleep.assert_called_once()

    @patch("icon_rapid7_surface_command.util.api_connection.time")
    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_no_retry_on_non_retryable_status(self, mock_request, mock_time):
        """A 401 fails immediately without consuming any retry budget."""
        mock_request.side_effect = _plugin_exception_with_status(401, cause="Unauthorized")

        result = self.connection.tag_assets(["55555555-5555-5555-5555-555555555555"], TAGS, "add", max_retries=3)

        self.assertEqual(result["success_count"], 0)
        self.assertEqual(result["failure_count"], 1)
        # Only one request made — no retries
        self.assertEqual(mock_request.call_count, 1)
        mock_time.sleep.assert_not_called()
        self.assertIn("401", result["failures"][0]["error"])

    @patch("icon_rapid7_surface_command.util.api_connection.time")
    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_exhausted_retries_records_failure(self, mock_request, mock_time):
        """If all retry attempts fail the asset is recorded as a failure."""
        mock_request.side_effect = _plugin_exception_with_status(503, cause="Service unavailable")

        result = self.connection.tag_assets(["66666666-6666-6666-6666-666666666666"], TAGS, "add", max_retries=2)

        self.assertEqual(result["success_count"], 0)
        self.assertEqual(result["failure_count"], 1)
        # 1 initial attempt + 2 retries = 3 total calls
        self.assertEqual(mock_request.call_count, 3)
        self.assertEqual(mock_time.sleep.call_count, 2)

    @patch("icon_rapid7_surface_command.util.api_connection.time")
    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_tag_assets_respects_retry_after_header(self, mock_request, mock_time):
        """A 429 response with a Retry-After header uses that value for the sleep delay."""
        from requests import Response as RequestsResponse

        mock_response = Mock(spec=RequestsResponse)
        mock_response.status_code = 429
        mock_response.headers = {"Retry-After": "30"}
        rate_limit_exc = PluginException(cause="Rate limited", assistance="Wait and retry")
        rate_limit_exc.data = mock_response

        mock_request.side_effect = [rate_limit_exc, Mock(status_code=204)]

        result = self.connection.tag_assets(["77777777-7777-7777-7777-777777777777"], TAGS, "add", max_retries=1)

        self.assertEqual(result["success_count"], 1)
        mock_time.sleep.assert_called_once_with(30.0)

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

        self.connection.tag_assets(["55555555-5555-5555-5555-555555555555"], TAGS, "add")

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


class TestTagAssetsAction(TestCase):
    """Tests for the TagAssets action class (action.py), covering the run() entry point."""

    def setUp(self):
        self.action = TagAssets()
        self.action.connection = MagicMock()

    def test_run_returns_counts_and_failures_from_api(self):
        """run() delegates to the API client and maps the result to output keys."""
        self.action.connection.api.tag_assets.return_value = {
            "success_count": 2,
            "failure_count": 1,
            "failures": [{"object_id": "abc-123", "error": "Not found"}],
        }
        params = {
            Input.OBJECT_IDS: ["id-1", "id-2", "id-3"],
            Input.TAGS: ["env:prod"],
            Input.OPERATION: "add",
        }

        result = self.action.run(params)

        self.assertEqual(result[Output.SUCCESS_COUNT], 2)
        self.assertEqual(result[Output.FAILURE_COUNT], 1)
        self.assertEqual(len(result[Output.FAILURES]), 1)
        self.assertEqual(result[Output.FAILURES][0]["object_id"], "abc-123")
        self.action.connection.api.tag_assets.assert_called_once_with(
            object_ids=params[Input.OBJECT_IDS],
            tags=params[Input.TAGS],
            operation=params[Input.OPERATION],
        )

    def test_run_all_success_returns_empty_failures(self):
        """run() with no failures returns an empty failures list."""
        self.action.connection.api.tag_assets.return_value = {
            "success_count": 3,
            "failure_count": 0,
            "failures": [],
        }
        params = {
            Input.OBJECT_IDS: ["id-1", "id-2", "id-3"],
            Input.TAGS: ["team:security"],
            Input.OPERATION: "set",
        }

        result = self.action.run(params)

        self.assertEqual(result[Output.SUCCESS_COUNT], 3)
        self.assertEqual(result[Output.FAILURE_COUNT], 0)
        self.assertEqual(result[Output.FAILURES], [])
