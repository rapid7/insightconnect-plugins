import os
import json

from icon_microsoft_intune.util.api import MicrosoftIntuneAPI
import logging


def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


def mocked_requests_request(*args, **kwargs):
    class MockResponse:
        def __init__(self, filename, status_code):
            self.status_code = status_code
            self.text = "error message"
            self.filename = filename

        def json(self):
            if self.filename == "json_error":
                raise json.decoder.JSONDecodeError("json error", "json error", 0)
            actual_joined_path = os.path.join(
                os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp"
            )
            return json.loads(read_file_to_string(actual_joined_path))

    if args[0] == "GET" and args[1] == "/deviceAppManagement/managedAppPolicies":
        return MockResponse("managed_app_policies", 200)

    if args[0] == "GET" and args[1] == "deviceAppManagement/managedAppStatuses('managedAppList')":
        return MockResponse("managed_app_list", 200)

    if args[0] == "GET" and args[1] == "deviceAppManagement/androidManagedAppProtections('T_3a18890f-ee6c-4421-adb2-29305e3e9ee5')?$expand=apps":
        return MockResponse("managed_app_policies_with_apps", 200)

    return MockResponse("add_app_to_policy_204", 204)


class MockConnection:
    def __init__(self):
        self.api = MicrosoftIntuneAPI(
            username="username",
            password="password",
            client_id="client_id",
            client_secret="client_secret",
            tenant_id="tenant_id",
            api_url="",
            logger=logging.getLogger("Test")
        )