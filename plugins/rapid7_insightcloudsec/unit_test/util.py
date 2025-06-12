import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

from icon_rapid7_insightcloudsec.connection.connection import Connection
from icon_rapid7_insightcloudsec.connection.schema import Input
import json


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.APIKEY: {"secretKey": "api_key"},
            Input.URL: "https://example.com",
            Input.SSLVERIFY: True,
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
                self.text = None

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(
                            os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp"
                        )
                    )
                )

        if kwargs.get("url") == "https://example.com/v2/public/resource/common/search" and kwargs.get("json", {}) == {
            "limit": "some_string",
            "offset": "another_string",
            "search_string": 1,
        }:
            return MockResponse("get_resource_id", 400)
        if kwargs.get("url") == "https://example.com/v2/public/resource/common/search":
            return MockResponse("get_resource_id", 200)
        if kwargs.get("url") == "https://example.com/v2/public/resource/instance:123:example:i-1234567890:/tags/list":
            return MockResponse("list_resource_tags", 200)
        if kwargs.get("url") == "https://example.com/v2/public/resource/instance:123:not_found:i-1234567890:/tags/list":
            return MockResponse("not_found", 404)
        if kwargs.get("json") == {"organization_name": "Example Organization"}:
            return MockResponse("empty_response", 200)
        if kwargs.get("json") == {"organization_name": "Invalid Organization"}:
            return MockResponse("not_found", 500)
        if kwargs.get("url") == "https://example.com/v2/public/resource/serviceuser:1:ABC1234567890:/detail":
            return MockResponse("get_resource_details", 200)
        if kwargs.get("url") == "https://example.com/v2/public/resource/serviceuser:1:invalid:/detail":
            return MockResponse("not_found", 404)
        if (
            kwargs.get("url")
            == "https://example.com/v2/public/servicegroup:123:1234567890:/policy/servicepolicy:123:1234567890:/detach"
        ):
            return MockResponse("empty_response", 200)
        if (
            kwargs.get("url")
            == "https://example.com/v2/public/servicegroup:123:invalid:/policy/servicepolicy:123:1234567890:/detach"
        ):
            return MockResponse("not_found", 404)
        if (
            kwargs.get("url")
            == "https://example.com/v2/public/servicegroup:123:1234567890:/policy/servicepolicy:123:invalid:/detach"
        ):
            return MockResponse("not_found", 404)
        if kwargs.get("json", {}).get("insight_id") == 98765:
            return MockResponse("insight_not_found", 500)
        if kwargs.get("json", {}).get("resource_ids", []) == ["storagecontainer:123:us-east-1:123456789:"]:
            return MockResponse("create_exemption", 200)
        if kwargs.get("json", {}).get("resource_ids", []) == [
            "storagecontainer:123:us-east-1:123456789:",
            "storagecontainer:123:us-east-1:987654321:",
        ]:
            return MockResponse("create_exemption_few_resources", 200)
        if kwargs.get("json", {}).get("resource_ids", []) == ["storagecontainer:123:us-east-1:111111111:"]:
            return MockResponse("create_exemption_2", 200)
        if kwargs.get("json") == {"exemption_ids": [111]}:
            return MockResponse("empty_response", 200)
        if kwargs.get("json") == {"exemption_ids": [111, 222]}:
            return MockResponse("empty_response", 200)
        if kwargs.get("json") == {"exemption_ids": [333]}:
            return MockResponse("not_found", 404)
        if kwargs.get("url") == "https://example.com/v2/public/clouds/list" and kwargs.get("json", {}).get(
            "filters"
        ) == [
            {
                "field_name": "account_id",
                "filter_type": "NOT",
                "filter_value": "463792522299",
                "filter_list_value": ["account_id"],
            }
        ]:
            return MockResponse("list_clouds", 200)
        raise Exception("Not implemented")
