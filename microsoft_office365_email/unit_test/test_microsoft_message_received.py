from komand.exceptions import PluginException
from unittest import TestCase
from unittest import mock
import timeout_decorator
import logging
import requests
import json
import maya

from icon_microsoft_office365_email.triggers.email_received import EmailReceived

# vars
from icon_microsoft_office365_email.util.icon_email import IconEmail
from icon_microsoft_office365_email.util.icon_file import IconFile

TEST_MAILBOX_ID = "bob@hotmail.com"
TEST_QUERY = "Find Me"
TEST_FOLDER_NAME = "Phishy"
TEST_TENANT = "MS6661337"
TEST_API_TOKEN = "api_token_123451234123412351235"
TEST_EMAIL_ID = "fakeID123456"

# files
GET_MESSAGES_PAYLOAD = "./payloads/get_messages_payload.json"
GET_FOLDERS_PAYLOAD = "./payloads/get_folders_paylaod.json"
GET_ATTACHMENT_EMAIL_PAYLOAD = "./payloads/get_attachment_email_payload.json"
GET_ATTACHMENT_FILE_PAYLOAD = "./payloads/get_attachments_file_payload.json"
GET_RAW_ATTACHMENT_PAYLOAD = "./payloads/get_raw_attachment_test.txt"
GET_ATTACHEMENT_WITH_ATTACHMENT = "./payloads/get_attachment_email_with_attachment_payload.json"
GET_HEADERS = "./payloads/get_headers_payload.json"
GET_JARED_TEST = "./payloads/payload_from_jared.txt"
GET_EMAIL_FROM_HELL = "./payloads/lots_of_eml_attached.eml"


# Get a real payload from file
def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


# This will catch timeout errors and return None, which will make tests pass
def timeout_pass(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except timeout_decorator.timeout_decorator.TimeoutError as e:
            print(f"Test timed out as expected: {e}")
            return None
    return func_wrapper


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, data, status_code):
            self.status_code = status_code
            self.text = data

        def raise_for_status(self):
            if self.status_code >= 400:
                raise requests.HTTPError(f"{self.status_code}")

        def json(self):
            return json.loads(self.text)

    mock_messages = read_file_to_string(GET_MESSAGES_PAYLOAD)
    mock_folders = read_file_to_string(GET_FOLDERS_PAYLOAD)
    mock_get_attachment_email = read_file_to_string(GET_ATTACHMENT_EMAIL_PAYLOAD)
    mock_get_attachment_file = read_file_to_string(GET_ATTACHMENT_FILE_PAYLOAD)
    mock_get_raw_attachment = read_file_to_string(GET_RAW_ATTACHMENT_PAYLOAD)
    mock_attachment_with_attachment = read_file_to_string(GET_ATTACHEMENT_WITH_ATTACHMENT)
    mock_get_headers = read_file_to_string(GET_HEADERS)
    mock_get_jared_test = read_file_to_string(GET_JARED_TEST)
    mock_get_email_from_hell = read_file_to_string(GET_EMAIL_FROM_HELL)

    if args[0] == f'https://graph.microsoft.com/v1.0/{TEST_TENANT}/users/{TEST_MAILBOX_ID}/messages?$orderby=receivedDateTime DESC':
        return MockResponse(mock_messages, 200)
    if args[0] == f'https://graph.microsoft.com/v1.0/{TEST_TENANT}/users/{TEST_MAILBOX_ID}/mailFolders':
        return MockResponse(mock_folders, 200)
    if args[0] == f'https://graph.microsoft.com/v1.0/{TEST_TENANT}/users/{TEST_MAILBOX_ID}/mailFolders/Inbox/messages?$orderby=receivedDateTime DESC':
        return MockResponse(mock_messages, 200)
    if args[0] == "https://graph.microsoft.com/v1.0/5c824599-dc8c-4d31-96fb-3b886d4f8f10/users/jschipp@komanddev.onmicrosoft.com/mailFolders?$skip=10":
        return MockResponse("{\"value\":[{\"displayName\":\"Cant Touch This\"}]}", 200)
    if args[0] == f"https://graph.microsoft.com/v1.0/{TEST_TENANT}/users/{TEST_MAILBOX_ID}/messages/{TEST_EMAIL_ID}/attachments?$expand=microsoft.graph.itemattachment/item":
        return MockResponse(mock_get_attachment_file, 200)
    if args[0] == f"https://graph.microsoft.com/v1.0/{TEST_TENANT}/users/{TEST_MAILBOX_ID}/messages/TEST_EMAIL_ATTACHMENT/attachments?$expand=microsoft.graph.itemattachment/item":
        return MockResponse(mock_get_attachment_email, 200)
    if args[0] == "https://graph.microsoft.com/beta/MS6661337/users/bob@hotmail.com/messages/12345/attachments/54321/$value":
        return MockResponse(mock_get_raw_attachment, 200)
    if args[0] == f"https://graph.microsoft.com/v1.0/{TEST_TENANT}/users/{TEST_MAILBOX_ID}/messages/TEST_EMAIL_ATTACHMENT_WITH_ATTACHMENT/attachments?$expand=microsoft.graph.itemattachment/item":
        return MockResponse(mock_attachment_with_attachment, 200)
    if args[0] == f"https://graph.microsoft.com/beta/{TEST_TENANT}/users/{TEST_MAILBOX_ID}/messages/TEST_EMAIL_ATTACHMENT_WITH_ATTACHMENT/attachments/this_is_a_fake_id_12345/$value":
        return MockResponse(mock_get_raw_attachment, 200)
    if args[0] == f"https://graph.microsoft.com/v1.0/{TEST_TENANT}/users/{TEST_MAILBOX_ID}/messages/message_headers_id_12345/?$select=internetMessageHeaders":
        return MockResponse(mock_get_headers, 200)
    if args[0] == "https://graph.microsoft.com/beta/MS6661337/users/bob@hotmail.com/messages/JARED_TEST/attachments/None/$value":
        return MockResponse(mock_get_jared_test, 200)
    if args[0] == "https://graph.microsoft.com/v1.0/MS6661337/users/bob@hotmail.com/messages/AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwBGAAAAAAAxDvrPc8q6SqGLTJ9iB-SGBwC8UQDN7ObVSLWQuxHJ-dDTAAAAAAEMAAC8UQDN7ObVSLWQuxHJ-dDTAAE0dZaGAAA=/?$select=internetMessageHeaders":
        return MockResponse(mock_get_headers, 200)
    if args[0] == "https://graph.microsoft.com/beta/MS6661337/users/bob@hotmail.com/messages/THIS_EMAIL_SUCKS/attachments/None/$value":
        return MockResponse(mock_get_email_from_hell, 200)
    if args[0] == "https://graph.microsoft.com/v1.0/MS6661337/users/bob@hotmail.com/messages/garbage_response/?$select=internetMessageHeaders":
        return MockResponse({}, 200)
    if args[0] == "https://graph.microsoft.com/v1.0/MS6661337/users/FAKE_JSON_MAILBOX/messages?$orderby=receivedDateTime DESC":
        return MockResponse({}, 200)

    print(f"Attempted to get:\n{args[0]}")
    return MockResponse(None, 404)


