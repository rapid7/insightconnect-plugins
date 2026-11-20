import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock

sys.path.append(os.path.abspath("../"))

from icon_rapid7_surface_command.actions.start_query import StartQuery
from insightconnect_plugin_runtime.exceptions import PluginException

JOB_ID = "0b1c2d3e-4f50-6172-8394-a5b6c7d8e9f0"


class TestStartQuery(TestCase):
    def setUp(self):
        self.action = StartQuery()
        self.action.connection = MagicMock()
        self.api = self.action.connection.api

    def run_and_validate(self, params):
        result = self.action.run(params)
        self.action.output.validate(result)  # the real output schema the plugin runtime enforces
        return result

    def test_saved_query_returns_running_job(self):
        self.api.start_query.return_value = {"status": "running", "job_id": JOB_ID, "items": []}

        result = self.run_and_validate({"query_id": " q-1 "})

        self.assertEqual(result, {"status": "running", "job_id": JOB_ID, "items": []})
        self.api.start_query.assert_called_once_with(query_id="q-1", cypher=None)

    def test_adhoc_query_is_passed_through(self):
        self.api.start_query.return_value = {"status": "running", "job_id": JOB_ID, "items": []}

        self.run_and_validate({"cypher": "MATCH (m:Machine) RETURN m", "query_id": ""})

        self.api.start_query.assert_called_once_with(query_id=None, cypher="MATCH (m:Machine) RETURN m")

    def test_finished_job_returns_cleaned_rows(self):
        self.api.start_query.return_value = {
            "status": "complete",
            "job_id": "",
            "items": [{"Name": "a", "Owner": None}],
        }

        result = self.run_and_validate({"query_id": "q-1"})

        self.assertEqual(result["status"], "complete")
        self.assertEqual(result["items"], [{"Name": "a"}])

    def test_both_inputs_are_rejected(self):
        with self.assertRaises(PluginException) as ctx:
            self.action.run({"query_id": "q-1", "cypher": "MATCH (m) RETURN m"})
        self.assertIn("Exactly one", ctx.exception.cause)
        self.api.start_query.assert_not_called()

    def test_no_input_is_rejected(self):
        for params in ({}, {"query_id": "", "cypher": "  "}):
            with self.subTest(params=params):
                with self.assertRaises(PluginException):
                    self.action.run(params)
        self.api.start_query.assert_not_called()

    def test_api_errors_propagate(self):
        self.api.start_query.side_effect = PluginException(cause="boom", assistance="")

        with self.assertRaises(PluginException) as ctx:
            self.action.run({"query_id": "q-1"})
        self.assertEqual(ctx.exception.cause, "boom")
