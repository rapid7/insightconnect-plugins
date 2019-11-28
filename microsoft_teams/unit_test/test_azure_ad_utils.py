import logging
import json
from time import sleep

from unittest import TestCase, mock
from icon_microsoft_teams.util.azure_ad_utils import get_user_info, add_user_to_group, remove_user_from_group, create_group, get_group_id_from_name, delete_group, enable_teams_for_group
from icon_microsoft_teams.connection.connection import Connection
from komand.exceptions import PluginException


class MockConnection():
    def __init__(self):
        self.tenant_id = "fake_tenant_id"

    def get_headers(self):
        return {"value": "header"}


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
            self.text = "This is some response text"

        def json(self):
            return self.json_data

    if args[0] == f'https://graph.microsoft.com/v1.0/fake_tenant_id/groups/fake_group_id/team':
        return MockResponse({}, 400)

    print(f"Failed api call: {args[0]}")
    return MockResponse(None, 404)


class TestAzureADUtils(TestCase):
    def test_get_user_info(self):
        log = logging.getLogger()
        connection = Connection()
        connection.logger = log

        with open("../tests/get_teams.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        connection.connect(connection_params)

        result = get_user_info(log, connection, "jmcadams@komanddev.onmicrosoft.com")

        self.assertEqual("Joey McAdams", result.get("displayName"))
        self.assertEqual("08290005-23ba-46b4-a377-b381d651a2fb", result.get("id"))

        result = get_user_info(log, connection, "jschipp@komanddev.onmicrosoft.com")

        self.assertEqual("Jon Schipp", result.get("displayName"))
        self.assertEqual("ac785ffe-530a-45a1-bbf4-e275457e464b", result.get("id"))

    def test_add_user_to_group(self):
        log = logging.getLogger()
        connection = Connection()
        connection.logger = log

        with open("../tests/get_teams.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        connection.connect(connection_params)

        # Komand-Test_Everyone
        # jmcadams@komanddev.onmicrosoft.com
        try:
            remove_user_from_group(log, connection, "7af08a76-01fe-4a1d-bfa1-84d2b5509cdd", "08290005-23ba-46b4-a377-b381d651a2fb")
            log.info("Successfully removed user.")
        except Exception as e:
            log.info("Remove user failed!")
            print(e)
            pass
        sleep(10)
        result = add_user_to_group(log, connection, "7af08a76-01fe-4a1d-bfa1-84d2b5509cdd", "08290005-23ba-46b4-a377-b381d651a2fb")

        self.assertTrue(result)

    def test_remove_user_from_group(self):
        log = logging.getLogger()
        connection = Connection()
        connection.logger = log

        with open("../tests/get_teams.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        connection.connect(connection_params)

        # Komand-Test_Everyone
        # jmcadams@komanddev.onmicrosoft.com
        try:
            add_user_to_group(log, connection, "7af08a76-01fe-4a1d-bfa1-84d2b5509cdd",
                              "08290005-23ba-46b4-a377-b381d651a2fb")
            log.info("Successfully addeded user.")
        except Exception as e:
            log.info("Add user failed!")
            print(e)
            pass
        sleep(10)
        result = remove_user_from_group(log, connection, "7af08a76-01fe-4a1d-bfa1-84d2b5509cdd", "08290005-23ba-46b4-a377-b381d651a2fb")

        self.assertTrue(result)

    def test_create_group(self):
        log = logging.getLogger()
        connection = Connection()
        connection.logger = log

        with open("../tests/get_teams.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        connection.connect(connection_params)

        owners = ["jmcadams@komanddev.onmicrosoft.com"]
        members = ["jschipp@komanddev.onmicrosoft.com", "jmcadams@komanddev.onmicrosoft.com"]

        result = create_group(log,
                              connection,
                              "test_group_delete_me",
                              "A test group to delete",
                              "nickname_goes_here",
                              True,
                              owners,
                              members)

        self.assertIsNotNone(result)
        self.assertEqual(result.get('displayName'), 'test_group_delete_me')
        self.assertEqual(result.get('description'), 'A test group to delete')

    def test_get_group_id(self):
        log = logging.getLogger()
        connection = Connection()
        connection.logger = log

        with open("../tests/get_teams.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        connection.connect(connection_params)
        result = get_group_id_from_name(log, connection, "test_group_delete_me")

        self.assertIsNotNone(result)
        self.assertEqual(type(result), str)

    def test_delete_group(self):
        log = logging.getLogger()
        connection = Connection()
        connection.logger = log

        with open("../tests/get_teams.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        connection.connect(connection_params)
        result = delete_group(log, connection, "test_group_delete_me")

        self.assertTrue(result)

    def test_enable_teams_for_group(self):
        log = logging.getLogger()
        connection = Connection()
        connection.logger = log

        with open("../tests/get_teams.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        connection.connect(connection_params)

        # try nuking the group first, create_group fails if it's already there
        try:
            delete_group(logging, connection, "test_group_delete_me")
            sleep(10)  # give Azure time to do it's thing
        except Exception:
            pass

        result = create_group(log,
                              connection,
                              "test_group_delete_me",
                              "A test group to delete",
                              "nickname_goes_here",
                              True,
                              None,
                              None)

        self.assertIsNotNone(result)
        self.assertEqual(result.get('displayName'), 'test_group_delete_me')
        self.assertEqual(result.get('description'), 'A test group to delete')

        group_id = result.get('id')
        success = enable_teams_for_group(log, connection, group_id)

        self.assertTrue(success)

    @mock.patch("requests.put", side_effect=mocked_requests_get)
    def test_enable_teams_for_group_and_sleep(self, mockGet):
        log = logging.getLogger()
        connection = MockConnection()
        connection.logger = log

        group_id = "fake_group_id"
        with self.assertRaises(PluginException):
            enable_teams_for_group(log, connection, group_id)

        # verify 5 attempts were made to enable the team
        self.assertEqual(mockGet.call_count, 5)
        self.assertEqual(mockGet.call_args_list[0][0][0],
                         'https://graph.microsoft.com/v1.0/fake_tenant_id/groups/fake_group_id/team')
        self.assertEqual(mockGet.call_args_list[4][0][0],
                         'https://graph.microsoft.com/v1.0/fake_tenant_id/groups/fake_group_id/team')
