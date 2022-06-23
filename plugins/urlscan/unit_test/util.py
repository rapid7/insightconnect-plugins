import json
import os

from komand_urlscan.connection.connection import Connection
from komand_urlscan.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        params = {
            Input.API_KEY: {"secretKey": "some_key"},
        }
        default_connection.connect(params)
        action.connection = default_connection
        return action

    @staticmethod
    def load_json(filename):
        with open((os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))) as file:
            return json.loads(file.read())

    @staticmethod
    def mocked_requests_post(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.status_code = status_code
                self.text = "error message"
                self.filename = filename

            def json(self):
                if self.filename == "json_error":
                    raise json.decoder.JSONDecodeError("json error", "json error", 0)
                return Util.load_json(f"payloads/{self.filename}.json.resp")

        if args[0] == 'https://urlscan.io/api/v1/search/?q=page.domain:"example.com"&size=10000&sort=_score':
            return MockResponse("search_domain", 200)
        if args[0] == 'https://urlscan.io/api/v1/search/?q=page.url: "http://example.com"&size=10000&sort=_score':
            return MockResponse("search_url", 200)
        if args[0] == 'https://urlscan.io/api/v1/search/?q=example*&size=10000&sort=_score':
            return MockResponse("search_domain", 200)
        if args[0] == 'https://urlscan.io/api/v1/search/?q=empty&size=10000&sort=_score':
            return MockResponse("search_empty", 200)
        if args[0] == "https://urlscan.io/api/v1/result/full_objects":
            return MockResponse("get_scan_results", 200)
        elif args[0] == "https://urlscan.io/api/v1/result/empty":
            return MockResponse("get_scan_results_empty_object", 200)
        elif args[0] == "https://urlscan.io/api/v1/result/404":
            return MockResponse("get_scan_results_empty_object", 404)
        elif kwargs.get("data").get("url") == "401":
            return MockResponse("submit_url_for_scan_401", 401)
        elif kwargs.get("data").get("url") == "429":
            return MockResponse("submit_url_for_scan_429", 429)
        elif kwargs.get("data").get("url") == "unexpect":
            return MockResponse("submit_url_for_scan_unexpect", 500)
        elif kwargs.get("data").get("url") == "json_error":
            return MockResponse("json_error", 500)
        elif kwargs.get("data").get("url") == "499":
            return MockResponse("submit_url_for_scan_499", 499)
        elif kwargs.get("data").get("url") == "201":
            return MockResponse("submit_url_for_scan_201", 201)
        return MockResponse("submit_url_for_scan_200", 200)
