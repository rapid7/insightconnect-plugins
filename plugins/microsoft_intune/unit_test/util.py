import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from icon_microsoft_intune.connection.connection import Connection
from icon_microsoft_intune.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action, connect_params: dict = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if not connect_params:
            connect_params = {
                Input.TENANT_ID: "intune_tenant",
                Input.CLIENT_ID: "client_id",
                Input.CLIENT_SECRET: {"secretKey": "client_secret"},
                Input.URL: "https://graph.microsoft.com",
                Input.CREDENTIALS: {"username": "user", "password": "pw"},
            }
        default_connection.connect(connect_params)
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
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                self.text = ""
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                return json.loads(self.text)

        url = args[1] if args else kwargs.get("url")
        data = kwargs.get("data")

        if url == "https://login.microsoftonline.com/intune_tenant/oauth2/v2.0/token":
            if data.get("client_secret") == "client_secret":
                return MockResponse(200, "access_token.json.resp")
        if url == "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices/valid-device-id":
            return MockResponse(200, "get_device.json.resp")
        if url == "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices/invalid-device-id":
            return MockResponse(404)
        if (
            url
            == "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices/valid-device-id/windowsDefenderScan"
        ):
            return MockResponse(204)
        if (
            url
            == "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices/invalid-device-id/windowsDefenderScan"
        ):
            return MockResponse(404)

        if (
            url
            == "https://graph.microsoft.com/v1.0/deviceManagement/windowsAutopilotDeviceIdentities/9e8fd111-6c41-1111-85b9-11395662e111"
        ):
            return MockResponse(200, "get_autopilot_device.json.resp")
        if url == "https://graph.microsoft.com/v1.0/deviceManagement/windowsAutopilotDeviceIdentities/invalid-id":
            return MockResponse(404)

        raise Exception(f"Not implemented: {kwargs}")
