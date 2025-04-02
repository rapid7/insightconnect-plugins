import functools
import json
import logging

import ldap3
from komand_active_directory_ldap import connection
from komand_active_directory_ldap.connection.schema import Input
from ldap3.core.connection import SyncStrategy
from ldap3.core.exceptions import (
    LDAPInvalidDnError,
    LDAPObjectClassError,
    LDAPOperationsErrorResult,
)
from ldap3.core.results import RESULT_OPERATIONS_ERROR, RESULT_SUCCESS


class MockConnection:
    RESULT = "result"
    DESCRIPTION = "description"
    SEARCH_RESULT = ""

    def __init__(self):
        self.result = {self.RESULT: RESULT_SUCCESS, self.DESCRIPTION: None}
        self.response = []
        self.check_names = True
        self.strategy = SyncStrategy(self)
        self.raise_exceptions = True

    def add(self, dn: str, object_class: [str], attributes: dict):
        self.result[self.RESULT] = RESULT_SUCCESS
        if attributes and attributes.get("run_error"):
            raise LDAPObjectClassError("Errors occurs")

    def default_modify(self, dn):
        if "CN=LDAPInvalidDnError,DC=example,DC=com" in dn:
            raise LDAPInvalidDnError("Some error")
        if "CN=wrong_result,DC=example,DC=com" in dn:
            self.result[self.RESULT] = RESULT_OPERATIONS_ERROR
            return

        self.result[self.RESULT] = RESULT_SUCCESS

    def modify(self, dn: str, changes: dict, controls=None):
        return self.default_modify(dn)

    def modify_dn(
        self, dn, relative_dn, delete_old_dn=True, new_superior=None, controls=None
    ):
        return self.default_modify(dn)

    def delete(self, dn: str, controls=None):
        self.result[self.RESULT] = RESULT_SUCCESS
        if "with_error" in dn:
            self.result[self.RESULT] = RESULT_OPERATIONS_ERROR
            self.result[self.DESCRIPTION] = "test description"

    def response_to_json(self):
        if self.result[self.DESCRIPTION] == "empty_search":
            return json.dumps({"entries": []})
        if MockConnection.SEARCH_RESULT == "empty_search":
            return json.dumps({"entries": []})
        if MockConnection.SEARCH_RESULT == "bad_response":
            return json.dumps({"entries": "bad response"})
        if MockConnection.SEARCH_RESULT == "no_response":
            return json.dumps({"entries": None})

        MockConnection.SEARCH_RESULT = ""
        return json.dumps({"entries": [{"dn": "DN=user"}]})

    def unbind(self):
        pass

    def search(
        self,
        search_base,
        search_filter,
        search_scope=ldap3.SUBTREE,
        dereference_aliases=ldap3.DEREF_ALWAYS,
        attributes=None,
    ):
        if "CN=LDAPInvalidDnError,DC=example,DC=com" in search_filter:
            raise LDAPInvalidDnError("Some error")
        if "CN=LDAPOperationsErrorResult,DC=example,DC=com" in search_filter:
            raise LDAPOperationsErrorResult("Some error")
        if "CN=wrong_result,DC=example,DC=com" in search_filter:
            self.result[self.RESULT] = RESULT_OPERATIONS_ERROR
            return
        if (
            "CN=empty_search,DC=example,DC=com" in search_filter
            or "CN=empty_search,DC=example,DC=com" in search_base
        ):
            self.result[self.DESCRIPTION] = "empty_search"
            return
        if "CN=empty_group,DC=example,DC=com" in search_base:
            self.result[self.DESCRIPTION] = "failed"
            return

        self.result[self.RESULT] = RESULT_SUCCESS
        self.result[self.DESCRIPTION] = "success"
        self.response = [
            {"dn": search_base, "attributes": {"userAccountControl": False}}
        ]

    class extend:
        class standard:
            @staticmethod
            def paged_search(
                search_base, search_filter, attributes, paged_size, generator
            ):
                if "CN=empty_search,DC=example,DC=com" in search_base:
                    MockConnection.SEARCH_RESULT = "empty_search"
                    return
                if "CN=bad_response,DC=example,DC=com" in search_base:
                    MockConnection.SEARCH_RESULT = "bad_response"
                    return
                if "CN=no_response,DC=example,DC=com" in search_base:
                    MockConnection.SEARCH_RESULT = "no_response"
                    return

                MockConnection.SEARCH_RESULT = RESULT_SUCCESS


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
                Input.USE_SSL: True,
                Input.USERNAME_PASSWORD: {"username": "bob", "password": "foobar"},
            }
        )


def default_connector(action):
    def connect(func):
        @functools.wraps(func)
        def wrapper_connect(*args, **kwargs):
            default_connection = DefaultConnection()
            default_connection.connect()
            action.connection = default_connection.conn
            return func(action=action, *args, **kwargs)

        return wrapper_connect

    return connect
