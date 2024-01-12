import json
import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

import insightconnect_plugin_runtime
from icon_cylance_protect.connection.connection import Connection
from icon_cylance_protect.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action, params: dict = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if not params:
            params = {
                Input.APPLICATION_ID: {"secretKey": "example-application-id"},
                Input.APPLICATION_SECRET: {"secretKey": "example-secret-key"},
                Input.TENANT_ID: {"secretKey": "example-tenant_id"},
                Input.URL: "URL",
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
        class MockResponse:
            def __init__(self, status_code: int, json_object: str = ""):
                self.status_code = status_code
                self.text = json.dumps(json_object)
                self.content = json.dumps(json_object)
                self.json_object = json_object

            def json(self):
                return self.json_object

        params = kwargs.get("params", {})
        data = kwargs.get("data", {})
        payload = kwargs.get("json", {})
        url = args[1]
        method = args[0]

        if url == "URL/globallists/v2":
            if method == "POST":
                if payload.get("reason") == "valid":
                    return MockResponse(200, {})
                elif payload.get("reason") == "invalid":
                    return MockResponse(200, ["error from the api"])

            elif args[0] == "DELETE":
                if payload.get("sha256") == "232cdf149baf0b1fd8cfddd940f5cbdf4142a7be387e57187b1aaedd238b1328":
                    return MockResponse(200, {})
                elif payload.get("sha256") == "232cdf149baf0b1fd8cfddd940f5cbdf4142a7be387e57187b1aaedd238b1329":
                    return MockResponse(200, ["error from the api"])

        elif url == "URL/devices/v2/1abc234d-5efa-6789-bcde-0f1abcde23f5":
            return MockResponse(
                200,
                {
                    "agent_version": "2.0.1540",
                    "date_found": "2020-05-29T10:12:45",
                    "file_path": "C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe",
                    "file_status": "Default",
                    "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                    "ip_addresses": ["1.1.1.1"],
                    "mac_addresses": ["00-60-26-26-D5-19"],
                    "name": "Example-Hostname",
                    "policy_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                    "state": "OffLine",
                },
            )

        elif url == "URL/devices/v2/macaddress/00-60-26-26-D5-19":
            return MockResponse(
                200,
                [
                    {
                        "agent_version": "2.0.1540",
                        "date_found": "2020-05-29T10:12:45",
                        "file_path": "C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe",
                        "file_status": "Default",
                        "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                        "ip_addresses": ["1.1.1.1"],
                        "mac_addresses": ["00-60-26-26-D5-19"],
                        "name": "Example-Hostname",
                        "policy_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                        "state": "OffLine",
                    }
                ],
            )

        elif url == "URL/devices/v2/hostname/hostname":
            return MockResponse(
                200,
                [
                    {
                        "agent_version": "2.0.1540",
                        "date_found": "2020-05-29T10:12:45",
                        "file_path": "C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe",
                        "file_status": "Default",
                        "id": "1abc234d-5efa-6789-bcde-0f1abcde23f6",
                        "ip_addresses": ["1.1.1.2"],
                        "mac_addresses": ["00-60-26-26-D5-19"],
                        "name": "Example-Hostname",
                        "policy_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                        "state": "OffLine",
                    }
                ],
            )

        elif url == "URL/devices/v2/hostname/bad_hostname":
            return MockResponse(
                200,
                [
                    {
                        "agent_version": "2.0.1540",
                        "date_found": "2020-05-29T10:12:45",
                        "file_path": "C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe",
                        "file_status": "Default",
                        "id": "1abc234d-5efa-6789-bcde-0f1abcde23f9",
                        "ip_addresses": ["1.1.1.2"],
                        "mac_addresses": ["00-60-26-26-D5-19"],
                        "name": "Example-Hostname",
                        "policy_id": "1abc234d-5efa-6789-bcde-0f1abcde23f9",
                        "state": "OffLine",
                    }
                ],
            )

        elif url == "URL/devices/v2/hostname/invalid_hostname":
            return MockResponse(404, [])

        elif url == "URL/devices/v2/hostname/invalid_post":
            return MockResponse(
                200,
                [
                    {
                        "agent_version": "2.0.1540",
                        "date_found": "2020-05-29T10:12:45",
                        "file_path": "C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe",
                        "file_status": "Default",
                        "id": "1abc234d-5efa-6789-bcde-0f1abcde23f9",
                        "ip_addresses": ["1.1.1.2"],
                        "mac_addresses": ["00-60-26-26-D5-19"],
                        "name": "Example-Hostname",
                        "policy_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                        "state": "OffLine",
                    }
                ],
            )

        elif url == "URL/devices/v2":
            if method == "DELETE":
                if "1abc234d-5efa-6789-bcde-0f1abcde23f5" in payload.get("device_ids", []):
                    return MockResponse(200, {"success": True})
                elif "1abc234d-5efa-6789-bcde-0f1abcde23f6" in payload.get("device_ids", []):
                    return MockResponse(200, {"success": True})
                elif "1abc234d-5efa-6789-bcde-0f1abcde23f9" in payload.get("device_ids", []):
                    return MockResponse(200, "")

        elif url in [
            "URL/devicecommands/v2/1ABC234D5EFA6789BCDE0F1ABCDE23F5/lockdown?value=true",
            "URL/devicecommands/v2/1ABC234D5EFA6789BCDE0F1ABCDE23F6/lockdown?value=true",
        ]:
            return MockResponse(
                200,
                {
                    "status": "COMPLETE",
                    "data": {
                        "id": "1ABC234D5EFA6789BCDE0F1ABCDE23F5",
                        "hostname": "Example-Hostname",
                        "tenant_id": "1abc234d5efa6789bcde0f1abcde23f5",
                        "connection_status": "locked",
                        "optics_device_version": "2.4.2100.1015",
                        "password": "unlock-pa22-w0rd",
                        "lockdown_expiration": "2020-07-11T21:15:29Z",
                        "lockdown_initiated": "2020-07-08T21:15:29Z",
                    },
                },
            )

        elif url == "URL/devices/v2?page=1?page_size=20":
            return MockResponse(
                200,
                {
                    "total_pages": 1,
                    "page_items": [
                        {
                            "agent_version": "2.0.1540",
                            "date_found": "2020-05-29T10:12:45",
                            "file_path": "C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe",
                            "file_status": "Default",
                            "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                            "ip_addresses": ["1.1.1.1"],
                            "mac_addresses": ["00-60-26-26-D5-19"],
                            "name": "hostname",
                            "policy_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                            "state": "OffLine",
                        }
                    ],
                },
            )

        elif url == "URL/devices/v2?page=2?page_size=20":
            return MockResponse(
                200,
                {
                    "total_pages": 0,
                    "page_items": [],
                },
            )

        elif url == "URL/threats/v2?page=1&page_size=100":
            return MockResponse(
                200,
                {
                    "total_pages": 1,
                    "page_items": [
                        {
                            "classification": "Malware",
                            "cylance_score": -1,
                            "file_size": 109395,
                            "global_quarantined": False,
                            "last_found": "2020-05-29T10:12:45",
                            "md5": "938C2CC0DCC05F2B68C4287040CFCF71",
                            "name": "honeyhashx86.exe",
                            "safelisted": False,
                            "sha256": "5FEDAEBE1C409A201C01053FE95DA99CF19F9999F0A5CA39BE93DE34488B9D80",
                            "sub_classification": "Exploit",
                            "unique_to_cylance": False,
                        },
                        {
                            "classification": "Malware",
                            "cylance_score": -1,
                            "file_size": 109395,
                            "global_quarantined": False,
                            "last_found": "2020-05-29T10:12:45",
                            "md5": "938C2CC0DCC05F2B68C4287040CFCF76",
                            "name": "honeyhashx86.exe",
                            "safelisted": False,
                            "sha256": "5FEDAEBE1C409A201C01053FE95DA99CF19F9999F0A5CA39BE93DE34488B9D86",
                            "sub_classification": "Exploit",
                            "unique_to_cylance": False,
                        },
                    ],
                },
            )

        elif (
            url
            == "URL/threats/v2/5FEDAEBE1C409A201C01053FE95DA99CF19F9999F0A5CA39BE93DE34488B9D80/devices?page=1?page_size=200"
        ):
            return MockResponse(
                200,
                {
                    "total_pages": 1,
                    "page_items": [
                        {
                            "agent_version": "2.0.1540",
                            "date_found": "2020-05-29T10:12:45",
                            "file_path": "C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe",
                            "file_status": "Default",
                            "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                            "ip_addresses": ["1.1.1.1"],
                            "mac_addresses": ["00-60-26-26-D5-19"],
                            "name": "hostname",
                            "policy_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                            "state": "OffLine",
                        }
                    ],
                },
            )

        elif url == "URL/policies/v2?page=1":
            return MockResponse(
                200,
                {
                    "total_pages": 1,
                    "page_items": [
                        {
                            "date_added": "2020-05-29T10:12:45",
                            "date_modified": "2020-05-29T10:12:45",
                            "device_count": 1,
                            "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
                            "name": "policy 1",
                        },
                        {
                            "date_added": "2020-05-29T10:12:45",
                            "date_modified": "2020-05-29T10:12:45",
                            "device_count": 1,
                            "id": "1abc234d-5efa-6789-bcde-0f1abcde23f9",
                            "name": "Default",
                        },
                    ],
                },
            )

        elif url in [
            "URL/devices/v2/1abc234d-5efa-6789-bcde-0f1abcde23f6/threats",
            "URL/devices/v2/1abc234d-5efa-6789-bcde-0f1abcde23f5/threats",
            "URL/devices/v2/1abc234d-5efa-6789-bcde-0f1abcde23f6",
        ]:
            return MockResponse(200, {})

        elif url == "URL/devices/v2/1abc234d-5efa-6789-bcde-0f1abcde23f9":
            return MockResponse(200, ["error from the api"])

        raise Exception("Not implemented")

    @staticmethod
    def mock_generate_token(*args, **kwargs):
        return "fake_token"

    @staticmethod
    def mock_find_agent_by_ip(*args, **kwargs):
        if args[1] == "1.1.1.1":
            return "1abc234d-5efa-6789-bcde-0f1abcde23f5"
        else:
            return args[1]
