from unittest import TestCase, mock
from komand_active_directory_ldap import connection
import logging


class MockServer:
    def __init__(self, host, port, use_ssl, get_info):
        self.host = host
        self.port = port
        self.use_ssl = use_ssl
        self.get_info = get_info


class MockConnection:
    def __init__(self, server, user, password, auto_encode, auto_escape, auto_bind, auto_referrals, authentication):
        self.server = server
        self.user = user


class TestHostFormatter(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection))
    def test_connection(self):
        params = {
            "host": "ldaps://12.12.12.12",
            "port": 345,
            "use_ssl": False,
            "username_and_password": {"username": "bob", "password": "foobar"},
        }
        logger = logging.getLogger("logger")
        conn = connection.Connection()
        conn.logger = logger
        conn.connect(params)

    def test_host_formatter(self):
        host_types = [
            "10.10.10.10",
            "11.11.11.11:345",
            "ldaps://12.12.12.12",
            "ldaps://14.14.14.14:345",
            "mydomain.com",
            "mydomain.com:345",
            "ldaps://mydomain.com",
            "ldaps://mydomain.com:345",
            "mydomain.com/stuff",
            "mydomain.com/stuff:345",
            "ldaps://mydomain.com/stuff",
            "ldaps://mydomain.com/stuff:345",
        ]
        output = list()
        conn = connection.Connection()
        for item in host_types:
            output.append(conn.host_formatter(item))
        self.assertEqual(
            output,
            [
                "10.10.10.10",
                "11.11.11.11",
                "12.12.12.12",
                "14.14.14.14",
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
