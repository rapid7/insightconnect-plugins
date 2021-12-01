import sys
import os
from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from icon_ipstack.actions import Lookup
from icon_ipstack.actions.lookup.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


class TestLookup(TestCase):
    @classmethod
    @patch("insightconnect_plugin_runtime.helper.open_url", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(Lookup())

    @patch("insightconnect_plugin_runtime.helper.open_url", side_effect=Util.mocked_requests_get)
    def test_lookup_basic_data(self, mock_request):
        actual = self.action.run({Input.HOST: "rapid7.com"})
        expected = {
            "address": "13.32.182.94",
            "city": "Shaw",
            "continent_code": "NA",
            "continent_name": "North America",
            "country_code": "US",
            "country_name": "United States",
            "latitude": "38.906898498535156",
            "location": {
                "calling_code": "1",
                "capital": "Washington D.C.",
                "country_flag": "https://assets.ipstack.com/flags/us.svg",
                "country_flag_emoji": "🇺🇸",
                "country_flag_emoji_unicode": "U+1F1FA U+1F1F8",
                "geoname_id": 4140463,
                "is_eu": False,
                "languages": [{"code": "en", "name": "English", "native": "English"}],
            },
            "longitude": "-77.02839660644531",
            "region_code": "DC",
            "region_name": "Washington",
            "type": "ipv4",
            "zip": "20026",
        }
        self.assertEqual(actual, expected)

    @patch("insightconnect_plugin_runtime.helper.open_url", side_effect=Util.mocked_requests_get)
    def test_lookup_detailed_data(self, mock_request):
        actual = self.action.run({Input.HOST: "ipstack_features"})
        expected = {
            "address": "155.52.187.7",
            "type": "ipv4",
            "continent_code": "NA",
            "continent_name": "North America",
            "country_code": "US",
            "country_name": "United States",
            "region_code": "MA",
            "region_name": "Massachusetts",
            "city": "Boston",
            "zip": "02115",
            "latitude": "42.3424",
            "longitude": "-71.0878",
            "location": {
                "geoname_id": 4930956,
                "capital": "Washington D.C.",
                "languages": [{"code": "en", "name": "English", "native": "English"}],
                "country_flag": "https://assets.ipstack.com/images/assets/flags_svg/us.svg",
                "country_flag_emoji": "🇺🇸",
                "country_flag_emoji_unicode": "U+1F1FA U+1F1F8",
                "calling_code": "1",
                "is_eu": False,
            },
            "time_zone": {
                "id": "America/New_York",
                "current_time": "2018-03-30T07:54:25-04:00",
                "gmt_offset": -14400,
                "code": "EDT",
                "is_daylight_saving": True,
            },
            "currency": {
                "code": "USD",
                "name": "US Dollar",
                "plural": "US dollars",
                "symbol": "$",
                "symbol_native": "$",
            },
            "connection": {"asn": 40127, "isp": "Longwood Medical and Academic Area (LMA)"},
        }
        self.assertEqual(actual, expected)

    @patch("insightconnect_plugin_runtime.helper.open_url", side_effect=Util.mocked_requests_get)
    def test_lookup_bad_auth(self, mock_request):
        expected = "The access key is blank or invalid"
        with self.assertRaises(PluginException) as exc:
            self.action.run({Input.HOST: "unauthorized_user"})
        self.assertEqual(exc.exception.cause, expected)

    @patch("insightconnect_plugin_runtime.helper.open_url", side_effect=Util.mocked_requests_get)
    def test_lookup_bad_input(self, mock_request):
        expected = "The supplied host address/domain is invalid"
        with self.assertRaises(PluginException) as exc:
            self.action.run({Input.HOST: "rapid7.typocom"})
        self.assertEqual(exc.exception.cause, expected)

    @patch("insightconnect_plugin_runtime.helper.open_url", side_effect=Util.mocked_requests_get)
    def test_lookup_domain_non_exist(self, mock_request):
        with self.assertRaises(PluginException) as exc:
            self.action.run({Input.HOST: "rapid7.typocom"})
        expected = "The supplied host address/domain is invalid"
        self.assertEqual(exc.exception.cause, expected)

    @patch("insightconnect_plugin_runtime.helper.open_url", side_effect=Util.mocked_requests_get)
    def test_lookup_bad_access_key(self, mock_request):
        temp = self.action.connection.token
        with self.assertRaises(PluginException) as exc:
            self.action.connection.token = "BADTOKEN"
            self.action.run({Input.HOST: "rapid7.typocom"})
        expected = "The access key is blank or invalid"
        self.assertEqual(exc.exception.cause, expected)
        self.action.connection.token = temp

    @patch("insightconnect_plugin_runtime.helper.open_url", side_effect=Util.mocked_requests_get)
    def test_lookup_limit_hit(self, mock_request):
        with self.assertRaises(PluginException) as exc:
            self.action.run({Input.HOST: "limit_hit"})
        expected = "The maximum monthly ip lookups has been hit"
        self.assertEqual(exc.exception.cause, expected)

    @patch("insightconnect_plugin_runtime.helper.open_url", side_effect=Util.mocked_requests_get)
    def test_lookup_user_inactive(self, mock_request):
        with self.assertRaises(PluginException) as exc:
            self.action.run({Input.HOST: "user_inactive"})
        expected = "The access key was recognized but the user account is not active"
        self.assertEqual(exc.exception.cause, expected)

    @patch("insightconnect_plugin_runtime.helper.open_url", side_effect=Util.mocked_requests_get)
    def test_lookup_unknown_error(self, mock_request):
        with self.assertRaises(PluginException) as exc:
            self.action.run({Input.HOST: "generic_error"})
        expected = "Check the input host domain and data in this error"
        self.assertEqual(exc.exception.assistance, expected)

    @patch("insightconnect_plugin_runtime.helper.open_url", side_effect=Util.mocked_requests_get)
    def test_lookup_route_changed(self, mock_request):
        with self.assertRaises(PluginException) as exc:
            self.action.run({Input.HOST: "404"})
        expected = "The requested resource does not exist, Error 404"
        self.assertEqual(exc.exception.cause, expected)

    @patch("insightconnect_plugin_runtime.helper.open_url", side_effect=Util.mocked_requests_get)
    def test_lookup_server_error(self, mock_request):
        with self.assertRaises(PluginException) as exc:
            self.action.run({Input.HOST: "server_error"})
        expected = PluginException(preset=PluginException.Preset.SERVER_ERROR)
        self.assertEqual(exc.exception.cause, expected.cause)