# Need this to mock log_stream and dispatcher from komand.Trigger
class MockDispatcher():

    # Will print trigger when send is called
    def write(self, msg):
        print(msg)

    # No clue why we need this, but it gets hit deep in the komand code
    def getvalue(self):
        return self

    # No clue why we need this, but it gets hit deep in the komand code
    def truncate(self, int):
        return None


# Mock the connection
class mockConnection:
    def __init__(self):
        self.tenant = TEST_TENANT
        self.auth_token = TEST_API_TOKEN

    def get_headers(self, api_token):
        return {
            "thisisaheader": "thisisavalue",
            "api_token": TEST_API_TOKEN
        }

    def get_auth_token(self):
        return TEST_API_TOKEN


# Finally, test class
class test_microsoft_message_received(TestCase):
    def setUp(self) -> None:
        pass

    # The timeout decorator allows us to kill the 'while True' loop without failing the test
    @timeout_pass
    @timeout_decorator.timeout(3)
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_microsoft_message_received(self, mock_get):
        mr = EmailReceived()
        params = {
            "mailbox_id": TEST_MAILBOX_ID,
            "subject_query": TEST_QUERY,
            "interval": 1
        }
        mr.connection = mockConnection()
        mr.log_stream = MockDispatcher()
        mr.dispatcher = MockDispatcher()
        mr.logger = logging.getLogger("TestLogger")
        mr.current_time = maya.MayaDT('2019-08-05T14:57:40Z')

        mr.run(params)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_make_message_ready_to_send(self, mock_get):
        mr = EmailReceived()
        flatten = False
        mr.connection = mockConnection()
        mr.log_stream = MockDispatcher()
        mr.dispatcher = MockDispatcher()
        mr.logger = logging.getLogger("TestLogger")

        test_message = json.loads(read_file_to_string(GET_MESSAGES_PAYLOAD)).get("value")[1]
        actual = mr.make_message_ready_to_send(TEST_MAILBOX_ID, test_message, flatten)

        self.assertIsInstance(actual, dict)
        self.assertEqual(actual.get('account'), TEST_MAILBOX_ID)
        self.assertEqual(actual.get('date_received'), '2019-08-05T14:57:40Z')
        self.assertEqual(actual.get('id'), 'AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwBGAAAAAAAxDvrPc8q6SqGLTJ9iB-SGBwC8UQDN7ObVSLWQuxHJ-dDTAAAAAAEMAAC8UQDN7ObVSLWQuxHJ-dDTAAE0dZaGAAA=')

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_make_message_ready_to_send_with_flatten(self, mock_get):
        mr = EmailReceived()
        flatten = True
        mr.connection = mockConnection()
        mr.log_stream = MockDispatcher()
        mr.dispatcher = MockDispatcher()
        mr.logger = logging.getLogger("TestLogger")

        test_message = json.loads(read_file_to_string(GET_MESSAGES_PAYLOAD)).get("value")[1]
        actual = mr.make_message_ready_to_send(TEST_MAILBOX_ID, test_message, flatten)

        self.assertIsInstance(actual, dict)
        self.assertEqual(actual.get('account'), TEST_MAILBOX_ID)
        self.assertEqual(actual.get('date_received'), '2019-08-05T14:57:40Z')
        self.assertEqual(actual.get('id'), 'AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwBGAAAAAAAxDvrPc8q6SqGLTJ9iB-SGBwC8UQDN7ObVSLWQuxHJ-dDTAAAAAAEMAAC8UQDN7ObVSLWQuxHJ-dDTAAE0dZaGAAA=')

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_microsoft_messages_no_folder(self, mock_patch):
        mr = EmailReceived()
        mr.connection = mockConnection()
        mr.logger = logging.getLogger("TestLogger")

        actual_val = mr.get_microsoft_messages(TEST_TENANT, TEST_MAILBOX_ID, "")
        expected_val = json.loads(read_file_to_string(GET_MESSAGES_PAYLOAD)).get("value")

        print(f"Actual: {actual_val}")
        print(f"Expected: {expected_val}")

        self.assertEqual(actual_val, expected_val)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_microsoft_messages_with_folder(self, mock_patch):
        mr = EmailReceived()
        mr.connection = mockConnection()
        mr.logger = logging.getLogger("TestLogger")

        actual_val = mr.get_microsoft_messages(TEST_TENANT, TEST_MAILBOX_ID, "Inbox")
        expected_val = json.loads(read_file_to_string(GET_MESSAGES_PAYLOAD)).get("value")

        print(f"Actual: {actual_val}")
        print(f"Expected: {expected_val}")

        self.assertEqual(actual_val, expected_val)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_microsoft_messages_invalid_json(self, mock_patch):
        mr = EmailReceived()
        mr.connection = mockConnection()
        mr.logger = logging.getLogger("TestLogger")

        with self.assertRaises(PluginException):
            mr.get_microsoft_messages(TEST_TENANT, "FAKE_JSON_MAILBOX", "")

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_microsoft_messages_bad_request(self, mock_patch):
        mr = EmailReceived()
        mr.connection = mockConnection()
        mr.logger = logging.getLogger("TestLogger")

        with self.assertRaises(PluginException):
            mr.get_microsoft_messages(TEST_TENANT, "notarealuser@somefakedomain.com", "")

    def test_convert_to_time(self):
        mr = EmailReceived()
        actual = mr.convert_to_time("2019-08-05T14:59:32Z")
        self.assertIsInstance(actual, maya.core.MayaDT)

    def test_get_new_messages(self):
        mr = EmailReceived()
        mr.current_time = mr.convert_to_time("2019-08-05T14:52:06Z")
        messages = json.loads(read_file_to_string(GET_MESSAGES_PAYLOAD)).get("value")

        actual = mr.get_new_messages(messages, mr.current_time)
        self.assertEqual(len(actual), 2)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_find_folder(self, mock_get):
        mr = EmailReceived()
        mr.connection = mockConnection()

        actual = mr.find_folder("Mike-Test", TEST_MAILBOX_ID)
        expected = "AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwAuAAAAAAAxDvrPc8q6SqGLTJ9iB-SGAQC8UQDN7ObVSLWQuxHJ-dDTAAAUtfMmAAA="

        self.assertEqual(actual, expected)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_find_folder_bad_folder_name(self, mock_get):
        mr = EmailReceived()
        mr.connection = mockConnection()

        with self.assertRaises(PluginException):
            mr.find_folder("I am a lost folder", TEST_MAILBOX_ID)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_find_folder_bad_mailbox_id(self, mock_get):
        mr = EmailReceived()
        mr.connection = mockConnection()

        with self.assertRaises(PluginException):
            mr.find_folder("I am a lost folder", "bad mailbox id")

    def test_filter_messages_by_subject(self):
        mr = EmailReceived()
        mr.connection = mockConnection()

        messages = json.loads(read_file_to_string(GET_MESSAGES_PAYLOAD)).get("value")

        actual = mr.filter_messages_by_subject("Weekly digest", messages)
        self.assertEqual(len(actual), 1)

    def test_filter_messages_by_subject_not_found(self):
        mr = EmailReceived()
        mr.connection = mockConnection()

        messages = json.loads(read_file_to_string(GET_MESSAGES_PAYLOAD)).get("value")

        actual = mr.filter_messages_by_subject("Can't find me", messages)
        self.assertEqual(len(actual), 0)

    def test_filter_messages_by_subject_bad_regex(self):
        mr = EmailReceived()
        mr.connection = mockConnection()

        messages = json.loads(read_file_to_string(GET_MESSAGES_PAYLOAD)).get("value")

        with self.assertRaises(PluginException):
            mr.filter_messages_by_subject("[", messages)

    def test_filter_messages_no_subject_query(self):
        mr = EmailReceived()
        mr.connection = mockConnection()

        messages = json.loads(read_file_to_string(GET_MESSAGES_PAYLOAD)).get("value")

        # Yes this is dumb, I just wanted to make sure it didn't throw an exception on
        # None or ""
        mr.filter_messages_by_subject("", messages)
        actual = mr.filter_messages_by_subject(None, messages)
        self.assertEqual(len(actual), 10)

    def test_get_attachments_for_no_attachments(self):
        mr = EmailReceived()
        mr.connection = mockConnection()

        actual_files, actual_email = mr.get_attachments(json.loads('{"hasAttachments":false}'), TEST_MAILBOX_ID)
        self.assertEqual(actual_files, [])
        self.assertEqual(actual_email, [])

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_attachments_file_type_attachment(self, mock_get):
        mr = EmailReceived()
        mr.connection = mockConnection()

        # double curly in format string
        fake_payload = f'{{"hasAttachments":true, "id": "{TEST_EMAIL_ID}"}}'
        print(fake_payload)

        actual_files, actual_email = mr.get_attachments(json.loads(fake_payload), TEST_MAILBOX_ID)

        self.assertEqual(actual_email, [])
        self.assertIsInstance(actual_files[0], IconFile)

        print(actual_files[0].content_type)
        print(actual_files[0].file_name)
        print(actual_files[0].content)

        self.assertEqual(actual_files[0].content_type, "image/jpeg")
        self.assertEqual(actual_files[0].file_name, "Photo on 4-29-19 at 11.21 AM.jpg")
        self.assertEqual(actual_files[0].content, "/9j/4AAQSkZJRgABAQAASAB...Not real bytes")

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_attachments_email_type_attachment(self, mock_get):
        mr = EmailReceived()
        mr.connection = mockConnection()

        # double curly in format string
        fake_payload = f'{{"hasAttachments":true, "id": "TEST_EMAIL_ATTACHMENT"}}'
        print(fake_payload)

        actual_files, actual_emails = mr.get_attachments(json.loads(fake_payload), TEST_MAILBOX_ID)

        self.assertEqual(actual_files, [])
        self.assertIsInstance(actual_emails[0], IconEmail)

        actual_email = actual_emails[0]
        self.assertEqual(actual_email.id, "")  # Attached emails don't have IDs. Thanks Microsoft
        self.assertEqual(actual_email.is_read, True)
        self.assertEqual(actual_email.account, TEST_MAILBOX_ID)
        self.assertEqual(actual_email.subject, "Attachment")
        self.assertEqual(actual_email.attached_files, [])
        self.assertEqual(actual_email.attached_emails, [])
        self.assertEqual(actual_email.flattened_attached_emails, [])
        self.assertEqual(actual_email.flattened_attached_files, [])
        self.assertEqual(actual_email.has_attachments, False)
        self.assertEqual(actual_email.date_received, "2019-08-06T19:19:47Z")
        self.assertEqual(len(actual_email.headers), 72)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_attachments_throws_exception(self, mock_get):
        mr = EmailReceived()
        mr.connection = mockConnection()

        fake_payload = f'{{"hasAttachments":true, "id": "TEST_EMAIL_ATTACHMENT"}}'

        with self.assertRaises(PluginException):
            mr.get_attachments(json.loads(fake_payload), "garbage@mailbox.id")

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_raw_attachment(self, mock_get):
        mr = EmailReceived()
        mr.connection = mockConnection()

        actual = mr.get_raw_attachment(TEST_TENANT, TEST_MAILBOX_ID, "12345", "54321")
        expected = read_file_to_string(GET_RAW_ATTACHMENT_PAYLOAD)

        self.assertEqual(actual, expected)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_raw_attachment_throws_plugin_exception(self, mock_get):
        mr = EmailReceived()
        mr.connection = mockConnection()

        with self.assertRaises(PluginException):
            mr.get_raw_attachment("Evict this guy", TEST_MAILBOX_ID, "12345", "54321")

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_attachments_with_attachments(self, mock_get):
        mr = EmailReceived()
        mr.connection = mockConnection()

        # double curly in format string
        fake_payload = f'{{"hasAttachments":true, "id": "TEST_EMAIL_ATTACHMENT_WITH_ATTACHMENT"}}'
        print(fake_payload)

        fake_payload_json = json.loads(fake_payload)
        actual_files, actual_emails = mr.get_attachments(fake_payload_json, TEST_MAILBOX_ID)

        self.assertEqual(actual_files, [])
        self.assertIsInstance(actual_emails[0], IconEmail)

        actual_email = actual_emails[0]
        self.assertEqual(actual_email.account, TEST_MAILBOX_ID)
        self.assertEqual(actual_email.id, "this_is_a_fake_id_12345")
        attached_email = actual_email.attached_emails[0]
        self.assertIsInstance(attached_email, IconEmail)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_microsoft_message_headers(self, mock_get):
        mr = EmailReceived()
        mr.connection = mockConnection()

        actual = mr.get_microsoft_message_headers(TEST_TENANT, TEST_MAILBOX_ID, "message_headers_id_12345")

        self.assertIsInstance(actual, list)
        self.assertEqual(len(actual), 67)
        self.assertEqual(actual[23], {'name': 'Accept-Language', 'value': 'en-US'})
        self.assertEqual(actual[37], {'name': 'MIME-Version', 'value': '1.0'})

    def test_get_microsoft_message_headers_throws_exception(self):
        mr = EmailReceived()
        mr.connection = mockConnection()

        with self.assertRaises(PluginException):
            mr.get_microsoft_message_headers(TEST_TENANT, TEST_MAILBOX_ID, "dont_find_me")

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_microsoft_message_headers_throws_exception_invalid_json(self, mockGet):
        mr = EmailReceived()
        mr.connection = mockConnection()

        with self.assertRaises(PluginException):
            mr.get_microsoft_message_headers(TEST_TENANT, TEST_MAILBOX_ID, "garbage_response")

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_set_attachments(self, mock_get):
        mr = EmailReceived()
        mr.connection = mockConnection()

        email_attachment = {'@odata.type': 'itemAttachment',
                            'item': {'hasAttachments': True}
                            }

        file_attachments_list = []
        email_attachments_list = []

        mr.set_attachments(email_attachment,
                           file_attachments_list,
                           email_attachments_list,
                           TEST_MAILBOX_ID,
                           'JARED_TEST')

        self.assertEqual(len(email_attachments_list), 1)
        self.assertEqual(len(email_attachments_list[0].attached_files), 4)
        self.assertEqual(len(email_attachments_list[0].attached_emails), 2)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_set_attachments_from_email_from_hell(self, mock_get):
        mr = EmailReceived()
        mr.connection = mockConnection()

        email_attachment = {'@odata.type': 'itemAttachment',
                            'item': {'hasAttachments': True}
                            }

        file_attachments_list = []
        email_attachments_list = []

        mr.set_attachments(email_attachment,
                           file_attachments_list,
                           email_attachments_list,
                           TEST_MAILBOX_ID,
                           'THIS_EMAIL_SUCKS')

        self.assertEqual(len(email_attachments_list), 1)
        self.assertEqual(len(email_attachments_list[0].attached_files), 0)
        self.assertEqual(len(email_attachments_list[0].attached_emails), 6)
