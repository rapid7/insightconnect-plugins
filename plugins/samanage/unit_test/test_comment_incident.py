import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_samanage.connection.connection import Connection
from komand_samanage.actions.comment_incident import CommentIncident
from unit_test.util import Util, mock_request_200
from unittest.mock import patch
from parameterized import parameterized


@patch("komand_samanage.util.api.request", side_effect=mock_request_200)
class TestCommentIncident(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(CommentIncident())

    @parameterized.expand(Util.load_parameters("comment_incident").get("parameters"))
    def test_change_incident_state(self, mock_request, incident_id, body, is_private, expected):
        actual = self.action.run({"incident_id": incident_id, "body": body, "is_private": is_private})
        self.assertEqual(actual, expected)
