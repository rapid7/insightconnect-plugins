import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_servicenow.connection.connection import Connection
from icon_servicenow.actions.get_incident_comments_worknotes import GetIncidentCommentsWorknotes
import json
import logging


class TestGetIncidentCommentsWorknotes(TestCase):
    def test_get_incident_comments_worknotes(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        pass
