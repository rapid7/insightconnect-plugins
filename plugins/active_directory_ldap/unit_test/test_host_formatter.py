import logging
from unittest import TestCase, mock

from komand_active_directory_ldap import connection
from komand_active_directory_ldap.connection.schema import Input
from komand_active_directory_ldap.util.api import ActiveDirectoryLdapAPI
from unit_test.common import MockConnection
from unit_test.common import MockServer


class TestHostFormatter(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection))
    def test_connection(self):
        params = {
            Input.HOST: "ldaps://12.12.12.12",
            Input.PORT: 345,
            Input.USE_SSL: False,
            Input.USERNAME_PASSWORD: {"username": "bob", "password": "foobar"},
        }
        conn = connection.Connection()
        conn.logger = logging.getLogger("test_connection")
        conn.connect(params)

    def test_host_formatter(self):
        host_types = [
            "10.10.10.10",
            "11.11.11.11:345",
            "ldap://12.12.12.12",
            "ldaps://13.13.13.13",
            "ldap://14.14.14.14:345",
            "ldaps://15.15.15.15:345",
            "mydomain.com",
            "mydomain.com:345",
            "ldap://mydomain.com",
            "ldaps://mydomain.com",
            "ldap://mydomain.com:345",
            "ldaps://mydomain.com:345",
            "mydomain.com/stuff",
            "mydomain.com/stuff:345",
            "ldap://mydomain.com/stuff",
            "ldaps://mydomain.com/stuff",
            "ldap://mydomain.com/stuff:345",
            "ldaps://mydomain.com/stuff:345",
        ]
        output = list()
        conn = ActiveDirectoryLdapAPI(None, None)
        conn.logger = logging.getLogger("test_host_formatter")
        for item in host_types:
            output.append(conn.host_formatter(item))
        self.assertEqual(
            output,
            [
                "10.10.10.10",
                "11.11.11.11",
                "12.12.12.12",
                "13.13.13.13",
                "14.14.14.14",
                "15.15.15.15",
                "mydomain.com",
                "mydomain.com",
                "mydomain.com",
                "mydomain.com",
                "mydomain.com",
                "mydomain.com",
                "mydomain.com",
                "mydomain.com",
                "mydomain.com",
                "mydomain.com",
                "mydomain.com",
                "mydomain.com",
            ],
        )
