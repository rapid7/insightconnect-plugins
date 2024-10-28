import os
import sys
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from icon_hybrid_analysis.actions.lookup_terms import LookupTerms
from icon_hybrid_analysis.actions.lookup_terms.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util


class TestLookUpTerms(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(LookupTerms())

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_lookup_terms_filename(self, mocked_request):
        actual = self.action.run({Input.FILENAME: "test", Input.VERDICT: "whitelisted"})
        expected = {
            "count": 1,
            "result": [
                {
                    "analysis_start_time": "2017-04-25 09:06:48",
                    "av_detect": "0",
                    "environment_description": "Windows 7 32 bit",
                    "environment_id": 100,
                    "job_id": "58ff0387aac2edb41849c732",
                    "sha256": "f6edcd8a1b4f7cb85486d0c6777f9174eadbc4d1d0d9e5aeba7132f30b34bc3e",
                    "size": 28895,
                    "submit_name": "pdf-test.pdf",
                    "type_short": "pdf",
                    "verdict": "whitelisted",
                }
            ],
            "search_terms": [{"id": "filename", "value": "test"}, {"id": "verdict", "value": "1"}],
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_lookup_terms_domain(self, mocked_request):
        actual = self.action.run({Input.DOMAIN: "example.com"})
        expected = Util.load_json(f"payloads/action_lookup_terms_domain.json.exp")
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_lookup_terms_country(self, mocked_request):
        actual = self.action.run({Input.COUNTRY: "AFG"})
        expected = Util.load_json(f"payloads/action_lookup_terms_country.json.exp")
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_lookup_terms_filetype(self, mocked_request):
        actual = self.action.run({Input.FILETYPE: "perl"})
        expected = Util.load_json(f"payloads/action_lookup_terms_filetype.json.exp")
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_lookup_terms_host(self, mocked_request):
        actual = self.action.run({Input.HOST: "198.51.100.1"})
        expected = Util.load_json(f"payloads/action_lookup_terms_host.json.exp")
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_lookup_terms_similarTo(self, mocked_request):
        actual = self.action.run({Input.SIMILAR_TO: "ef537f25c895bfa782526529a9b63d97aa631564d5d789c2b765448c8635fb6c"})
        expected = {
            "count": 0,
            "result": [],
            "search_terms": [
                {"id": "similar_to", "value": "ef537f25c895bfa782526529a9b63d97aa631564d5d789c2b765448c8635fb6c"}
            ],
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_lookup_terms_tag(self, mocked_request):
        actual = self.action.run({Input.TAG: "ransomware"})
        expected = Util.load_json(f"payloads/action_lookup_terms_tag.json.exp")
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_lookup_terms_url(self, mocked_request):
        actual = self.action.run({Input.URL: "http://example.com"})
        expected = Util.load_json(f"payloads/action_lookup_terms_url.json.exp")
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_lookup_terms_port(self, mocked_request):
        actual = self.action.run({Input.PORT: 8080})
        expected = Util.load_json(f"payloads/action_lookup_terms_port.json.exp")
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_lookup_terms_bad_domain(self, mocked_request):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.DOMAIN: "http://example.com"})

        self.assertEqual("The entered domain has the wrong format.", context.exception.cause)
        self.assertEqual("Please check domain in input and try again.", context.exception.assistance)

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_lookup_terms_bad_url(self, mocked_request):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.URL: "example.com"})

        self.assertEqual("The entered URL has the wrong format.", context.exception.cause)
        self.assertEqual(
            "Please check URL and try again. In its most common form, a URL starts with http:// or https:// followed by www, then the website name.",
            context.exception.assistance,
        )

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_lookup_terms_bad_host(self, mocked_request):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.HOST: "1"})

        self.assertEqual("Invalid IP address.", context.exception.cause)
        self.assertEqual(
            "Check address input and try again. Allowed kind are: IPv4 Address", context.exception.assistance
        )
