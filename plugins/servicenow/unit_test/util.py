import json
import logging
import os

from icon_servicenow.connection.connection import Connection
from icon_servicenow.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.INSTANCE: "rapid7",
                Input.CLIENT_LOGIN: {"username": "user1", "password": "mypassword"},
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def read_file_to_bytes(filename):
        with open(filename, "rb") as my_file:
            return my_file.read()

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code, headers=None):
                if headers is None:
                    headers = {"Content-Type": "application/json"}
                self.status_code = status_code
                self.headers = headers
                self.content = Util.read_file_to_bytes(
                    os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.resp")
                )
                self.text = self.content.decode("UTF-8")

            def json(self):
                return json.loads(self.text)

        if kwargs["url"] in [
            "https://rapid7.service-now.com/api/now/attachment/b259f4062d9f78f9ffdd6efd05c492c7/file",
            "https://rapid7.service-now.com/api/now/attachment/52e4a8abb1b66fc04ba11001955e7dcb/file",
            "https://rapid7.service-now.com/api/now/attachment/53e4a8abb1b66fc04ba11001955e7dcb/file",
        ]:
            return MockResponse("get_attachment_file", 200, {})
        elif (
            kwargs["url"]
            == "https://rapid7.service-now.com/api/now/attachment?sysparm_query=table_sys_id=3072d01d07a552f6d0ea83ef29c936be"
        ):
            return MockResponse("get_attachment_by_table_sys_id.json", 200)
        elif (
            kwargs["url"]
            == "https://rapid7.service-now.com/api/now/attachment?sysparm_query=table_sys_id=51e4a8abb1b66fc04ba11001955e7dcb"
        ):
            return MockResponse("get_attachment_by_table_sys_id_many.json", 200)
        elif (
            kwargs["url"]
            == "https://rapid7.service-now.com/api/now/attachment?sysparm_query=table_sys_id=c1565da4456c2df374793d471d6ae8dd"
        ):
            return MockResponse("get_attachment_by_table_sys_id_empty.json", 200)
        elif kwargs["url"] == "https://rapid7.service-now.com/api/sn_chg_rest/v1/change":
            return MockResponse("create_change_request.json", 200)
        elif kwargs["url"] in (
            "https://rapid7.service-now.com/api/now/table/sn_vul_vulnerable_item",
            "https://rapid7.service-now.com/api/now/table/sn_vul_vulnerable_item/12345",
        ):
            return MockResponse("create_vulnerability.json", 201)

        raise Exception("Not implemented")
