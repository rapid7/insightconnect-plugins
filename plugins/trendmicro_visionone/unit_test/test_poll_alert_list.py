import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from unittest.mock import patch
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.triggers.poll_alert_list import PollAlertList
import logging
import json
import timeout_decorator


# Test class
class TestPollAlertList(TestCase):
    def test_poll_alert_list_some_function_to_test(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here

        Here and in following tests you should test everything you can in your trigger that's not in the run loop.
        """
        self.fail("Unimplemented Test")