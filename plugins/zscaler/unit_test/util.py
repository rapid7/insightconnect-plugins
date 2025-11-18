import os
import sys

sys.path.append(os.path.abspath("../"))

import json
import logging
import insightconnect_plugin_runtime

from icon_zscaler.connection import Connection
from icon_zscaler.connection.schema import Input

STUB_CONNECTION = {
    Input.API_KEY: {"secretKey": "my-secret-key"},
    Input.CREDENTIALS: {"password": "password123", "username": "user@zscalerbeta.net"},
    Input.URL: "https://sample.com",
}


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(STUB_CONNECTION)
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

        if url.endswith("authenticatedSession"):
            return MockResponse(200)

        if method == "DELETE" and url.endswith("users/12345"):
            return MockResponse(204)
        if method == "DELETE" and url.endswith("users/99999"):
            return MockResponse(404, "")

        if method == "GET" and url.endswith("/v1/status"):
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
