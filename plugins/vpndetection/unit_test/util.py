import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.action import Action

from icon_vpndetection.connection.connection import Connection

API_KEY = "9de5069c5afe602b2ea0a04b66beb2c0"


class MockResponse:
    def __init__(self, status_code: int, filename: str = None, text: str = ""):
        self.status_code = status_code
        self.text = Util.read_file_to_string(f"responses/{filename}") if filename else text

    def json(self):
        return json.loads(self.text)


class Util:
    @staticmethod
    def default_connector(action: Action, api_key: str = "") -> Action:
        connection = Connection()
        connection.logger = logging.getLogger("connection logger")
        connection.connect({"api_key": {"secretKey": api_key}} if api_key else {})
        action.connection = connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def read_file_to_dict(filename: str) -> dict:
        return json.loads(Util.read_file_to_string(filename))

    @staticmethod
    def mock_request(method: str, url: str, headers: dict = None, timeout: int = None) -> MockResponse:
        authorization = (headers or {}).get("Authorization")
        if authorization is not None and authorization != f"Bearer {API_KEY}":
            return MockResponse(401, text='{"error": "invalid API key"}')
        if url == "https://api.vpndetection.io/185.220.101.1":
            return MockResponse(200, "lookup_keyless.json.resp")
        if url == "https://api.vpndetection.io/188.42.45.201":
            return MockResponse(200, "lookup_keyed.json.resp")
        if url == "https://api.vpndetection.io/10.0.0.1":
            return MockResponse(200, "lookup_bogon.json.resp")
        if url == "https://api.vpndetection.io/1.1.1.1":
            return MockResponse(200, "lookup_bogon.json.resp")
        if url == "https://api.vpndetection.io/198.51.100.7":
            return MockResponse(429, text='{"error": "rate limit exceeded"}')
        if url == "https://api.vpndetection.io/198.51.100.8":
            return MockResponse(503, text="Service Unavailable")
        if url == "https://api.vpndetection.io/198.51.100.9":
            return MockResponse(200, text="<html></html>")
        raise NotImplementedError(f"No mock for {method} {url}")
