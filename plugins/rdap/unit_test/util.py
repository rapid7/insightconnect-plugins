import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from icon_rdap.connection import Connection
from insightconnect_plugin_runtime.action import Action


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect({})
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r", encoding="utf-8"
        ) as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_dict(filename: str) -> dict:
        return json.loads(Util.read_file_to_string(filename))

    @staticmethod
    def mock_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                self.text = ""
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                return json.loads(self.text)

        if kwargs.get("url") == "https://rdap.net/domain/example.com":
            return MockResponse(200, "domain_lookup_found_domain.json.resp")
        if kwargs.get("url") == "https://rdap.net/domain/example":
            return MockResponse(404, "")
        if kwargs.get("url") == "https://rdap.net/domain/examplefail.com":
            return MockResponse(404, "")

        if kwargs.get("url").startswith("https://rdap.net/autnum/12345"):
            return MockResponse(200, "asn_lookup.json.resp")
        if kwargs.get("url").startswith("https://rdap.net/autnum/99999"):
            return MockResponse(404, "")

        if kwargs.get("url") == "https://rdap.net/ip/2.2.2.2":
            return MockResponse(200, "ip_lookup_with_asn.json.resp")
        if kwargs.get("url") == "https://rdap.net/ip/1.1.1.1":
            return MockResponse(200, "ip_lookup.json.resp")
        if kwargs.get("url") == "https://rdap.net/ip/invalid_ip":
            return MockResponse(400, "")
        if kwargs.get("url") == "https://rdap.net/ip/255.255.11.135":
            return MockResponse(404, "")

        raise NotImplementedError("Not implemented", kwargs)

    @staticmethod
    def mock_rdap_lookup(*args, **kwargs):
        if kwargs.get("ip_address") == "2.2.2.2":
            return Util.read_file_to_dict("responses/ip_lookup_ipwhois_lookup.json.resp")

        raise NotImplementedError("Not implemented", kwargs)
