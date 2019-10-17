from unittest import TestCase
from komand.exceptions import PluginException
from komand_box.actions.user_info_from_login import UserInfoFromLogin
import logging


class MockUser():
    def __init__(self):
        self.address = "FAKE"
        self.avatar_url = "FAKE"
        self.id = "8830457340"
        self.job_title = "FAKE"
        self.login = "randomtestuser@somerandomdomain.com"
        self.name = "FAKE"
        self.phone = "FAKE"
        self.space_amount = "FAKE"
        self.space_used = "FAKE"
        self.timezone = "FAKE"


class MockBoxConnection():
    def __init__(self):
        pass

    def users(self, filter_term):
        if filter_term == 'randomtestuser@somerandomdomain.com':
            return [MockUser()]
        else:
            return None


class MockConnection():
    def __init__(self):
        self.box_connection = MockBoxConnection()


class TestUserInfoFromLogin(TestCase):
    def setUp(self) -> None:
        pass

    def test_get_user_info(self):
        log = logging.getLogger("Test Logger")

        user_info = UserInfoFromLogin()
        user_info.connection = MockConnection()
        user_info.logger = log

        actual = user_info.run({"login": "randomtestuser@somerandomdomain.com"})

        self.assertEqual('8830457340', actual.get('id'))
        self.assertEqual('randomtestuser@somerandomdomain.com', actual.get('login'))

    def test_get_user_info_not_found(self):
        log = logging.getLogger("Test Logger")

        user_info = UserInfoFromLogin()
        user_info.connection = MockConnection()
        user_info.logger = log

        with self.assertRaises(PluginException):
            user_info.run({"login": "dontfindme@somefakedomain.com"})


