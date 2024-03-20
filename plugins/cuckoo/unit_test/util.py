from komand_cuckoo.connection import Connection
from komand_cuckoo.connection.schema import Input
import insightconnect_plugin_runtime
import json
import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

STUB_URL = "http://0.0.0.0:0000"


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.URL: STUB_URL
        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r", encoding="utf-8"
        ) as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_dict(filename: str) -> dict:
        return json.loads(Util.read_file_to_string(filename))

    @staticmethod
    def mock_request(*args, **kwargs):
        url = kwargs.get("url")
        # Cuckoo Status
        if url == f"{STUB_URL}/cuckoo/status":
            return MockResponse(200, "cuckoo_status_success.json.resp")
        # Delete Task
        if url == f"{STUB_URL}/tasks/delete/1":
            return MockResponse(200, "delete_task_success.json.resp")
        # Exit
        if url == f"{STUB_URL}/exit":
            return MockResponse(200, "exit_success.json.resp")
        # Get File
        if url == f"{STUB_URL}/files/get/1":
            return MockResponse(200, "get_file_success.json.resp")
        # Get Memory
        if url == f"{STUB_URL}/memory/get/1/1":
            return MockResponse(200, "get_memory_success.json.resp")
        # Get PCAP
        if url == f"{STUB_URL}/pcap/get/1":
            return MockResponse(200, "get_pcap_success.json.resp")
        # Get Report
        if url == f"{STUB_URL}/tasks/report/1/json":
            return MockResponse(200, "get_report_success.json.resp")
        # Get Screenshots
        if url == f"{STUB_URL}/tasks/screenshots/1/1":
            return MockResponse(200, "get_screenshots_success.json.resp")
        # List Machines
        if url == f"{STUB_URL}/machines/list":
            return MockResponse(200, "list_machines_success.json.resp")
        # List Memory
        if url == f"{STUB_URL}/memory/list/1":
            return MockResponse(200, "list_memory_success.json.resp")
        # List Tasks
        if url == f"{STUB_URL}/tasks/list/1/1":
            return MockResponse(200, "list_tasks_success.json.resp")
        # Reboot Task
        if url == f"{STUB_URL}/tasks/reboot/1":
            return MockResponse(200, "reboot_task_success.json.resp")
        # Rerun Report
        if url == f"{STUB_URL}/tasks/rereport/1":
            return MockResponse(200, "rerun_report_success.json.resp")
        # Reschedule Task
        if url == f"{STUB_URL}/tasks/reschedule/1/1":
            return MockResponse(200, "reschedule_task_success.json.resp")
        # Submit Files
        if url == f"{STUB_URL}/tasks/create/file":
            return MockResponse(200, "submit_files_success.json.resp")
        # Submit URL
        if url == f"{STUB_URL}/tasks/create/url":
            return MockResponse(200, "submit_url_success.json.resp")
        # View File
        if url == f"{STUB_URL}/files/view/id/1":
            return MockResponse(200, "view_file_success.json.resp")
        if url == f"{STUB_URL}/files/view/sha256/275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f":
            return MockResponse(200, "view_file_success.json.resp")
        if url == f"{STUB_URL}/files/view/md5/9de5069c5afe602b2ea0a04b66beb2c0":
            return MockResponse(200, "view_file_success.json.resp")
        # View Machine
        if url == f"{STUB_URL}/machines/view/machine":
            return MockResponse(200, "view_machine_success.json.resp")
        # View Task
        if url == f"{STUB_URL}/tasks/view/1":
            return MockResponse(200, "view_task_success.json.resp")
        # VPN Status
        if url == f"{STUB_URL}/vpn/status":
            return MockResponse(200, "vpn_status_success.json.resp")
        # Error Handling
        if url == f"{STUB_URL}/machines/view/fourhundred":
            return MockResponse(400, "error.json.resp")
        if url == f"{STUB_URL}/machines/view/fourhundredandone":
            return MockResponse(401, "error.json.resp")
        if url == f"{STUB_URL}/machines/view/fourhundredandthree":
            return MockResponse(403, "error.json.resp")
        if url == f"{STUB_URL}/machines/view/fourhundredandfour":
            return MockResponse(404, "error.json.resp")
        if url == f"{STUB_URL}/machines/view/fourhundredandeighteen":
            return MockResponse(418, "error.json.resp")
        if url == f"{STUB_URL}/machines/view/fivehundred":
            return MockResponse(500, "error.json.resp")
        if url == f"{STUB_URL}/machines/view/threehundredandone":
            return MockResponse(301, "error.json.resp")
        raise NotImplementedError("Not implemented", kwargs)


class MockResponse:
    def __init__(self, status_code: int, filename: str = None, headers: dict = {}):
        self.status_code = status_code
        self.text = ""
        self.headers = headers
        if filename:
            self.text = Util.read_file_to_string(f"responses/{filename}")
            self.content = bytes(Util.read_file_to_string(f"responses/{filename}"), "utf-8")

    def json(self):
        return json.loads(self.text)
