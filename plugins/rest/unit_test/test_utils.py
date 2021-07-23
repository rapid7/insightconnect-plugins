import sys
import os
from komand_rest.util.util import *
import json

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
import logging


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
        self.text = "This is some error text"

    def json(self):
        if self.status_code == 418:
            raise json.decoder.JSONDecodeError("I am a teapot", "NA", 0)
        return json.loads(json.dumps(self.json_data))


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    payload = [{"key": "value"}]

    if args[0] == "get":
        if args[1] == "www.google.com/":
            return MockResponse(payload, 200)
        if args[1] == "www.401.com/":
            return MockResponse(payload, 401)
        if args[1] == "www.418.com/":
            return MockResponse(payload, 418)

    print(f"mocked_requests_get failed looking for: {args[0]}")
    return MockResponse(None, 404)


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

        test_response = MockResponse([{"key": "value"}], 200)
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
