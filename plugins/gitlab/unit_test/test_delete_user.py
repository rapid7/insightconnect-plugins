import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_gitlab.connection.connection import Connection
from icon_gitlab.actions.delete_user import DeleteUser
import json
import logging


class TestDeleteUser(TestCase):
    def test_delete_user(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
