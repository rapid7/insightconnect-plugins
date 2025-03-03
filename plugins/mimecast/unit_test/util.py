import json
import logging
import os.path
import sys
from io import BytesIO
from zipfile import ZipFile

sys.path.append(os.path.abspath("../"))
from komand_mimecast.connection import Connection
from komand_mimecast.connection.schema import Input
from komand_mimecast.util.constants import API, DATA_FIELD


FILE_ZIP_CONTENT_1 = {"acc": "ABC123", "datetime": "2022-01-01T12:00:00"}
FILE_ZIP_CONTENT_2 = {"acc": "ABC1234", "datetime": "2022-01-01T12:00:00"}
FILE_ZIP_CONTENT_3 = {"acc": "ABC12345"}
SIEM_LOGS_HEADERS_RESPONSE = {"mc-siem-token": "token123"}


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.CLIENT_ID: {"secretKey": "test"},
                Input.CLIENT_SECRET: {"secretKey": "test"},
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def load_json(filename):
        with open((os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))) as file:
            return json.loads(file.read())

    @staticmethod
    def get_mocked_zip_json_decode_error(path_traversal=False):
        zip_file = BytesIO()
        with ZipFile(zip_file, "w") as myzip:
            filename = get_filename("0", path_traversal)
            myzip.writestr(filename, """{type": "MTA", "data": '}""")
        return zip_file.getvalue()

    @staticmethod
    def get_mocked_zip(path_traversal=False):
        file_contents = [
            {"type": "MTA", "data": [FILE_ZIP_CONTENT_1]},
            {"type": "MTA", "data": [FILE_ZIP_CONTENT_2]},
            {"type": "MTA", "data": [FILE_ZIP_CONTENT_3]},
        ]
        zip_file = BytesIO()
        with ZipFile(zip_file, "w") as myzip:
            for i, content in enumerate(file_contents):
                filename = get_filename(i, path_traversal)
                myzip.writestr(filename, json.dumps(content))
        return zip_file.getvalue()

    @staticmethod
    def mocked_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename: str = None):
                self.filename = filename

            def json(self):
                return Util.load_json(f"responses/{self.filename}")

            @property
            def status_code(self):
                return 200

        class MockResponseZip:
            def __init__(self, status_code, content, headers, json, text=""):
                self.status_code = status_code
                self.content = content
                self.headers_value = headers
                self.json_value = json
                self.text = text

            @property
            def headers(self):
                return self.headers_value

            def json(self):
                return json.loads(self.json_value)

        if kwargs.get("url") == f"{API}/oauth/token":
            return MockResponse(200, "authenticate.json.resp")
        if kwargs.get("url") == f"{API}/api/directory/add-group-member":
            if "test4@rapid7.com" in kwargs.get(DATA_FIELD):
                return MockResponse("add_group_member.json.resp")
            elif "bad@rapid7.com" in kwargs.get(DATA_FIELD):
                return MockResponse("add_group_member_bad.json.resp")
        elif kwargs.get("url") == f"{API}/api/policy/blockedsenders/create-policy":
            if "some test policy" in kwargs.get(DATA_FIELD):
                return MockResponse("create_blocked_sender_policy.json.resp")
        elif kwargs.get("url") == f"{API}/api/policy/blockedsenders/delete-policy":
            if "1234" in kwargs.get(DATA_FIELD):
                return MockResponse("delete_blocked_sender_policy.json.resp")
            else:
                return MockResponse("delete_blocked_sender_policy_bad.json.resp")
        elif kwargs.get("url") == f"{API}/api/message-finder/search":
            return MockResponse("search_message_tracking.json.resp")
        elif kwargs.get("url") == f"{API}/api/ttp/url/create-managed-url":
            if "https://www.test.net/" in kwargs.get(DATA_FIELD):
                return MockResponse("create_managed_url.json.resp")
            if "https://www.bad.net/" in kwargs.get(DATA_FIELD):
                return MockResponse("create_managed_url_bad.json.resp")
        elif kwargs.get("url") == f"{API}/api/ttp/url/decode-url":
            if "https://protect-xx.mimecast.com/" in kwargs.get(DATA_FIELD):
                return MockResponse("decode_url.json.resp")
        elif kwargs.get("url") == f"{API}/api/directory/remove-group-member":
            if "test4@rapid7.com" in kwargs.get(DATA_FIELD):
                return MockResponse("delete_group_member.json.resp")
            elif "bad@rapid7.com" in kwargs.get(DATA_FIELD):
                return MockResponse("delete_group_member_bad.json.resp")
        elif kwargs.get("url") == f"{API}/api/ttp/url/delete-managed-url":
            if "wOi3MCwjYFYhZfkYlp2RMAhvN30QSmqOT7D-I9Abwlmy7ZH7eCwvY3I" in kwargs.get(DATA_FIELD):
                return MockResponse("delete_managed_url.json.resp")
            elif "bad_id" in kwargs.get(DATA_FIELD):
                return MockResponse("delete_managed_url_bad.json.resp")
        elif kwargs.get("url") == f"{API}/api/directory/find-groups":
            if "test_query" in kwargs.get(DATA_FIELD):
                return MockResponse("find_groups_empty_groups.json.resp")
            elif "500" in kwargs.get(DATA_FIELD):
                return MockResponse("find_groups_500.json.resp")
            elif "403" in kwargs.get(DATA_FIELD):
                return MockResponse("find_groups_403.json.resp")
            elif "404" in kwargs.get(DATA_FIELD):
                return MockResponse("find_groups_404.json.resp")
            else:
                return MockResponse("find_groups.json.resp")
        elif kwargs.get("url") == f"{API}/api/audit/get-audit-events":
            return MockResponse("get_audit_events.json.resp")
        elif kwargs.get("url") == f"{API}/api/ttp/url/get-all-managed-urls":
            if "test_domain" in kwargs.get(DATA_FIELD):
                return MockResponse("get_managed_url_empty_response.json.resp")
            else:
                return MockResponse("get_managed_url.json.resp")
        elif kwargs.get("url") == f"{API}/api/ttp/url/get-logs":
            return MockResponse("get_ttp_url_logs.json.resp")
        elif kwargs.get("url") == f"{API}/api/managedsender/permit-or-block-sender":
            if "permit" in kwargs.get(DATA_FIELD):
                return MockResponse("permit_or_block_sender.json.resp")
            elif "block" in kwargs.get(DATA_FIELD):
                if "bad_email" in kwargs.get(DATA_FIELD):
                    return MockResponse("permit_or_block_sender_bad.json.resp")
                else:
                    return MockResponse("block_sender.json.resp")
        return "Not implemented"


def get_filename(i, path_traversal):
    return f"filename-{i}-from-mimecast.json" if not path_traversal else f"../filename-{i}-from-mimecast.json"
