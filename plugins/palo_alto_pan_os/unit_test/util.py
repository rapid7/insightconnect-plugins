import logging
import os
import sys

from komand_palo_alto_pan_os.connection.connection import Connection
from komand_palo_alto_pan_os.connection.schema import Input

sys.path.append(os.path.abspath("../"))


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.SERVER: "https://example.com",
            Input.CREDENTIALS: {"password": "password", "username": "user"},
            Input.VERIFY_CERT: True,
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
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code) -> None:
                self.filename = filename
                self.status_code = status_code
                self.text = self.load_data()

            def load_data(self):
                return Util.read_file_to_string(
                    os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.resp")
                )

        params = kwargs.get("params", {})
        job_id = params.get("job-id")
        log_type = params.get("log-type")
        element = params.get("element")
        action = params.get("action")
        xpath = params.get("xpath")
        cmd = params.get("cmd")

        if params == {"type": "keygen", "user": "user", "password": "password"}:
            return MockResponse("key", 200)
        if log_type == "config":
            return MockResponse("get_job_id", 200)
        if log_type == "system":
            return MockResponse("get_job_id2", 200)
        if log_type == "threat":
            return MockResponse("get_job_id3", 200)
        if log_type == "traffic":
            return MockResponse("get_job_id4", 200)
        if job_id == "1":
            return MockResponse("get_config_logs", 200)
        if job_id == "2":
            return MockResponse("get_system_logs", 200)
        if job_id == "3":
            return MockResponse("get_threat_logs", 200)
        if job_id == "4":
            return MockResponse("get_traffic_logs", 200)
        if cmd == "<commit></commit>":
            return MockResponse("commit", 200)
        if cmd == "<commit><partial><admin><member>admin-name</member></admin></partial></commit>":
            return MockResponse("commit2", 200)
        if cmd == "<show><jobs><id>1</id></jobs></show>":
            return MockResponse("op", 200)
        if cmd == "<show><commit-locks/></show>":
            return MockResponse("op2", 200)
        if (
            action == "get"
            and xpath
            == "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address/entry[@name='1.1.1.1']"
        ):
            return MockResponse("get_object_ipv4", 200)
        if (
            action == "get"
            and xpath
            == "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address/entry[@name='IPv6']"
        ):
            return MockResponse("get_object_ipv6", 200)
        if (
            action == "get"
            and xpath
            == "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address/entry[@name='test.com']"
        ):
            return MockResponse("get_object_domain", 200)
        if (
            action == "get"
            and xpath
            == "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address-group/entry[@name='Test Group']"
        ):
            return MockResponse("get_objects_from_group", 200)
        if (
            action == "get"
            and xpath
            == "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address-group/entry[@name='Invalid Group']"
        ):
            return MockResponse("get_objects_from_group_bad", 200)
        if (
            action == "show"
            and xpath
            == "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address-group/entry[@name='Test Group']"
        ):
            return MockResponse("show_group", 200)
        if (
            action == "get"
            and xpath
            == '/config/devices/entry[@name="localhost.localdomain"]/vsys/entry[@name="vsys1"]/rulebase/security/rules/entry[@name="Test Policy"]'
        ):
            return MockResponse("get_policy", 200)
        if (
            action == "get"
            and xpath
            == "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase/security/rules/entry[@name='Test Rule']"
        ):
            return MockResponse("get_policy2", 200)
        if (
            action == "get"
            and xpath
            == '/config/devices/entry[@name="localhost.localdomain"]/vsys/entry[@name="vsys1"]/rulebase/security/rules/entry[@name="Invalid Policy"]'
        ):
            return MockResponse("get_policy_bad", 200)
        if (
            action in ["get", "show"]
            and xpath == "/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='Test Policy']"
        ):
            return MockResponse("get_policy", 200)
        if (
            action in ["get", "show"]
            and xpath == "/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='Invalid Rule Name']"
        ):
            return MockResponse("invalid_rule_name", 200)
        if (
            action == "edit"
            and element
            == '<entry name="Test Policy"><to><member>any</member></to><from><member>any</member></from><source><member>any</member></source><destination><member>any</member></destination><service><member>application-default</member><member>any</member></service><application><member>any</member></application><category><member>adult</member><member>abused-drugs</member><member>test1</member></category><hip-profiles><member>any</member></hip-profiles><source-user><member>Joe Smith</member></source-user><action>drop</action></entry>'
        ):
            return MockResponse("invalid_url_category_parameter", 200)
        if action in ["edit", "set", "delete"]:
            return MockResponse("successful", 200)

        raise Exception("Not implemented")
