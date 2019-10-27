from unittest import TestCase

from komand.exceptions import PluginException

from komand_box.actions.get_user_groups import GetUserGroups
from komand_box.connection.connection import Connection
import logging


class MockBoxResponse():
    def __init__(self):
        self.ok = True
        self.content = b'{"entries":[{"group":{"name": "bloop"}}, {"group":{"name": "blah"}}]}'


class MockBoxConnection():
    def __init__(self):
        pass

    def make_request(self, type, url):
        if "8830457340" in url:
            return MockBoxResponse()
        else:
            response = MockBoxResponse()
            response.ok = False
            return response


class MockConnection():
    def __init__(self):
        self.box_connection = MockBoxConnection()


class TestGetUserGroups(TestCase):
    def setUp(self) -> None:
        pass

    def test_get_user_groups(self):
        log = logging.getLogger("Test Logger")

        user_info = GetUserGroups()
        user_info.connection = MockConnection()
        user_info.logger = log

        actual_output = user_info.run({"user_id": "8830457340"})

        actual = actual_output.get("groups")

        self.assertEqual(2, len(actual))
        self.assertEqual('bloop', actual[0].get('name'))
        self.assertEqual('blah', actual[1].get('name'))

    def test_get_user_groups_not_found(self):
        log = logging.getLogger("Test Logger")

        user_info = GetUserGroups()
        user_info.connection = MockConnection()
        user_info.logger = log

        with self.assertRaises(PluginException):
            user_info.run({"user_id": "666"})

    def test_real_connection_get_user_groups(self):
        pass
        # log = logging.getLogger("Test Logger")
        #
        # connection_params = {
        #     #  Copy connection parameters here
        # }
        #
        # user_info = GetUserGroups()
        # user_info.connection = Connection()
        # user_info.logger = log
        # user_info.connection.logger = log
        # user_info.connection.connect(connection_params)
        #
        # # 8624955246 - No groups
        # params = {
        #     "user_id": "8830457340"
        # }
        #
        # actual = user_info.run(params)
        #
        # #  Set breakpoint here
        # self.assertEqual(actual, "")




