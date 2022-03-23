import asyncio
import json
import logging
import os

from insightconnect_plugin_runtime.exceptions import PluginException
from icon_rapid7_insightidr.connection import Connection
from icon_rapid7_insightidr.connection.schema import Input
from requests.models import HTTPError


class Meta:
    version = "0.0.0"


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.meta = Meta()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.URL: "https://rapid7.com",
                Input.API_KEY: {"secretKey": "4472f2g7-991z-4w70-li11-7552w8qm0266"},
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
    async def mocked_async_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status = status_code
                self.text = "This is some error text"

            def raise_for_status(self):
                if self.status == 404:
                    raise HTTPError("Not found", response=self)

            async def json(self):
                if self.filename == "error":
                    raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
                if self.filename == "empty":
                    return {}

                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp")
                    )
                )

        if args[0] == "https://rapid7.com/log_search/management/labels/00000000-0000-0000-0000-000000000006":
            return MockResponse("label_006", 200)
        elif args[0] == "https://rapid7.com/log_search/management/labels/00000000-0000-0000-0000-000000000007":
            return MockResponse("label_007", 200)
        elif args[0] == "https://rapid7.com/log_search/management/labels/not exist label - 404":
            return MockResponse("label_404", 404)

        raise Exception("Not implemented")

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                self.text = "This is some error text"

            def raise_for_status(self):
                if self.status_code == 404:
                    raise HTTPError("Not found", response=self)

            def json(self):
                if self.filename == "error":
                    raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
                if self.filename == "empty":
                    return {}

                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp")
                    )
                )

        if args[0] == "https://rapid7.com/log_search/management/logs":
            return MockResponse("logs", 200)
        elif (
            args[0] == "https://rapid7.com/log_search/query/logs/log_id"
            or args[0] == "https://rapid7.com/log_search/query/logsets/log_id"
        ):
            return MockResponse("log_id", 200)
        elif (
            args[0] == "https://rapid7.com/log_search/query/logs/log_id2"
            or args[0] == "https://rapid7.com/log_search/query/logsets/log_id2"
        ):
            return MockResponse("log_id2", 200)
        elif (
            args[0] == "https://rapid7.com/log_search/query/logs/log_id3"
            or args[0] == "https://rapid7.com/log_search/query/logsets/log_id3"
        ):
            return MockResponse("log_id3", 200)
        elif (
            args[0] == "https://rapid7.com/log_search/query/logs/log_id4"
            or args[0] == "https://rapid7.com/log_search/query/logsets/log_id4"
        ):
            return MockResponse("log_id4", 200)
        elif (
            args[0] == "https://rapid7.com/log_search/query/logs/log_id5"
            or args[0] == "https://rapid7.com/log_search/query/logsets/log_id5"
        ):
            return MockResponse("log_id5", 200)
        elif args[0] == "https://rapid7.com/log_search/management/logsets":
            return MockResponse("logsets", 200)

        raise Exception("Not implemented")
