import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_servicenow.connection.connection import Connection
from icon_servicenow.actions.update_ci import UpdateCi
import json
import logging


class TestUpdateCi(TestCase):
    def test_update_ci(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        pass
