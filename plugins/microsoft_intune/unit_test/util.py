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
                Input.TENANTID: "intune_tenant",
                Input.CLIENTID: "client_id",
                Input.CLIENTSECRET: {"secretKey": "client_secret"},
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
        method = args[0]
        data = kwargs.get("data")
        params = kwargs.get("params")

        if url == "https://login.microsoftonline.com/intune_tenant/oauth2/v2.0/token":
            if data.get("client_secret") == "client_secret":
                return MockResponse(200, "access_token.json.resp")
        if url == "https://graph.microsoft.com/v1.0/deviceAppManagement/mobileApps":
            return MockResponse(200, "get_managed_apps_first_page.json.resp")
        if url == "https://graph.microsoft.com/v1.0/deviceAppManagement/mobileApps?$top=500&$skiptoken=500":
            return MockResponse(200, "get_managed_apps_second_page.json.resp")
        if (
            url
            == "https://graph.microsoft.com/v1.0/deviceAppManagement/mobileApps/9de5069c-5afe-602b-2ea0-a04b66beb2c0"
        ):
            return MockResponse(200, "get_managed_apps_by_id.json.resp")
        if (
            url
            == "https://graph.microsoft.com/v1.0/deviceAppManagement/mobileApps/9de5069c-5afe-602b-2ea0-a04b66beb2c1"
        ):
            return MockResponse(404)
        if (
            url
            == "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices/9de5069c-5afe-602b-2ea0-a04b66beb2c0/rebootNow"
        ):
            return MockResponse(204)
        if (
            url
            == "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices/9de5069c-5afe-602b-2ea0-a04b66beb2c0/syncDevice"
        ):
            return MockResponse(204)
        if (
            url
            == "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices/9de5069c-5afe-602b-2ea0-a04b66beb2c0/windowsDefenderUpdateSignatures"
        ):
            return MockResponse(204)
        if params == {"$filter": "deviceName eq 'INTUNE-W10'"}:
            return MockResponse(200, "get_devices_by_filter.json.resp")
        if params == {"$filter": "emailAddress eq 'user@example.com'"}:
            return MockResponse(200, "get_devices_by_filter.json.resp")
        if params == {"$filter": "emailAddress eq 'user2@example.com'"}:
            return MockResponse(200, "get_devices_empty.json.resp")
        if url == "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices":
            return MockResponse(200, "get_devices.json.resp")
        if (
            url
            == "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices/9de5069c-5afe-602b-2ea0-a04b66beb2c0/wipe"
        ):
            return MockResponse(204)
        if method == "DELETE":
            if (
                url
                == "https://graph.microsoft.com/v1.0/deviceManagement/windowsAutopilotDeviceIdentities/9de5069c-5afe-602b-2ea0-a04b66beb2c0"
            ):
                return MockResponse(200)
            if (
                url
                == "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices/9de5069c-5afe-602b-2ea0-a04b66beb2c0"
            ):
                return MockResponse(204)
        if url == "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices/valid-device-id":
            return MockResponse(200, "get_device.json.resp")
        if url == "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices/invalid-device-id":
            return MockResponse(404)
        if (
            url
            == "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices/9de5069c-5afe-602b-2ea0-a04b66beb2c0/windowsDefenderScan"
        ):
            return MockResponse(204)
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
