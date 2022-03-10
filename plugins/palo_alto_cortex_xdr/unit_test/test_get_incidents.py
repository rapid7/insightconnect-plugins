import sys
import os
import timeout_decorator
from unittest import TestCase
from unittest.mock import patch
from icon_palo_alto_cortex_xdr.triggers.get_incidents import GetIncidents
from icon_palo_alto_cortex_xdr.triggers.get_incidents.schema import Input
from unit_test.util import Util, MockTrigger
from typing import Callable, Optional

sys.path.append(os.path.abspath("../"))


def timeout_pass(error_callback: Optional[Callable] = None):
    def func_timeout(func):
        def func_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except timeout_decorator.timeout_decorator.TimeoutError:
                if error_callback:
                    return error_callback()
                return None

        return func_wrapper

    return func_timeout


def check_error():
    expected = {
        "incident": {
            "incident_id": "1",
            "creation_time": 1642917540319,
            "modification_time": 1642919521805,
            "status": "new",
            "severity": "high",
            "description": "Example description",
            "alert_count": 14,
            "low_severity_alert_count": 0,
            "med_severity_alert_count": 10,
            "high_severity_alert_count": 4,
            "user_count": 1,
            "host_count": 1,
            "xdr_url": "https://example.com/incident-view?caseId=1",
            "starred": False,
            "hosts": ["example-host"],
            "users": ["administrator"],
            "incident_sources": ["XDR Agent"],
            "wildfire_hits": 4,
            "alerts_grouping_status": "Disabled",
            "mitre_tactics_ids_and_names": [
                "TA0002 - Execution",
                "TA0005 - Defense Evasion",
                "TA0006 - Credential Access",
            ],
            "mitre_techniques_ids_and_names": [
                "T1059 - Command and Scripting Interpreter",
                "T1059.001 - Command and Scripting Interpreter: PowerShell",
                "T1064 - Scripting",
                "T1086 - PowerShell",
            ],
            "alert_categories": ["Malware"],
        }
    }
    if MockTrigger.actual == expected:
        return True

    TestCase.assertDictEqual(TestCase(), MockTrigger.actual, expected)


class TestGetIncidents(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetIncidents())

    @timeout_pass(error_callback=check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    @patch("requests.post", side_effect=Util.mocked_requests)
    @patch("time.time", return_value=1642917540.319)
    def test_get_incidents(self, mock_send, mock_post, mock_time):
        self.action.run({Input.FREQUENCY: 5})
