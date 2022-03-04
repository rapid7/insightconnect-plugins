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
            "eventinfo": {
                "results": [],
                "num_found": 0,
                "num_available": 0,
                "approximate_unaggregated": 0,
                "num_aggregated": 0,
                "contacted": 5,
                "completed": 5,
            },
            "success": True,
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
        expected = {
            "eventinfo": {
                "results": [],
                "num_found": 0,
                "num_available": 0,
                "approximate_unaggregated": 0,
                "num_aggregated": 0,
                "contacted": 5,
                "completed": 5,
            },
            "success": True,
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
