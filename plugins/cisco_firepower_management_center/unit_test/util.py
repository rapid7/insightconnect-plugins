import json
import logging
import os
from typing import Any

from icon_cisco_firepower_management_center.connection.connection import Connection
from icon_cisco_firepower_management_center.connection.schema import Input

next_response = False


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.SERVER: "https://example.com",
            Input.USERNAME_AND_PASSWORD: {"password": "password", "username": "user"},
            Input.SSL_VERIFY: True,
            Input.PORT: 443,
            Input.HOST_INPUT_PORT: 8307,
            Input.CERTIFICATE_PASSPHRASE: {"secretKey": "test12345"},
            Input.CERTIFICATE: "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",
            Input.DOMAIN: "Global",
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
        return Util.read_file_to_string(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{filename}.resp")
        )

    @staticmethod
    def load_parameters(filename):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"parameters/{filename}.json.resp")
            )
        )

    class MockSSLSocket:
        def __init__(self, *args, **kwargs) -> None: ...

        def connect(self, address: Any) -> None: ...

        def send(self, data: bytes) -> None: ...

        def write(self, data: bytes) -> None:
            global next_response
            if data == b"\x00\x00\x00\x03\x00\x00\x00\xcc":
                next_response = True

        def recv(self, buflen: int = 1024) -> bytes:
            global next_response
            if buflen == 4:
                return b"\x00\x08\x00\x00"
            if buflen == 28:
                next_response = False
                return b"Done processing 4 commands.\n"
            if next_response:
                return b"\x00\x00\x00\x03\x00\x00\x00\x1c"
            return b"\x00\x00\x00\x01\x00\x00\x00\x04"

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                self.headers = {"X-auth-access-token": "token", "DOMAINS": "[]", "DOMAIN_UUID": "1"}
                if self.filename in [
                    "get_server_version",
                    "url_object",
                    "access_policy",
                    "access_rule",
                    "deployable_devices",
                ]:
                    self.text = Util.load_data(self.filename)

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(
                            os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp"
                        )
                    )
                )

            def close(self):
                pass

        if args[0] == "https://example.com/api/fmc_platform/v1/info/serverversion":
            return MockResponse("get_server_version", 200)
        if args[0] == "https://example.com/api/fmc_config/v1/domain/1/object/urls":
            return MockResponse("url_object", 201)
        if kwargs.get("json", {}) is None:
            if (
                args[1]
                == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/urls"
            ):
                return MockResponse("url_object", 200)
            if (
                args[1]
                == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/policy/accesspolicies"
            ):
                return MockResponse("access_policy", 200)
        if args[0] == "https://example.com/api/fmc_config/v1/domain/1/object/urls/00000000-0000-0000-0000-000000000001":
            return MockResponse("url_object", 200)
        if (
            args[0]
            == "https://example.com/api/fmc_config/v1/domain/1/policy/accesspolicies?name=Test_Policy&expanded=true"
        ):
            return MockResponse("access_policy", 200)
        if (
            args[0]
            == "https://example.com/api/fmc_config/v1/domain/1/policy/accesspolicies/00000000-0000-0000-0000-000000000001/accessrules"
        ):
            return MockResponse("access_rule", 201)
        if args[0] == "https://example.com/api/fmc_config/v1/domain/1/deployment/deployabledevices?expanded=true":
            return MockResponse("deployable_devices", 200)
        if args[0] == "https://example.com/api/fmc_platform/v1/auth/generatetoken":
            return MockResponse("token", 204)
        if args[1] == "https://example.com/api/fmc_platform/v1/info/domain":
            return MockResponse("domain", 200)
        if (
            args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/networkaddresses"
        ):
            return MockResponse("get_address_objects", 200)
        if (
            args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/networkgroups"
        ):
            return MockResponse("get_address_groups", 200)
        if (
            args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/networkgroups/00000000-0000-0000-0000-000000000001"
        ):
            return MockResponse("add_address_to_group", 200)
        if (
            args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/networkgroups/00000000-0000-0000-0000-000000000003"
        ):
            return MockResponse("add_address_to_group_empty_objects", 200)
        if (
            args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/networkgroups/00000000-0000-0000-0000-000000000002"
        ):
            return MockResponse("remove_address_from_group", 200)
        if (
            args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/fqdns/00000000-0000-0000-0000-000000000001"
        ):
            return MockResponse("create_object_fqdn", 200)
        if (
            args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/hosts/00000000-0000-0000-0000-000000000001"
        ):
            return MockResponse("create_object_ipv4", 200)
        if (
            args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/hosts/00000000-0000-0000-0000-000000000002"
        ):
            return MockResponse("create_object_ipv6", 200)
        if (
            args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/networks/00000000-0000-0000-0000-000000000001"
        ):
            return MockResponse("create_object_ipv4_cidr", 200)
        if (
            args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/networks/00000000-0000-0000-0000-000000000002"
        ):
            return MockResponse("create_object_ipv6_cidr", 200)
        if (
            args[0] == "GET"
            and args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/hosts"
        ):
            return MockResponse("get_hosts", 200)
        if (
            args[0] == "GET"
            and args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/fqdns"
        ):
            return MockResponse("get_fqdns", 200)
        if (
            args[0] == "GET"
            and args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/networks"
        ):
            return MockResponse("get_networks", 200)
        if (
            args[0] == "DELETE"
            and args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/fqdns/00000000-0000-0000-0000-000000000001"
        ):
            return MockResponse("create_object_fqdn", 200)
        if (
            args[0] == "DELETE"
            and args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/hosts/00000000-0000-0000-0000-000000000001"
        ):
            return MockResponse("create_object_ipv4", 200)
        if (
            args[0] == "DELETE"
            and args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/hosts/00000000-0000-0000-0000-000000000002"
        ):
            return MockResponse("create_object_ipv6", 200)
        if (
            args[0] == "DELETE"
            and args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/hosts/00000000-0000-0000-0000-000000000001"
        ):
            return MockResponse("create_object_ipv4_cidr", 200)
        if (
            args[0] == "DELETE"
            and args[1]
            == "https://example.com/api/fmc_config/v1/domain/44d88612-fea8-a8f3-6de8-2e1278abb02f/object/hosts/00000000-0000-0000-0000-000000000002"
        ):
            return MockResponse("create_object_ipv6_cidr", 200)
        if (
            args[0] == "POST"
            and args[1]
            == "https://example.com/api/fmc_config/v1/domain/1/policy/accesspolicies/00000000-0000-0000-0000-000000000001/accessrules"
        ):
            return MockResponse("access_rule", 200)
        if kwargs.get("json", {}).get("name") == "example.com":
            return MockResponse("create_object_fqdn", 200)
        if kwargs.get("json", {}).get("name") == "Test_Policy":
            return MockResponse("access_policy", 200)
        if kwargs.get("json", {}).get("name") == "Test_Policy":
            return MockResponse("access_rule", 200)
        if kwargs and kwargs.get("json", {}).get("name") == "1.1.1.1":
            return MockResponse("create_object_ipv4", 200)
        if kwargs and kwargs.get("json", {}).get("name") == "123:45:6::1":
            return MockResponse("create_object_ipv6", 200)
        if kwargs and kwargs.get("json", {}).get("name") == "2.2.2.2-31":
            return MockResponse("create_object_ipv4_cidr", 200)
        if kwargs and kwargs.get("json", {}).get("name") == "123:45:6::0-127":
            return MockResponse("create_object_ipv6_cidr", 200)
        raise Exception("Not implemented")
