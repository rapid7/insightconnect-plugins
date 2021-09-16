import sys
import os
from unittest.mock import patch
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_proofpoint_tap.actions.fetch_forensics import FetchForensics
from komand_proofpoint_tap.actions.fetch_forensics.schema import Input, Output
from unit_test.test_util import Util
from unittest import TestCase

sys.path.append(os.path.abspath("../"))


class TestFetchForensics(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(FetchForensics())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_threat_id_and_include_campaign_forensic(self, mock_request):
        actual = self.action.run({Input.THREAT_ID: "abcd1234", Input.INCLUDE_CAMPAIGN_FORENSICS: True})
        expected = {
            "generated": "2021-06-27T18:48:04.302Z",
            "reports": [
                {
                    "scope": "THREAT",
                    "id": "abcd1234",
                    "name": "www.testcase.com",
                    "threatStatus": "active",
                    "forensics": [
                        {
                            "type": "screenshot",
                            "display": "Screenshot",
                            "engine": "static",
                            "malicious": True,
                            "note": "Screenshot",
                            "time": 0,
                            "what": {"url": "https://testcase2.com"},
                            "platforms": [{"name": "static", "os": "static", "version": "0"}],
                        }
                    ],
                }
            ],
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_threat_id_without_include_campaign_forensic(self, mock_request):
        actual = self.action.run({Input.THREAT_ID: "abcd1234", Input.INCLUDE_CAMPAIGN_FORENSICS: False})
        expected = {
            "generated": "2021-06-27T18:48:04.302Z",
            "reports": [
                {
                    "scope": "THREAT",
                    "id": "abcd1234",
                    "name": "www.testcase.com",
                    "threatStatus": "active",
                    "forensics": [
                        {
                            "type": "screenshot",
                            "display": "Screenshot",
                            "engine": "static",
                            "malicious": True,
                            "note": "Screenshot",
                            "time": 0,
                            "what": {"url": "https://testcase2.com"},
                            "platforms": [{"name": "static", "os": "static", "version": "0"}],
                        }
                    ],
                }
            ],
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_campaign_id(self, mock_request):
        actual = self.action.run({Input.CAMPAIGN_ID: "11111111-aaaa-2222-3333-bbbbbbbbbbbb"})

        expected = {
            "generated": "2021-06-27T19:58:04.283Z",
            "reports": [
                {
                    "scope": "CAMPAIGN",
                    "id": "11111111-aaaa-2222-3333-bbbbbbbbbbbb",
                    "name": "Emotet",
                    "forensics": [
                        {
                            "type": "behavior",
                            "display": "Test",
                            "engine": "iee",
                            "malicious": False,
                            "note": "Test2",
                            "time": 0,
                            "what": {"rule": "behavior_123456789"},
                            "platforms": [{"name": "Win10", "os": "win", "version": "win10"}],
                        }
                    ],
                }
            ],
        }

        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_two_parameters_error(self, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run(
                {
                    Input.THREAT_ID: "abcd1234",
                    Input.INCLUDE_CAMPAIGN_FORENSICS: True,
                    Input.CAMPAIGN_ID: "11111111-aaaa-2222-3333-bbbbbbbbbbbb",
                }
            )

        self.assertEqual(error.exception.cause, "Both Campaign ID and Threat ID were provided.")
        self.assertEqual(
            error.exception.assistance,
            "Only one of the following two parameters can be used: Campaign ID or Threat ID.",
        )

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_no_parameters_error(self, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.THREAT_ID: "", Input.INCLUDE_CAMPAIGN_FORENSICS: True, Input.CAMPAIGN_ID: ""})

        self.assertEqual(error.exception.cause, "One of the following inputs must be provided.")
        self.assertEqual(error.exception.assistance, "Please enter either Threat ID or Campaign ID.")

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_fetch_forensics_blacklisted_as_boolean(self, mock_request):
        actual = self.action.run({Input.THREAT_ID: "blacklisted_as_boolean", Input.INCLUDE_CAMPAIGN_FORENSICS: False})

        expected = {
            "generated": "2021-06-27T19:58:04.283Z",
            "reports": [
                {
                    "scope": "THREAT",
                    "id": "blacklisted_as_boolean",
                    "name": "www.testcase.com",
                    "threatStatus": "active",
                    "forensics": [
                        {
                            "display": "Attachment with SHA-256: 30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050",
                            "engine": "av",
                            "malicious": True,
                            "note": "Attachment with SHA-256: 30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050",
                            "platforms": [
                                {
                                    "name": "pps",
                                    "os": "pps",
                                }
                            ],
                            "type": "attachment",
                            "what": {
                                "blacklisted": True,
                                "rule": "Av",
                                "sha256": "30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050",
                            },
                        }
                    ],
                }
            ],
        }

        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_fetch_forensics_blacklisted_as_integer(self, mock_request):
        actual = self.action.run({Input.THREAT_ID: "blacklisted_as_integer", Input.INCLUDE_CAMPAIGN_FORENSICS: False})

        expected = {
            "generated": "2021-06-27T19:58:04.283Z",
            "reports": [
                {
                    "scope": "THREAT",
                    "id": "blacklisted_as_integer",
                    "name": "www.testcase.com",
                    "threatStatus": "active",
                    "forensics": [
                        {
                            "display": "Attachment with SHA-256: 30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050",
                            "engine": "av",
                            "malicious": True,
                            "note": "Attachment with SHA-256: 30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050",
                            "platforms": [
                                {
                                    "name": "pps",
                                    "os": "pps",
                                }
                            ],
                            "type": "attachment",
                            "what": {
                                "blacklisted": True,
                                "rule": "Av",
                                "sha256": "30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050",
                            },
                        }
                    ],
                }
            ],
        }

        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_fetch_forensics_blacklisted_as_boolean_and_integer(self, mock_request):
        actual = self.action.run(
            {Input.THREAT_ID: "blacklisted_as_boolean_and_integer", Input.INCLUDE_CAMPAIGN_FORENSICS: False}
        )

        expected = {
            "generated": "2021-06-27T19:58:04.283Z",
            "reports": [
                {
                    "scope": "THREAT",
                    "id": "blacklisted_as_boolean_and_integer",
                    "name": "www.testcase.com",
                    "threatStatus": "active",
                    "forensics": [
                        {
                            "display": "Attachment with SHA-256: 30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050",
                            "engine": "av",
                            "malicious": True,
                            "note": "Attachment with SHA-256: 30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050",
                            "platforms": [
                                {
                                    "name": "pps",
                                    "os": "pps",
                                }
                            ],
                            "type": "attachment",
                            "what": {
                                "blacklisted": True,
                                "rule": "Av",
                                "sha256": "30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050",
                            },
                        },
                        {
                            "display": "Attachment with SHA-256: 30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050",
                            "engine": "av",
                            "malicious": True,
                            "note": "Attachment with SHA-256: 30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050",
                            "platforms": [
                                {
                                    "name": "pps",
                                    "os": "pps",
                                }
                            ],
                            "type": "attachment",
                            "what": {
                                "blacklisted": True,
                                "rule": "Av",
                                "sha256": "30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050",
                            },
                        },
                    ],
                }
            ],
        }

        self.assertEqual(actual, expected)
