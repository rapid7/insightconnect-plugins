from unittest import TestCase, mock
from komand.exceptions import PluginException
from icon_microsoft_office365_email.actions.get_email_from_user import GetEmailFromUser
from icon_microsoft_office365_email.actions.get_email_from_user.schema import Input, Output

import os
import json


# Get a real payload from file
def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
            self.text = "This is some error text"

        def json(self):
            return json.loads(self.json_data)

    # Since this is folder down from the base unit_test folder, the base path may change on us if we're
    # running the whole suite, or just these tests.
    actual_path = os.path.dirname(os.path.realpath(__file__))
    actual_joined_path = os.path.join(actual_path, "payloads/get_messages_from_user.json")
    get_messages_from_user_payload = read_file_to_string(actual_joined_path)

    if args[0] == f'https://login.microsoftonline.com/test_tenant_id/oauth2/token':
        return MockResponse({"access_token": "test_api_token6"}, 200)
    if args[0] == f'https://graph.microsoft.com/v1.0/test_tenant_id/users/bob@hotmail.com/messages?$search="from:From"&$top=250':
        return MockResponse(get_messages_from_user_payload, 200)
    if args[0] == f'https://graph.microsoft.com/v1.0/test_tenant_id/users/bob@hotmail.com/messages?$search="from:BAD JSON"&$top=250':
        return MockResponse({}, 200)
    if args[0] == f'https://graph.microsoft.com/v1.0/test_tenant_id/users/bob@hotmail.com/messages?$search="from:THROW EXCEPTION"&$top=250':
        raise Exception("This is an exception")

    print(f"mocked_requests_get failed looking for: {args[0]}")
    return MockResponse(None, 404)


# Mock the connection
class MockConnection:
    def __init__(self):
        self.tenant = "test_tenant_id"
        self.auth_token = "test_api_token"

    def get_headers(self, api_token):
        return {
            "thisisaheader": "thisisavalue",
            "api_token": self.auth_token
        }

    def get_auth_token(self):
        return self.auth_token


class TestGetMessageFromUser(TestCase):
    def setUp(self) -> None:
        self.params = {
            Input.MAILBOX_ID: "bob@hotmail.com",
            Input.FROM_CONTAINS: "From",
            Input.SUBJECT_CONTAINS: "",
            Input.BODY_CONTAINS: "",
            Input.MAX_NUMBER_TO_RETURN: 250
        }

    def test_make_kql_for_request(self):
        get_messages = GetEmailFromUser()
        actual = get_messages.make_kql_for_request("From", "Subject", "Body", 250)

        expected = '$search="from:From subject:\'Subject\' body:\'Body\'"&$top=250'
        self.assertEqual(actual, expected)

    def test_make_kql_for_request_throws_exception(self):
        get_messages = GetEmailFromUser()

        with self.assertRaises(PluginException):
            get_messages.make_kql_for_request("", "", "", 250)

    def test_make_kql_for_request_sets_max_on_invalid(self):
        get_messages = GetEmailFromUser()
        actual = get_messages.make_kql_for_request("From", "Subject", "Body", 1000)

        expected = '$search="from:From subject:\'Subject\' body:\'Body\'"&$top=250'
        self.assertEqual(actual, expected)

    def test_make_kql_for_request_sets_max_on_invalid2(self):
        get_messages = GetEmailFromUser()
        actual = get_messages.make_kql_for_request("From", "Subject", "Body", -10)

        expected = '$search="from:From subject:\'Subject\' body:\'Body\'"&$top=250'
        self.assertEqual(actual, expected)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_messages_from_user(self, mock_get):
        get_messages = GetEmailFromUser()
        get_messages.connection = MockConnection()
        actual = get_messages.get_messages_from_user("bob@hotmail.com", '$search="from:From"&$top=250')

        self.assertTrue(len(actual), 3)
        self.assertEqual(actual[2].get('id'), 'AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwBGAAAAAAAxDvrPc8q6SqGLTJ9iB-SGBwC8UQDN7ObVSLWQuxHJ-dDTAAE-L_Q7AAC8UQDN7ObVSLWQuxHJ-dDTAAE-MJpHAAA=')

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_messages_from_user_404(self, mock_get):
        get_messages = GetEmailFromUser()
        get_messages.connection = MockConnection()

        with self.assertRaises(PluginException):
            get_messages.get_messages_from_user("bob@hotmail.com", '$search="from:DONT FIND ME"&$top=250')

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_messages_from_user_bad_json(self, mock_get):
        get_messages = GetEmailFromUser()
        get_messages.connection = MockConnection()

        with self.assertRaises(PluginException):
            get_messages.get_messages_from_user("bob@hotmail.com", '$search="from:BAD JSON"&$top=250')

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_messages_from_user_throws_exception(self, mock_get):
        get_messages = GetEmailFromUser()
        get_messages.connection = MockConnection()

        with self.assertRaises(PluginException):
            get_messages.get_messages_from_user("bob@hotmail.com", '$search="from:THROW EXCEPTION"&$top=250')

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_run(self, mock_get):
        get_messages = GetEmailFromUser()
        get_messages.connection = MockConnection()

        actual = get_messages.run(self.params)
        actual_output = actual.get(Output.EMAIL_LIST)
        self.assertEqual(len(actual_output), 3)
        for email in actual_output:
            print(type(email))
            self.assertIsInstance(email, dict)

        self.assertEqual(actual_output[2].get('subject'), 'Fwd: Joey Test')
