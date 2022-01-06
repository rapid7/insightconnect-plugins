import json
import logging
import os
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_palo_alto_mine_meld.connection.connection import Connection
from icon_palo_alto_mine_meld.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.URL: "https://example.com",
                Input.CREDENTIALS: {"password": "password", "username": "user"},
                Input.PORT: 443,
                Input.SSL_VERIFY: True,
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
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                self.text = "This is some error text"

                if self.filename == "update_list_error":
                    self.text = {"error": {"message": "Unknown config data file"}}

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp")
                    )
                )

        if args[0] == "GET" and args[1] == "https://example.com:443/config/data/domain_list_add_indicators":
            return MockResponse("update_list_add_domain_get_indicators", 200)
        elif args[0] == "GET" and args[1] == "https://example.com:443/config/data/domain_list_remove_indicators":
            return MockResponse("update_list_remove_domain_get_indicators", 200)
        if args[0] == "GET" and args[1] == "https://example.com:443/config/data/ipv4_list_add_indicators":
            return MockResponse("update_list_add_ipv4_get_indicators", 200)
        elif args[0] == "GET" and args[1] == "https://example.com:443/config/data/ipv4_list_remove_indicators":
            return MockResponse("update_list_remove_ipv4_get_indicators", 200)
        if args[0] == "GET" and args[1] == "https://example.com:443/config/data/ipv6_list_add_indicators":
            return MockResponse("update_list_add_ipv6_get_indicators", 200)
        elif args[0] == "GET" and args[1] == "https://example.com:443/config/data/ipv6_list_remove_indicators":
            return MockResponse("update_list_remove_ipv6_get_indicators", 200)
        if args[0] == "GET" and args[1] == "https://example.com:443/config/data/url_list_add_indicators":
            return MockResponse("update_list_add_url_get_indicators", 200)
        elif args[0] == "GET" and args[1] == "https://example.com:443/config/data/url_list_remove_indicators":
            return MockResponse("update_list_remove_url_get_indicators", 200)
        elif args[1] == "https://example.com:443/config/data/domain_list_add_indicators":
            return MockResponse("update_list_successful", 200)
        elif args[1] == "https://example.com:443/config/data/domain_list_remove_indicators":
            return MockResponse("update_list_successful", 200)
        elif args[1] == "https://example.com:443/config/data/ipv4_list_add_indicators":
            return MockResponse("update_list_successful", 200)
        elif args[1] == "https://example.com:443/config/data/ipv4_list_remove_indicators":
            return MockResponse("update_list_successful", 200)
        elif args[1] == "https://example.com:443/config/data/ipv6_list_add_indicators":
            return MockResponse("update_list_successful", 200)
        elif args[1] == "https://example.com:443/config/data/ipv6_list_remove_indicators":
            return MockResponse("update_list_successful", 200)
        elif args[1] == "https://example.com:443/config/data/url_list_add_indicators":
            return MockResponse("update_list_successful", 200)
        elif args[1] == "https://example.com:443/config/data/url_list_remove_indicators":
            return MockResponse("update_list_successful", 200)
        elif args[1] == "https://example.com:443/config/data/invalid_list_indicators":
            return MockResponse("update_list_error", 400)

        raise Exception("Not implemented")
