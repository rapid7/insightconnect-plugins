from unittest import TestCase, mock
import json
import logging
import requests
import os
from icon_microsoft_teams.triggers.new_message_received import NewMessageReceived
from komand.exceptions import PluginException


# Get a real payload from file
def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


class MockConnection:
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
    def test_sort_messages_from_request(self):
        with open(os.path.join(os.path.dirname(__file__), "./payloads/get_messages.json")) as f:
            text = f.read()
            json_payload = json.loads(text)

        log = logging.getLogger("Test")

        nmr = NewMessageReceived()
        nmr.logger = log

        result = nmr.sort_messages_from_request(json_payload)

        newest = result[0]
        oldest = result[-1]

        self.assertEqual(newest.get("body").get("content"), "This should be first")
        self.assertEqual(oldest.get("body").get("content"), "This is very old")

    def test_compile_message_content(self):
        nmr = NewMessageReceived()
        regex = nmr.compile_message_content(".")
        self.assertTrue(regex.search("stuff"))

        with self.assertRaises(PluginException):
            nmr.compile_message_content("[")

    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_get_sorted_messages(self, mockGet):
        log = logging.getLogger("Test")
        nmr = NewMessageReceived()
        nmr.logger = log
        nmr.connection = MockConnection()

        messages = nmr.get_sorted_messages("http://somefakeendpoint.com")

        self.assertIsNotNone(messages)
        self.assertEqual(messages[0].get("body").get("content"), "This should be first")
        self.assertEqual(messages[-1].get("body").get("content"), "This is very old")

    def test_setup_endpoint(self):
        log = logging.getLogger("Test")
        nmr = NewMessageReceived()
        nmr.logger = log
        nmr.connection = MockConnection()

        # This was a mess to figure out...because I'm importing with from I have to refer to the class it's being
        #  called from and not the actual function that's being imported
        with mock.patch(
            "icon_microsoft_teams.triggers.new_message_received.trigger.get_teams_from_microsoft",
            return_value=[{"id": "team"}],
        ):
            with mock.patch(
                "icon_microsoft_teams.triggers.new_message_received.trigger.get_channels_from_microsoft",
                return_value=[{"id": "channel"}],
            ):
                endpoint = nmr.setup_endpoint("channel", "team")

        self.assertEqual("https://graph.microsoft.com/beta/teams/team/channels/channel/messages", endpoint)
