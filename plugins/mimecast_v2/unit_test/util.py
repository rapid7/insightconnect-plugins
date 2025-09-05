import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

import gzip
from io import BytesIO

from icon_mimecast_v2.connection.connection import Connection
from icon_mimecast_v2.connection.schema import Input
from icon_mimecast_v2.util.constants import BASE_URL
from requests.exceptions import HTTPError

STUB_CONNECTION = {
    Input.CLIENT_ID: {"secretKey": "test"},
    Input.CLIENT_SECRET: {"secretKey": "test"},
}


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(connect_params if connect_params else STUB_CONNECTION)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename),
            "r",
            encoding="utf-8",
        ) as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_bytes(filename: str) -> bytes:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "rb") as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_dict(filename: str) -> dict:
        return json.loads(Util.read_file_to_string(filename))

    @staticmethod
    def mocked_request(*args, **kwargs):
        class MockResponse:
            def __init__(
                self,
                status_code: int,
                filename: str = None,
                url: str = None,
                gzip=False,
            ):
                self.filename = filename
                self.status_code = status_code
                self.text = "This is some error text"
                self.headers = {}
                self.url = url
                self.gzip = gzip
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}.json.resp")
                if gzip:
                    self.content = self._gzip_compress(self.text)

            def _gzip_compress(self, data):
                """Compress content using gzip."""
                buf = BytesIO()  # Create a buffer to hold the gzipped content
                with gzip.GzipFile(fileobj=buf, mode="wb") as f:
                    f.write(data.encode("utf-8"))  # Write the string data to gzip (must be bytes)
                return buf.getvalue()

            def iter_content(self, chunk_size: int = 8192):
                for index in range(0, len(self.content), chunk_size):
                    yield self.content[index : index + chunk_size]

            def json(self):
                return json.loads(self.text)

            def raise_for_status(self):
                if self.status_code == 200:
                    return
                raise HTTPError("Bad response", response=self)

        # Connection endpoints
        if args[0].url == f"{BASE_URL}oauth/token":
            return MockResponse(200, "authenticate")

        if (
            args[0].url
            == f"{BASE_URL}siem/v1/batch/events/cg?type=receipt&dateRangeStartsAt=2000-01-07&dateRangeEndsAt=2000-01-07&pageSize=1"
        ):
            return MockResponse(
                403 if kwargs.get("type") in ("WARNING_ALL",) else 200,
                "monitor_siem_logs_batch",
            )

        # SIEM Logs endpoints
        if args[0].url in [
            f"{BASE_URL}siem/v1/batch/events/cg?type=receipt&dateRangeStartsAt=2000-01-06&dateRangeEndsAt=2000-01-06&pageSize=100",
            f"{BASE_URL}siem/v1/batch/events/cg?type=url+protect&dateRangeStartsAt=2000-01-06&dateRangeEndsAt=2000-01-06&pageSize=100",
            f"{BASE_URL}siem/v1/batch/events/cg?type=attachment+protect&dateRangeStartsAt=2000-01-06&dateRangeEndsAt=2000-01-06&pageSize=100",
            f"{BASE_URL}siem/v1/batch/events/cg?type=receipt&dateRangeStartsAt=2000-01-06&dateRangeEndsAt=2000-01-06&pageSize=100&nextPage=NDU1NA%3D%3D",
            f"{BASE_URL}siem/v1/batch/events/cg?type=url+protect&dateRangeStartsAt=2000-01-06&dateRangeEndsAt=2000-01-06&pageSize=100&nextPage=NDU1NA%3D%3D",
            f"{BASE_URL}siem/v1/batch/events/cg?type=attachment+protect&dateRangeStartsAt=2000-01-06&dateRangeEndsAt=2000-01-06&pageSize=100&nextPage=NDU1NA%3D%3D",
            f"{BASE_URL}siem/v1/batch/events/cg?type=attachment+protect&dateRangeStartsAt=2000-01-07&dateRangeEndsAt=2000-01-07&pageSize=100",
            f"{BASE_URL}siem/v1/batch/events/cg?type=receipt&dateRangeStartsAt=2000-01-07&dateRangeEndsAt=2000-01-07&pageSize=100",
            f"{BASE_URL}siem/v1/batch/events/cg?type=url+protect&dateRangeStartsAt=2000-01-07&dateRangeEndsAt=2000-01-07&pageSize=100",
            f"{BASE_URL}siem/v1/batch/events/cg?type=attachment+protect&dateRangeStartsAt=1999-12-31&dateRangeEndsAt=1999-12-31&pageSize=1",
            f"{BASE_URL}siem/v1/batch/events/cg?type=receipt&dateRangeStartsAt=1999-12-31&dateRangeEndsAt=1999-12-31&pageSize=1",
            f"{BASE_URL}siem/v1/batch/events/cg?type=url+protect&dateRangeStartsAt=1999-12-31&dateRangeEndsAt=1999-12-31&pageSize=1",
            "https://api.services.mimecast.com/siem/v1/batch/events/cg?type=attachment+protect&dateRangeStartsAt=1999-12-30&dateRangeEndsAt=1999-12-30&pageSize=100&nextPage=NDU1NA%3D%3D",
            "https://api.services.mimecast.com/siem/v1/batch/events/cg?type=receipt&dateRangeStartsAt=1999-12-30&dateRangeEndsAt=1999-12-30&pageSize=100&nextPage=NDU1NA%3D%3D",
            "https://api.services.mimecast.com/siem/v1/batch/events/cg?type=url+protect&dateRangeStartsAt=1999-12-30&dateRangeEndsAt=1999-12-30&pageSize=100&nextPage=NDU1NA%3D%3D",
        ]:
            return MockResponse(200, "monitor_siem_logs_batch")
        if args[0].url in [
            f"{BASE_URL}siem/v1/batch/events/cg?type=receipt&dateRangeStartsAt=2000-01-03&dateRangeEndsAt=2000-01-03&pageSize=100",
            f"{BASE_URL}siem/v1/batch/events/cg?type=attachment+protect&dateRangeStartsAt=2000-01-03&dateRangeEndsAt=2000-01-03&pageSize=100",
            f"{BASE_URL}siem/v1/batch/events/cg?type=url+protect&dateRangeStartsAt=2000-01-03&dateRangeEndsAt=2000-01-03&pageSize=100",
        ]:
            return MockResponse(200, "monitor_siem_logs_batch_duplicates")
        if args[0].url in [
            "https://api.services.mimecast.com/siem/v1/batch/events/cg?type=attachment+protect&dateRangeStartsAt=1999-12-31&dateRangeEndsAt=1999-12-31&pageSize=1&nextPage=KDU1NA%3D%3D",
            "https://api.services.mimecast.com/siem/v1/batch/events/cg?type=receipt&dateRangeStartsAt=1999-12-31&dateRangeEndsAt=1999-12-31&pageSize=1&nextPage=KDU1NA%3D%3D",
            "https://api.services.mimecast.com/siem/v1/batch/events/cg?type=url+protect&dateRangeStartsAt=1999-12-31&dateRangeEndsAt=1999-12-31&pageSize=1&nextPage=KDU1NA%3D%3D",
        ]:
            return MockResponse(200, "monitor_siem_logs_batch_additional")
        if (
            args[0].url
            == f"{BASE_URL}siem/v1/batch/events/cg?type=receipt&dateRangeStartsAt=2000-01-05&dateRangeEndsAt=2000-01-05&pageSize=100&nextPage=JDU1NA%3D%3D"
        ):
            return MockResponse(200, "monitor_siem_logs_batch_to_invalid_json")
        if (
            args[0].url
            == f"{BASE_URL}siem/v1/batch/events/cg?type=receipt&dateRangeStartsAt=2000-01-02&dateRangeEndsAt=2000-01-02&pageSize=100"
        ):
            return MockResponse(401, "monitor_siem_logs_error")
        if (
            args[0].url
            == f"{BASE_URL}siem/v1/batch/events/cg?type=receipt&dateRangeStartsAt=2000-01-04&dateRangeEndsAt=2000-01-04&pageSize=100"
        ):
            return MockResponse(401, "monitor_siem_logs_json_error")
        if (
            args[0].url
            == f"{BASE_URL}siem/v1/batch/events/cg?type=receipt&dateRangeStartsAt=2000-01-05&dateRangeEndsAt=2000-01-05&pageSize=100"
        ):
            raise AttributeError
        if args[0].url == "https://example.com/":
            return MockResponse(200, "monitor_siem_logs", gzip=True)
        if args[0].url == "https://exampleadditional.com/":
            return MockResponse(200, "monitor_siem_logs_additional", gzip=True)
        if args[0].url == "https://invalidjson.com/":
            return MockResponse(200, "monitor_siem_logs_json_error", gzip=True)

        # TTP Logs endpoints
        if args[0].url == f"{BASE_URL}api/ttp/impersonation/get-logs":
            return MockResponse(
                (403 if kwargs.get("type") in ("WARNING_ALL", "WARNING_TTP_IMPERSONATION") else 200),
                "get_impersonation_logs",
            )
        elif args[0].url == f"{BASE_URL}api/ttp/attachment/get-logs":
            return MockResponse(
                (403 if kwargs.get("type") in ("WARNING_ALL", "WARNING_TTP_ATTACHMENT") else 200),
                "get_attachment_logs",
            )
        elif args[0].url == f"{BASE_URL}api/ttp/url/get-logs":
            if kwargs.get("type") in ("PAGINATION",):
                if "EXAMPLE_TOKEN" in args[0].body.decode():
                    return MockResponse(200, "get_url_logs_pagination_page_2")
                return MockResponse(200, "get_url_logs_pagination")
            return MockResponse(
                (403 if kwargs.get("type") in ("WARNING_ALL", "WARNING_TTP_URL") else 200),
                "get_url_logs",
            )

        raise Exception("Not implemented mock response.")
