import sys
import os
from unittest import TestCase
from unittest.mock import patch
from komand_carbon_black_defense.actions.find_event import FindEvent
from komand_carbon_black_defense.actions.find_event.schema import Input as FindEventSchemaInput
from unit_tests.util import Util
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_tests.mock import (
    mock_request,
)

sys.path.append(os.path.abspath("../tests/"))


class TestFindEvent(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.params = {
            "device_external_ip": ["2001:db8:1:1:1:1:1:1"],
            "process_name": ["svchost.exe"],
            "enriched_event_type": ["CREATE_PROCESS"],
            "process_hash": ["275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"],
            "device_name": ["\."],
            "time_range": "-2d",
        }

    def setUp(self) -> None:
        self.connection, self.action = Util.default_connector(FindEvent())

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_find_event_all_inputs(self, _mock_req):
        actual = self.action.run(
            {
                FindEventSchemaInput.PROCESS_NAME: self.params.get("process_name"),
                FindEventSchemaInput.DEVICE_NAME: self.params.get("device_name"),
                FindEventSchemaInput.DEVICE_EXTERNAL_IP: self.params.get("device_external_ip"),
                FindEventSchemaInput.ENRICHED_EVENT_TYPE: self.params.get("enriched_event_type"),
                FindEventSchemaInput.PROCESS_HASH: self.params.get("process_hash"),
                FindEventSchemaInput.TIME_RANGE: self.params.get("time_range"),
            }
        )
        expected = {
            "success": True,
            "results": [
                {
                    "backend_timestamp": "2000-01-01T00:00:00.000Z",
                    "device_group_id": 0,
                    "device_id": 1234567,
                    "device_name": "wb-auto-qa",
                    "device_policy_id": 6525,
                    "device_timestamp": "2000-01-01T00:00:00.000Z",
                    "enriched": True,
                    "enriched_event_type": "NETWORK",
                    "event_description": "The operation was <accent>blocked by Cb Defense</accent>.",
                    "event_id": "9de5069c5afe602b2ea0a04b66beb2c0",
                    "event_network_inbound": False,
                    "event_network_local_ipv4": "192.0.2.0/24",
                    "event_network_location": "Times Square,NY,United States",
                    "event_network_protocol": "TCP",
                    "event_network_remote_ipv4": "203.0.113.0/24",
                    "event_network_remote_port": 443,
                    "event_type": "netconn",
                    "ingress_time": 1647340061569,
                    "legacy": True,
                    "org_id": "44d88612fea8a8f36de82e1278abb02f",
                    "parent_guid": "44d88612fea8a8f36de82e1278abb02f-0049ffdb-000003c4-00000000-1d8336797e1b8e5",
                    "parent_pid": 123,
                    "process_guid": "44d88612fea8a8f36de82e1278abb02f-0049ffdb-0000175c-00000000-1d836263d49edea",
                    "process_hash": [
                        "9de5069c5afe602b2ea0a04b66beb2c0",
                        "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
                    ],
                    "process_name": "c:\\windows\\system32\\setup.exe",
                    "process_pid": [1234],
                    "process_username": ["user1"],
                    "sensor_action": ["DENY", "BLOCK"],
                }
            ],
            "approximate_unaggregated": 100,
            "num_aggregated": 10,
            "num_available": 1,
            "num_found": 100,
            "contacted": 48,
            "completed": 48,
        }
        self.assertEqual(actual, expected)

    # test finding event via single input
    @patch("requests.request", side_effect=mock_request)
    def test_find_event_single_input(self, _mock_req):
        actual = self.action.run(
            {
                FindEventSchemaInput.PROCESS_NAME: self.params.get("process_name"),
            }
        )
        print(actual)
        expected = {
            "success": True,
            "results": [
                {
                    "backend_timestamp": "2000-01-01T00:00:00.000Z",
                    "device_group_id": 0,
                    "device_id": 1234567,
                    "device_name": "wb-auto-qa",
                    "device_policy_id": 6525,
                    "device_timestamp": "2000-01-01T00:00:00.000Z",
                    "enriched": True,
                    "enriched_event_type": "NETWORK",
                    "event_description": "The operation was <accent>blocked by Cb Defense</accent>.",
                    "event_id": "9de5069c5afe602b2ea0a04b66beb2c0",
                    "event_network_inbound": False,
                    "event_network_local_ipv4": "192.0.2.0/24",
                    "event_network_location": "Times Square,NY,United States",
                    "event_network_protocol": "TCP",
                    "event_network_remote_ipv4": "203.0.113.0/24",
                    "event_network_remote_port": 443,
                    "event_type": "netconn",
                    "ingress_time": 1647340061569,
                    "legacy": True,
                    "org_id": "44d88612fea8a8f36de82e1278abb02f",
                    "parent_guid": "44d88612fea8a8f36de82e1278abb02f-0049ffdb-000003c4-00000000-1d8336797e1b8e5",
                    "parent_pid": 123,
                    "process_guid": "44d88612fea8a8f36de82e1278abb02f-0049ffdb-0000175c-00000000-1d836263d49edea",
                    "process_hash": [
                        "9de5069c5afe602b2ea0a04b66beb2c0",
                        "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
                    ],
                    "process_name": "c:\\windows\\system32\\setup.exe",
                    "process_pid": [1234],
                    "process_username": ["user1"],
                    "sensor_action": ["DENY", "BLOCK"],
                }
            ],
            "approximate_unaggregated": 100,
            "num_aggregated": 10,
            "num_available": 1,
            "num_found": 100,
            "contacted": 48,
            "completed": 48,
        }
        self.assertEqual(actual, expected)

    # test finding an event with invalid credentials
    @patch("requests.request", side_effect=mock_request)
    def test_find_event_unauthorized(self, _mock_req):
        with self.assertRaises(PluginException) as exception:
            self.connection.host = "url_invalid"
            self.action.run(
                {
                    FindEventSchemaInput.PROCESS_NAME: self.params.get("process_name"),
                    FindEventSchemaInput.DEVICE_NAME: self.params.get("device_name"),
                    FindEventSchemaInput.DEVICE_EXTERNAL_IP: self.params.get("device_external_ip"),
                    FindEventSchemaInput.ENRICHED_EVENT_TYPE: self.params.get("enriched_event_type"),
                    FindEventSchemaInput.PROCESS_HASH: self.params.get("process_hash"),
                }
            )
        cause = "Either the organization key, API key, or connector ID configured in your connection is invalid."
        self.assertEqual(exception.exception.cause, cause)

    # testing a user not entering a criteria to search by
    @patch("requests.request", side_effect=mock_request)
    def test_get_job_id_for_enriched_event_with_no_criteria(self, _mock_req):
        with self.assertRaises(PluginException) as exception:
            self.action.run({FindEventSchemaInput.PROCESS_NAME: ""})
        cause = "No inputs were provided."
        self.assertEqual(exception.exception.cause, cause)

    # test get details for specific event with an invalid org key
    @patch("requests.request", side_effect=mock_request)
    def test_get_details_for_specific_event_forbidden(self, _mock_req):
        self.connection.org_key = "org_key_forbidden"
        with self.assertRaises(PluginException) as exception:
            self.action.run(
                {
                    FindEventSchemaInput.PROCESS_NAME: self.params.get("process_name"),
                    FindEventSchemaInput.DEVICE_NAME: self.params.get("device_name"),
                    FindEventSchemaInput.DEVICE_EXTERNAL_IP: self.params.get("device_external_ip"),
                    FindEventSchemaInput.ENRICHED_EVENT_TYPE: self.params.get("enriched_event_type"),
                    FindEventSchemaInput.PROCESS_HASH: self.params.get("process_hash"),
                    FindEventSchemaInput.TIME_RANGE: self.params.get("time_range"),
                }
            )
        cause = (
            "Access to resource at url/api/investigate/v2/orgs/org_key_forbidden/enriched_events/search_jobs is "
            "forbidden. The client has authenticated but does not have permission to perform the POST operation."
        )
        self.assertEqual(exception.exception.cause, cause)
