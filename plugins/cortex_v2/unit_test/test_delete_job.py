import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_cortex_v2.connection.connection import Connection
from icon_cortex_v2.actions.delete_job import DeleteJob
import json
import logging
from unittest.mock import patch


class TestDeleteJob(TestCase):
    def test_delete_job(self):
        self.fail("Unimplemented Test Case")
