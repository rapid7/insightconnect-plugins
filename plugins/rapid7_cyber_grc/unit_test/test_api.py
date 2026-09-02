import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from icon_rapid7_cyber_grc.connection.connection import Connection
from icon_rapid7_cyber_grc.util.api import CyberGrcAPI, clean_record
from util import API_KEY, BASE_URL, PAGED_ENTITY, MockResponse, Util


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

    def test_list_records_raises_when_the_body_has_no_value_array(self, mock_request):
        # Returning [] here would report an API change as a collection that is empty.
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, {"@odata.context": "x"})

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertIn("unexpected response for Risks", context.exception.cause)
        self.assertIn("value array", context.exception.assistance)

    def test_list_records_names_the_type_it_received_when_the_shape_is_wrong(self, mock_request):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, {"value": {"id": 1}})

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertIn("returned a JSON object", context.exception.assistance)

    def test_list_records_pages_and_truncates_a_top_the_api_would_refuse(self, mock_request):
        # The API caps $top at 100 and answers a larger value with a 400, so a bigger
        # ceiling has to be honoured by paging instead of being passed through.
        records = self.client.list_records(PAGED_ENTITY, top=250)

        self.assertNotIn("$top", Util.calls[0]["params"])
        self.assertEqual(len(Util.calls), 2)
        self.assertEqual([item["id"] for item in records], [1, 2])

    def test_list_records_stops_paging_once_the_top_is_reached(self, mock_request):
        records = self.client.list_records(PAGED_ENTITY, top=101)

        self.assertEqual(len(records), 2)

    def test_list_records_sends_a_top_the_api_accepts_unchanged(self, mock_request):
        self.client.list_records(PAGED_ENTITY, top=100)

        self.assertEqual(Util.calls[0]["params"]["$top"], 100)
        self.assertEqual(len(Util.calls), 1)

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
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, {"success": True, "message": "Deleted"})

        self.assertEqual(self.client.delete_record("Risks", 5)["message"], "Deleted")

    def test_delete_record_raises_when_the_api_reports_a_refused_delete(self, mock_request):
        # A refused delete comes back as a 200, which would otherwise look successful.
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(
            200,
            {"success": False, "fkViolation": True, "fkViolationTable": ["Tasks", "Audits"], "message": "Still in use"},
        )

        with self.assertRaises(PluginException) as context:
            self.client.delete_record("Risks", 5)

        self.assertEqual(context.exception.cause, "Cyber GRC refused to delete Risks record 5.")
        self.assertIn("Still in use", context.exception.assistance)
        self.assertIn("Tasks, Audits", context.exception.assistance)

    def test_delete_record_explains_a_refused_delete_that_gives_no_reason(self, mock_request):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, {"success": False})

        with self.assertRaises(PluginException) as context:
            self.client.delete_record("Risks", 5)

        self.assertIn("without giving a reason", context.exception.assistance)

    def test_get_record_rejects_a_response_that_is_not_a_single_record(self, mock_request):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, [{"id": 5}])

        with self.assertRaises(PluginException) as context:
            self.client.get_record("Risks", 5)

        self.assertIn("unexpected response for Risks 5", context.exception.cause)
        self.assertIn("returned a JSON array", context.exception.assistance)

    def test_update_record_explains_a_read_back_that_failed_after_a_successful_update(self, mock_request):
        def put_succeeds_then_get_fails(method, *args, **kwargs):
            return MockResponse(204) if method == "PUT" else MockResponse(404)

        mock_request.side_effect = put_succeeds_then_get_fails

        with self.assertRaises(PluginException) as context:
            self.client.update_record("Risks", 5, {"name": "Renamed"})

        self.assertIn("was updated, but it could not be read back", context.exception.cause)
        self.assertIn("answered 204 No Content", context.exception.assistance)

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

    @parameterized.expand([["forbidden", 403], ["not_found", 404], ["rate_limited", 429]])
    def test_request_names_the_failing_request(self, mock_request, _name, status_code):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(status_code, {"error": "x"})

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertIn(f"GET {BASE_URL}/api/v2/Risks", context.exception.assistance)

    def test_a_forbidden_response_repeats_the_reason_the_api_gave(self, mock_request):
        # A 403 is not always a missing permission: the live API uses it for a feature
        # that is switched off for the whole tenant, which the user needs to be told.
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(
            403, {"message": "The feature 'custom.custom_control_sets' is currently disabled."}
        )

        with self.assertRaises(PluginException) as context:
            self.client.create_record("ControlSets", {"name": "x"})

        self.assertEqual(context.exception.cause, "Forbidden.")
        self.assertIn("custom.custom_control_sets", context.exception.assistance)

    def test_an_overlong_api_message_is_left_out_of_the_assistance(self, mock_request):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(403, {"message": "x" * 400})

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertNotIn("x" * 400, context.exception.assistance)
        self.assertIn("x" * 400, context.exception.data)

    def test_request_repeats_the_retry_after_delay_the_api_asked_for(self, mock_request):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(
            429, {"error": "slow down"}, headers={"Content-Type": "application/json", "Retry-After": "30"}
        )

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertIn("delay of 30 seconds", context.exception.assistance)

    def test_a_bad_request_reports_what_the_api_objected_to_without_the_stack_trace(self, mock_request):
        # An OData error carries a stack trace alongside the one useful sentence.
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(
            400,
            {
                "error": {
                    "message": "Could not find a property named 'nosuchfield' on type 'GetRiskDto'.",
                    "innererror": {"stacktrace": "   at Microsoft.OData.UriParser..."},
                }
            },
        )

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks", filter_="nosuchfield eq 1")

        self.assertIn("as a bad request", context.exception.cause)
        self.assertIn("Could not find a property named 'nosuchfield'", context.exception.assistance)
        self.assertNotIn("stacktrace", context.exception.assistance)

    def test_a_401_from_an_unrecognised_path_does_not_blame_the_api_key(self, mock_request):
        # Any path the API key middleware does not recognise, including a misspelled
        # record type, falls through to the interactive scheme and answers 401.
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(
            401, {"error": "unauthorized", "error_description": "JWT validation failed", "scheme": "compyl-microsoft"}
        )

        with self.assertRaises(PluginException) as context:
            self.client.list_records("NotAType")

        self.assertIn("does not expose", context.exception.cause)
        self.assertIn("not the problem", context.exception.assistance)
        self.assertIn("/api/v2 suffix", context.exception.assistance)

    def test_a_401_with_no_json_body_blames_the_api_key(self, mock_request):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(401, text="Unauthorized")

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertEqual(context.exception.cause, "Unauthorized.")

    def test_a_401_from_the_api_key_scheme_blames_the_api_key(self, mock_request):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(
            401,
            {"error": "unauthorized", "error_description": "A valid API key is required.", "scheme": "ApiKey"},
        )

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertEqual(context.exception.cause, "Unauthorized.")
        self.assertIn("revoked or expired", context.exception.assistance)

    @parameterized.expand([["success", 200], ["sign_in_page", 401]])
    def test_request_recognises_the_web_interface_answering_instead_of_the_api(self, mock_request, _name, status_code):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(
            status_code, text="<!DOCTYPE html><html></html>", headers={"Content-Type": "text/html"}
        )

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertEqual(context.exception.cause, "Cyber GRC returned a web page instead of an API response.")
        self.assertIn("api-01.azurewebsites.net", context.exception.assistance)

    def test_request_recognises_a_web_page_served_without_a_content_type(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.client.list_records("Garbled")

        self.assertIn("web page", context.exception.cause)

    def test_request_reports_an_unparseable_json_body(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.client.list_records("Truncated")

        self.assertIn("not JSON", context.exception.cause)
        self.assertIn('{"value": [', context.exception.data)

    def test_request_reports_a_url_with_no_scheme(self, mock_request):
        mock_request.side_effect = requests.exceptions.MissingSchema("No scheme supplied")

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertIn("not a valid URL", context.exception.cause)
        self.assertIn("including the scheme", context.exception.assistance)

    def test_request_reports_an_unreachable_host(self, mock_request):
        mock_request.side_effect = requests.exceptions.ConnectionError("Name or service not known")

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertIn("Could not reach", context.exception.cause)
        self.assertIn("reachable from the InsightConnect orchestrator", context.exception.assistance)

    def test_request_reports_an_unsendable_api_key_without_quoting_it(self, mock_request):
        # requests quotes the offending header value, which is the API key itself.
        mock_request.side_effect = requests.exceptions.InvalidHeader(f"Invalid return character: {API_KEY}")

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertIn("cannot be sent in an HTTP header", context.exception.cause)
        self.assertNotIn(API_KEY, context.exception.data or "")

    def test_the_api_key_is_never_included_in_exception_data(self, mock_request):
        mock_request.side_effect = requests.exceptions.ConnectionError(f"failed with X-API-Key {API_KEY}")

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertNotIn(API_KEY, context.exception.data)
        self.assertIn("[REDACTED]", context.exception.data)

    def test_surrounding_whitespace_is_trimmed_from_the_url_and_api_key(self, mock_request):
        client = CyberGrcAPI(
            url=f"  {BASE_URL}/  ", api_key=f" {API_KEY}\n", ssl_verify=True, logger=self.client.logger
        )

        self.assertEqual(client.url, BASE_URL)
        self.assertEqual(client.session.headers["X-API-Key"], API_KEY)

    def test_request_raises_a_server_error_for_a_5xx_response(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.client.list_records("Broken")

        self.assertIn("server error (500)", context.exception.cause)
        self.assertIn("nothing to correct in the workflow", context.exception.assistance)

    def test_request_reports_an_unexpected_status_code(self, mock_request):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(418, {"message": "I am a teapot"})

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertIn("unexpected status (418)", context.exception.cause)
        self.assertEqual(context.exception.assistance, "I am a teapot")

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

        self.assertIn("did not respond within 120 seconds", context.exception.cause)
        self.assertIn("narrow it with a Filter", context.exception.assistance)

    def test_request_reports_a_transport_failure(self, mock_request):
        mock_request.side_effect = requests.exceptions.TooManyRedirects("too many redirects")

        with self.assertRaises(PluginException) as context:
            self.client.list_records("Risks")

        self.assertIn("request to Cyber GRC failed", context.exception.cause)
        self.assertIn("transport level failure", context.exception.assistance)


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
