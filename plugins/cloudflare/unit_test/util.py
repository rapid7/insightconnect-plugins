import logging
import sys
import os

import insightconnect_plugin_runtime

sys.path.append(os.path.abspath("../"))

from icon_cloudflare.connection.connection import Connection
from icon_cloudflare.connection.schema import Input
import json


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.APITOKEN: {"secretKey": "api_token"},
        }
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

        url = kwargs.get("url", "")
        json_data = kwargs.get("json", {})
        params = kwargs.get("params", {})

        if url == "https://api.cloudflare.com/client/v4/zones/invalid_id/firewall/access_rules/rules":
            return MockResponse(404, "")
        if json_data == {"mode": "block", "configuration": {"value": "198.51.100.1", "target": "ip"}}:
            return MockResponse(200, "create_zone_access_rule_ipv4.json.resp")
        if json_data == {"mode": "block", "configuration": {"value": "2001:db8:1:1:1:1:1:1", "target": "ip6"}}:
            return MockResponse(200, "create_zone_access_rule_ipv6.json.resp")
        if json_data == {
            "mode": "whitelist",
            "configuration": {"value": "198.51.100.1/16", "target": "ip_range"},
            "notes": "Test",
        }:
            return MockResponse(200, "create_zone_access_rule_ipv4_range.json.resp")
        if json_data == {
            "mode": "block",
            "configuration": {"value": "2001:db8:1:1:1:1:1:1/48", "target": "ip_range"},
            "notes": "Test",
        }:
            return MockResponse(200, "create_zone_access_rule_ipv6_range.json.resp")
        if json_data == {"mode": "challenge", "configuration": {"value": "as12345", "target": "asn"}}:
            return MockResponse(200, "create_zone_access_rule_asn.json.resp")
        if json_data == {"mode": "challenge", "configuration": {"value": "GB", "target": "country"}}:
            return MockResponse(200, "create_zone_access_rule_country.json.resp")

        if (
            url
            == "https://api.cloudflare.com/client/v4/zones/9de5069c5afe602b2ea0a04b66beb2c0/firewall/access_rules/rules/9de5069c5afe602b2ea0a04b66beb2c0"
        ):
            return MockResponse(200, "delete_zone_access_rule.json.resp")
        if (
            url
            == "https://api.cloudflare.com/client/v4/zones/9de5069c5afe602b2ea0a04b66beb2c0/firewall/access_rules/rules/invalid_rule_id"
        ):
            return MockResponse(404, "")
        if (
            url
            == "https://api.cloudflare.com/client/v4/zones/invalid_zone_id/firewall/access_rules/rules/9de5069c5afe602b2ea0a04b66beb2c0"
        ):
            return MockResponse(404, "")

        if params == {"name": "Example Account", "page": 1, "per_page": 1, "direction": "asc"}:
            return MockResponse(200, "list_accounts.json.resp")
        if params == {"direction": "desc"}:
            return MockResponse(200, "list_accounts.json.resp")
        if params == {"name": "Invalid Name", "direction": "desc"}:
            return MockResponse(200, "list_accounts_empty.json.resp")

        if url == "https://api.cloudflare.com/client/v4/accounts/9de5069c5afe602b2ea0a04b66beb2c0/rules/lists":
            return MockResponse(200, "get_lists.json.resp")
        if url == "https://api.cloudflare.com/client/v4/accounts/invalid_id/rules/lists":
            return MockResponse(404, "")

        if url == "https://api.cloudflare.com/client/v4/zones/12345/firewall/access_rules/rules":
            return MockResponse(404, "")
        if params == {"match": "any", "page": 1, "per_page": 20, "order": "mode", "direction": "desc"}:
            return MockResponse(200, "get_zone_access_rules_all.json.resp")
        if params == {
            "notes": "Test",
            "mode": "block",
            "match": "any",
            "configuration.target": "ip",
            "page": 1,
            "per_page": 20,
            "order": "mode",
            "direction": "desc",
        }:
            return MockResponse(200, "get_zone_access_rules_ip.json.resp")
        if params == {"match": "all", "configuration.value": "1.1.1.1", "order": "mode", "direction": "desc"}:
            return MockResponse(200, "get_zone_access_rules_empty.json.resp")
        if params == {
            "match": "all",
            "configuration.target": "asn",
            "order": "configuration.value",
            "direction": "asc",
        }:
            return MockResponse(200, "get_zone_access_rules_asn.json.resp")
        if params == {"match": "all", "configuration.target": "country", "order": "mode", "direction": "desc"}:
            return MockResponse(200, "get_zone_access_rules_country.json.resp")
        if params == {
            "mode": "whitelist",
            "match": "all",
            "configuration.target": "ip_range",
            "configuration.value": "198.51.100.1/16",
            "order": "configuration.target",
            "direction": "asc",
        }:
            return MockResponse(200, "get_zone_access_rules_ip_range.json.resp")

        if params == {"match": "any", "page": 1, "per_page": 20, "order": "name", "direction": "asc"}:
            return MockResponse(200, "get_zones_all.json.resp")
        if params == {
            "match": "all",
            "name": "example.com",
            "account.name": "Example Account",
            "account.id": "9de5069c5afe602b2ea0a04b66beb2c0",
            "status": "pending",
            "page": 1,
            "per_page": 20,
            "order": "account.name",
            "direction": "asc",
        }:
            return MockResponse(200, "get_zones_by_name.json.resp")
        if params == {
            "match": "all",
            "account.id": "12345",
            "page": 1,
            "per_page": 20,
            "order": "account.id",
            "direction": "desc",
        }:
            return MockResponse(200, "get_zones_empty.json.resp")

        raise NotImplementedError("Not implemented", kwargs)
