import json
import logging
import sys
import os

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
                        self.text = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                return json.loads(self.text)

        params = kwargs.get("params", {})
        data = kwargs.get("data", {})
        url = kwargs.get("url", "")
        method = kwargs.get("method", "")

        if url == "https://login.salesforce.com/services/oauth2/token":
            if data.get("client_id") == "invalid-client-id":
                return MockResponse(401)
            return MockResponse(200, "get_token.json.resp")
        if url == "https://example.com/services/data/":
            return MockResponse(200, "get_version.json.resp")

        if method == "POST":
            if url == "https://example.com/services/data/v58.0/sobjects/Topic":
                return MockResponse(400)
            if url == "https://example.com/services/data/v58.0/sobjects/Quote":
                return MockResponse(400)
            if url == "https://example.com/services/data/v58.0/sobjects/invalid_object_name":
                return MockResponse(404)
            if url == "https://example.com/services/data/v58.0/sobjects/Account":
                return MockResponse(201, "create_record_success_account.json.resp")
            if url == "https://example.com/services/data/v58.0/sobjects/Document":
                return MockResponse(201, "create_record_success_document.json.resp")

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
                if params == {"start": "2023-07-19T16:21:15.340+00:00", "end": "2023-07-20T16:21:15.340+00:00"}:
                    return MockResponse(200, "get_updated_users.json.resp")
                if params == {"start": "2023-07-20T16:15:15.340+00:00", "end": "2023-07-20T16:21:15.340+00:00"}:
                    return MockResponse(200, "get_updated_users.json.resp")
                if params == {"start": "2023-07-20T16:10:15.340+00:00", "end": "2023-07-20T16:21:15.340+00:00"}:
                    return MockResponse(200, "get_updated_users_empty.json.resp")
                if params == {"start": "invalid", "end": "2023-07-20T16:21:15.340+00:00"}:
                    return MockResponse(400)
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
                    return MockResponse(200, "get_fields_1.json.resp")
                if params == {"fields": "Name"}:
                    return MockResponse(200, "get_fields_2.json.resp")
                if params == {"fields": "id,Name,deScription,ParentId"}:
                    return MockResponse(200, "get_fields_3.json.resp")
                if params == {"fields": "invalid"}:
                    return MockResponse(400)
            if url == "https://example.com/services/data/v58.0/query":
                if params == {
                    "q": "SELECT Id, FirstName, LastName, Email, Alias, IsActive FROM User WHERE Id = '005Hn00000HVWwxIAH' AND UserType = 'Standard'"
                }:
                    return MockResponse(200, "get_specific_user.json.resp")
                if params == {
                    "q": "SELECT Id, FirstName, LastName, Email, Alias, IsActive FROM User WHERE UserType = 'Standard'"
                }:
                    return MockResponse(200, "get_users.json.resp")
                if params == {
                    "q": "SELECT LoginTime, UserId, LoginType, LoginUrl, SourceIp, Status, Application, Browser FROM LoginHistory WHERE LoginTime >= 2023-07-19T16:21:15.340262+00:00 AND LoginTime < 2023-07-20T16:21:15.340262+00:00"
                }:
                    return MockResponse(200, "get_login_history.json.resp")
                if params == {
                    "q": "SELECT LoginTime, UserId, LoginType, LoginUrl, SourceIp, Status, Application, Browser FROM LoginHistory WHERE LoginTime >= 2023-07-20T15:21:15.340262+00:00 AND LoginTime < 2023-07-20T16:21:15.340262+00:00"
                }:
                    return MockResponse(200, "get_login_history.json.resp")
                if params == {
                    "q": "SELECT LoginTime, UserId, LoginType, LoginUrl, SourceIp, Status, Application, Browser FROM LoginHistory WHERE LoginTime >= 2023-07-20T14:21:15.340262+00:00 AND LoginTime < 2023-07-20T16:21:15.340262+00:00"
                }:
                    return MockResponse(200, "get_login_history_empty.json.resp")
                if params == {"q": "SELECT FIELDS(STANDARD) FROM Folder"}:
                    return MockResponse(200, "advanced_search_all.json.resp")
                if params == {"q": "SELECT FIELDS(STANDARD) FROM Account WHERE Name='Example Account'"}:
                    return MockResponse(200, "advanced_search_by_name.json.resp")
                if params == {"q": "SELECT FIELDS(STANDARD) FROM Account WHERE Name='Test'"}:
                    return MockResponse(200, "advanced_search_first_page.json.resp")
                if params == {"q": "SELECT FIELDS(STANDARD) FROM Account WHERE Name='Empty'"}:
                    return MockResponse(200, "advanced_search_empty.json.resp")
                if params == {"q": "SELECT LastName FROM Contact LIMIT=10"}:
                    return MockResponse(400)
            if url == "https://example.com/services/data/v58.0/query/01gRO0000012345678-500":
                return MockResponse(200, "advanced_search_second_page.json.resp")
            if url == "https://example.com/services/data/v58.0/query/01gRO0000087654321-500":
                return MockResponse(200, "get_users_next_page.json.resp")
            if url == "https://example.com/services/data/v58.0/query/02cS10000087654321-500":
                return MockResponse(200, "get_login_history_next_page.json.resp")

            if url == "https://example.com/services/data/v58.0/parameterizedSearch":
                if params.get("q") == "test":
                    return MockResponse(200, "simple_search_valid_text.json.resp")
                if params.get("q") == "":
                    return MockResponse(400)
            if url == "https://example.com/services/data/v58.0/sobjects/Folder/00lHn000002nFolder":
                return MockResponse(200, "get_record_valid.json.resp")
            if url == "https://example.com/services/data/v58.0/sobjects/Folder/NOT_FOUND/00lHn00000not_found":
                return MockResponse(404)

        raise NotImplementedError("Not implemented", kwargs)
