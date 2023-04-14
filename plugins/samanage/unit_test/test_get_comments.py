import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_samanage.connection.connection import Connection
from komand_samanage.actions.get_comments import GetComments
from unit_test.util import Util, mock_request_200
from unittest.mock import patch
from parameterized import parameterized


@patch("komand_samanage.util.api.request", side_effect=mock_request_200)
class TestGetComments(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetComments())

    @parameterized.expand(Util.load_parameters("get_comments").get("parameters"))
    def test_get_comments(self, mock_request, incident_id, expected):
        actual = self.action.run({"incident_id": incident_id})
        self.assertEqual(actual, expected)
