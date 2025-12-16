import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from icon_azure_ad_admin.connection.connection import Connection
from icon_azure_ad_admin.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action, connect_params: dict = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if not connect_params:
            connect_params = {
                Input.TENANT_ID: "azure_tenant",
                Input.APPLICATION_ID: "app_id",
                Input.APPLICATION_SECRET: {"secretKey": "app_secret"},
            }
        default_connection.connect(connect_params)
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
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code: int, filename: str = None) -> None:
                self.status_code = status_code
                self.text = ""
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                return json.loads(self.text)

        method = kwargs.get("method")
        url = args[0] if args else kwargs.get("url")
        params = kwargs.get("params")
        json_data = kwargs.get("json")
        data = kwargs.get("data")

        if url == "https://login.microsoftonline.com/azure_tenant/oauth2/token":
            if data.get("client_secret") == "app_secret":
                return MockResponse(200, "access_token.json.resp")
        if url == "https://graph.microsoft.com/v1.0/azure_tenant/devices/9de5069c-5afe-602b-2ea0-a04b66beb2c0":
            if json_data == {"accountEnabled": False}:
                return MockResponse(204)
            if json_data == {"accountEnabled": True}:
                return MockResponse(204)
            if method == "DELETE":
                return MockResponse(204)
        if url == "https://graph.microsoft.com/v1.0/azure_tenant/devices/invalid":
            if method in ["PATCH", "DELETE"]:
                return MockResponse(404)
        if url == "https://graph.microsoft.com/v1.0/azure_tenant/devices/12345678-1234-1234-1234-987654321011":
            return MockResponse(200, "get_device.json.resp")
        if url == "https://graph.microsoft.com/v1.0/azure_tenant/devices/invalid-id":
            return MockResponse(400, "")
        if url == "https://graph.microsoft.com/v1.0/azure_tenant/devices":
            if params.get("$search") == '"displayName:Win-123_3123"':
                return MockResponse(200, "search_device_all_parameters.json.resp")
            if params.get("$search") == '"displayName:Win"':
                return MockResponse(200, "search_device_pagination_page1.json.resp")
            if params.get("$search") == '"displayName:SinglePage"':
                return MockResponse(200, "search_device_pagination_single_page.json.resp")
            if params.get("$search") == '"displayName:LoopLimit"':
                return MockResponse(200, "search_device_pagination_loop_limit.json.resp")
            if params.get("$search") == '"displayName:MultiPage"':
                return MockResponse(200, "search_device_pagination_multipage1.json.resp")
            if params.get("$orderBy") == "invalidParameter":
                return MockResponse(400, "")
            return MockResponse(200, "search_device_no_parameters.json.resp")
        # Handle pagination nextLink URLs
        if url == "https://graph.microsoft.com/v1.0/azure_tenant/devices?$skiptoken=page2":
            return MockResponse(200, "search_device_pagination_page2.json.resp")
        if url == "https://graph.microsoft.com/v1.0/azure_tenant/devices?$skiptoken=looplimit_next":
            # Always return the same response with nextLink to test loop limit
            return MockResponse(200, "search_device_pagination_loop_limit.json.resp")
        if url == "https://graph.microsoft.com/v1.0/azure_tenant/devices?$skiptoken=multipage2":
            return MockResponse(200, "search_device_pagination_multipage2.json.resp")
        if url == "https://graph.microsoft.com/v1.0/azure_tenant/devices?$skiptoken=multipage3":
            return MockResponse(200, "search_device_pagination_multipage3.json.resp")
        raise Exception(f"Not implemented: {kwargs}")
