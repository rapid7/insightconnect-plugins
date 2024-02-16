import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from komand_domaintools.actions.reverse_whois import ReverseWhois
from komand_domaintools.actions.reverse_whois.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from util import mock_responder, Util
from parameterized import parameterized


class TestReverseWhois(TestCase):
    @mock.patch("domaintools.API.account_information", side_effect=mock_responder)
    def setUp(self, mock_post) -> None:
        self.action = Util.default_connector(ReverseWhois())
        self.params = {
            Input.TERMS: "test.com",
            Input.EXCLUDE: "example.com",
            Input.SCOPE: "historic",
            Input.MODE: "quote",
        }

    @mock.patch("domaintools.API.reverse_whois", side_effect=mock_responder)
    def test_reverse_whois(self, mock_request):
        response = self.action.run(self.params)
        expected = Util.load_expected("test_reverse_whois")
        self.assertEqual(response, expected)

    @parameterized.expand(
        [
            ("500.com", PluginException.causes[PluginException.Preset.UNKNOWN]),
            ("400.com", PluginException.causes[PluginException.Preset.BAD_REQUEST]),
            ("503.com", PluginException.causes[PluginException.Preset.SERVICE_UNAVAILABLE]),
            ("401.com", PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            ("404.com", PluginException.causes[PluginException.Preset.NOT_FOUND]),
        ],
    )
    @mock.patch("domaintools.API.reverse_whois", side_effect=mock_responder)
    def test_reverse_whois_fail(self, terms, exception, mock_request):
        with self.assertRaises(PluginException) as context:
            self.params["terms"] = terms
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
