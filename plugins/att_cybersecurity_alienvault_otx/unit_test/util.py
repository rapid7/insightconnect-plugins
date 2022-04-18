import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

from komand_att_cybersecurity_alienvault_otx.connection.connection import Connection
from komand_att_cybersecurity_alienvault_otx.connection.schema import Input
import json


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.API_KEY: {"secretKey": "3395856ce81f2b7382dee72602f798b642f14140"},
            Input.URL: "https://example.com",
        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def load_parameters(filename):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"parameters/{filename}.json.resp")
            )
        )

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(
                            os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp"
                        )
                    )
                )

        if args[0] == "https://example.com/api/v1/indicators/url/https://example.com/general":
            return MockResponse("get_indicator_details_url_general", 200)
        if args[0] == "https://example.com/api/v1/indicators/url/https://example.com/url_list":
            return MockResponse("get_indicator_details_url_list", 200)
        if args[0] == "https://example.com/api/v1/indicators/IPv4/198.51.100.100/general":
            return MockResponse("get_indicator_details_ipv4_general", 200)
        if args[0] == "https://example.com/api/v1/indicators/IPv4/198.51.100.100/geo":
            return MockResponse("get_indicator_details_ipv4_geo", 200)
        if args[0] == "https://example.com/api/v1/indicators/IPv4/198.50.100.100/url_list":
            return MockResponse("get_indicator_details_ipv4_url_list", 200)
        if args[0] == "https://example.com/api/v1/indicators/hostname/example.com/passive_dns":
            return MockResponse("get_indicator_details_hostname_passive_dns", 200)
        if args[0] == "https://example.com/api/v1/indicators/hostname/example.com/geo":
            return MockResponse("get_indicator_details_hostname_geo", 200)
        raise Exception("Not implemented")
