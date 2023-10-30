import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_sentinelone.actions.update_analyst_verdict import UpdateAnalystVerdict
from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestUpdateAnalystVerdict(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(UpdateAnalystVerdict())

    @parameterized.expand(
        [
            [
                "one_incident",
                Util.read_file_to_dict("inputs/update_analyst_verdict_one_incident.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "two_incidents",
                Util.read_file_to_dict("inputs/update_analyst_verdict_two_incidents.json.inp"),
                Util.read_file_to_dict("expected/affected_2.json.exp"),
            ],
            [
                "duplicated_incidents",
                Util.read_file_to_dict("inputs/update_analyst_verdict_duplicated_incidents.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "incident_with_same_status",
                Util.read_file_to_dict("inputs/update_analyst_verdict_incident_with_same_status.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "non_existing_incident",
                Util.read_file_to_dict("inputs/update_analyst_verdict_non_existing_incident.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "one_alert_incident",
                Util.read_file_to_dict("inputs/update_analyst_verdict_one_alert_incident.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "two_alert_incidents",
                Util.read_file_to_dict("inputs/update_analyst_verdict_two_alert_incidents.json.inp"),
                Util.read_file_to_dict("expected/affected_2.json.exp"),
            ],
            [
                "duplicated_alert_incidents",
                Util.read_file_to_dict("inputs/update_analyst_verdict_duplicated_alert_incidents.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "alert_incident_with_same_status",
                Util.read_file_to_dict("inputs/update_analyst_verdict_alert_incident_with_same_status.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "non_existing_alert_incident",
                Util.read_file_to_dict("inputs/update_analyst_verdict_non_existing_alert_incident.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
        ]
    )
    def test_update_analyst_verdict(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "empty_list",
                Util.read_file_to_dict("inputs/update_analyst_verdict_empty_list.json.inp"),
                "No incident IDs were provided.",
                "Please provide incident IDs and try again.",
            ],
            [
                "non_existing_incident",
                Util.read_file_to_dict("inputs/update_analyst_verdict_bad.json.inp"),
                "No threats to update in SentinelOne.",
                "Please verify the log, the threats are already set to the new analyst verdict or do not exist in "
                "SentinelOne.",
            ],
            [
                "with_the_same_status",
                Util.read_file_to_dict("inputs/update_analyst_verdict_bad_2.json.inp"),
                "No threats to update in SentinelOne.",
                "Please verify the log, the threats are already set to the new analyst verdict or do not exist in "
                "SentinelOne.",
            ],
            [
                "nothing_to_update",
                Util.read_file_to_dict("inputs/update_analyst_verdict_bad_3.json.inp"),
                "No threats to update in SentinelOne.",
                "Please verify the log, the threats are already set to the new analyst verdict or do not exist in "
                "SentinelOne.",
            ],
            [
                "empty_alert_list",
                Util.read_file_to_dict("inputs/update_analyst_verdict_empty_alert_list.json.inp"),
                "No incident IDs were provided.",
                "Please provide incident IDs and try again.",
            ],
            [
                "non_existing_alert_incident",
                Util.read_file_to_dict("inputs/update_analyst_verdict_alert_bad.json.inp"),
                "No alerts to update in SentinelOne.",
                "Please verify the log, the alerts are already set to the new analyst verdict or do not exist in "
                "SentinelOne.",
            ],
            [
                "alert_with_the_same_status",
                Util.read_file_to_dict("inputs/update_analyst_verdict_alert_bad_2.json.inp"),
                "No alerts to update in SentinelOne.",
                "Please verify the log, the alerts are already set to the new analyst verdict or do not exist in "
                "SentinelOne.",
            ],
            [
                "alert_nothing_to_update",
                Util.read_file_to_dict("inputs/update_analyst_verdict_alert_bad_3.json.inp"),
                "No alerts to update in SentinelOne.",
                "Please verify the log, the alerts are already set to the new analyst verdict or do not exist in "
                "SentinelOne.",
            ],
        ]
    )
    def test_update_analyst_verdict_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
