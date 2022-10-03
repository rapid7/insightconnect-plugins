import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightidr.connection import Connection
from komand_rapid7_insightidr.connection.schema import Input
from requests.models import HTTPError


class Meta:
    version = "0.0.0"


class Util:
    STUB_URL_API = "https://us.api.insight.rapid7.com"
    STUB_URL_REST = "https://us.rest.logs.insight.rapid7.com"

    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.meta = Meta()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.REGION: "United States 1",
                Input.API_KEY: {"secretKey": "4472f2g7-991z-4w70-li11-7552w8qm0266"},
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

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

        if args[0] == f"{Util.STUB_URL_API}/log_search/management/labels/00000000-0000-0000-0000-000000000006":
            return MockResponse("label_006", 200)
        elif args[0] == f"{Util.STUB_URL_API}/log_search/management/labels/00000000-0000-0000-0000-000000000007":
            return MockResponse("label_007", 200)
        elif args[0] == f"{Util.STUB_URL_API}/log_search/management/labels/not exist label - 404":
            return MockResponse("label_404", 404)

        raise Exception("Not implemented")

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
                self.text = "This is some error text"
                self.content = None
                if self.filename == "not_found":
                    self.text = "Not found."
                if self.filename == "download_attachment":
                    self.content = b"test"

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

        if kwargs.get("params") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:1234567890",
            "index": 0,
            "size": 0,
        }:
            return MockResponse("invalid_size", 400)
        if kwargs.get("params") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:1234567890",
            "index": 0,
            "size": 1,
        }:
            return MockResponse("list_comments", 200)
        if kwargs.get("params") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:1234567899",
            "index": 0,
            "size": 1,
        }:
            return MockResponse("list_attachments", 200)
        if kwargs.get("params") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:9876543210",
            "index": 0,
            "size": 1,
        }:
            return MockResponse("list_empty", 200)
        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/attachments/rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890/metadata"
        ):
            return MockResponse("get_attachment_information", 200)
        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/attachments/rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:123456789/metadata"
        ):
            return MockResponse("get_attachment_information", 404)
        if kwargs.get("json") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:1234567890",
            "body": "test",
            "attachments": ["rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890"],
        }:
            return MockResponse("create_comment", 200)
        if kwargs.get("json") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:1234567890",
            "body": "test",
            "attachments": [],
        }:
            return MockResponse("create_comment_without_attachment", 200)
        if kwargs.get("json") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:1234567890",
            "body": "",
            "attachments": ["rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890"],
        }:
            return MockResponse("create_comment_without_body", 200)
        if kwargs.get("json") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:not_found",
            "body": "test",
            "attachments": ["rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890"],
        }:
            return MockResponse("create_comment", 404)
        if (
            kwargs.get("method") == "DELETE"
            and kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/comments/rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:comment:not_found"
        ):
            return MockResponse("not_found", 404)
        if (
            kwargs.get("method") == "DELETE"
            and kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/attachments/rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:comment:not_found"
        ):
            return MockResponse("not_found", 404)
        if kwargs.get("method") == "DELETE":
            return MockResponse("success", 204)
        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/attachments/rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890"
        ):
            return MockResponse("download_attachment", 200)
        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/attachments/rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:not_found"
        ):
            return MockResponse("not_found", 404)
        if kwargs.get("files") == {"filedata": ("test.txt", b"test", "text/plain")}:
            return MockResponse("upload_attachment", 200)
        if kwargs.get("files") == {"filedata": ("test", b"test", "text/plain")}:
            return MockResponse("upload_attachment_without_file_extension", 200)
        if args[0] == f"{Util.STUB_URL_API}/log_search/management/logs":
            return MockResponse("logs", 200)
        elif (
            args[0] == f"{Util.STUB_URL_API}/log_search/query/logs/log_id"
            or args[0] == f"{Util.STUB_URL_API}/log_search/query/logsets/log_id"
        ):
            return MockResponse("log_id", 200)
        elif (
            args[0] == f"{Util.STUB_URL_API}/log_search/query/logs/log_id2"
            or args[0] == f"{Util.STUB_URL_API}/log_search/query/logsets/log_id2"
        ):
            return MockResponse("log_id2", 200)
        elif (
            args[0] == f"{Util.STUB_URL_API}/log_search/query/logs/log_id3"
            or args[0] == f"{Util.STUB_URL_API}/log_search/query/logsets/log_id3"
        ):
            return MockResponse("log_id3", 200)
        elif (
            args[0] == f"{Util.STUB_URL_API}/log_search/query/logs/log_id4"
            or args[0] == f"{Util.STUB_URL_API}/log_search/query/logsets/log_id4"
        ):
            return MockResponse("log_id4", 200)
        elif args[0] == f"{Util.STUB_URL_API}/log_search/management/logsets":
            return MockResponse("logsets", 200)

        raise Exception("Not implemented")
