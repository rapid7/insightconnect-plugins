import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_rapid7_cyber_grc.actions import (
    CountRecords,
    CreateRecord,
    DeleteRecord,
    GetRecord,
    GetRecordHistory,
    ListRecords,
    UpdateRecord,
    UploadFlatFile,
)
from util import BASE_URL, Util


@patch("requests.Session.request", side_effect=Util.mock_request)
class TestGenericActions(TestCase):
    def setUp(self):
        Util.calls = []
        Util.updated = {}

    def test_list_records_targets_the_chosen_record_type(self, mock_request):
        actual = Util.default_connector(ListRecords()).run(
            {"record_type": "Vendors", "order_by": "name asc", "skip": 10, "top": 0}
        )

        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/Vendors")
        self.assertEqual(Util.calls[0]["params"], {"$orderby": "name asc", "$skip": 10})
        self.assertEqual(actual["count"], 2)

    def test_get_record_targets_the_chosen_record_type(self, mock_request):
        actual = Util.default_connector(GetRecord()).run({"record_type": "Locations", "id": 3})

        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/Locations/3")
        self.assertEqual(Util.calls[0]["params"], {})
        self.assertEqual(actual["record"]["id"], 3)

    def test_create_record_targets_the_chosen_record_type(self, mock_request):
        actual = Util.default_connector(CreateRecord()).run({"record_type": "Departments", "record": {"name": "Legal"}})

        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/Departments")
        self.assertEqual(actual["record"]["name"], "Legal")

    def test_update_record_targets_the_chosen_record_type(self, mock_request):
        actual = Util.default_connector(UpdateRecord()).run(
            {"record_type": "Departments", "id": 3, "record": {"name": "Legal and Compliance"}}
        )

        self.assertEqual(Util.calls[0]["method"], "PUT")
        self.assertEqual(actual["record"]["name"], "Legal and Compliance")

    def test_delete_record_targets_the_chosen_record_type(self, mock_request):
        actual = Util.default_connector(DeleteRecord()).run({"record_type": "Departments", "id": 3})

        self.assertEqual(Util.calls[0]["method"], "DELETE")
        self.assertTrue(actual["result"]["success"])

    def test_count_records_returns_the_count(self, mock_request):
        actual = Util.default_connector(CountRecords()).run({"record_type": "Risks", "filter": "statusID eq 3"})

        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/Risks/$count")
        self.assertEqual(actual["count"], 7)

    def test_get_record_history_returns_entries_and_a_count(self, mock_request):
        actual = Util.default_connector(GetRecordHistory()).run({"record_type": "Risks", "id": 8})

        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/Risks/8/History")
        self.assertEqual(actual["count"], 2)
        self.assertEqual(actual["history"][0]["name"], "Older")

    def test_upload_flat_file_sends_the_file_and_operation(self, mock_request):
        actual = Util.default_connector(UploadFlatFile()).run(
            {
                "file_name": "assets.csv",
                "file": "aWQsbmFtZQo=",
                "operation_type": "Append",
                "description": "Nightly export",
                "id": 0,
            }
        )

        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/flatfile-integrations")
        self.assertEqual(Util.calls[0]["json"]["operationType"], "Append")
        self.assertEqual(actual["result"]["fileName"], "assets.csv")

    def test_get_record_surfaces_a_missing_record(self, mock_request):
        with self.assertRaises(PluginException) as context:
            Util.default_connector(GetRecord()).run({"record_type": "Missing", "id": 1})

        self.assertEqual(context.exception.cause, "Not found.")
