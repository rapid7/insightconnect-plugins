import os
import sys

sys.path.append(os.path.abspath("../"))

from komand_sentinelone.actions.update_analyst_verdict import UpdateAnalystVerdict
from komand_sentinelone.actions.update_analyst_verdict.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from unittest import TestCase
from unit_test.util import Util
from unittest.mock import patch


class TestUpdateAnalystVerdict(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(UpdateAnalystVerdict())
        Util.mock_response_params = {}

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_update_analyst_verdict(self, mock_request):
        test_cases = []
        for _type in ["threat", "alert"]:
            test_cases.append(
                {
                    "verdict": "true positive",
                    "ids": [f"valid_{_type}_id_1", f"valid_{_type}_id_2"],
                    "expected": {"affected": 2},
                    "_type": f"{_type}s",
                    "description": f"Test updating analyst verdict on 2 valid {_type}s.",
                }
            )
            test_cases.append(
                {
                    "verdict": "suspicious",
                    "ids": [f"valid_{_type}_id_1", f"valid_{_type}_id_1", f"valid_{_type}_id_1", f"valid_{_type}_id_1"],
                    "expected": {"affected": 1},
                    "_type": f"{_type}s",
                    "description": f"Test updating analyst verdict on a valid duplicated {_type}s.",
                }
            )
            test_cases.append(
                {
                    "verdict": "false positive",
                    "ids": [f"valid_{_type}_id_1", f"same_status_{_type}_id_1"],
                    "expected": {"affected": 1},
                    "_type": f"{_type}s",
                    "description": f"Test updating analyst verdict on a valid and a same status {_type}s.",
                }
            )
            test_cases.append(
                {
                    "verdict": "suspicious",
                    "ids": [f"valid_{_type}_id_1", f"non_existing_{_type}_id_1"],
                    "expected": {"affected": 1},
                    "_type": f"{_type}s",
                    "description": f"Test updating analyst verdict on a valid and a non existing {_type}s.",
                }
            )

        for case in test_cases:
            with self.subTest(case["description"]):
                actual = self.action.run(
                    {Input.INCIDENT_IDS: case["ids"], Input.ANALYST_VERDICT: case["verdict"], Input.TYPE: case["_type"]}
                )
                self.assertEqual(case["expected"], actual)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_update_analyst_verdict_exceptions(self, mock_request):
        test_cases = []
        for _type in ["threat", "alert"]:
            test_cases.append(
                {
                    "verdict": "false_positive",
                    "ids": [f"same_status_{_type}_id_1"],
                    "_type": f"{_type}s",
                    "description": f"Test updating analyst verdict on a {_type}s with the same status already set.",
                }
            )
            test_cases.append(
                {
                    "verdict": "suspicious",
                    "ids": [f"non_existing_{_type}_id_1"],
                    "_type": f"{_type}s",
                    "description": f"Test updating analyst verdict on a non existing {_type}s.",
                }
            )
            test_cases.append(
                {
                    "verdict": "false_positive",
                    "ids": [f"non_existing_{_type}_id_1", f"same_status_{_type}_id_1"],
                    "_type": f"{_type}s",
                    "description": f"Test updating analyst verdict on a non existing {_type}s.",
                }
            )

        for case in test_cases:
            incident_type = case["_type"]
            with self.subTest(case["description"]):
                with self.assertRaises(PluginException) as error:
                    self.action.run(
                        {
                            Input.INCIDENT_IDS: case["ids"],
                            Input.ANALYST_VERDICT: case["verdict"],
                            Input.TYPE: incident_type,
                        }
                    )
                self.assertEqual(f"No {incident_type} to update in SentinelOne.", error.exception.cause)
                self.assertEqual(
                    f"Please verify the log, the {incident_type} are already set to the new analyst"
                    " verdict or do not exist in SentinelOne.",
                    error.exception.assistance,
                )
