import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase, mock
from icon_checkpoint_ngfw.connection.connection import Connection
from icon_checkpoint_ngfw.actions.add_access_rule import AddAccessRule
import json
import logging


# Get a real payload from file
def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


# This method will be used by the mock to replace requests.get
def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
            self.text = str(json_data)

        def json(self):
            return json.loads(self.json_data)

        def raise_for_status(self):
            if self.status_code > 300:
                raise Exception("This is an exception")

    # Since this is folder down from the base unit_test folder, the base path may change on us if we're
    # running the whole suite, or just these tests.
    actual_path = os.path.dirname(os.path.realpath(__file__))
    actual_joined_path_login = os.path.join(actual_path, "payloads/login.json")
    actual_joined_path_add_rule = os.path.join(actual_path, "payloads/login.json")
    actual_joined_path_show_sessions = os.path.join(actual_path, "payloads/show_sessions.json")

    login_payload = read_file_to_string(actual_joined_path_login)
    add_rule_payload = read_file_to_string(actual_joined_path_add_rule)
    show_sessions = read_file_to_string(actual_joined_path_show_sessions)

    if args[0] == 'https://1.1.1.1:666/web_api/login':
        return MockResponse(login_payload, 200)
    if args[0] == 'https://1.1.1.1:666/web_api/add-access-rule':
        return MockResponse(add_rule_payload, 200)
    if args[0] == 'https://1.1.1.1:666/web_api/publish':
        return MockResponse("{}", 200)
    if args[0] == 'https://1.1.1.2:666/web_api/login':
        return MockResponse(login_payload, 200)
    if args[0] == 'https://1.1.1.2:666/web_api/add-access-rule':
        payload = {
          "code": "generic_error",
          "message": "Runtime error: An object is locked by another session."
        }
        return MockResponse(payload, 400)
    if args[0] == 'https://1.1.1.2:666/web_api/show-sessions':
        return MockResponse(show_sessions, 200)
    if args[0] == 'https://1.1.1.2:666/web_api/publish':
        return MockResponse("{}", 200)
    if args[0] == 'https://1.1.1.2:666/web_api/discard':
        return MockResponse("{}", 200)

    print(f"mocked_requests_get failed looking for: {args[0]}")
    return MockResponse(None, 404)


class TestAddAccessRule(TestCase):
    def test_integration_add_access_rule(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = AddAccessRule()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/add_access_rule.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception:
            message = """
            Could not find or read sample tests from /tests directory
            
            An exception here likely means you didn't fill out your samples correctly in the /tests directory 
            Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory
            """
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        # TODO: The following assert should be updated to look for data from your action
        # For example: self.assertEquals({"success": True}, results)
        self.assertIsNotNone(results)

    @mock.patch("requests.post", side_effect=mocked_requests_post)
    def test_add_access_rule(self, mockPost):
        logger = logging.getLogger("test")
        test_connection = Connection()
        test_action = AddAccessRule()

        test_connection.logger = logger
        test_action.logger = logger

        connection_params = {
            "port": 666,
            "server": "1.1.1.1",
            "ssl_verify": False,
            "username_password": {
                "password": "password",
                "username": "admin"
            }
        }

        action_params = {
            "action": "Drop",
            "layer": "Network",
            "list_of_services": ["AOL"],
            "name": "Test from Komand",
            "position": "top",
            "discard_other_sessions": False
        }

        test_connection.connect(connection_params)
        test_action.connection = test_connection
        result = test_action.run(action_params)

        expected = {'access_rule': {'uid': 'fakeUID', 'sid': 'fakeSID', 'url': 'https://1.1.1.1:666/web_api', 'session-timeout': 600, 'last-login-was-at': {'posix': 10000, 'iso-8601': '2020-02-28T10:49-0500'}, 'disk-space-message': "Partition /opt has: 716 MB of free space and it's lower than required: 2000 MB\n", 'api-server-version': '1.1'}}

        self.assertEqual(expected, result)

    @mock.patch("requests.post", side_effect=mocked_requests_post)
    def test_add_access_rule_object_locked(self, mockPost):
        logger = logging.getLogger("test")
        test_connection = Connection()
        test_action = AddAccessRule()

        test_connection.logger = logger
        test_action.logger = logger

        connection_params = {
            "port": 666,
            "server": "1.1.1.2",
            "ssl_verify": True,
            "username_password": {
                "password": "password",
                "username": "admin"
            }
        }

        action_params = {
            "action": "Drop",
            "layer": "Network",
            "list_of_services": ["AOL"],
            "name": "Test from Komand",
            "position": "top",
            "discard_other_sessions": True
        }

        test_connection.connect(connection_params)
        test_action.connection = test_connection
        with self.assertRaises(Exception):  # When the add rule call is retried it will throw an exception
            test_action.run(action_params)

        # This asserts that we've called the mock with these arguments
        # specifically, I want to make sure we're calling the discard endpoint
        mockPost.assert_any_call('https://1.1.1.2:666/web_api/discard', headers={'Content-Type': 'application/json', 'X-chkp-sid': 'fakeSID'}, json={'uid': '0892b540-5fff-4f6f-90d4-b94b15a14f09'}, verify=True)



