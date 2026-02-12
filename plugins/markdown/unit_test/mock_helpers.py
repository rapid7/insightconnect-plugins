import json
import os.path
from unittest import mock
from typing import Callable
from unittest.mock import Mock


class MockResponse:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.text = self.json()

    def json(self):
        with open(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                f"responses/{self.filename}.json.resp",
            )
        ) as file:
            return json.load(file)


def mocked_request(side_effect: Callable) -> Mock:
    return mock.Mock(side_effect=side_effect)


def mock_request_markdown_to_pdf(*args):
    return MockResponse("markdown_to_pdf").json()
