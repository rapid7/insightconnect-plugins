from requests import Response
from komand_rest.util.util import Common
from insightconnect_plugin_runtime.exceptions import PluginException
import insightconnect_plugin_runtime
import logging
import json


class MockConnection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        # setup api
        self.api = MockConnectionApi()


class MockConnectionApi:
    """
    Mock connection API to replace the requests library for unit testing
    """

    def __init__(self, fail_on_error=True):
        # setup
        self.fail_on_error = fail_on_error
        pass

    # method signature from the existing connection.api in util.py
    def call_api(
        self, method: str, path: str, data: str = None, json_data: dict = None, headers: dict = None
    ) -> Response:
        # don't use requests here, fill a response object on our own
        response = self.fill_response_obj_test(method, path, data, json_data, headers)
        return response

    def fill_response_obj_test(
        self, method: str, path: str, data: str = None, json_data: dict = None, headers: dict = None
    ) -> MockResponse:

        # when we want a succesful request, use google.com in the test

        if path == "https://www.google.com":
            response = MockResponse({"SampleSuccessBody": "SampleVal"}, 200, "SAMPLETEXT for method " + method)
            response.headers = {"SampleHeader": "SampleVal"}
            return response
        else:
            response = MockResponse({"SampleBodyError": "SampleVal"}, 404, "TRYGOOGLE for method " + method)
            response.headers = {"SampleError": "SampleVal"}
            return response


class MockResponse:
    def __init__(self, json_data, status_code, text):
        self.json_data = json_data
        self.status_code = status_code
        self.text = text
        self.headers = {}

    def json(self):
        if self.status_code == 418:
            raise json.decoder.JSONDecodeError("I am a teapot", "NA", 0)
        return json.loads(json.dumps(self.json_data))
