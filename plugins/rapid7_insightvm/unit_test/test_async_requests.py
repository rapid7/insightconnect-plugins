import os
import sys

sys.path.append(os.path.abspath("../"))

import asyncio
import json
from unittest import TestCase

from komand_rapid7_insightvm.util import async_requests


class MockResponse:
    def __init__(self) -> None:
        self.status = 200

    async def text(self) -> str:
        return '{"test_key": "test_value"}'

    async def json(self):
        return json.loads(await self.text())


class MockSession:
    async def request(self, url, method, **kwargs):
        return MockResponse()


class TestAsyncRequests(TestCase):
    def test_async_request(self) -> None:
        loop = asyncio.new_event_loop()

        asyc_obj = async_requests.AsyncRequests("user", "pass", False)
        session = MockSession()
        test_response = loop.run_until_complete(asyc_obj.async_request(session, "www.google.com"))

        self.assertIsNotNone(test_response)
        self.assertEqual(test_response.get("test_key"), "test_value")
