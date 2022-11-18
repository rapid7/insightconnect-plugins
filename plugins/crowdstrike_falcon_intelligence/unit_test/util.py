import json
import logging
import sys
import os

import insightconnect_plugin_runtime

sys.path.append(os.path.abspath("../"))

from icon_crowdstrike_falcon_intelligence.connection import Connection
from icon_crowdstrike_falcon_intelligence.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action, params=None):
        if not params:
            params = {
                Input.BASEURL: "https://crowdstrike_url",
                Input.CLIENTSECRET: {"secretKey": "my-api-key"},
                Input.CLIENTID: "my_id",
            }
        action.connection = Connection()
        action.connection.meta = "{}"
        action.connection.logger = logging.getLogger("connection logger")
        action.connection.connect(params)
        action.logger = logging.getLogger("action logger")
        return action

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
        class MockResponse:
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                self.text = ""
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                return json.loads(self.text)

        method = kwargs.get("method")
        url = kwargs.get("url")
        json_data = kwargs.get("json", {})
        params = kwargs.get("params", {})

        if url == "https://crowdstrike_url/oauth2/token":
            return MockResponse(201, "auth_token.json.resp")
        if url == "https://crowdstrike_url/falconx/entities/submissions/v1" and method == "GET":
            if params.get("ids")[0].startswith("404"):
                return MockResponse(200, "check_analysis_status_invalid_id.json.resp")
            if len(params.get("ids")) == 1:
                return MockResponse(200, "check_analysis_status.json.resp")
            if len(params.get("ids")) == 5:
                return MockResponse(200, "check_analysis_status_many_ids.json.resp")
        if url == "https://crowdstrike_url/falconx/entities/artifacts/v1" and method == "GET":
            if params.get("id").startswith("404"):
                return MockResponse(500, "")
            else:
                return MockResponse(200, "download_artifact.json.resp")
        if url == "https://crowdstrike_url/falconx/entities/reports/v1" and method == "GET":
            if params.get("ids")[0].startswith("404"):
                return MockResponse(200, "get_full_report_invalid_id.json.resp")
            if len(params.get("ids")) == 1:
                return MockResponse(200, "get_full_report.json.resp")
            if len(params.get("ids")) == 2:
                return MockResponse(200, "get_full_report_many_ids.json.resp")
        if url == "https://crowdstrike_url/falconx/queries/reports/v1" and method == "GET":
            if params.get("filter") == "verdict: 'no verdict'":
                return MockResponse(200, "get_reports_ids.json.resp")
            elif params.get("filter") == "invalid: filter":
                return MockResponse(400, "get_reports_ids_invalid_filter.json.resp")
        if url == "https://crowdstrike_url/falconx/entities/report-summaries/v1" and method == "GET":
            if params.get("ids")[0].startswith("404"):
                return MockResponse(200, "get_short_report_invalid_id.json.resp")
            if len(params.get("ids")) == 1:
                return MockResponse(200, "get_short_report.json.resp")
            if len(params.get("ids")) == 4:
                return MockResponse(200, "get_short_report_many_ids.json.resp")
        if url == "https://crowdstrike_url/falconx/queries/submissions/v1" and method == "GET":
            if params.get("filter") == "state: 'error'":
                return MockResponse(200, "get_submissions_ids.json.resp")
            elif params.get("filter") == "invalid: filter":
                return MockResponse(400, "get_submissions_ids_invalid_filter.json.resp")
        if url == "https://crowdstrike_url/falconx/entities/submissions/v1" and method == "POST":
            return MockResponse(200, "submit_analysis.json.resp")

        raise NotImplementedError("Not implemented", kwargs)
