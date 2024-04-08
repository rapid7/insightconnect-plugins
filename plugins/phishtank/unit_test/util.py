import json
import os
import sys
import logging

import insightconnect_plugin_runtime
from komand_phishtank.connection.connection import Connection
from komand_phishtank.connection.schema import Input

sys.path.append(os.path.abspath("../"))


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {Input.CREDENTIALS: {"secretKey": "phishtank-secret-key"}}
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
        url = kwargs.get("data").get("url")

        if url == "https%3A//cielobbfidelidade.xyz/home/":
            return MockResponse(200, "check.resp")
        # error handling
        if url == "https%3A//miraclecamstudio.com/":
            return MockResponse(403, "check_error.json.resp")
        if url == "https%3A//postmn.top/kUquEi/":
            return MockResponse(400, "check_error.json.resp")
        if url == "https%3A//hypevision.online/SBB/index/":
            return MockResponse(401, "check_error.json.resp")
        if url == "https%3A//dzaxcbngj.blogspot.com/":
            return MockResponse(404, "check_error.json.resp")
        if url == "https%3A//dbmobile-online.app/":
            return MockResponse(429, "check_error.json.resp")
        if url == "https%3A//telegram.webcsc.xyz/":
            return MockResponse(500, "check_error.json.resp")
        if url == "https%3A//yahoocurrentlyattmail.urest.org/":
            return MockResponse(422, "check_error.json.resp")
        if url == "https%3A//returns_zero_data":
            return MockResponse(409, "check_error.json.resp")
        raise NotImplementedError("Not Implemented", kwargs)


class MockResponse:
    def __init__(self, status_code: int, filename: str = None, headers: dict = {}):
        self.status_code = status_code
        self.text = ""
        self.headers = headers
        if filename:
            self.text = Util.read_file_to_string(f"response/{filename}")
            self.content = bytes(Util.read_file_to_string(f"response/{filename}"), "utf-8")

    def json(self):
        return json.loads(self.text)
