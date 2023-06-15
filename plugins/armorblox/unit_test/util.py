import json
import logging
import os
from icon_armorblox.connection.connection import Connection
from icon_armorblox.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action, params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.API_KEY: {"api_key": {"secretKey": ""}},
            Input.TENANT_NAME : "tenant_name",
        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action


    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code

            def json(self):
                f = open(os.path.join(
                            os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json"
                        ))
                result = json.load(f)
                f.close()
                return result
        if args[0] == "https://tenant_name.armorblox.io/api/v1beta1/organizations/tenant_name/incidents/10597":
            return MockResponse("get_remediation_action", 200)
        elif args[0] == "https://tenant_name.armorblox.io/api/v1beta1/organizations/tenant_name/incidents/11081":
            return MockResponse("get_remediation_action", 200)
        elif args[0] == "https://tenant_name.armorblox.io/api/v1beta1/organizations/tenant_name/incidents/11063":
            return MockResponse("get_remediation_action", 200)

        raise Exception("Not implemented")
