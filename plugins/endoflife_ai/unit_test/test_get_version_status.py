import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from icon_endoflife_ai.actions.get_version_status import GetVersionStatus
from icon_endoflife_ai.actions.get_version_status.schema import Input, Output

from util import default_connector, mocked_requests_request, STUB_CONNECTION_WITH_KEY


class TestGetVersionStatus(TestCase):
    def setUp(self) -> None:
        self.action = default_connector(GetVersionStatus())

    @mock.patch("requests.request", side_effect=mocked_requests_request)
    def test_get_version_status(self, mock_request):
        results = self.action.run({Input.PRODUCT: "nodejs", Input.VERSION: "20"})
        expected = {
            "found": True,
            "product": "nodejs",
            "version": "20",
            "status": "eol",
            "eol_date": "2026-04-30",
            "days_past_eol": 145,
            "score": 60,
            "band": "High",
            "grade": "C",
            "cisa_kev_exposure": 0,
            "extended_support_available": True,
            "eol_date_source": "vendor-fetched",
            "eol_date_confidence": "high",
            "product_url": "https://endoflife.ai/nodejs",
        }
        self.assertEqual(expected, results)
        self.assertNotIn(Output.DAYS_UNTIL_EOL, results, "null values are cleaned from the output")
        self.action.output.validate(results)

    @mock.patch("requests.request", side_effect=mocked_requests_request)
    def test_get_version_status_not_found(self, mock_request):
        results = self.action.run({Input.PRODUCT: "nodejs", Input.VERSION: "99"})
        expected = {Output.FOUND: False, Output.MESSAGE: 'Version "99" not found for "nodejs"'}
        self.assertEqual(expected, results)
        self.action.output.validate(results)

    @mock.patch("requests.request", side_effect=mocked_requests_request)
    def test_get_version_status_encodes_path_and_sends_key(self, mock_request):
        action = default_connector(GetVersionStatus(), STUB_CONNECTION_WITH_KEY)
        action.run({Input.PRODUCT: " NodeJS ", Input.VERSION: "8.0"})
        method, url = mock_request.call_args[0]
        self.assertEqual("GET", method)
        self.assertEqual("https://api.endoflife.ai/v1/score/nodejs/8.0", url, "slug is trimmed and lowercased")
        self.assertEqual("test-key", mock_request.call_args[1]["headers"]["X-API-Key"])

    @mock.patch("requests.request", side_effect=mocked_requests_request)
    def test_get_version_status_anonymous_has_no_key_header(self, mock_request):
        self.action.run({Input.PRODUCT: "nodejs", Input.VERSION: "20"})
        self.assertNotIn("X-API-Key", mock_request.call_args[1]["headers"])

    @mock.patch("requests.request", side_effect=mocked_requests_request)
    def test_get_version_status_rate_limited(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.PRODUCT: "nodejs", Input.VERSION: "limited"})
        self.assertEqual(PluginException.Preset.RATE_LIMIT, context.exception.preset)

    @mock.patch("requests.request", side_effect=mocked_requests_request)
    def test_get_version_status_server_error(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.PRODUCT: "nodejs", Input.VERSION: "broken"})
        self.assertEqual(PluginException.Preset.SERVER_ERROR, context.exception.preset)

    def test_get_version_status_requires_both_inputs(self):
        with self.assertRaises(PluginException):
            self.action.run({Input.PRODUCT: "nodejs", Input.VERSION: " "})
