from unittest import TestCase, mock

from komand_active_directory_ldap.actions.move_object import MoveObject
from komand_active_directory_ldap.actions.move_object.schema import Input, Output

from common import MockConnection, MockServer, default_connector


class TestActionMoveObject(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=MoveObject())
    def test_move_object(self, action):
        actual = action.run({Input.DISTINGUISHED_NAME: "CN=Users,DC=example,DC=com"})
        expected = {Output.SUCCESS: True}

        self.assertEqual(actual, expected)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=MoveObject())
    def test_move_object_false(self, action):
        actual = action.run(
            {Input.DISTINGUISHED_NAME: "CN=wrong_result,DC=example,DC=com"}
        )
        expected = {Output.SUCCESS: False}

        self.assertEqual(actual, expected)
