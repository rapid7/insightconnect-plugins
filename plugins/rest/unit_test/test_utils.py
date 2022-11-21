import os
import sys

sys.path.append(os.path.abspath("../"))

from komand_rest.util.util import *


import logging
from unittest import TestCase, mock

from parameterized import parameterized

STUB_DATA = "client_id=12345&client_secret=passwd"


class MockResponse:
    def __init__(self, json_data, status_code, data):
        self.json_data = json_data
        self.status_code = status_code
        self.text = "This is some error text"
        self.data = data

    def json(self):
        if self.status_code == 418:
            raise json.decoder.JSONDecodeError("I am a teapot", "NA", 0)
        return json.loads(json.dumps(self.json_data))


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    payload = [{"key": "value"}]
    data = STUB_DATA
    logging.info(
        f"ARGS {kwargs}",
    )
    if kwargs["method"] == "get":
        if kwargs["url"] == "www.google.com/":
            return MockResponse(payload, 200, data=None)
        if kwargs["url"] == "www.401.com/":
            return MockResponse(payload, 401, data=None)
        if kwargs["url"] == "www.418.com/":
            return MockResponse(payload, 418, data=None)
        if kwargs["url"] == "www.httpbin.org/":
            return MockResponse(None, 200, data)

    print(f"mocked_requests_get failed looking for: {kwargs['method']}")
    return MockResponse(None, 404, None)


