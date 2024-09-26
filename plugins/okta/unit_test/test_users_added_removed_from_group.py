import os
import sys

import timeout_decorator

sys.path.append(os.path.abspath("../"))

from typing import Callable, Optional
from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate
from komand_okta.triggers.users_added_removed_from_group import UsersAddedRemovedFromGroup
from komand_okta.triggers.users_added_removed_from_group.schema import Input, UsersAddedRemovedFromGroupOutput

from util import Util


def timeout_pass(error_callback: Optional[Callable] = None):
    def func_timeout(func):
        def func_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except timeout_decorator.timeout_decorator.TimeoutError:
                if error_callback:
                    return error_callback()
                return None

        return func_wrapper

    return func_timeout


class MockTrigger:
    actual = None

    @staticmethod
    def send(params):
        MockTrigger.actual = params


def check_error():
    expected = Util.read_file_to_dict("expected/users.json.exp")
    validate(MockTrigger.actual, UsersAddedRemovedFromGroupOutput.schema)
    if MockTrigger.actual == expected:
        return True
    TestCase.assertDictEqual(TestCase(), MockTrigger.actual, expected)


@patch("requests.request", side_effect=Util.mock_request)
class TestUsersAddedRemovedFromGroup(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UsersAddedRemovedFromGroup())

    @timeout_pass(error_callback=check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    def test_users_added_removed_from_group_some_function_to_test(
        self, mock_request: MagicMock, mock_send: MockTrigger
    ) -> None:
        self.action.run({Input.GROUPIDS: ["12345"], Input.INTERVAL: 10})
