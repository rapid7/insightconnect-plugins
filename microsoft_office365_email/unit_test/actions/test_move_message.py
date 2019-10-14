from unittest import TestCase, mock
from komand.exceptions import PluginException
from icon_microsoft_office365_email.actions.move_email import MoveEmail
import json
import os
import requests


# Get a real payload from file
def read_file_to_string(filename: str) -> str:
    with open(filename) as my_file:
        return my_file.read()


# Mock the connection
class MockConnection:
    def __init__(self):
        self.tenant = "test_tenant_id"
        self.auth_token = "test_api_token"

    def get_headers(self, api_token: str) -> {str: str}:
        return {
            "thisisaheader": "thisisavalue",
            "api_token": self.auth_token
        }

    def get_auth_token(self) -> str:
        return self.auth_token


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
            self.text = "This is some error text"

        def json(self) -> dict:
            return json.loads(self.json_data)

        def raise_for_status(self):
            if self.status_code >= 400:
                raise requests.HTTPError("Who's BAD")

    # Since this is folder down from the base unit_test folder, the base path may change on us if we're
    # running the whole suite, or just these tests.
    actual_path = os.path.dirname(os.path.realpath(__file__))
    actual_joined_path = os.path.join(actual_path, "payloads/get_folders_payload.json")
    folder_payload = read_file_to_string(actual_joined_path)
    fake_next_folder_payload = '{"value": []}'

    move_message_path = os.path.join(actual_path, "payloads/move_message_success_payload.json")
    move_message_success = read_file_to_string(move_message_path)

    if args[0] == 'https://login.microsoftonline.com/test_tenant_id/oauth2/token':
        return MockResponse({"access_token": "test_api_token6"}, 200)
    if args[0] == 'https://graph.microsoft.com/v1.0/test_tenant_id/users/bob@hotmail.com/mailFolders':
        return MockResponse(folder_payload, 200)
    if args[0] == 'https://graph.microsoft.com/v1.0/5c824599-dc8c-4d31-96fb-3b886d4f8f10/users/jschipp@komanddev.onmicrosoft.com/mailFolders?$skip=10':
        return MockResponse(fake_next_folder_payload, 200)
    if args[0] == 'https://graph.microsoft.com/v1.0/test_tenant_id/users/Fake_Json/mailFolders':
        return MockResponse("[", 200)
    if args[0] == 'https://graph.microsoft.com/v1.0/test_tenant_id/users/bob@hotmail.com/messages/fake_id_12345/move':
        return MockResponse(move_message_success, 200)

    print(f"mocked_requests_get failed looking for: {args[0]}")
    return MockResponse(None, 404)


class TestMoveEmail(TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_find_folder(self, mockGet):
        move_message = MoveEmail()
        move_message.connection = MockConnection()
        actual = move_message.find_folder("Mike-Test", "bob@hotmail.com")

        self.assertEqual("fake_dest_54321", actual)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_find_folder_invalid_folder_name(self, mockGet):
        move_message = MoveEmail()
        move_message.connection = MockConnection()

        with self.assertRaises(PluginException):
            move_message.find_folder("dont_find_me", "bob@hotmail.com")

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_find_folder_invalid_bad_json(self, mockGet):
        move_message = MoveEmail()
        move_message.connection = MockConnection()

        with self.assertRaises(PluginException):
            move_message.find_folder("Fake_Json", "Fake_Json")

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_find_folder_invalid_bad_request(self, mockGet):
        move_message = MoveEmail()
        move_message.connection = MockConnection()

        with self.assertRaises(PluginException):
            move_message.find_folder("DONT FIND ME", "DONT FIND ME")

    @mock.patch('requests.post', side_effect=mocked_requests_get)
    def test_move_message(self, mockGet):
        move_message = MoveEmail()
        move_message.connection = MockConnection()

        actual = move_message.move_message("fake_id_12345", "bob@hotmail.com", "fake_dest_54321")
        self.assertTrue(actual)

    @mock.patch('requests.post', side_effect=mocked_requests_get)
    def test_move_message_404(self, mockGet):
        move_message = MoveEmail()
        move_message.connection = MockConnection()

        with self.assertRaises(PluginException):
            move_message.move_message("fake_id_mclovin", "bob@hotmail.com", "fake_dest_54321")

    @mock.patch('requests.post', side_effect=mocked_requests_get)
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_run(self, mockPost, mockGet):
        move_message = MoveEmail()
        move_message.connection = MockConnection()

        params = {
            "folder_name": "Mike-Test",
            "email_id": "fake_id_12345",
            "mailbox_id": "bob@hotmail.com"
        }

        actual = move_message.run(params)
        self.assertEqual(True, actual.get("success"))
