import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from icon_bitdefender_gravityzone.actions.get_endpoints_list import GetEndpointsList
from icon_bitdefender_gravityzone.actions.get_endpoints_list.schema import Input, Output
from util import NETWORK_URL, Util


@patch("requests.Session.send")
class TestGetEndpointsList(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetEndpointsList())

    def test_maps_endpoints(self, mock_send):
        mock_send.return_value = Util.payload_response("get_endpoints_list.json.resp")

        result = self.action.run({})

        self.action.output.validate(result)
        self.assertEqual(2, result[Output.TOTAL])
        self.assertEqual(1, result[Output.PAGES_COUNT])
        self.assertEqual(1, result[Output.PAGE])
        self.assertEqual(30, result[Output.PER_PAGE])
        self.assertEqual(
            {
                "id": "5a4f2c3b6e9d1a0012345678",
                "name": "WORKSTATION-01",
                "label": "Finance laptop",
                "fqdn": "workstation-01.example.com",
                "group_id": "5a4f2c3b6e9d1a0012345679",
                "is_managed": True,
                "machine_type": 1,
                "operating_system_version": "Windows 11 Pro",
                "ip": "10.0.0.15",
                "macs": ["00:1a:2b:3c:4d:5e"],
                "managed_with_best": True,
                "is_isolated": False,
            },
            result[Output.ENDPOINTS][0],
        )

    def test_null_fields_are_mapped_to_empty_values(self, mock_send):
        mock_send.return_value = Util.payload_response("get_endpoints_list.json.resp")

        endpoint = self.action.run({})[Output.ENDPOINTS][1]

        self.assertEqual("", endpoint["label"])
        self.assertEqual("", endpoint["fqdn"])
        self.assertEqual("", endpoint["ip"])
        self.assertEqual([], endpoint["macs"])
        self.assertTrue(endpoint["is_isolated"])

    def test_inputs_are_passed_to_the_api(self, mock_send):
        mock_send.return_value = Util.payload_response("get_endpoints_list.json.resp")
        filters = {"details": {"name": "WORKSTATION"}, "depth": {"allItemsRecursively": True}}

        self.action.run(
            {
                Input.PARENT_ID: "5a4f2c3b6e9d1a0012345679",
                Input.IS_MANAGED: False,
                Input.PAGE: 2,
                Input.PER_PAGE: 50,
                Input.FILTERS: filters,
            }
        )

        payload = Util.sent_payload(mock_send)
        self.assertEqual(NETWORK_URL, Util.sent_request(mock_send).url)
        self.assertEqual("getEndpointsList", payload["method"])
        self.assertEqual(
            {"page": 2, "perPage": 50, "parentId": "5a4f2c3b6e9d1a0012345679", "isManaged": False, "filters": filters},
            payload["params"],
        )

    def test_defaults_when_inputs_are_omitted(self, mock_send):
        mock_send.return_value = Util.rpc_result({"items": [], "total": 0})

        result = self.action.run({})

        self.assertEqual({"page": 1, "perPage": 30}, Util.sent_payload(mock_send)["params"])
        self.assertEqual({"endpoints": [], "total": 0, "pages_count": 0, "page": 1, "per_page": 30}, result)
        self.action.output.validate(result)
