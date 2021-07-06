import sys
import os
import mock

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_urlscan.actions.submit_url_for_scan import SubmitUrlForScan
from komand.exceptions import PluginException
import json


def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, filename, status_code):
            self.status_code = status_code
            self.text = "error message"
            self.filename = filename

        def json(self):
            if self.filename == "json_error":
                raise json.decoder.JSONDecodeError("json error", "json error", 0)
            actual_joined_path = os.path.join(
                os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp"
            )
            return json.loads(read_file_to_string(actual_joined_path))

    if kwargs["data"]["url"] == "401":
        return MockResponse("submit_url_for_scan_401", 401)
    elif kwargs["data"]["url"] == "429":
        return MockResponse("submit_url_for_scan_429", 429)
    elif kwargs["data"]["url"] == "unexpect":
        return MockResponse("submit_url_for_scan_unexpect", 500)
    elif kwargs["data"]["url"] == "json_error":
        return MockResponse("json_error", 500)
    elif kwargs["data"]["url"] == "499":
        return MockResponse("submit_url_for_scan_499", 499)
    elif kwargs["data"]["url"] == "201":
        return MockResponse("submit_url_for_scan_201", 201)

    return MockResponse("submit_url_for_scan_200", 200)


class MockConnection:
    def __init__(self):
        self.server = "test_tenant_id"
        self.headers = {}


@mock.patch("requests.post", side_effect=mocked_requests_post)
class TestSubmitUrlForScan(TestCase):
    def test_submit_url_for_scan(self, mock_post):
        action = SubmitUrlForScan()
        action.connection = MockConnection()

        actual = action.run({"public": True, "url": "test"})
        expected = {"was_scan_skipped": False, "scan_id": "123"}

        self.assertEqual(actual, expected)

    def test_submit_url_for_scan_201(self, mock_post):
        action = SubmitUrlForScan()
        action.connection = MockConnection()

        actual = action.run({"public": False, "url": "201"})
        expected = {"was_scan_skipped": True, "scan_id": ""}

        self.assertEqual(actual, expected)

    def test_submit_url_for_scan_401(self, mock_post):
        action = SubmitUrlForScan()
        action.connection = MockConnection()

        with self.assertRaises(PluginException) as error:
            action.run({"public": True, "url": "401"})

        self.assertTrue("Invalid API key provided" in error.exception.cause)
        self.assertTrue("Verify your API key configured in your connection is correct" in error.exception.assistance)

    def test_submit_url_for_scan_429(self, mock_post):
        action = SubmitUrlForScan()
        action.connection = MockConnection()

        with self.assertRaises(PluginException) as error:
            action.run({"public": False, "url": "429"})

        self.assertTrue("API limit error." in error.exception.cause)

    def test_submit_url_for_scan_unexpect(self, mock_post):
        action = SubmitUrlForScan()
        action.connection = MockConnection()

        with self.assertRaises(PluginException) as error:
            action.run({"public": True, "url": "unexpect"})

        self.assertTrue("Received an unexpected response from the Urlscan API. " in error.exception.cause)
        self.assertTrue("If the problem persists, please contact support." in error.exception.assistance)

    def test_submit_url_for_scan_json_decoder_error(self, mock_post):
        action = SubmitUrlForScan()
        action.connection = MockConnection()

        with self.assertRaises(PluginException) as error:
            action.run({"public": True, "url": "json_error"})

        self.assertTrue("Received an unexpected response from the Urlscan API. " in error.exception.cause)
        self.assertTrue("(non-JSON or no response was received). Response was: " in error.exception.assistance)

    def test_submit_url_for_scan_499(self, mock_post):
        action = SubmitUrlForScan()
        action.connection = MockConnection()

        with self.assertRaises(PluginException) as error:
            action.run({"public": True, "url": "499"})

        self.assertTrue("Error 499. " in error.exception.cause)
        self.assertTrue("Test 499" in error.exception.assistance)
