from unittest import TestCase, mock
from komand_active_directory_ldap.actions.add_user import AddUser
from komand_active_directory_ldap.actions.add_user.schema import Input, Output
from .common import MockServer
from .common import MockConnection
from .common import DefaultConnection
from komand.exceptions import PluginException


class TestHostFormatter(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    def test_add_user(self):
        default_connection = DefaultConnection()
        default_connection.connect()

        add_user = AddUser()
        add_user.connection = default_connection.conn
        results = add_user.run(
            {
                Input.DOMAIN_NAME: "example.com",
                Input.FIRST_NAME: "firstname",
                Input.LAST_NAME: "lastname",
                Input.USER_OU: "CN=Users",
            }
        )

        self.assertEqual(results, {Output.SUCCESS: True})

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    def test_add_user_raise(self):
        default_connection = DefaultConnection()
        default_connection.connect()

        add_user = AddUser()
        add_user.connection = default_connection.conn
        with self.assertRaises(PluginException) as context:
            add_user.run(
                {
                    Input.DOMAIN_NAME: "example.com",
                    Input.FIRST_NAME: "firstname",
                    Input.LAST_NAME: "lastname",
                    Input.USER_OU: "CN=Users",
                    Input.ADDITIONAL_PARAMETERS: {"run_error": True},
                }
            )

        self.assertTrue("LDAP returned an error message." in context.exception.cause)
        self.assertTrue("Creating new user failed, error returned by LDAP." in context.exception.assistance)
