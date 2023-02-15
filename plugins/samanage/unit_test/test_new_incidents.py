import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from unittest.mock import patch
from komand_samanage.connection.connection import Connection
from komand_samanage.triggers.new_incidents import NewIncidents
import logging
import json
import timeout_decorator


# Test class
class TestNewIncidents(TestCase):
    def test_new_incidents_some_function_to_test(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here

        Here and in following tests you should test everything you can in your trigger that's not in the run loop.
        """
        self.fail("Unimplemented Test")