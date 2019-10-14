import json
from unittest import TestCase, mock

import requests
from komand.exceptions import PluginException

from icon_microsoft_office365_email.actions.send_email import SendEmail


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

    if args[0] == 'https://login.microsoftonline.com/test_tenant_id/oauth2/token':
        return MockResponse({"access_token": "test_api_token6"}, 200)
    if args[0] == 'https://graph.microsoft.com/v1.0/test_tenant_id/users/good@request.call/sendMail':
        return MockResponse({}, 202)
    if args[0] == 'https://graph.microsoft.com/v1.0/test_tenant_id/users/dont@find.this/sendMail':
        return MockResponse({}, 200)  # will fail

    print(f"mocked_requests_get failed looking for: {args[0]}")
    return MockResponse(None, 404)


class TestSendEmail(TestCase):

    @mock.patch('requests.post', side_effect=mocked_requests_get)
    def test_send_message(self, mockPatch):
        sm = SendEmail()
        sm.connection = MockConnection()
        params = {
            'from': {
                'emailAddress': {
                    'address': "good@request.call"
                }
            }
        }

        actual = sm.send_message(params, 'good@request.call')
        self.assertTrue(actual)

    @mock.patch('requests.post', side_effect=mocked_requests_get)
    def test_send_message_not_202(self, mockPatch):
        sm = SendEmail()
        sm.connection = MockConnection()
        params = {
            'from': {
                'emailAddress': {
                    'address': "dont@find.this"
                }
            }
        }

        actual = sm.send_message(params, 'dont@find.this')
        self.assertFalse(actual)

    @mock.patch('requests.post', side_effect=mocked_requests_get)
    def test_send_message_throws_exception(self, mockPatch):
        sm = SendEmail()
        sm.connection = MockConnection()
        params = {
            'from': {
                'emailAddress': {
                    'address': "this@raises.exception"
                }
            }
        }

        with self.assertRaises(PluginException):
            sm.send_message(params, 'this@raises.exception')

    def test_make_email_container(self):
        email_list = ['test1@hotmail.com', 'test2@hotmail.com']
        sm = SendEmail()
        actual = sm.make_email_container(email_list)

        self.assertEqual('test1@hotmail.com', actual[0].get('emailAddress').get('address'))
        self.assertEqual('test2@hotmail.com', actual[1].get('emailAddress').get('address'))

    def test_make_attachment(self):
        message = {'message': {}}
        attachment = {
            'filename': 'test.txt',
            'content': '123456'
        }

        sm = SendEmail()
        sm.make_attachment(attachment, message)
        actual = message.get('message').get('attachments')
        self.assertEqual(actual[0].get('Name'), 'test.txt')
        self.assertEqual(actual[0].get('ContentBytes'), '123456')
        self.assertEqual(actual[0].get('@odata.type'), '#Microsoft.OutlookServices.FileAttachment')

    def test_compose_email(self):
        params = {
            "attachment": {
                "content": "foobar",
                "filename": "msoffice.exe"
            },
            "bcc": ["bob@bcc.com"],
            "body": "this is a body",
            "cc": ["bob@cc.com", "bob2@cc.com"],
            "is_html": False,
            "email_from": "dave@hotmail.com",
            "email_to": "bob@hotmail.com",
            "subject": "Phishy subject"
        }

        sm = SendEmail()
        actual = sm.compose_email(params)

        expected = '{"message": {"subject": "Phishy subject", "body": {"contentType": "text", "content": "this is a body"}, "from": {"emailAddress": {"address": "dave@hotmail.com"}}, "toRecipients": [{"emailAddress": {"address": "bob@hotmail.com"}}], "ccRecipients": [{"emailAddress": {"address": "bob@cc.com"}}, {"emailAddress": {"address": "bob2@cc.com"}}], "bccRecipients": [{"emailAddress": {"address": "bob@bcc.com"}}], "attachments": [{"@odata.type": "#Microsoft.OutlookServices.FileAttachment", "Name": "msoffice.exe", "ContentBytes": "foobar"}]}, "saveToSentItems": "false"}'

        expected_json = json.loads(json.dumps(expected))
        self.assertEqual(actual, expected_json)

    def test_compose_html_email(self):
        params = {
            "attachment": {
                "content": "foobar",
                "filename": "msoffice.exe"
            },
            "bcc": ["bob@bcc.com"],
            "body": "this is a body",
            "cc": ["bob@cc.com", "bob2@cc.com"],
            "is_html": True,
            "email_from": "dave@hotmail.com",
            "email_to": "bob@hotmail.com",
            "subject": "Phishy subject"
        }

        sm = SendEmail()
        actual = sm.compose_email(params)

        expected = '{"message": {"subject": "Phishy subject", "body": {"contentType": "html", "content": "this is a body"}, "from": {"emailAddress": {"address": "dave@hotmail.com"}}, "toRecipients": [{"emailAddress": {"address": "bob@hotmail.com"}}], "ccRecipients": [{"emailAddress": {"address": "bob@cc.com"}}, {"emailAddress": {"address": "bob2@cc.com"}}], "bccRecipients": [{"emailAddress": {"address": "bob@bcc.com"}}], "attachments": [{"@odata.type": "#Microsoft.OutlookServices.FileAttachment", "Name": "msoffice.exe", "ContentBytes": "foobar"}]}, "saveToSentItems": "false"}'

        expected_json = json.loads(json.dumps(expected))
        self.assertEqual(actual, expected_json)

    @mock.patch('requests.post', side_effect=mocked_requests_get)
    def test_run(self, mockGet):
        params = {
            "attachment": {
                "content": "foobar",
                "filename": "msoffice.exe"
            },
            "bcc": ["bob@bcc.com"],
            "body": "this is a body",
            "cc": ["bob@cc.com", "bob2@cc.com"],
            "is_html": False,
            "email_from": "good@request.call",
            "email_to": "bob@hotmail.com",
            "subject": "Phishy subject"
        }

        sm = SendEmail()
        sm.connection = MockConnection()

        actual = sm.run(params)
        expected = True
        self.assertEqual(actual.get("success"), expected)
