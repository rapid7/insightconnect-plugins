import sys
import os
sys.path.append(os.path.abspath('../'))

from komand.exceptions import PluginException
from unittest import TestCase
from komand_rapid7_insightvm.util import async_requests
import requests
import json
import pytest
import asyncio


class MockResponse():

    def __init__(self):
        self.text = '{"resources": [{"thing1": "data"},{"thing2": "data"}], "page": {"number": 0, "totalPages": 2}}'
        self.status_code = 200

    def json(self):
        return json.loads(self.text)


class MockSession():
    def __init__(self):
        self.counter = 0
        self.headers = dict()

    def get(self, url, verify, **kwargs):
        mock_response = MockResponse()
        if url == 'exception.com':
            raise requests.HTTPError

        if url == 'bad password':
            mock_response.status_code = 401
        if url == 'paged_request':
            if self.counter > 0:
                temp = json.loads(mock_response.text)
                temp['page']['number'] += 1
                mock_response.text = json.dumps(temp)
            self.counter += 1

        return mock_response

class TestAsyncRequests(TestCase):

   async def async_helper(self, items):
        test_object = async_requests.AsyncRequests(username='user', password='password')
        async with test_object.get_async_session() as async_session:
            tasks: [asyncio.Future] = []
            for item in items:
                payload = item
                tasks.append(asyncio.ensure_future(test_object.async_request(session=async_session,
                                                                             endpoint='url',payload=payload, method='get')))
    def test_async_resource_request(self):
        items = []
        response = asyncio.run(self.async_helper(items))
        self.assertIsNotNone(response)
        self.assertEqual(response.get('resources'), [{"thing1": "data"}, {"thing2": "data"}])