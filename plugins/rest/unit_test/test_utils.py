import os
import sys

from komand_rest.util.util import *

sys.path.append(os.path.abspath("../"))

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
    data = "client_id=12345&client_secret=passwd"
    if args[0] == "get":
        if args[1] == "www.google.com/":
            return MockResponse(payload, 200, data=None)
        if args[1] == "www.401.com/":
            return MockResponse(payload, 401, data=None)
        if args[1] == "www.418.com/":
            return MockResponse(payload, 418, data=None)
        if args[1] == "www.httpbin.org/":
            return MockResponse(None, 200, data)

    print(f"mocked_requests_get failed looking for: {args[0]}")
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
            ("get", "/", STUB_DATA, {"Content-Type": "application/json"}, STUB_DATA),
            ("get", "/", STUB_DATA, {"Content-Type": "application/x-www-form-urlencoded"}, STUB_DATA)
        ]
    )
    @mock.patch("requests.request", side_effect=mocked_requests_get)
    def test_data_string(self, method, route, data, headers, mock_expected, mock_get):
        api = RestAPI("www.httpbin.org", None, True, {})
        result = api.call_api(method, route, data, headers)
        result = result.data
        self.assertEqual(result, mock_expected)

    # @mock.patch("requests.request", side_effect=mocked_requests_get)
    # def test_get_data_string_is_unencoded(self, mock_get):
    #     log = logging.getLogger("Test")
    #     api = RestAPI("www.httpbin.org", log, True, {})
    #     result = api.call_api("get", "/", STUB_DATA)
    #     result = result.data
    #     self.assertEqual(STUB_DATA, result)
    #
    # @mock.patch("requests.request", side_effect=mocked_requests_get)
    # def test_get_data_string_is_encoded(self, mock_get):
    #     log = logging.getLogger("Test")
    #     api = RestAPI("www.httpbin.org", log, True, {})
    #     result = api.call_api("get", "/", STUB_DATA, headers={"Content-Type": "application/x-www-form-urlencoded"})
    #     result = result.data
    #     self.assertEqual(STUB_DATA, result)

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
