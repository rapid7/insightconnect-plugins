import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock

sys.path.append(os.path.abspath("../"))

from icon_rapid7_surface_command.actions.get_query_result import GetQueryResult
from insightconnect_plugin_runtime.exceptions import PluginException

JOB_ID = "0b1c2d3e-4f50-6172-8394-a5b6c7d8e9f0"


class TestGetQueryResult(TestCase):
    def setUp(self):
        self.action = GetQueryResult()
        self.action.connection = MagicMock()
        self.api = self.action.connection.api

    def run_and_validate(self, params):
        result = self.action.run(params)
        self.action.output.validate(result)  # the real output schema the plugin runtime enforces
        return result

    def test_complete_job_returns_cleaned_rows(self):
        self.api.get_query_result.return_value = {
            "status": "complete",
            "job_id": JOB_ID,
            "items": [{"Name": "a", "Owner": None}],
        }

        result = self.run_and_validate({"job_id": JOB_ID, "max_wait": 60})

        self.assertEqual(result, {"status": "complete", "job_id": JOB_ID, "items": [{"Name": "a"}]})
        self.api.get_query_result.assert_called_once_with(job_id=JOB_ID, max_wait=60)

    def test_running_job_is_a_normal_result(self):
        self.api.get_query_result.return_value = {"status": "running", "job_id": JOB_ID, "items": []}

        result = self.run_and_validate({"job_id": JOB_ID})

        self.assertEqual(result["status"], "running")

    def test_unset_max_wait_uses_default(self):
        self.api.get_query_result.return_value = {"status": "running", "job_id": JOB_ID, "items": []}

        self.action.run({"job_id": f" {JOB_ID} "})

        self.api.get_query_result.assert_called_once_with(job_id=JOB_ID, max_wait=180)

    def test_blank_job_id_is_rejected(self):
        with self.assertRaises(PluginException) as ctx:
            self.action.run({"job_id": "  "})
        self.assertIn("Job ID is required", ctx.exception.cause)
        self.api.get_query_result.assert_not_called()

    def test_api_errors_propagate(self):
        self.api.get_query_result.side_effect = PluginException(cause="expired", assistance="")

        with self.assertRaises(PluginException) as ctx:
            self.action.run({"job_id": JOB_ID})
        self.assertEqual(ctx.exception.cause, "expired")
