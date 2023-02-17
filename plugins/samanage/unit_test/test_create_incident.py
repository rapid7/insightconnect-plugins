import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_samanage.connection.connection import Connection
from komand_samanage.actions.create_incident import CreateIncident
from unit_test.util import Util, mock_request_200
from unittest.mock import patch
from parameterized import parameterized


@patch("komand_samanage.util.api.request", side_effect=mock_request_200)
class TestCreateIncident(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(CreateIncident())

    @parameterized.expand(Util.load_parameters("create_incident").get("parameters"))
    def test_create_incident(
        self,
        mock_request,
        name,
        requester,
        priority,
        description,
        due_at,
        assignee,
        incidents,
        problem,
        solutions,
        category_name,
        expected,
    ):
        actual = self.action.run(
            {
                "name": name,
                "requester": requester,
                "priority": priority,
                "description": description,
                "due_at": due_at,
                "assignee": assignee,
                "incidents": incidents,
                "problem": problem,
                "solutions": solutions,
                "category_name": category_name,
            }
        )
        self.assertEqual(actual, expected)
