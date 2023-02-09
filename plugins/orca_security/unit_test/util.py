import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

from icon_orca_security.connection.connection import Connection
from icon_orca_security.connection.schema import Input
import json


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.API_TOKEN: {"secretKey": "api_token"},
            Input.REGION: "EU",
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
    def load_parameters(filename):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"parameters/{filename}.json.resp")
            )
        )

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                self.text = ""
                self.content = ""
                if self.filename == "invalid_field":
                    self.text = "severity field does not exist"
                if self.filename == "invalid_email":
                    self.text = "invalid user email"
                if self.filename == "invitation_not_found":
                    self.text = "there is not pending invite for user id invalid_user@example.com"
                if self.filename == "not_found":
                    self.text = "alert_id orca-002 does not exist"
                if self.filename == "asset_not_found":
                    self.text = "asset invalid_asset_id not found"
                if self.filename == "file_not_found":
                    self.text = "no associated files"
                if self.filename == "file_content":
                    self.content = b"PK\x03\x04\x14\x00\x01\x00\x08\x00C\x9c\xe1P\xdd,Z\x04\xc2\x00\x00\x004\x01\x00\x00\r\x00\x00\x00eicarcom2.zipx\x7fM\xfcg\x8ac\xe7<\xa8`@\xdd\x9do\x18&\xb1\xea\xfe\xbd\xf2\xcc7<\xc4\xd7\x101\xbe\xb7\x0c[oS[\xde\x16j\xbf \x1c#\x90\xde\xe0\x07\x0f\xe2'6\\\xb6Foee\xc4\x84\xc1$Z\r\xb3 s\x81+\xeb\xfc\x82\xec\xa5\x92;\xb88*F\xfbu\xc1\xe8ag\xd2\r\x9bzZ9/\xa1\xcdaS.\xa3\x9b`\x19*\x0e\x05\x13\x14\r\xff\x04\xbb\x9fM\xec[.\xd5\x85M\x02aY\xac\xa7Zf\x91Q\xaao\x873ws\x9a\x00-;\x1e`\xbf+\xd17,\xefr\x8b\xd3\x9e\x8d\xc6~0\x9a@\xeb0\x8b\x9dK\xd92\xbd\x8ab7e\xd2\xcf\xbd\x10\xd1,\xa4\xbf\xe8L\xb1+p6\xe8\r\r\x83\x04\x99\nB\x95,+G\xd1PK\x01\x02\x00\x00\x14\x00\x01\x00\x08\x00C\x9c\xe1P\xdd,Z\x04\xc2\x00\x00\x004\x01\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00eicarcom2.zipPK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x00;\x00\x00\x00\xed\x00\x00\x00\x00\x00"

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(
                            os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp"
                        )
                    )
                )

        if kwargs.get("data") == {
            "invite_user_email": "user",
            "all_cloud_accounts": True,
            "cloud_accounts": [],
            "should_send_email": True,
            "role_id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        }:
            return MockResponse("invalid_email", 400)
        if kwargs.get("data") == {"delete_invite_email": "user"}:
            return MockResponse("invalid_email", 400)
        if kwargs.get("data") == {"delete_invite_email": "invalid_user@example.com"}:
            return MockResponse("invitation_not_found", 400)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/user/session":
            return MockResponse("get_access_token", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/alerts/orca-001/status/close":
            return MockResponse("update_alert_status_close", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/alerts/orca-001/status/in_progress":
            return MockResponse("update_alert_status_in_progress", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/alerts/orca-001/status/dismiss":
            return MockResponse("update_alert_status_dismiss", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/alerts/orca-001/status/open":
            return MockResponse("update_alert_status_open", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/alerts/orca-002/status/close":
            return MockResponse("not_found", 500)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/alerts/orca-001/severity":
            return MockResponse("update_alert_severity", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/alerts/orca-002/severity":
            return MockResponse("not_found", 400)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/alerts/orca-001":
            return MockResponse("get_alert", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/alerts/orca-002":
            return MockResponse("not_found", 400)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/assets/test-asset-123":
            return MockResponse("get_asset", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/assets/invalid_asset_id":
            return MockResponse("asset_not_found", 400)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/assets" and not kwargs.get("params"):
            return MockResponse("get_assets", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/assets" and kwargs.get("params") == {
            "asset_unique_id": "invalid_asset_id"
        }:
            return MockResponse("get_assets_empty", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/assets" and kwargs.get("params"):
            return MockResponse("get_assets", 200)
        if (
            kwargs.get("url") == "https://app.eu.orcasecurity.io/api/organization/users"
            and kwargs.get("method") == "POST"
        ):
            return MockResponse("add_user", 200)
        if (
            kwargs.get("url") == "https://app.eu.orcasecurity.io/api/organization/users"
            and kwargs.get("method") == "DELETE"
        ):
            return MockResponse("add_user", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/rbac/access/user":
            return MockResponse("get_users", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/alerts/orca-001/verify":
            return MockResponse("verify_alert", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/alerts/orca-002/verify":
            return MockResponse("not_found", 400)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/query/alerts":
            return MockResponse("get_alerts", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/alerts/orca-001/download_malicious_file":
            return MockResponse("download_malicious_file", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/alerts/orca-001/download_malicious_file":
            return MockResponse("download_malicious_file", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/alerts/orca-002/download_malicious_file":
            return MockResponse("not_found", 404)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/alerts/orca-003/download_malicious_file":
            return MockResponse("file_not_found", 404)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/rbac/roles/44d88612-fea8-a8f3-6de8-2e1278abb02f":
            return MockResponse("get_role", 200)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/rbac/roles/44d88612-fea8-a8f3-6de8-2e1278abb02e":
            return MockResponse("get_role", 404)
        if kwargs.get("url") == "https://app.eu.orcasecurity.io/api/rbac/roles":
            return MockResponse("get_roles", 200)
        if kwargs.get("params") == {"state.severity": "hazardous", "limit": 1}:
            return MockResponse("get_alerts", 200)
        if kwargs.get("params") == {"state.severity": "hazardous", "limit": 20}:
            return MockResponse("get_alerts", 200)
        if kwargs.get("params") == {"limit": 1}:
            return MockResponse("get_alerts", 200)
        if kwargs.get("params") == {"alert_labels": "empty", "limit": 1}:
            return MockResponse("get_alerts_empty", 200)
        if kwargs.get("params") == {"severity": "hazardous", "limit": 20}:
            return MockResponse("invalid_field", 400)
        if args and args[0] == "https://example.com/file":
            return MockResponse("file_content", 200)
        raise Exception("Not implemented")
