import json
import logging
import sys
import os

import insightconnect_plugin_runtime

from icon_sophos_central.connection import Connection
from icon_sophos_central.connection.schema import Input

sys.path.append(os.path.abspath("../"))


class Meta:
    version = "0.0.0"


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.CLIENT_ID: {"secretKey": "my-client_id"},
            Input.CLIENT_SECRET: {"secretKey": "my-secret-key"},
            Input.REGION: "US East",
            Input.TENANT_ID: {"secretKey": "my-tenant_id"},
        }
        default_connection.meta = Meta()
        default_connection.connect(params)
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

        json_data = kwargs.get("json", {})
        params = kwargs.get("params", {})
        url = args[1]
        method = args[0]

        if url in ["https://id.sophos.com/api/v2/oauth2/token", "https://api.central.sophos.com/whoami/v1"]:
            return MockResponse(200, "")

        if "/endpoint/v1/settings/blocked-items" in url:
            if method == "GET":
                if params == {"page": 1, "pageSize": 50, "pageTotal": True}:
                    return MockResponse(200, "get_blocked_items.json.resp")
                if params == {"pageTotal": False}:
                    return MockResponse(200, "get_blocked_items_no_params.json.resp")

            if method == "DELETE":
                if url.endswith("0da7bc3d-valid_id"):
                    return MockResponse(200, "remove_blocked_item.json.resp")
                if url.endswith("invalidId"):
                    return MockResponse(400, "")

            if method == "POST":
                if json_data.get("properties").get("sha256") == "050c194cbbb":
                    return MockResponse(201, "add_blocked_item.json.resp")
                if json_data.get("properties").get("sha256") == "duplicatedSha":
                    return MockResponse(409, "")

        if "/endpoint/v1/settings/allowed-items" in url:
            if method == "GET":
                if params.get("pageTotal"):
                    return MockResponse(200, "get_allowed_items_with_page_total.json.resp")
                else:
                    return MockResponse(200, "get_allowed_items_all.json.resp")

            if method == "POST":
                if json_data.get("originEndpointId") == "invalid_id":
                    return MockResponse(400)
                elif json_data.get("properties").get("fileName") == "existing_sample.txt":
                    return MockResponse(409)
                elif json_data.get("type") == "path":
                    return MockResponse(201, "add_allowed_item_path.json.resp")
                elif json_data.get("type") == "sha256":
                    return MockResponse(201, "add_allowed_item_sha256.json.resp")
                elif json_data.get("type") == "certificateSigner":
                    return MockResponse(201, "add_allowed_item_certificate_signer.json.resp")

            if method == "DELETE":
                if url.endswith("invalid_id"):
                    return MockResponse(400)
                elif url.endswith("0da7bc3d2h"):
                    return MockResponse(200, "remove_allowed_item.json.resp")

        if url.endswith("/endpoint/v1/endpoint-groups") and method == "GET":
            if params.get("search") == "not_found_name":
                return MockResponse(200, "get_endpoint_groups_not_found.json.resp")
            if params.get("fields") == ["name", "id", "description", "type"]:
                return MockResponse(200, "get_endpoint_groups_specified_fields.json.resp")
            if params.get("ids") == ["f8d03561-90d1-4c18-b576-34509e843ee8"]:
                return MockResponse(200, "get_endpoint_groups_with_ids.json.resp")
            if params.get("searchFields") == ["name"]:
                return MockResponse(200, "get_endpoint_groups_with_search.json.resp")
            if params.get("groupType") == "non_existing_group_type":
                return MockResponse(400)
            else:
                return MockResponse(200, "get_endpoint_groups_all.json.resp")

        if json_data == {
            "name": "Example Group",
            "type": "server",
            "description": "Example description",
        }:
            return MockResponse(201, "endpoint_group.json.resp")
        if json_data == {
            "name": "Example Group",
            "type": "computer",
            "description": "Example description",
            "endpointIds": ["9de5069c-5afe-602b-2ea0-a04b66beb2c0"],
        }:
            return MockResponse(201, "endpoint_group2.json.resp")
        if json_data == {
            "name": "Example Group",
            "type": "computer",
            "description": "Example description",
            "endpointIds": ["invalid_id"],
        }:
            return MockResponse(404)
        if (
            url
            == "https://api-us03.central.sophos.com/endpoint/v1/endpoint-groups/9de5069c-5afe-602b-2ea0-a04b66beb2c0"
        ):
            return MockResponse(200, "endpoint_group2.json.resp")
        if url == "https://api-us03.central.sophos.com/endpoint/v1/endpoint-groups/invalid_id":
            return MockResponse(404)
        if url == "https://api-us03.central.sophos.com/endpoint/v1/endpoint-groups/invalid_id/endpoints":
            return MockResponse(404)
        if params == {"ids": ["9de5069c-5afe-602b-2ea0-a04b66beb2c0"]}:
            return MockResponse(200, "remove_endpoint_from_group.json.resp")
        if params == {"ids": ["9de5069c-5afe-602b-2ea0-a04b66beb333"]}:
            return MockResponse(200, "remove_endpoint_from_group_endpoint_not_found.json.resp")
        if json_data == {"ids": ["9de5069c-5afe-602b-2ea0-a04b66beb2c0"]}:
            return MockResponse(201, "add_endpoint_to_group.json.resp")
        if json_data == {"ids": ["9de5069c-5afe-602b-2ea0-a04b66beb333"]}:
            return MockResponse(404)
        if json_data == {
            "enabled": True,
            "ids": ["9de5069c-5afe-602b-2ea0-a04b66beb2c0"],
            "comment": "Example comment",
        }:
            return MockResponse(202, "enable_isolation.json.resp")
        if json_data == {
            "enabled": False,
            "ids": ["9de5069c-5afe-602b-2ea0-a04b66beb2c0"],
            "comment": "Example comment",
        }:
            return MockResponse(202, "disable_isolation.json.resp")
        if json_data == {"enabled": True, "ids": ["invalid_id"], "comment": "Example comment"}:
            return MockResponse(404)

        if params == {"fields": ["hostname", "os"], "pageSize": 1, "pageTotal": False}:
            return MockResponse(200, "get_endpoints_in_group_selected_fields.json.resp")
        if params == {"sort": ["id:asc"], "fields": ["hostname", "os"], "pageSize": 2, "pageTotal": True}:
            return MockResponse(200, "get_endpoints_in_group_sort_asc.json.resp")
        if params == {"sort": ["id:desc"], "fields": ["hostname", "os"], "pageSize": 2, "pageTotal": True}:
            return MockResponse(200, "get_endpoints_in_group_sort_desc.json.resp")
        if params == {"fields": ["hostname", "os"], "pageFromKey": "exampleKey", "pageSize": 2, "pageTotal": True}:
            return MockResponse(200, "get_endpoints_in_group_next_page.json.resp")
        if params == {
            "fields": ["hostname", "os"],
            "pageSize": 2,
            "pageTotal": True,
            "search": "DESKTOP-1234568",
            "searchFields": ["hostname"],
        }:
            return MockResponse(200, "get_endpoints_in_group_search_hostname.json.resp")
        if params == {
            "fields": ["hostname", "os"],
            "pageSize": 2,
            "pageTotal": True,
            "search": "windows",
            "searchFields": ["osName"],
        }:
            return MockResponse(200, "get_endpoints_in_group_search_os_name.json.resp")
        if params == {
            "fields": ["hostname", "os"],
            "pageSize": 2,
            "pageTotal": True,
            "search": "TEST1",
            "searchFields": ["hostname"],
        }:
            return MockResponse(200, "get_endpoints_in_group_search_empty.json.resp")
        if (
            url
            == "https://api-us03.central.sophos.com/endpoint/v1/endpoint-groups/9de5069c-5afe-602b-2ea0-a04b66beb2c0/endpoints"
        ):
            return MockResponse(200, "get_endpoints_in_group.json.resp")

        raise NotImplementedError("Not implemented", kwargs)
