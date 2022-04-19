import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

from komand_rapid7_insightvm.connection.connection import Connection
from komand_rapid7_insightvm.connection.schema import Input
import json


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {Input.URL: "https://example.com", Input.CREDENTIALS: {"password": "password", "username": "user"}}
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
                self.text = self.load_data()

            def load_data(self):
                return Util.read_file_to_string(
                    os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp")
                )

            def json(self):
                return json.loads(self.text)

            def raise_for_status(self):
                if 200 <= self.status_code <= 300:
                    pass
                else:
                    raise Exception("Error")

        if kwargs.get("url") == "https://example.com/api/3/reports?page=0&size=10&sort=ASC":
            return MockResponse("list_reports", 200)
        if kwargs.get("url") == "https://example.com/api/3/reports?page=1&size=10&sort=ASC":
            return MockResponse("list_reports_2", 200)
        if kwargs.get("url") == "https://example.com/api/3/assets/1":
            return MockResponse("get_asset", 200)
        if kwargs.get("url") == "https://example.com/api/3/assets/2":
            return MockResponse("get_asset_invalid_id", 404)
        if kwargs.get("url") == "https://example.com/api/3/assets/3":
            return MockResponse("delete_asset", 200)
        if kwargs.get("url") == "https://example.com/api/3/assets/4":
            return MockResponse("delete_asset_invalid_id", 404)
        if kwargs.get("url") == "https://example.com/api/3/sites/1/excluded_targets":
            return MockResponse("get_site_excluded_targets", 200)
        if kwargs.get("url") == "https://example.com/api/3/sites/1/included_targets":
            return MockResponse("get_site_included_targets", 200)
        if kwargs.get("json") == {
            "filters": [{"field": "last-scan-date", "operator": "is-earlier-than", "value": 30}],
            "match": "all",
        }:
            return MockResponse("list_inactive_assets", 200)
        if kwargs.get("json") == {
            "filters": [{"field": "last-scan-date", "operator": "is-earlier-than", "value": 10}],
            "match": "all",
        }:
            return MockResponse("list_inactive_assets_not_found", 200)
        if kwargs.get("json") == "2022-01-01T00:00:00.000000Z":
            return MockResponse("update_vulnerability_exception_expiration_date", 200)
        if kwargs.get("json") == "2022-01-10T00:00:00.000000Z":
            return MockResponse("update_vulnerability_exception_expiration_date_invalid_id", 404)
        if kwargs.get("json", {}).get("scope", {}).get("vulnerability") == "test_vulnerability":
            return MockResponse("create_exception", 200)
        if kwargs.get("params") == [("sort", "expires,ASC")]:
            return MockResponse("get_expiring_vulnerability_exceptions", 200)

        raise Exception("Not implemented")
