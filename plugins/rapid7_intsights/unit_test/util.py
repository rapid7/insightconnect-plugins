import json
import logging
import sys
import os

from icon_rapid7_intsights.connection import Connection
from icon_rapid7_intsights.connection.schema import Input

sys.path.append(os.path.abspath("../"))


class Util:
    request_count = 0

    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {Input.ACCOUNT_ID: {"secretKey": "account_id"}, Input.API_KEY: {"secretKey": "api_key"}}
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def read_file_to_dict(filename):
        return json.loads(Util.read_file_to_string(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)))

    @staticmethod
    def mock_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                if filename:
                    self.text = Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.json.resp")
                    )
                else:
                    self.text = ""

            def json(self):
                return json.loads(self.text)

        if (
            kwargs.get("url") == "https://api.intsights.com/public/v1/test-credentials"
            and kwargs.get("auth").username == "wrong"
        ):
            return MockResponse(401)
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/test-credentials":
            return MockResponse(200)
        elif kwargs.get("url") == "https://api.intsights.com/public/v2/iocs/ioc-by-value?iocValue=rapid7.com":
            return MockResponse(200, "iocs_ioc-by-value")
        elif (
            kwargs.get("url") == "https://api.intsights.com/public/v1/iocs/enrich/rapid7.com"
            and Util.request_count == 0
        ):
            Util.request_count = Util.request_count + 1
            return MockResponse(200, "enrich_indicator-in_progress")
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/iocs/enrich/rapid7.com":
            return MockResponse(200, "enrich_indicator")
        elif kwargs.get("url") == "https://api.intsights.com/public/v2/iocs/ioc-by-value?iocValue=empty":
            return MockResponse(204)
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/data/alerts/add-alert":
            return MockResponse(200, "add_manual_alert")
        elif (
            kwargs.get("url") == "https://api.intsights.com/public/v1/data/alerts/alerts-list"
            and kwargs.get("params", {}).get("alertType") == "Phishing"
        ):
            return MockResponse(200, "get_alerts_empty_list")
        elif (
            kwargs.get("url") == "https://api.intsights.com/public/v1/data/alerts/alerts-list"
            and kwargs.get("params", {}).get("alertType") == "Phishing,AttackIndication"
        ):
            return MockResponse(200, "get_alerts_with_types_list")
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/data/alerts/alerts-list":
            return MockResponse(200, "get_alerts")
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/data/alerts/get-complete-alert/123":
            return MockResponse(200, "get_complete_alert_by_id")
        elif (
            kwargs.get("url") == "https://api.intsights.com/public/v1/iocs/rescan"
            and kwargs.get("json", {}).get("IocValue") == "bad"
        ):
            return MockResponse(200, "rescan_indicator.bad")
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/iocs/rescan/status/abcdefg123456":
            return MockResponse(200, "get_indicator_scan_status")
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/iocs/rescan/status/bad":
            return MockResponse(200, "get_indicator_scan_status.bad")
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/iocs/rescan":
            return MockResponse(200, "rescan_indicator")
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/cves/get-cves-list" and kwargs.get("params").get(
            "cveId[]"
        ) == ["CVE-2020-7064"]:
            return MockResponse(200, "get_cve_by_id")
        elif (
            kwargs.get("url") == "https://api.intsights.com/public/v1/cves/get-cves-list"
            and kwargs.get("params").get("cveId[]") == ["CVE-2021-7064"]
            and kwargs.get("params").get("offset") == "2020-08-24T21:47:14.824Z::1f4110cdadb1170007011140"
        ):
            return MockResponse(200, "get_cve_by_id")
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/cves/get-cves-list" and kwargs.get("params").get(
            "cveId[]"
        ) == ["CVE-2021-7064"]:
            return MockResponse(200, "get_cve_by_id_with_offset")
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/cves/get-cves-list" and kwargs.get("params").get(
            "cveId[]"
        ) == ["CVE-2021-3739", "CVE-2020-7064"]:
            return MockResponse(200, "get_cve_by_ids")
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/cves/get-cves-list" and kwargs.get("params").get(
            "cveId[]"
        ) == ["empty"]:
            return MockResponse(200, "get_cve_by_id_empty")
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/cves/get-cves-list":
            return MockResponse(200, "get_cve_by_ids")
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/cves/add-cves" and kwargs.get("json").get(
            "cveIds"
        ) == ["CVE-1999-0003"]:
            return MockResponse(200, "add_cve_with_one_id")
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/cves/add-cves" and kwargs.get("json").get(
            "cveIds"
        ) == ["CVE-2021-3739", "CVE-2020-7064", "CVE-1999-003"]:
            return MockResponse(200, "add_cve_with_many_id")
        elif (
            kwargs.get("url") == "https://api.intsights.com/public/v1/cves/add-cves"
            and kwargs.get("json").get("cveIds") == []
        ):
            return MockResponse(200, "delete_cve_empty")
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/cves/delete-cves" and kwargs.get("json").get(
            "cveIds"
        ) == ["CVE-1999-0003"]:
            return MockResponse(200, "delete_cve_with_one_id")
        elif kwargs.get("url") == "https://api.intsights.com/public/v1/cves/delete-cves" and kwargs.get("json").get(
            "cveIds"
        ) == ["CVE-2021-3739", "CVE-2020-7064", "CVE-1999-003"]:
            return MockResponse(200, "delete_cve_with_many_id")
        elif (
            kwargs.get("url") == "https://api.intsights.com/public/v1/cves/delete-cves"
            and kwargs.get("json").get("cveIds") == []
        ):
            return MockResponse(200, "delete_cve_empty")
        else:
            raise NotImplementedError("Not implemented", kwargs)
