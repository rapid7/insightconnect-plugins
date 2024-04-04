import json
import requests
import sys
import os

sys.path.append(os.path.abspath("../"))


class Util:
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
        comments = kwargs.get("files", {}).get("comments")
        print(comments)
        if comments == (None, "success"):
            return MockResponse(200, "submit_success.json.resp")
        if comments == (None, "400"):
            return MockResponse(400, "submit_success.json.resp")
        if comments == (None, "connection"):
            return MockResponse("ConnectionError", "submit_success.json.resp")
        if comments == (None, "redirect"):
            return MockResponse("TooManyRedirects", "submit_success.json.resp")
        if comments == (None, "timeout"):
            return MockResponse("Timeout", "submit_success.json.resp")
        raise NotImplementedError("Not implemented", kwargs)


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

    def raise_for_status(self):
        print(self.status_code)
        if self.status_code == 400:
            raise requests.exceptions.HTTPError("400")
        if self.status_code == "Timeout":
            raise requests.exceptions.Timeout("Timeout")
        if self.status_code == "ConnectionError":
            raise requests.exceptions.ConnectionError("ConnectionError")
        if self.status_code == "TooManyRedirects":
            raise requests.exceptions.TooManyRedirects("TooManyRedirects")
