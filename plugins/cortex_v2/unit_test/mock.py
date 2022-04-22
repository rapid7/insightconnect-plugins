import os
import json
import logging
from icon_cortex_v2.connection import Connection
from icon_cortex_v2.connection.schema import Input


class MockResponse:
    def __init__(self, file_name="", status_code: int = 0, content=None):
        self.file_name = file_name
        self.status_code = status_code
        self.content = content

    @staticmethod
    def read_file_to_string(file_name):
        with open(file_name) as file_descriptor:
            return file_descriptor.read()

    def json(self):
        return json.loads(self.read_file_to_string(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"resources/{self.file_name}.json.resp")
        ))
        # return {"status_code": self.status_code, "content": self.content}


class Mock:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.API_KEY: {"secretKey": ""},
            Input.PROTOCOL: "HTTP",
            Input.HOST: "0.0.0.0",
            Input.PORT: 9999,
            Input.VERIFY: False,
        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def mocked_request(method: str, path: str, headers, json, params, proxies, verify=False):
        endpoint = path.split("/", 4)[-1]
        if method == "GET":
            if endpoint == "status":
                return MockResponse(status_code=200, content='{"versions":{"Cortex":"1.1.4"},"config":{"authType":"none"}}')
            elif endpoint == "analyzer":
                return MockResponse(status_code=200, file_name="get_analyzers")
            elif endpoint == "analyzer/VirusTotal_GetReport_3_0":
                return MockResponse(status_code=200, file_name="get_analyzer")
            elif endpoint == "analyzer/type/domain":
                return MockResponse(status_code=200, file_name="get_analyzer_by_type")
            elif endpoint == "job":
                return MockResponse(status_code=200, file_name="get_jobs")
            elif endpoint == "job/02pxZ35f7bX4Lnij":
                return MockResponse(status_code=200, file_name="get_job_details")
            elif endpoint == "job/02pxZ35f7bX4Lnij/report":
                return MockResponse(status_code=200, file_name="get_job_report")
        elif method == "POST":
            if endpoint == "analyzer/VirusTotal_GetReport_3_0/run":
                pass
        elif method == "DELETE":
            if endpoint == "job/02pxZ35f7bX4Lnij":
                return MockResponse(status_code=200)
        else:
            raise Exception("Not implemented")
