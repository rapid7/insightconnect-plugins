import json
import logging
import os
import sys
from unittest import TestCase, mock

import requests

sys.path.append(os.path.abspath("../"))

from icon_microsoft_teams.triggers.new_chat_message_received import NewChatMessageReceived
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

GET_INDICATORS_RESPONSE = {
    "domains": [],
    "urls": [],
    "email_addresses": [],
    "hashes": {"md5_hashes": [], "sha1_hashes": [], "sha256_hashes": []},
    "ip_addresses": {"ipv4_addresses": [], "ipv6_addresses": []},
    "mac_addresses": [],
    "cves": [],
    "uuids": [],
}


# Get a real payload from file
def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


class MockConnection:
    def __init__(self) -> None:
        self.resource_endpoint = "https://graph.microsoft.com"

    def get_headers(self):
        return {"header": "value"}


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, data, status_code):
            self.status_code = status_code
            self.text = data

        def raise_for_status(self):
            if self.status_code >= 400:
                raise requests.HTTPError(f"{self.status_code}")

        def json(self):
            return json.loads(self.text)

    messages_payload = read_file_to_string(os.path.join(os.path.dirname(__file__), "./payloads/get_messages.json"))

    if args[0] == "http://somefakeendpoint.com":
        return MockResponse(messages_payload, 200)

    print(f"Attempted to get:\n{args[0]}")
    return MockResponse(None, 404)


class TestNewMessageReceived(TestCase):
    def setUp(self) -> None:
        self.log = logging.getLogger("Test")
        self.nmr = NewChatMessageReceived()
        self.nmr.logger = self.log
        self.nmr.connection = MockConnection()

    def test_sort_messages_from_request(self):
        with open(os.path.join(os.path.dirname(__file__), "./payloads/get_chat_messages.json")) as file:
            text = file.read()
            json_payload = json.loads(text)

        result = self.nmr.sort_messages_from_request(json_payload)
        self.assertEqual(result[0].get("body").get("content"), "This should be first")
        self.assertEqual(result[1].get("body").get("content"), "This is very old")

    def test_compile_message_content(self):
        regex = self.nmr.compile_message_content(".")
        self.assertTrue(regex.search("stuff"))
        with self.assertRaises(PluginException):
            self.nmr.compile_message_content("[")

    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_get_sorted_messages(self, mockGet):
        messages = self.nmr.get_sorted_messages("http://somefakeendpoint.com")
        self.assertIsNotNone(messages)
        self.assertEqual(messages[0].get("body").get("content"), "This should be first")
        self.assertEqual(messages[1].get("body").get("content"), "This is very old")

    @parameterized.expand(
        [
            (0, GET_INDICATORS_RESPONSE),
            (1, GET_INDICATORS_RESPONSE),
            (
                2,
                dict(
                    GET_INDICATORS_RESPONSE,
                    **{
                        "domains": ["example.com"],
                        "urls": [
                            "http://example.com/s/?domain=test",
                            "https://example.com?domain=test",
                            "https://example.com",
                        ],
                    },
                ),
            ),
        ]
    )
    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_indicators(self, message_number, expected_result, mockGet):
        messages = self.nmr.get_sorted_messages("http://somefakeendpoint.com")
        indicators = [self.nmr.get_indicators(message.get("body", {}).get("content")) for message in messages]
        self.assertEqual(indicators[message_number], expected_result)

    def test_setup_endpoint(self):
        endpoint = self.nmr.setup_endpoint("chatid")
        self.assertEqual(
            "https://graph.microsoft.com/beta/chats/chatid/messages",
            endpoint,
        )
