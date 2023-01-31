import json
import logging
import sys
import os

import insightconnect_plugin_runtime

sys.path.append(os.path.abspath("../"))

from icon_topdesk.connection import Connection
from icon_topdesk.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action, params=None):
        if not params:
            params = {
                Input.CREDENTIALS: {"username": "user", "password": "password"},
                Input.DOMAIN: "exampledomain",
            }
        action.connection = Connection()
        action.connection.meta = "{}"
        action.connection.logger = logging.getLogger("connection logger")
        action.connection.connect(params)
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
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                self.text = ""
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                return json.loads(self.text)

        params = kwargs.get("params", {})
        json_data = kwargs.get("json", {})
        url = kwargs.get("url", {})
        method = kwargs.get("method", {})

        if kwargs.get("url") == "https://exampledomain.topdesk.net/tas/api/incidents" and kwargs.get("method") == "GET":
            if params.get("query") == "status==firstLine;number==I203999":
                return MockResponse(204)
            if params.get("fields") == "non_existing_field,id":
                return MockResponse(206, "list_incidents_fields_with_invalid_and_existing_key.json.resp")
            if params.get("query") == "status==invalidStatus":
                return MockResponse(400)
            if params.get("sort") == "non_existing_field:desc":
                return MockResponse(400)
            if params.get("fields") == "non_existing_field":
                return MockResponse(400)
            if params.get("query") == "status==firstLine" and params.get("fields") is None:
                return MockResponse(206, "list_incidents_found.json.resp")

        if (
            kwargs.get("url") == "https://exampledomain.topdesk.net/tas/api/incidents"
            and kwargs.get("method") == "POST"
        ):
            if json_data.get("location") and json_data.get("location").get("id") == "invalid_location":
                return MockResponse(400)
            if json_data.get("callerLookup") is None and json_data.get("callerName") is None:
                return MockResponse(400)
            if json_data.get("entryType") and json_data.get("entryType").get("name") == "non_existing_entry_type":
                return MockResponse(400)
            if (
                json_data.get("callType")
                and json_data.get("callType").get("name") == "Failure"
                and json_data.get("category")
                and json_data.get("category").get("name") == "Hardware"
            ):
                return MockResponse(201, "create_incident_correct.json.resp")

        if (
            kwargs.get("url").startswith("https://exampledomain.topdesk.net/tas/api/incidents/id/")
            and kwargs.get("method") == "GET"
        ):
            if "44d88612-fea8-a8f3-6de8-2e1278abb02f" in kwargs.get("url"):
                return MockResponse(200, "get_incident_by_id_found.json.resp")
            if "44d88612-fea8-a8f3-6de8-2e1278abb02g" in kwargs.get("url"):
                return MockResponse(404)
            if "invalid_id" in kwargs.get("url"):
                return MockResponse(400)

        if (
            kwargs.get("url").startswith("https://exampledomain.topdesk.net/tas/api/incidents/number/")
            and kwargs.get("method") == "GET"
        ):
            if "I 2301 103" in kwargs.get("url"):
                return MockResponse(200, "get_incident_by_number_found.json.resp")
            if "I 2301 903" in kwargs.get("url"):
                return MockResponse(404)
            if "invalid_number" in kwargs.get("url"):
                return MockResponse(404)

        if url == "https://exampledomain.topdesk.net/tas/api/suppliers" and method == "GET":
            if params == {}:
                return MockResponse(200, "list_suppliers_10_items.json.resp")
            if params.get("page_size") == 2:
                return MockResponse(200, "list_suppliers_2_items.json.resp")
            if params.get("page_size") == 11:
                return MockResponse(200, "list_suppliers_11_items.json.resp")
            if params.get("page_size") == 101:
                return MockResponse(400, "")
            if params.get("query") == "invalid":
                return MockResponse(400, "")
            if params.get("query") == "name==Name 9":
                return MockResponse(200, "list_suppliers_query_name.json.resp")
            if params.get("query") == "name==unknown":
                return MockResponse(204, "")
            if params.get("page_size") == 5 and params.get("query") == "forFirstLine==false":
                return MockResponse(200, "list_suppliers_query_first_line.json.resp")
            if (
                params.get("page_size") == 2
                and params.get("query") == "forChangeManagement==false"
                and params.get("start") == 2
            ):
                return MockResponse(200, "list_suppliers_query_first_line.json.resp")

        if url == "https://exampledomain.topdesk.net/tas/api/incidents/id/success1":
            return MockResponse(200, "update_incident1.json.resp")
        if url == "https://exampledomain.topdesk.net/tas/api/incidents/id/success2":
            return MockResponse(200, "update_incident2.json.resp")
        if url == "https://exampledomain.topdesk.net/tas/api/incidents/id/success3":
            return MockResponse(200, "update_incident3.json.resp")
        if url == "https://exampledomain.topdesk.net/tas/api/incidents/id/invalid_id":
            return MockResponse(404, "")
        if url == "https://exampledomain.topdesk.net/tas/api/incidents/id/invalid_input":
            return MockResponse(400, "")

        if url == "https://exampledomain.topdesk.net/tas/api/incidents/number/success1":
            return MockResponse(200, "update_incident1.json.resp")
        if url == "https://exampledomain.topdesk.net/tas/api/incidents/number/success2":
            return MockResponse(200, "update_incident2.json.resp")
        if url == "https://exampledomain.topdesk.net/tas/api/incidents/number/success3":
            return MockResponse(200, "update_incident3.json.resp")
        if url == "https://exampledomain.topdesk.net/tas/api/incidents/number/invalid_number":
            return MockResponse(404, "")
        if url == "https://exampledomain.topdesk.net/tas/api/incidents/number/invalid_input":
            return MockResponse(400, "")

        if url == "https://exampledomain.topdesk.net/tas/api/operators":
            if params == {"page_size": 10}:
                return MockResponse(200, "list_operators_all_fields.json.resp")
            if params == {"page_size": 10, "query": "dynamicName=='Invalid Name'"}:
                return MockResponse(200, "empty_list.json.resp")
            if params == {"page_size": 10, "query": "dynamicName=='Test User'", "fields": "id,dynamicName"}:
                return MockResponse(200, "list_operators_selected_fields.json.resp")
            if params == {"start": 1, "page_size": 100, "query": "dynamicName=='Test User'"}:
                return MockResponse(200, "list_operators_all_fields.json.resp")

        if url == "https://exampledomain.topdesk.net/tas/api/operatorgroups":
            if params == {"page_size": 10}:
                return MockResponse(200, "list_operator_groups_all_fields.json.resp")
            if params == {"page_size": 10, "query": "groupName=='Invalid Name'"}:
                return MockResponse(200, "empty_list.json.resp")
            if params == {"page_size": 10, "query": "groupName=='Test Group'", "fields": "id,groupName"}:
                return MockResponse(200, "list_operator_groups_selected_fields.json.resp")
            if params == {"start": 1, "page_size": 100, "query": "groupName=='Test Group'"}:
                return MockResponse(200, "list_operator_groups_all_fields.json.resp")

        if url == "https://exampledomain.topdesk.net/tas/api/locations":
            if params.get("query") == "branch.name==not_found":
                return MockResponse(200, "list_locations_and_branches_not_found.json.resp")
            if params.get("query") == "non_existing_key==invalid_value":
                return MockResponse(400)
            if not params.get("query"):
                return MockResponse(200, "list_locations_and_branches_found.json.resp")

        raise NotImplementedError("Not implemented", kwargs)
