import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from icon_rapid7_cyber_grc.connection.connection import Connection
from icon_rapid7_cyber_grc.util.api import clean_record
from util import BASE_URL, PAGED_ENTITY, MockResponse, Util


@patch("requests.Session.request", side_effect=Util.mock_request)
class TestCyberGrcAPI(TestCase):
    def setUp(self):
        self.client = Util.default_connector(Connection()).connection.client
        Util.calls = []
        Util.updated = {}

    def test_list_records_unwraps_the_odata_value_array(self, mock_request):
        records = self.client.list_records("Risks")

        self.assertEqual([item["id"] for item in records], [1, 2])

    def test_list_records_strips_odata_annotations_from_each_record(self, mock_request):
        for item in self.client.list_records("Risks"):
            self.assertNotIn("@odata.context", item)

    def test_list_records_follows_the_next_link(self, mock_request):
        records = self.client.list_records(PAGED_ENTITY)

        self.assertEqual([item["id"] for item in records], [1, 2])
        self.assertEqual(len(Util.calls), 2)

    def test_list_records_does_not_page_past_an_explicit_top(self, mock_request):
        records = self.client.list_records(PAGED_ENTITY, top=1)

        self.assertEqual([item["id"] for item in records], [1])
        self.assertEqual(len(Util.calls), 1)

    def test_list_records_sends_only_the_query_options_that_were_set(self, mock_request):
        self.client.list_records("Risks", filter_="statusID eq 3", order_by="modifiedDate asc", top=0, skip=None)

        self.assertEqual(Util.calls[0]["params"], {"$filter": "statusID eq 3", "$orderby": "modifiedDate asc"})

    def test_list_records_returns_an_empty_list_when_the_body_has_no_value_array(self, mock_request):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, {"@odata.context": "x"})

        self.assertEqual(self.client.list_records("Risks"), [])

    def test_count_records_parses_the_plain_text_body(self, mock_request):
        self.assertEqual(self.client.count_records("Risks"), 7)
        self.assertTrue(Util.calls[0]["url"].endswith("/api/v2/Risks/$count"))

    def test_count_records_raises_when_the_body_is_not_a_number(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.client.count_records("Uncountable")

        self.assertEqual(context.exception.cause, "Cyber GRC returned an unexpected record count.")

    def test_get_record_requests_the_key_path_and_strips_annotations(self, mock_request):
        result = self.client.get_record("Risks", 5)

        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/Risks/5")
        self.assertEqual(result["id"], 5)
        self.assertNotIn("@odata.context", result)

    def test_create_record_posts_the_body(self, mock_request):
        result = self.client.create_record("Risks", {"name": "New risk"})

        self.assertEqual(Util.calls[0]["method"], "POST")
        self.assertEqual(Util.calls[0]["json"], {"name": "New risk"})
        self.assertEqual(result["name"], "New risk")

    def test_update_record_puts_the_body_to_the_key_path(self, mock_request):
        result = self.client.update_record("Risks", 5, {"name": "Renamed"})

        self.assertEqual(Util.calls[0]["method"], "PUT")
        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/Risks/5")
        self.assertEqual(result["name"], "Renamed")

    def test_update_record_reads_the_record_back_after_an_empty_response(self, mock_request):
        # A successful update answers 204 with no body, so the record is re-read.
        self.client.update_record("Risks", 5, {"name": "Renamed"})

        self.assertEqual([call["method"] for call in Util.calls], ["PUT", "GET"])
        self.assertEqual(Util.calls[1]["url"], f"{BASE_URL}/api/v2/Risks/5")

    def test_update_record_supplies_the_route_key_as_the_body_id(self, mock_request):
        self.client.update_record("Risks", 5, {"name": "Renamed"})

        self.assertEqual(Util.calls[0]["json"], {"name": "Renamed", "id": 5})

    def test_update_record_does_not_overwrite_an_id_the_caller_supplied(self, mock_request):
        self.client.update_record("Risks", 5, {"id": 5, "name": "Renamed"})

        self.assertEqual(Util.calls[0]["json"], {"id": 5, "name": "Renamed"})

    def test_update_record_returns_the_body_when_the_api_sends_one(self, mock_request):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, {"id": 5, "name": "From body"})

        self.assertEqual(self.client.update_record("Risks", 5, {"name": "x"}), {"id": 5, "name": "From body"})

    def test_delete_record_reports_success_for_an_empty_204_response(self, mock_request):
        result = self.client.delete_record("Risks", 5)

        self.assertEqual(Util.calls[0]["method"], "DELETE")
        self.assertEqual(result, {"success": True})

    def test_delete_record_returns_the_body_when_the_api_sends_one(self, mock_request):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(
            200, {"success": False, "fkViolation": True, "message": "In use"}
        )

        self.assertEqual(self.client.delete_record("Risks", 5)["fkViolation"], True)

    def test_get_record_history_uses_the_path_form_that_accepts_api_keys(self, mock_request):
        history = self.client.get_record_history("Risks", 5)

        # History() is what the spec documents, but that form is routed to an
        # interactive-only auth scheme and answers 401 for API keys.
        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/Risks/5/History")
        self.assertEqual(len(history), 2)

    def test_upload_flat_file_sends_the_documented_v1_body(self, mock_request):
        result = self.client.upload_flat_file(
            file_name="assets.csv", contents="aWQK", operation_type="Replace", description="Weekly", record_id=0
        )

        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/flatfile-integrations")
        self.assertEqual(
            Util.calls[0]["json"],
            {"ID": 0, "FileName": "assets.csv", "bytes": "aWQK", "operationType": "Replace", "Description": "Weekly"},
        )
        self.assertTrue(result["success"])

    @parameterized.expand(
        [
            ["bad_request", 400, "Bad request."],
            ["unauthorized", 401, "Unauthorized."],
            ["forbidden", 403, "Forbidden."],
            ["not_found", 404, "Not found."],
            ["rate_limited", 429, "Too many requests."],
        ]
    )
    def test_request_maps_status_codes_to_actionable_errors(self, mock_request, _name, status_code, cause):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(status_code, {"error": "x"})

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertEqual(context.exception.cause, cause)

    def test_request_raises_a_server_error_for_a_5xx_response(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.client.list_records("Broken")

        self.assertEqual(context.exception.cause, PluginException.causes[PluginException.Preset.SERVER_ERROR])

    def test_request_raises_an_invalid_json_error_for_an_unparseable_body(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.client.list_records("Garbled")

        self.assertEqual(context.exception.cause, PluginException.causes[PluginException.Preset.INVALID_JSON])

    def test_request_includes_the_response_body_on_a_bad_request(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks", filter_="invalid")

        self.assertIn("invalid filter", context.exception.data)

    def test_request_reports_an_unverifiable_certificate_clearly(self, mock_request):
        mock_request.side_effect = requests.exceptions.SSLError("self signed certificate")

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertIn("TLS certificate", context.exception.cause)

    def test_request_reports_a_timeout(self, mock_request):
        mock_request.side_effect = requests.exceptions.Timeout("timed out")

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertEqual(context.exception.cause, PluginException.causes[PluginException.Preset.TIMEOUT])

    def test_request_reports_a_transport_failure(self, mock_request):
        mock_request.side_effect = requests.exceptions.ConnectionError("no route to host")

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertEqual(context.exception.cause, PluginException.causes[PluginException.Preset.UNKNOWN])


class TestCleanRecord(TestCase):
    def test_odata_annotations_are_removed(self):
        self.assertEqual(clean_record({"@odata.context": "x", "id": 1}), {"id": 1})

    def test_unset_fields_are_omitted_rather_than_returned_as_null(self):
        self.assertEqual(clean_record({"id": 1, "businessImpact": None}), {"id": 1})

    def test_nested_objects_are_cleaned(self):
        self.assertEqual(
            clean_record({"assignedTo": {"userEmail": "a@example.com", "title": None}}),
            {"assignedTo": {"userEmail": "a@example.com"}},
        )

    def test_records_nested_in_arrays_are_cleaned(self):
        self.assertEqual(clean_record({"tasks": [{"id": 1, "name": None}]}), {"tasks": [{"id": 1}]})

    def test_values_that_are_not_records_pass_through(self):
        self.assertEqual(clean_record("7"), "7")
