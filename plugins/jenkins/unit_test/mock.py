import json
import os
from typing import Callable
from unittest import mock

import requests


class MockResponse:
    def __init__(self, filename: str, status_code: int) -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = json.dumps(self.json())
        self.headers = {"Location": "http://jenkins/queue/item/1/"}

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file_:
            return json.load(file_)


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.request = mock.Mock(side_effect=side_effect)


def mock_conditions(request: requests.Request, status_code: int) -> MockResponse:
    if status_code in (200,):
        if request.url == "http://localhost:8080/job/ExampleName/1/api/json?depth=0":
            return MockResponse("build_info", status_code)
        elif request.url == "http://localhost:8080/job/ExampleName/api/json?depth=0":
            return MockResponse("get_job_info", status_code)
        elif request.url == "http://localhost:8080/job/ExampleName/build":
            return MockResponse("build_job", status_code)
    raise Exception("Response has been not implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 200)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 500)
