import os
import sys

sys.path.append(os.path.abspath("../"))

import json
import logging
import insightconnect_plugin_runtime

from icon_zscaler.connection import Connection
from icon_zscaler.connection.schema import Input

STUB_CONNECTION = {
    Input.CLIENT_ID: "test-client-id",
    Input.PRIVATE_KEY: {
        "privateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIIBogIBAAJBALRiMLAHudeSA/x3hB2f+2NRkJLA2jBImmA2RsjFOW5EP0FF\n-----END RSA PRIVATE KEY-----"
    },
    Input.VANITY_DOMAIN: "testcompany",
    Input.CLOUD: "zsapi.net",
}


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(STUB_CONNECTION)
        # Bypass real JWT signing by pre-setting a mock token on both clients
        default_connection.zia_client._token = "mock-access-token-12345"
        default_connection.zia_client._token_expiry = 9999999999
        default_connection.zpa_client._token = "mock-access-token-12345"
        default_connection.zpa_client._token_expiry = 9999999999
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
            def __init__(self, status_code: int, filename: str = None, headers: dict = {}):
                self.status_code = status_code
                self.text = ""
                self.headers = headers
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                return json.loads(self.text)

        url = kwargs.get("url", "")
        method = kwargs.get("method", "")
        params = kwargs.get("params", {})
        data = kwargs.get("data", {})

        # Handle OAuth token requests
        if "oauth2/v1/token" in url:
            return MockResponse(200, "oauth_token.json.resp")

        # Handle ZPA endpoints
        if "/zpa/api/v1/application" in url and method == "GET":
            return MockResponse(200, "zpa_application.json.resp")
        if "/zpa/api/v1/serverGroup" in url and method == "GET":
            return MockResponse(200, "zpa_server_group.json.resp")

        if method == "DELETE" and url.endswith("users/12345"):
            return MockResponse(204)
        if method == "DELETE" and url.endswith("users/99999"):
            return MockResponse(404, "")

        if method == "GET" and url.endswith("/status"):
            return MockResponse(200, "get_status.json.resp")

        if method == "GET" and url.endswith("users"):
            if params.get("name") == "Not exist":
                return MockResponse(200, "empty_list.json.resp")
            else:
                return MockResponse(200, "get_users.json.resp")

        if method == "GET" and url.endswith("departments"):
            return MockResponse(200, "departments_list.json.resp")

        if method == "GET" and url.endswith("groups"):
            return MockResponse(200, "groups_list.json.resp")

        if method == "POST" and url.endswith("users"):
            if "Valid user data" in data:
                return MockResponse(200, "create_user.json.resp")
            if "Mandatory fields" in data:
                return MockResponse(200, "create_user_mandatory_fields.json.resp")
            if "Invalid department" in data:
                return MockResponse(400, "")
            if "Invalid group" in data:
                return MockResponse(400, "")

        if method == "GET":
            if url.endswith("urlCategories"):
                if params.get("customOnly"):
                    return MockResponse(200, "list_url_categories_only_custom.json.resp")
                else:
                    return MockResponse(200, "list_url_categories_all.json.resp")

            if url.endswith("urlCategories/CUSTOM_01"):
                return MockResponse(200, "get_url_category_by_name_custom.json.resp")
            if url.endswith("urlCategories/RADIO_STATIONS"):
                return MockResponse(200, "get_url_category_by_name_predefined.json.resp")

        if method == "PUT":
            if url.endswith("urlCategories/CUSTOM_01"):
                if "example11.com" in json.loads(data).get("urls"):
                    return MockResponse(200, "update_urls_of_url_category_custom_add.json.resp")
                else:
                    return MockResponse(400)
            if url.endswith("urlCategories/RADIO_STATIONS"):
                return MockResponse(200, "update_urls_of_url_category_predefined_add.json.resp")
            if url.endswith("urlCategories/CUSTOM_02"):
                return MockResponse(200, "update_urls_of_url_category_custom_remove.json.resp")

        raise NotImplementedError("Not implemented", kwargs)
