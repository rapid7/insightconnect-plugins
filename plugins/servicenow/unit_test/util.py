import json
import logging
import os

from icon_servicenow.connection.connection import Connection
from icon_servicenow.connection.schema import Input

INCIDENT_URL = "https://rapid7.service-now.com/api/now/table/incident"
JOURNAL_URL = "https://rapid7.service-now.com/api/now/table/sys_journal_field"
JOURNAL_FIELDS = "sys_id,sys_created_on,name,element_id,sys_tags,value,sys_created_by,element"


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.INSTANCE: "rapid7",
                Input.CLIENT_LOGIN: {"username": "user1", "password": "mypassword"},
                Input.CLIENT_ID: "blah",
                Input.CLIENT_SECRET: {"secretKey": "blah"},
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def read_file_to_bytes(filename):
        with open(filename, "rb") as my_file:
            return my_file.read()

    @staticmethod
    def read_file_to_dict(filename):
        return json.loads(Util.read_file_to_string(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)))

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code, headers=None):
                if headers is None:
                    headers = {"Content-Type": "application/json"}
                self.status_code = status_code
                self.headers = headers
                if filename:
                    self.content = Util.read_file_to_bytes(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.resp")
                    )
                    self.text = self.content.decode("UTF-8")

            def json(self):
                return json.loads(self.text)

        if kwargs["url"] in [
            "https://rapid7.service-now.com/api/now/attachment/b259f4062d9f78f9ffdd6efd05c492c7/file",
            "https://rapid7.service-now.com/api/now/attachment/52e4a8abb1b66fc04ba11001955e7dcb/file",
            "https://rapid7.service-now.com/api/now/attachment/53e4a8abb1b66fc04ba11001955e7dcb/file",
        ]:
            return MockResponse("get_attachment_file", 200, {})
        elif kwargs["url"] == "https://rapid7.service-now.com/oauth_token.do":
            return MockResponse("get_oauth_token.json", 200)
        elif (
            kwargs["url"]
            == "https://rapid7.service-now.com/api/now/attachment?sysparm_query=table_sys_id=3072d01d07a552f6d0ea83ef29c936be"
        ):
            return MockResponse("get_attachment_by_table_sys_id.json", 200)
        elif (
            kwargs["url"]
            == "https://rapid7.service-now.com/api/now/attachment?sysparm_query=table_sys_id=51e4a8abb1b66fc04ba11001955e7dcb"
        ):
            return MockResponse("get_attachment_by_table_sys_id_many.json", 200)
        elif (
            kwargs["url"]
            == "https://rapid7.service-now.com/api/now/attachment?sysparm_query=table_sys_id=c1565da4456c2df374793d471d6ae8dd"
        ):
            return MockResponse("get_attachment_by_table_sys_id_empty.json", 200)
        elif kwargs["url"] == "https://rapid7.service-now.com/api/sn_chg_rest/v1/change":
            return MockResponse("create_change_request.json", 200)
        elif kwargs["url"] in (
            "https://rapid7.service-now.com/api/now/table/sn_vul_vulnerable_item",
            "https://rapid7.service-now.com/api/now/table/sn_vul_vulnerable_item/12345",
        ):
            return MockResponse("create_vulnerability.json", 201)
        elif kwargs["url"] in ("https://rapid7.service-now.com/api/now/table/sn_vul_third_party_entry",):
            return MockResponse("create_third_party_vulnerability_entry.json", 201)

        elif kwargs.get("url") == "https://rapid7.service-now.com/api/now/table/sn_si_incident/d1234":
            return MockResponse("", 204)
        elif kwargs.get("url") == "https://rapid7.service-now.com/api/now/table/sn_si_incident/d12345":
            return MockResponse("delete_security_incident_invalid_sys_id.json", 404)

        elif kwargs.get("url") == "https://rapid7.service-now.com/api/now/table/sn_si_incident/g123456":
            return MockResponse("get_security_incident_success.json", 200)
        elif kwargs.get("url") == "https://rapid7.service-now.com/api/now/table/sn_si_incident/g1234567":
            return MockResponse("get_security_incident_invalid_sys_id.json", 404)
        elif kwargs.get("url") == "https://rapid7.service-now.com/api/now/table/sn_si_incident/invalid":
            return MockResponse("get_security_incident_invalid_sys_id.json", 404)
        elif (
            kwargs.get("url")
            == "https://rapid7.service-now.com/api/now/table/sn_si_incident/9de5069c5afe602b2ea0a04b66beb2c0"
        ):
            if kwargs.get("json") == {"short_description": "updated incident"}:
                return MockResponse("create_security_incident.json", 200)
            elif kwargs.get("json", {}).get("short_description") == "updated incident":
                return MockResponse("create_security_incident.json", 200)
        elif kwargs.get("url") == "https://rapid7.service-now.com/api/now/table/sn_si_incident":
            if kwargs.get("params") == {}:
                return MockResponse("search_security_incident_all.json", 200)
            elif kwargs.get("params") == {"sysparm_fields": "sys_id,number.priority"}:
                return MockResponse("search_security_incident_fields.json", 200)
            elif kwargs.get("params") == {"sysparm_query": "priority=3"}:
                return MockResponse("search_security_incident_query.json", 200)
            elif kwargs.get("params") == {"sysparm_limit": 1, "sysparm_offset": 1}:
                return MockResponse("search_security_incident_limit_offset.json", 200)
            elif kwargs.get("params") == {"sysparm_query": "number=SIR111111"}:
                return MockResponse("search_security_incident_empty_list.json", 200)
            elif kwargs.get("json") == {"short_description": "test incident"}:
                return MockResponse("create_security_incident.json", 200)
            elif kwargs.get("json", {}).get("short_description") == "new incident":
                return MockResponse("create_security_incident.json", 200)

        elif kwargs.get("url") == f"{JOURNAL_URL}?sysparm_query=element_id=j1&sysparm_fields={JOURNAL_FIELDS}":
            return MockResponse("get_incident_comments_worknotes_journal.json", 200)
        elif kwargs.get("url") in (
            f"{JOURNAL_URL}?sysparm_query=element_id=j2&sysparm_fields={JOURNAL_FIELDS}",
            f"{JOURNAL_URL}?sysparm_query=element_id=j2^element=comments&sysparm_fields={JOURNAL_FIELDS}",
            f"{JOURNAL_URL}?sysparm_query=element_id=j2^element=work_notes&sysparm_fields={JOURNAL_FIELDS}",
            f"{JOURNAL_URL}?sysparm_query=element_id=j3&sysparm_fields={JOURNAL_FIELDS}",
            f"{JOURNAL_URL}?sysparm_query=element_id=j4&sysparm_fields={JOURNAL_FIELDS}",
            f"{JOURNAL_URL}?sysparm_query=element_id=j5&sysparm_fields={JOURNAL_FIELDS}",
            f"{JOURNAL_URL}?sysparm_query=element_id=j7&sysparm_fields={JOURNAL_FIELDS}",
            f"{JOURNAL_URL}?sysparm_query=element_id=not-a-sys-id&sysparm_fields={JOURNAL_FIELDS}",
        ):
            return MockResponse("get_incident_comments_worknotes_journal_empty.json", 200)
        elif kwargs.get("url") == f"{JOURNAL_URL}?sysparm_query=element_id=j6&sysparm_fields={JOURNAL_FIELDS}":
            return MockResponse("get_incident_comments_worknotes_journal_forbidden.json", 403)

        elif kwargs.get("url") == f"{INCIDENT_URL}/j2":
            if kwargs.get("params") == {
                "sysparm_fields": "comments,work_notes",
                "sysparm_display_value": "true",
            }:
                return MockResponse("get_incident_comments_worknotes_incident_record.json", 200)
            elif kwargs.get("params") == {"sysparm_fields": "comments", "sysparm_display_value": "true"}:
                return MockResponse("get_incident_comments_worknotes_incident_record_comments.json", 200)
            elif kwargs.get("params") == {"sysparm_fields": "work_notes", "sysparm_display_value": "true"}:
                return MockResponse("get_incident_comments_worknotes_incident_record_work_notes.json", 200)
        elif kwargs.get("url") == f"{INCIDENT_URL}/j3":
            return MockResponse("get_incident_comments_worknotes_incident_record_empty.json", 200)
        elif kwargs.get("url") == f"{INCIDENT_URL}/j4":
            return MockResponse("get_incident_comments_worknotes_incident_not_found.json", 404)
        elif kwargs.get("url") == f"{INCIDENT_URL}/j5":
            return MockResponse("get_incident_comments_worknotes_login_page.html", 200, {})
        elif kwargs.get("url") == f"{INCIDENT_URL}/j7":
            # A field the caller cannot read is left out of the record, so a record asked for both
            # journal fields comes back holding only the one the caller is allowed to see.
            return MockResponse("get_incident_comments_worknotes_incident_record_comments.json", 200)

        raise Exception("Not implemented")
