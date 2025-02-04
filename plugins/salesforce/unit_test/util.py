import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

import insightconnect_plugin_runtime
from komand_salesforce.connection import Connection
from komand_salesforce.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action, params: dict = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if not params:
            params = {
                Input.CLIENTID: "example-client-id",
                Input.CLIENTSECRET: {"secretKey": "example-secret-key"},
                Input.SALESFORCEACCOUNTUSERNAMEANDPASSWORD: {
                    "username": "example-username",
                    "password": "example-password",
                },
                Input.SECURITYTOKEN: {"secretKey": "example-secret-key"},
            }
        default_connection.connect(params)
        action.connection = default_connection
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
                self.content = b""
                if filename:
                    if filename == "bytes":
                        self.content = b"test"
                    else:
                        file_content = Util.read_file_to_string(f"responses/{filename}.json.resp")
                        self.text = file_content
                        self.content = f"{file_content}".encode()

            def json(self):
                return json.loads(self.text)

        params = kwargs.get("params", {})
        data = kwargs.get("data", {})
        url = kwargs.get("url", "")
        method = kwargs.get("method", "")

        if url == "https://bad_domain/services/oauth2/token":
            from requests.exceptions import ConnectionError as DNSError

            raise DNSError()

        if url == "https://login.salesforce.com/services/oauth2/token":
            if data.get("client_id") == "invalid-client-id":
                return MockResponse(400, "invalid_grant")  # returns 400 when failing to get a token.
            if data.get("client_id") == "valid-id-bad-endpoint":
                return MockResponse(503)
            if data.get("client_id") == "invalid-id-for-connection":
                return MockResponse(400, "invalid_client_id")
            if data.get("client_id") == "retry-request":
                return MockResponse(400, "retry_request")
            if data.get("client_id") == "unsupported-grant-type":
                return MockResponse(400, "unsupported_grant_type")
            return MockResponse(200, "get_token")
        if url == "https://example.com/services/data/":
            return MockResponse(200, "get_version")

        if method == "POST":
            if url == "https://example.com/services/data/v58.0/sobjects/Topic":
                return MockResponse(400)
            if url == "https://example.com/services/data/v58.0/sobjects/Quote":
                return MockResponse(400)
            if url == "https://example.com/services/data/v58.0/sobjects/invalid_object_name":
                return MockResponse(404)
            if url == "https://example.com/services/data/v58.0/sobjects/Account":
                return MockResponse(201, "create_record_success_account")
            if url == "https://example.com/services/data/v58.0/sobjects/Document":
                return MockResponse(201, "create_record_success_document")

        if method == "DELETE":
            if url == "https://example.com/services/data/v58.0/sobjects/invalid_object_name/100AA000000aa0aAAA":
                return MockResponse(404)
            if url == "https://example.com/services/data/v58.0/sobjects/Account/200AA000000aa0aAAA":
                return MockResponse(404)
            if url == "https://example.com/services/data/v58.0/sobjects/Account/000AA000000aa0aAAA":
                return MockResponse(204)

        if method == "PATCH":
            if url == "https://example.com/services/data/v58.0/sobjects/Account/000AA000000aa0aAAA":
                return MockResponse(204)
            if url == "https://example.com/services/data/v58.0/sobjects/invalid_object_name/100AA000000aa0aAAA":
                return MockResponse(404)
            if url == "https://example.com/services/data/v58.0/sobjects/Account/200AA000000aa0aAAA":
                return MockResponse(400)
            if url == "https://example.com/services/data/v58.0/sobjects/Account/300AA000000aa0aAAA":
                return MockResponse(404)

        if method == "GET":
            if url == "https://example.com/services/data/v58.0/sobjects/User/updated":
                # all of these query until now - just check the start parameter to determine the mocked resp
                params_start = params.get("start")
                if params_start == "2023-07-20T16:10:15.340+00:00":
                    return MockResponse(200, "get_updated_users_empty")
                elif params_start == "invalid":
                    return MockResponse(400)
                else:
                    return MockResponse(200, "get_updated_users")
            if url == "https://example.com/services/data/v58.0/sobjects/Document/invalid/body":
                return MockResponse(404)
            if url == "https://example.com/services/data/v58.0/sobjects/Invalid/015Hn000002ge67890/body":
                return MockResponse(404)
            if url == "https://example.com/services/data/v58.0/sobjects/Document/empty/body":
                return MockResponse(200)
            if url == "https://example.com/services/data/v58.0/sobjects/Document/015Hn000002ge12345/body":
                return MockResponse(200, "bytes")
            if url == "https://example.com/services/data/v58.0/sobjects/Attachment/015Hn000002ge67890/body":
                return MockResponse(200, "bytes")
            if url == "https://example.com/services/data/v58.0/sobjects/Invalid/001Hn00001uLl12345":
                return MockResponse(404)
            if url == "https://example.com/services/data/v58.0/sobjects/Account/invalid":
                return MockResponse(404)
            if url == "https://example.com/services/data/v58.0/sobjects/Account/001Hn00001uLl12345":
                if params == {"fields": "Id,Name,Description"}:
                    return MockResponse(200, "get_fields_1")
                if params == {"fields": "Name"}:
                    return MockResponse(200, "get_fields_2")
                if params == {"fields": "id,Name,deScription,ParentId"}:
                    return MockResponse(200, "get_fields_3")
                if params == {"fields": "invalid"}:
                    return MockResponse(400)
            if url == "https://example.com/services/data/v58.0/query":
                params_q = params.get("q")
                params_db_table = params_q.split("FROM ")[1].split(" ")[0]
                if params_db_table == "User":
                    if (
                        params_q
                        == "SELECT Id, FirstName, LastName, Email, Alias, IsActive FROM User WHERE UserType = 'Standard' AND LastModifiedDate >= 2023-07-20T16:10:15.340262+00:00 AND LastModifiedDate < 2023-07-20T16:21:15.340262+00:00"
                    ):
                        return MockResponse(200, "get_specific_user_empty")
                    if (
                        params_q
                        == "SELECT Id, FirstName, LastName, Email, Alias, IsActive FROM User WHERE UserType = 'Standard' AND LastModifiedDate >= invalid AND LastModifiedDate < 2023-07-20T16:21:15.340262+00:00"
                    ):
                        return MockResponse(400)
                    if (
                        params_q
                        == "SELECT Id, FirstName, LastName, Email, Alias, IsActive FROM User WHERE UserType = 'Standard'"
                    ):
                        return MockResponse(200, "get_users")
                    return MockResponse(200, "get_specific_user")
                if params_db_table == "LoginHistory":
                    if (
                        params_q
                        == "SELECT LoginTime, UserId, LoginType, LoginUrl, SourceIp, Status, Application, Browser FROM LoginHistory WHERE LoginTime >= 2023-07-20T14:21:15.340262+00:00 AND LoginTime < 2023-07-20T16:21:15.340262+00:00"
                    ):
                        return MockResponse(200, "get_login_history_empty")
                    return MockResponse(200, "get_login_history")
                if params == {"q": "SELECT FIELDS(STANDARD) FROM Folder"}:
                    return MockResponse(200, "advanced_search_all")
                if params == {"q": "SELECT FIELDS(STANDARD) FROM Account WHERE Name='Example Account'"}:
                    return MockResponse(200, "advanced_search_by_name")
                if params == {"q": "SELECT FIELDS(STANDARD) FROM Account WHERE Name='Test'"}:
                    return MockResponse(200, "advanced_search_first_page")
                if params == {"q": "SELECT FIELDS(STANDARD) FROM Account WHERE Name='Empty'"}:
                    return MockResponse(200, "advanced_search_empty")
                if params == {"q": "SELECT LastName FROM Contact LIMIT=10"}:
                    return MockResponse(400)
            if url == "https://example.com/services/data/v58.0/query/01gRO0000012345678-500":
                return MockResponse(200, "advanced_search_second_page")
            if url == "https://example.com/services/data/v58.0/query/01gRO0000087654321-500":
                return MockResponse(200, "get_users_next_page")
            if url == "https://example.com/services/data/v58.0/query/02cS10000087654321-500":
                return MockResponse(200, "get_login_history_next_page")

            if url == "https://example.com/services/data/v58.0/parameterizedSearch":
                if params.get("q") == "test":
                    return MockResponse(200, "simple_search_valid_text")
                if params.get("q") == "":
                    return MockResponse(400)
            if url == "https://example.com/services/data/v58.0/sobjects/Folder/00lHn000002nFolder":
                return MockResponse(200, "get_record_valid")
            if url == "https://example.com/services/data/v58.0/sobjects/Folder/NOT_FOUND/00lHn00000not_found":
                return MockResponse(404)

        raise NotImplementedError("Not implemented", kwargs)
