import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any
from unittest import TestCase
from unittest.mock import MagicMock

from requests.structures import CaseInsensitiveDict

from icon_whoisfreaks.connection.connection import Connection
from icon_whoisfreaks.connection.schema import Input

API_KEY = "unit-test-api-key-0123456789abcdef"


class MockResponse:
    def __init__(self, status_code: int = 200, body: Any = b"", headers: dict = None):
        if isinstance(body, (dict, list)):
            body = json.dumps(body)
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.status_code = status_code
        self.headers = CaseInsensitiveDict(headers or {})
        self._body = body
        self.closed = False

    def iter_content(self, chunk_size: int = 1):
        for start in range(0, len(self._body), chunk_size):
            yield self._body[start : start + chunk_size]

    def close(self):
        self.closed = True


class FakeSession:
    """Replays queued responses, or raises queued exceptions, and records every request. The last item repeats."""

    def __init__(self, *responses):
        self.queue = list(responses)
        self.calls = []

    def request(self, method, url, **kwargs):
        self.calls.append(dict(kwargs, method=method, url=url))
        item = self.queue.pop(0) if len(self.queue) > 1 else self.queue[0]
        if isinstance(item, BaseException):
            raise item
        return item


def connect(component, *responses) -> FakeSession:
    """Attach a connected Connection whose HTTP session replays the given responses."""
    connection = Connection()
    connection.logger = logging.getLogger("connection")
    connection.connect({Input.API_KEY: {"secretKey": API_KEY}})
    session = FakeSession(*(responses or (MockResponse(200, {}),)))
    connection.client._session = lambda: session
    connection.client._sleep = MagicMock()
    component.connection = connection
    component.logger = logging.getLogger("component")
    return session


class ActionTestCase(TestCase):
    """Runs an action against fake WhoisFreaks responses and validates its output against the output schema."""

    action_class = None

    def run_action(self, params: dict, *responses) -> tuple:
        action = self.action_class()
        session = connect(action, *responses)
        output = action.run(params)
        action.output.validate(output)
        return output, session

    def assert_request(self, session: FakeSession, method: str, path: str, params: dict = None, body: Any = None):
        call = session.calls[-1]
        self.assertEqual(method, call["method"])
        self.assertEqual(f"https://api.whoisfreaks.com{path}", call["url"])
        self.assertEqual(API_KEY, call["headers"]["X-API-KEY"])
        self.assertFalse(call["allow_redirects"])
        self.assertEqual(params, call["params"])
        self.assertEqual(body, call["json"])
        self.assertNotIn(API_KEY, json.dumps(call["params"] or {}))
