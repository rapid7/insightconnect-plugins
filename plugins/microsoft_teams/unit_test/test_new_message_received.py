import json
import logging
import os
import sys
from unittest import TestCase, mock

import requests

sys.path.append(os.path.abspath("../"))

from icon_microsoft_teams.triggers.new_message_received import NewMessageReceived
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from util import MockConnection

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


def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, data, status_code) -> None:
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

    return MockResponse(None, 404)


class TestNewMessageReceived(TestCase):
    def setUp(self) -> None:
        self.log = logging.getLogger("Test")
        self.nmr = NewMessageReceived()
        self.nmr.logger = self.log
        self.nmr.connection = MockConnection()

    def test_sort_messages_from_request(self) -> None:
        with open(os.path.join(os.path.dirname(__file__), "./payloads/get_messages.json")) as file:
            text = file.read()
            json_payload = json.loads(text)
        result = self.nmr.sort_messages_from_request(json_payload)
        self.assertEqual(result[0].get("body").get("content"), "This should be first")
        self.assertEqual(result[1].get("body").get("content"), "This is very old")

    def test_compile_message_content(self) -> None:
        regex = self.nmr.compile_message_content(".")
        self.assertTrue(regex.search("stuff"))
        with self.assertRaises(PluginException):
            self.nmr.compile_message_content("[")

    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_get_sorted_messages(self, mock_get) -> None:
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
    def test_indicators(self, message_number, expected_result, mock_get) -> None:
        messages = self.nmr.get_sorted_messages("http://somefakeendpoint.com")
        indicators = [self.nmr.get_indicators(message.get("body", {}).get("content")) for message in messages]
        self.assertEqual(indicators[message_number], expected_result)

    def test_setup_endpoint(self) -> None:
        self.nmr.connection.client.get_teams.return_value = [{"id": "team-id"}]
        self.nmr.connection.client.get_channels.return_value = [{"id": "channel-id"}]

        endpoint = self.nmr.setup_endpoint("channel", "team")
        self.assertEqual("https://graph.microsoft.com/v1.0/teams/team-id/channels/channel-id/messages", endpoint)
        self.nmr.connection.client.get_teams.assert_called_with("team")
        self.nmr.connection.client.get_channels.assert_called_with("team-id", "channel")
