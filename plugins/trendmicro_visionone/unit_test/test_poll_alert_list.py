import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.triggers.poll_alert_list import PollAlertList
from timeout_decorator import timeout, timeout_decorator


class TestPollAlertList(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.trigger = PollAlertList()
        self.trigger.connection = self.connection

    @timeout_decorator.timeout(15)
    @patch(
        "icon_trendmicro_visionone.triggers.poll_alert_list.PollAlertList.send",
        side_effect=lambda output: None,
    )
    def test_integration_poll_alert_list(self, mock_send):
        log = logging.getLogger("Test")

        try:
            with open("/python/src/tests/get_alert_list.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                trigger_params = test_json.get("input")
        except Exception as e:
            message = f"Error reading JSON file: {e}"
            self.fail(message)

        test_conn = Connection()
        test_conn.logger = log
        test_conn.connect(connection_params)

        test_poll_alert_list = PollAlertList()
        test_poll_alert_list.connection = test_conn
        test_poll_alert_list.logger = log

        try:
            test_poll_alert_list.run(trigger_params)
        except timeout_decorator.TimeoutError as e:
            self.assertIsInstance(e, timeout_decorator.TimeoutError)
        else:
            self.fail("Expected TimeoutError was not raised.")
