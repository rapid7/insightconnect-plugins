from komand_active_directory_ldap import connection
from komand_active_directory_ldap.connection.schema import Input
import logging
from ldap3.core.exceptions import LDAPObjectClassError
from ldap3.core.results import RESULT_SUCCESS


class MockConnection:
    def __init__(self):
        self.result = RESULT_SUCCESS

    def add(self, dn: str, object_class: [str], attributes: dict):
        self.result = RESULT_SUCCESS
        if attributes and attributes.get("run_error"):
            raise LDAPObjectClassError("Errors occurs")

    def modify(self, dn: str, changes: dict, controls=None):
        self.result = RESULT_SUCCESS
        pass


class MockServer:
    def __init__(self, host, port, use_ssl, get_info):
        self.host = host
        self.port = port
        self.use_ssl = use_ssl
        self.get_info = get_info


class DefaultConnection:
    def __init__(self):
        self.conn = connection.Connection()
        self.conn.logger = logging.getLogger("test_connection")

    def connect(self):
        self.conn.connect(
            {
                Input.HOST: "ldaps://12.12.12.12",
                Input.PORT: 345,
                Input.USE_SSL: False,
                Input.USERNAME_PASSWORD: {"username": "bob", "password": "foobar"},
            }
        )
