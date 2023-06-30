import json
import logging
import os
import sys
from komand_vmray.connection.connection import Connection
from komand_vmray.connection.schema import Input
from typing import Callable
import requests
from unittest import mock

sys.path.append(os.path.abspath("../"))


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.URL: "https://www.example.com",
                Input.API_KEY: {"secretKey": "abc"}
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
    def load_data(filename, path="payloads"):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"{path}/{filename}.json.resp")
            )
        )

    def mocked_request(side_effect: Callable) -> None:
        mock_function = requests
        mock_function.request = mock.Mock(side_effect=side_effect)

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
                    self.text = str(self.json())

            def json(self):
                return Util.load_data(self.filename)

            def raise_for_status(self):
                return

        logging.info("MOCKING...")

        logging.info("PREPARED REQUEST:")
        logging.info(f"URL: {args[0].url}")
        url = args[0].url
        if url == "https://www.example.com/rest/analysis":
            return MockResponse("get_analysis_all", 200)
        if url == "https://www.example.com/rest/analysis/submission/1490045":
            return MockResponse("get_analysis_submission", 200)
        if url == "https://www.example.com/rest/analysis/1490045":
            return MockResponse("get_analysis_id", 200)
        if url == "https://www.example.com/rest/analysis/submission/1490045":
            return MockResponse("get_analysis_submission", 200)
        if url == "https://www.example.com/rest/analysis/405":
            return MockResponse("get_analysis_405", 405)
        if url == "https://www.example.com/rest/analysis/401":
            return MockResponse("get_analysis_401", 401)
        raise Exception("Not implemented")
