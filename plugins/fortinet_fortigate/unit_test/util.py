import json
import logging
import os
from icon_fortinet_fortigate.connection.connection import Connection
from icon_fortinet_fortigate.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.HOSTNAME: "https://example.com",
                Input.API_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
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
    def load_data(filename):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.json.resp")
            )
        )

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                if self.filename == "not_found":
                    self.text = 'Response was: {"message": "Not Found"}'
                elif self.filename == "already_exists":
                    self.text = 'Response was: {"message": "Already Exists"}'
                else:
                    self.text = "Error message"

            def json(self):
                return Util.load_data(self.filename)

        params = kwargs.get("params")
        url = kwargs.get("url")
        json_payload = kwargs.get("json")
        method = kwargs.get("method")

        if json_payload == {"name": "1.1.1.1", "type": "ipmask", "subnet": "1.1.1.1/32"}:
            return MockResponse("create_address_object_ipv4", 200)
        if json_payload == {
            "name": "1111:2222:3333:4444:5555:6666:7777:8888",
            "type": "ipprefix",
            "ip6": "1111:2222:3333:4444:5555:6666:7777:8888/128",
        }:
            return MockResponse("create_address_object_ipv6", 200)
        if json_payload == {"name": "example.com", "type": "fqdn", "fqdn": "example.com"}:
            return MockResponse("create_address_object_domain", 200)
        if json_payload == {"name": "2.2.2.2", "type": "ipmask", "subnet": "2.2.2.2/32"}:
            return MockResponse("already_exists", 500)
        if params == {"filter": "name=@Test Policy"}:
            return MockResponse("get_policies", 200)
        if params == {"filter": "name=@Invalid Policy"}:
            return MockResponse("empty_results", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/address" and params == {"filter": []}:
            return MockResponse("get_all_address_objects", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/address6" and params == {"filter": []}:
            return MockResponse("get_ipv6_address_object", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/address" and params == {"filter": ["name=@1.1.1.1"]}:
            return MockResponse("get_ipv4_address_object", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/address6" and params == {"filter": ["name=@1.1.1.1"]}:
            return MockResponse("empty_results", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/address" and params == {
            "filter": ["name=@test.com", "fqdn=@test.com"]
        }:
            return MockResponse("get_domain_address_object", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/address6" and params == {"filter": ["name=@test.com"]}:
            return MockResponse("empty_results", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/address" and params == {
            "filter": ["name=@1111:2222:3333:4444:5555:6666:7777:8888"]
        }:
            return MockResponse("empty_results", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/address6" and params == {
            "filter": [
                "name=@1111:2222:3333:4444:5555:6666:7777:8888",
                "ip6=@1111:2222:3333:4444:5555:6666:7777:8888/128",
            ]
        }:
            return MockResponse("get_ipv6_address_object", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/address" and params == {
            "filter": ["name=@1.1.1.1", "subnet=@1.1.1.1 255.255.255.255"]
        }:
            return MockResponse("get_ipv4_address_object", 200)
        if params == {"filter": "name=@1.1.1.1"}:
            return MockResponse("get_ipv4_address_object", 200)
        if params == {"filter": "name=@example.com"}:
            return MockResponse("get_domain_address_object", 200)
        if params == {"filter": "name=@1111:2222:3333:4444:5555:6666:7777:8888"}:
            return MockResponse("get_ipv6_address_object", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/address/1.1.1.1" and method == "DELETE":
            return MockResponse("delete_address_object_ipv4", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/address/test.com" and method == "DELETE":
            return MockResponse("delete_address_object_domain", 200)
        if (
            url
            == "https://example.com/api/v2/cmdb/firewall/address6/1111%3A2222%3A3333%3A4444%3A5555%3A6666%3A7777%3A8888"
            and method == "DELETE"
        ):
            return MockResponse("delete_address_object_ipv6", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/address/1.1.1.1":
            return MockResponse("get_ipv4_address_object", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/address/test.com":
            return MockResponse("get_domain_address_object", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/address/example.com":
            return MockResponse("get_domain_address_object2", 200)
        if (
            url
            == "https://example.com/api/v2/cmdb/firewall/address/1111%3A2222%3A3333%3A4444%3A5555%3A6666%3A7777%3A8888"
        ):
            return MockResponse("not_found", 404)
        if (
            url
            == "https://example.com/api/v2/cmdb/firewall/address6/1111%3A2222%3A3333%3A4444%3A5555%3A6666%3A7777%3A8888"
        ):
            return MockResponse("get_ipv6_address_object", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/address/invalid_object":
            return MockResponse("not_found", 404)
        if url == "https://example.com/api/v2/cmdb/firewall/address6/invalid_object":
            return MockResponse("not_found", 404)
        if params == {"filter": "name=@Invalid Group"}:
            return MockResponse("not_found", 404)
        if url == "https://example.com/api/v2/cmdb/firewall/addrgrp":
            return MockResponse("get_address_group", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/addrgrp6":
            return MockResponse("get_ipv6_address_group", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/addrgrp/Address Object Group":
            return MockResponse("modify_address_group", 200)
        if url == "https://example.com/api/v2/cmdb/firewall/addrgrp6/IPv6 Address Object Group":
            return MockResponse("modify_ipv6_address_group", 200)
        raise Exception("Not implemented")
