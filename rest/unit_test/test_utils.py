import sys
import os
from komand_rest.util.util import *

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
import logging


class MockResponse():
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
        self.text = "This is some error text"

    def json(self):
        return json.loads(json.dumps(self.json_data))

# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    payload = [{"key":"value"}]

    if args[0] == 'get':
        if args[1] == 'www.google.com/':
            return MockResponse(payload, 200)

    print(f"mocked_requests_get failed looking for: {args[0]}")
    return MockResponse(None, 404)

class TestUtil(TestCase):

    @mock.patch('requests.request', side_effect=mocked_requests_get)
    def test_get_non_object(self, mock_get):
        log = logging.getLogger("Test")
        api = RestAPI("www.google.com", log, False, {})

        actual = api.call_api("get", "/", None, None, None)
        expected = [{'key': 'value'}]
        self.assertEqual(actual.json(), expected)

    def test_body_object(self):
        common = Common()

        test_response = MockResponse([{"key":"value"}], 200)
        actual = common.body_object(test_response)
        expected = {"object":[{"key":"value"}]}

        self.assertEqual(actual, expected)