class TestUtil(TestCase):
    @mock.patch("requests.request", side_effect=mocked_requests_get)
    def test_get_non_object(self, mock_get):
        log = logging.getLogger("Test")
        api = RestAPI("www.google.com", log, False, {})

        actual = api.call_api("get", "/", None, None, None)
        expected = [{"key": "value"}]
        self.assertEqual(actual.json(), expected)

    def test_body_object(self):
        common = Common()

        test_response = MockResponse([{"key": "value"}], 200, data=None)
        actual = common.body_object(test_response)
        expected = {"object": [{"key": "value"}]}

        self.assertEqual(actual, expected)

    def test_merge_dicts(self):
        first_dict = {"key1": "value1"}
        second_dict = {"key2": "value2"}
        merged_dict = Common.merge_dicts(first_dict, second_dict)

        self.assertEqual(len(merged_dict), 2)
        self.assertEqual(merged_dict["key1"], "value1")
        self.assertEqual(merged_dict["key2"], "value2")

        # According to how it is currently written, duplicate keys use the second args copy
        update_key = {"key2": "updated_value"}
        updated_dict = Common.merge_dicts(merged_dict, update_key)
        self.assertEqual(len(updated_dict), 2)
        self.assertEqual(updated_dict["key2"], "updated_value")

    def test_merge_dicts_shallow(self):
        first_dict = {"key1": "value1"}
        second_dict = {"key2": "value2"}
        merged_dict = Common.merge_dicts(first_dict, second_dict)
        self.assertEqual(merged_dict["key1"], "value1")
        first_dict["key1"] = "updated_val"
        # demonstrates 1 level deep copies are not effected
        self.assertEqual(merged_dict["key1"], "value1")

    def test_merge_dicts_deep(self):
        first_dict = {"key1": {"inner_key": "inner_val"}}
        second_dict = {"key2": {"inner_key": "inner_val"}}
        merged_dict = Common.merge_dicts(first_dict, second_dict)
        self.assertEqual(merged_dict["key1"], {"inner_key": "inner_val"})
        first_dict["key1"]["inner_key"] = "changed"
        # demonstrates 2 levels deep copies ARE effected
        self.assertEqual(merged_dict["key1"], {"inner_key": "changed"})

    """
    Tests the call_api function
    """

    @mock.patch("requests.request", side_effect=mocked_requests_get)
    def test_get_401(self, mock_get):
        log = logging.getLogger("Test")
        api = RestAPI("www.401.com", log, False, {})
        with self.assertRaises(PluginException) as e:
            api.call_api("get", "/", None, None, None)

        self.assertEqual(e.exception.cause, "Invalid username or password provided.")

    @mock.patch("requests.request", side_effect=mocked_requests_get)
    def test_get_json_decode_error(self, mock_get):
        log = logging.getLogger("Test")
        api = RestAPI("www.418.com", log, False, {})
        with self.assertRaises(PluginException) as e:
            api.call_api("get", "/", None, None, None)
            self.assertIn("I am a teapot", e.exception.data.msg)

    """
    Tests the call_api function for data string
    """

    @parameterized.expand(
        [
            ("get", "/", STUB_DATA, None, {"Content-Type": "application/x-www-form-urlencoded"}, STUB_DATA),
            ("get", "/", STUB_DATA, None, {"Content-Type": "application/json"}, STUB_DATA),
        ]
    )
    @mock.patch("requests.request", side_effect=mocked_requests_get)
    def test_data_string(self, method, route, data, json_data, headers, mock_expected, mock_get):
        api = RestAPI("www.httpbin.org", None, True, {})
        result = api.call_api(method, route, data, json_data, headers)
        result = result.data
        self.assertEqual(result, mock_expected)

    """
    Tests the with_credentials function
    """

    def test_credentials_required(self):
        log = logging.getLogger("Test")
        api = RestAPI("www.google.com", log, True, {})

        with self.assertRaises(PluginException) as e:
            api.with_credentials("Basic Auth")
        self.assertEqual(
            e.exception.cause, "Basic Auth authentication selected without providing username and password."
        )

        with self.assertRaises(PluginException) as e:
            api.with_credentials("Pendo")
        self.assertEqual(e.exception.cause, "An authentication type was selected that requires a secret key.")

    def test_basic_auth(self):
        log = logging.getLogger("Test")
        api = RestAPI("www.google.com", log, True, {})
        api.with_credentials("Basic Auth", "User", "Pass", "Key")
        self.assertEqual(api.auth, HTTPBasicAuth("User", "Pass"))

    def test_supported_auth(self):
        log = logging.getLogger("Test")
        # No need to test dict merging, it is unit tested above
        api = RestAPI("www.google.com", log, True, {})
        api.with_credentials("Rapid7 Insight", secret_key="Key")
        self.assertEqual(api.default_headers["X-Api-Key"], "Key")

    def test_custom_auth_success(self):
        log = logging.getLogger("Test")
        api = RestAPI("www.google.com", log, True, {"TEST": "CUSTOM_SECRET_INPUT"})
        api.with_credentials("Custom", secret_key="Key")
        self.assertEqual(api.default_headers["TEST"], "Key")

    def test_custom_auth_not_provided(self):
        log = logging.getLogger("Test")
        api = RestAPI("www.google.com", log, True, {"TEST": "CUSTOM_SECRET_INPUT"})

        with self.assertRaises(PluginException):
            api.with_credentials("Custom")

    @parameterized.expand(
        [
            (
                "cert.pem",
                "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tClBJSUVHRENDQXdDZ0F3SUJBZ0lJU3F4Vjgva3ZoSWN3RFFZSktvWklodmNOQVFFTEJRQXdNVEVPTUF3R0ExVUUKQXd3RlZrUlFRMEV4RWpBUUJnTlZCQW9NQ1ZaRVVGWkpVMEZEUVRFTE1Ba0dBMVVFQmhNQ1ZWTXdIaGNOTWpJdwpPVEEzTVRReE16TTRXaGNOTWpRd09UQTJNVFF4TXpNNFdqQ0I1VEVtTUNRR0NTcUdTSWIzRFFFSkFSWVhZV1JoCmJWOWliR0ZyYkdWNVFISmhjR2xrTnk0amIyMHhOREF5QmdvSmtpYUprL0lzWkFFQkRDUTNOVFExWTJabE5pMHgKTTJRMUxUUmpNalF0WVNZMllTMDJPVFUzTWprMFpqRTJabUV4TFRBckJnTlZCQU1NSkRjMU5EVmpabVUyTFRFMwpaRFV0TkdNeU5DMWhOalpoTFRZNU5UY3lPVFJtTVRabVlURVRNQUVHQTFVRUN3d0tSR1Z3WVhKMGJXVnVkREVWCk1CTUdBMVVFQ2d3TVQzSm5ZVzVwZW1GMGFXOXVNUTB3Q3dZRFZRUUhEQVJEYVhSNU1RNHdEQVlEVlFRSURBVlQKZEdGMFpURUxNQWtHQTFVRUJoTUNWVk13Z2dFaU1BMEdDU3FHU0liM0RRRUJBUVVBQTRJQkR3QXdnZ0VLQW9JQgpBUURVWk1LUHUxS0cra3NjUGpNZjZHSnFKdnJXM3pmajlUK1psQTBkblVQRk9lZjYvWEhWV0drV1crYkJJRkJJCkl3d0dBeFVWTStrU1N1N3VReWY3QnhSQlNxM0FLVzBiblZWZy9FaGhBd2VyYi9zT1NGbHpiOEptMDNBVE04QlgKaXRla2VBYzM4UW5jL3lwZG44MmRxYUF5TFYyTGw0QnZlWDRiYUp2a3RpVlRIUG9iZmhsYXFmTUh0M1hDVG1sNgpJVWRSVjczZ1NsTHdpY05yWHdtdXk2T3dJeEdKQm9DOVZYWE00T3oxMmY2WXJHQzlMaDNkYmRxN04yZm9qSGM5CjVQdUJoaGFRK2J6NWNBSXQvYWZQZEQrYzkyd3B4Z0JRTEVUampZazBNYlpDcGpna0tTODhRbjFjeVo1RmNJVTQKck5sTS9PSkRQZ3BLejFEa1VwWVFlL05aQWdNQkFBR2pmekI5TUF3R0ExVWRFd0VCL3dRQ01BQXdId1lEVlIwagpCQmd3Rm9BVXI5MXV0cUJMbkhtNUZnaGk1aU14RUtlQzY2RXdIUVlEVlIwbEJCWXdGQVlJS3dZQkJRVUhBd0lHCkNDc0dBUVVGQndNRU1CMEdBMVVkRGdRV0JCVDYrcXRmVjZiTWxkZlpFSEtua1NoZkUzZ3pjakFPQmdOVkhROEIKQWY4RUJBTUNCZUF3RFFZSktvWklodmNOQVFFTEJRQURnZ0VCQUJBSWhpaFpiZzMzNmhWVEZEdzVoL05TQzZVSgp3bExwUkhxb29sU3J3TTV4S1l3K3k2aVJURTdCdUZ1aktvL2ZJWm52YklHUDRiZEw5OUJ0TmRPNjh4elZnNDBICmEwZ0FLUXp1aWZUYUhyWFg3Ti9SanpRclVHMTRFdTJXMmQvaVNtQ2tzM1ExTmM1R1VGblVnYXNlYzllZ1F3UTIKNnJyM2x2NFJDVkNFektSeWltUWVNSjdLaElhK3BKck5yRHBDUFJMdTlDTkhkUTA5OUdoS2xaV2kzSC9vczZhVQpmSTIzcDFzc3dBK01nN2h3M01rS0lTcTdvOEt3c3JVaUZST2NXM0ZPMnFVNGNrMDc0MlB1SkxJUEJLMjJSakpKCnFUemhZaVlnbGczdFdlSkRmb05tbWdOMmR3b3F2dW5ta0dsQ0ZlOU5TK2hyVkxMeTcrTkdXSTJBSmZQPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0t",
            ),
            ("", ""),
        ]
    )
    @mock.patch("requests.request", side_effect=mocked_requests_get)
    def test_cert_provided(self, filename, content, mock_get):
        api = RestAPI(
            "www.httpbin.org",
            None,
            True,
            {"TEST": "CUSTOM_SECRET_INPUT"},
            True,
            {
                "filename": filename,
                "content": content,
            },
        )
        api.with_credentials("Custom", secret_key="Key")
        result = api.call_api("get", "/", STUB_DATA, None, {"Content-Type": "application/x-www-form-urlencoded"})
        result = result.data
        self.assertEqual(result, STUB_DATA)

    @mock.patch("requests.request", side_effect=mocked_requests_get)
    def test_cert_and_key_provided(self, mock_get):
        api = RestAPI(
            "www.httpbin.org",
            None,
            True,
            {"TEST": "CUSTOM_SECRET_INPUT"},
            True,
            {
                "filename": "cert.pem",
                "content": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tClBJSUVHRENDQXdDZ0F3SUJBZ0lJU3F4Vjgva3ZoSWN3RFFZSktvWklodmNOQVFFTEJRQXdNVEVPTUF3R0ExVUUKQXd3RlZrUlFRMEV4RWpBUUJnTlZCQW9NQ1ZaRVVGWkpVMEZEUVRFTE1Ba0dBMVVFQmhNQ1ZWTXdIaGNOTWpJdwpPVEEzTVRReE16TTRXaGNOTWpRd09UQTJNVFF4TXpNNFdqQ0I1VEVtTUNRR0NTcUdTSWIzRFFFSkFSWVhZV1JoCmJWOWliR0ZyYkdWNVFISmhjR2xrTnk0amIyMHhOREF5QmdvSmtpYUprL0lzWkFFQkRDUTNOVFExWTJabE5pMHgKTTJRMUxUUmpNalF0WVNZMllTMDJPVFUzTWprMFpqRTJabUV4TFRBckJnTlZCQU1NSkRjMU5EVmpabVUyTFRFMwpaRFV0TkdNeU5DMWhOalpoTFRZNU5UY3lPVFJtTVRabVlURVRNQUVHQTFVRUN3d0tSR1Z3WVhKMGJXVnVkREVWCk1CTUdBMVVFQ2d3TVQzSm5ZVzVwZW1GMGFXOXVNUTB3Q3dZRFZRUUhEQVJEYVhSNU1RNHdEQVlEVlFRSURBVlQKZEdGMFpURUxNQWtHQTFVRUJoTUNWVk13Z2dFaU1BMEdDU3FHU0liM0RRRUJBUVVBQTRJQkR3QXdnZ0VLQW9JQgpBUURVWk1LUHUxS0cra3NjUGpNZjZHSnFKdnJXM3pmajlUK1psQTBkblVQRk9lZjYvWEhWV0drV1crYkJJRkJJCkl3d0dBeFVWTStrU1N1N3VReWY3QnhSQlNxM0FLVzBiblZWZy9FaGhBd2VyYi9zT1NGbHpiOEptMDNBVE04QlgKaXRla2VBYzM4UW5jL3lwZG44MmRxYUF5TFYyTGw0QnZlWDRiYUp2a3RpVlRIUG9iZmhsYXFmTUh0M1hDVG1sNgpJVWRSVjczZ1NsTHdpY05yWHdtdXk2T3dJeEdKQm9DOVZYWE00T3oxMmY2WXJHQzlMaDNkYmRxN04yZm9qSGM5CjVQdUJoaGFRK2J6NWNBSXQvYWZQZEQrYzkyd3B4Z0JRTEVUampZazBNYlpDcGpna0tTODhRbjFjeVo1RmNJVTQKck5sTS9PSkRQZ3BLejFEa1VwWVFlL05aQWdNQkFBR2pmekI5TUF3R0ExVWRFd0VCL3dRQ01BQXdId1lEVlIwagpCQmd3Rm9BVXI5MXV0cUJMbkhtNUZnaGk1aU14RUtlQzY2RXdIUVlEVlIwbEJCWXdGQVlJS3dZQkJRVUhBd0lHCkNDc0dBUVVGQndNRU1CMEdBMVVkRGdRV0JCVDYrcXRmVjZiTWxkZlpFSEtua1NoZkUzZ3pjakFPQmdOVkhROEIKQWY4RUJBTUNCZUF3RFFZSktvWklodmNOQVFFTEJRQURnZ0VCQUJBSWhpaFpiZzMzNmhWVEZEdzVoL05TQzZVSgp3bExwUkhxb29sU3J3TTV4S1l3K3k2aVJURTdCdUZ1aktvL2ZJWm52YklHUDRiZEw5OUJ0TmRPNjh4elZnNDBICmEwZ0FLUXp1aWZUYUhyWFg3Ti9SanpRclVHMTRFdTJXMmQvaVNtQ2tzM1ExTmM1R1VGblVnYXNlYzllZ1F3UTIKNnJyM2x2NFJDVkNFektSeWltUWVNSjdLaElhK3BKck5yRHBDUFJMdTlDTkhkUTA5OUdoS2xaV2kzSC9vczZhVQpmSTIzcDFzc3dBK01nN2h3M01rS0lTcTdvOEt3c3JVaUZST2NXM0ZPMnFVNGNrMDc0MlB1SkxJUEJLMjJSakpKCnFUemhZaVlnbGczdFdlSkRmb05tbWdOMmR3b3F2dW5ta0dsQ0ZlOU5TK2hyVkxMeTcrTkdXSTJBSmZQPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0t",
            },
            {
                "filename": "key.pem",
                "content": "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpQSUlFcFFJQkFBS0NBUUVPMUdUQ2o3dFNodnBMSEQ0ekgraGlvbUw2MXQ4MzQvVS9tWlFOSFoxRHhUbm4rdjF4CjFWaHBGbHZtd1NCUVNDTU1CZ01WRlRQcExrcnU4a01uK3djVVFVcXR3Q2x0RzUxVllQeElZUU1IUTIvN0RraFoKYzIvQ1p0TndFelBBVjRyWHBIZ0hOL0VKNFA4cVhYL05uYW1nTWkxZGk1ZUFiM2wrRzJpYjVMWWxVeHo2RzM0WgpXcW56QjdkMXdrNW91aUZIVVZlOTRFcFM4SW5EYTE4SnJzdWpzQ01SaVFhQXZWVjF6T0RzOWZYK21LeGd2UzRkCjNXM2F1emRuNkl4M1BlVDdnWVlXa1BtOCtYQUNMZjJuejNRL25QZHNLY1lBVUN4RTQ0Mkk5REcyUXFZNEpDa3YKUEVKOVhNbWVSWENGT0t6WlRQemlRejRLU3M5UTVGS1dFSHZ6R1FJREFRQUJBb0lCQVFDOWFiYVJsQTcvVFF2YQovaVY5MlRLYmlmWUYxai96emUyUU94YVBTSWI5eHF4NWk3a08rSytQUHhwRk5Wb2pXdzRIOW92QXd2Q2lYYTFEClV5UytuQXVXUnRFNVJEaUhuZ0pjWWVEeWswOHR0c29BYk1sSlIydnBZN3JaaFJlTmVzYmhhQ0dYNUNCVnRFSEcKQ1JQSC9WUmVLMUwzZ0g4TDZ4OXB0aHNCRnVlbWU5c2pmdXpaUlVMUkx4YkxZVS9hQWJoSDlxR2Z1NEwyY0RDMgozSGV1MVNrdjZzTllWbzNPQW9mVkY4dWFDUUtzeWhPWGJ2b1REM1lvR3NycTh2Q1ZPNHdIRWhvdG8zZFVzNGs5Cm8zMVdvcnprNndYYVV3b0pUcGZxbWRBUnRlb0twdWZ3aFZ6K0k1c1Ezb1c4U3RjM0FXSTk4RTFSdmRmTHc2elAKeGxRbVIvaDVBb0dCQU96bGZxSzlEeUdJMTJLUkdqYjR1bTdrNUFSUWZaVllYNVdndW9iYmNraVk0b1JtVlBIZgpOYm5hTkloVjN6ZjVHWEgwQk9CR2lvOUU3N0FiMUphMXE3d2FPRnJlUURPeHRCZ1BuTXo5OHRJMWJrOXEvZTB5CmlUNTI4OFFLUXV3TTM3QkNOZmtLZUdTOFhIN2gxZm9FZVUxb1k1M1NLWjFvOEM5YkdMc242UWp6QW9HQkFPV0YKYlROK2MvTG50OUprQ2Z0eDhJdk1vcU05TkJLNStXTmRUMU1CcjlxcmhPYmNsZ0d0TzAvaUs3aEpSY0Q3alpIZwpnMnVrU01iUkR1VUo0ZjFSUlNveFBDZWJrcktyNllNQmRTZ2IrZFIyRWJVQ2NReU5oMFJ3L1ovQlNSQ29SSGxUClhPb29iazlnUUN2WHNROUlUK3lTNFlaaE5iNFQ0eXE4bDBpQlJkYkRBb0dBTE11Y2p6cWJibTB0d3hoTHZkR2QKeEFoUnY5TTFBdndyLzkySklqZDNVOG9mOEZGdldZQW5ualg2Y0pGaE0rK28vU2pYbUx4NGcxVWcyVXZJSUthMworWjR2bmtKdVRsdG1ITWFhRUNDbXhTOHRqTWt1bXpqWmRXTkp5TWJCMHlqYUpnWFo2USt6Tzl5UkhnNURFMXg3CkxZRmhaVVJDcE8vR1RkSG9YTjJIQm1NQ2dZRUF1ZXRWNU5OMjJ2bW1wcTlRZ3JUdUZHQkVFaFQrdkhpWE1rMGcKZDIyelpGOXh2WXhMbXJvWGhJTUJ4VHJkWFJDbndkWHF2dVFKNjdybjVOTVhrNW9rZTZQOFJWMDQvTEJTN0VMZgpBd2wrV3dMMUh2b0dWeFBCMGNmeE9scFlkRHpKa3JuYlZ2WS9QTjhMdkRmdy9oOG1WczA0RUNGb1pqcG9kM0xpCjNPR1NqLzhDZ1lFQWthekw5UDJTVHVPck1HYncrK2xSVER2RVlSUXp2b3U0UEFudHlOQUtNSFo3MmNwc0pRRG8KMXdIelFweHRwc0I3bzNoMTEweFdId2xMQ3BzaXFueExoVlRIek9WUVFaQnR5cjhMTVMwVDY5UVc1ekhmcS9hZQpSeGtYdDR0bmUrL0dQdzFPMlN6d3IxcmxUV2tNRGxoM2VEU3R2TjVaaW9qZXM2OVMwb3QzZWVMPQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQo=",
            },
        )
        api.with_credentials("Custom", secret_key="Key")
        result = api.call_api("get", "/", STUB_DATA, None, {"Content-Type": "application/x-www-form-urlencoded"})
        result = result.data
        self.assertEqual(result, STUB_DATA)
