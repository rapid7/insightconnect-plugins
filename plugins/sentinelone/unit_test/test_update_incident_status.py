import os
import sys

sys.path.append(os.path.abspath("../"))

from komand_sentinelone.actions.update_incident_status import UpdateIncidentStatus
from komand_sentinelone.actions.update_incident_status.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from unittest import TestCase
from unit_test.util import Util
from unittest.mock import patch


class TestUpdateIncidentStatus(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(UpdateIncidentStatus())
        Util.mock_response_params = {}

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_update_incident_status(self, mock_request):
        test_cases = []
        for _type in ["threat", "alert"]:
            test_cases.append(
                {
                    "status": "resolved",
                    "threat_id": f"valid_{_type}_id_1",
                    "expected": {"affected": 1},
                    "_type": f"{_type}",
                    "description": f"Test updating incident status on 1 valid {_type}.",
                }
            )

        for case in test_cases:
            with self.subTest(case["description"]):
                actual = self.action.run(
                    {
                        Input.THREAT_ID: case["threat_id"],
                        Input.INCIDENT_STATUS: case["status"],
                        Input.TYPE: case["_type"],
                    }
                )
                self.assertEqual(case["expected"], actual)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_update_incident_status_exception_when_same_status_already_set(self, mock_request):
        test_cases = []
        for _type in ["threat", "alert"]:
            test_cases.append(
                {
                    "status": "in_progress",
                    "threat_id": f"same_status_{_type}_id_1",
                    "_type": f"{_type}",
                    "description": f"Test updating incident status on a {_type} with the same status already set.",
                }
            )
        for case in test_cases:
            incident_type = case["_type"]
            with self.subTest(case["description"]):
                with self.assertRaises(PluginException) as error:
                    self.action.run(
                        {
                            Input.THREAT_ID: case["threat_id"],
                            Input.INCIDENT_STATUS: case["status"],
                            Input.TYPE: incident_type,
                        }
                    )
                self.assertEqual(f"No {incident_type} to update in SentinelOne.", error.exception.cause)
                self.assertEqual(
                    f"Please verify the log, the {incident_type} are already set to the new analyst verdict",
                    error.exception.assistance,
                )

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_update_incident_status_exception_when_incident_does_not_exists(self, mock_request):
        test_cases = []
        for _type in ["threat", "alert"]:
            test_cases.append(
                {
                    "status": "unresolved",
                    "threat_id": f"non_existing_{_type}_id_1",
                    "_type": f"{_type}",
                    "description": f"Test updating incident status on a non existing {_type}.",
                }
            )

        for case in test_cases:
            incident_type = case["_type"]
            with self.subTest(case["description"]):
                with self.assertRaises(PluginException) as error:
                    self.action.run(
                        {
                            Input.THREAT_ID: case["threat_id"],
                            Input.INCIDENT_STATUS: case["status"],
                            Input.TYPE: incident_type,
                        }
                    )
                self.assertEqual(f"No {incident_type} to update in SentinelOne.", error.exception.cause)
                self.assertEqual(
                    f"Please verify the log, the {incident_type} are do not exist in SentinelOne.",
                    error.exception.assistance,
                )
