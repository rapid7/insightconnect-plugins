import os
import sys

sys.path.append(os.path.abspath("../"))

import json
import logging
import requests

from icon_palo_alto_cortex_xdr.connection.connection import Connection
from icon_palo_alto_cortex_xdr.connection.schema import Input

from typing import Dict, Any
from unittest.mock import MagicMock


class MockTrigger:
    actual = None

    @staticmethod
    def send(params):
        MockTrigger.actual = params


class MockTask:
    actual = None

    @staticmethod
    def send(params):
        MockTask.actual = params


class Util:
    @staticmethod
    def read_file_to_dict(filename):
        with open(filename, "rt", encoding="utf8"):
            return json.loads(
                Util.read_file_to_string(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))
            )

    @staticmethod
    def read_file_to_string(filename):
        with open(filename, "rt", encoding="utf8") as my_file:
            return my_file.read()

    @staticmethod
    def load_parameters(filename: str) -> Dict[str, Any]:
        return json.loads(
            Util.read_file_to_string(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    f"parameters/{filename}.json.resp",
                )
            )
        )

    @staticmethod
    def load_expected(filename: str) -> Dict[str, Any]:
        return json.loads(
            Util.read_file_to_string(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    f"expected/{filename}.json.exp",
                )
            )
        )

    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.API_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
                Input.API_KEY_ID: "1",
                Input.SECURITY_LEVEL: "Standard",
                Input.URL: "https://example.com/",
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return default_connection, action

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code, url: str = None):
                self.filename = filename
                self.status_code = status_code
                self.text = ""
                self.url = url
                self.request = MagicMock()
                self.headers = MagicMock()
                self.raise_for_status = MagicMock()

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(
                            os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp"
                        )
                    )
                )

            def raise_for_status(self):
                if self.status_code < 200 or self.status_code > 399:
                    raise requests.HTTPError()

        # breakpoint()
        if kwargs.get("url") == "https://example.com/public_api/v1/incidents/get_incidents/":
            return MockResponse("get_incidents", 200)
        if kwargs.get("url") == "connection url":
            return MockResponse("connection", 200)
        if kwargs.get("url") == "https://example.com/public_api/v1/alerts/get_alerts":
            post_body = kwargs.get("post_body").get("request_data")
            if post_body.get("search_from") == 0:
                return MockResponse("monitor_alerts", 200)
            if post_body.get("search_from") == 100:
                return MockResponse("monitor_alerts_two", 200)
            if post_body.get("search_from") == 200:
                return MockResponse("monitor_alerts_three", 200)

        raise Exception("Not implemented")
