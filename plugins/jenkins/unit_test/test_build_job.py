import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_jenkins.actions.build_job import BuildJob
from komand_jenkins.actions.build_job.schema import Input, Output

from mock import mock_request_200, mock_request_500
from util import Util

STUB_PARAMETERS = {Input.NAME: "ExampleName", Input.PARAMETERS: {}}
STUB_EXPECTED = {Output.JOB_NUMBER: 1, Output.BUILD_NUMBER: 1}


class TestBuildJob(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(BuildJob())

    @patch("jenkins.Jenkins.jenkins_request", side_effect=mock_request_200)
    def test_build_job(self, mock_requests: MagicMock) -> None:
        response = self.action.run(STUB_PARAMETERS)
        validate(response, self.action.output.schema)
        self.assertEqual(response, STUB_EXPECTED)
        mock_requests.assert_called()

    @patch("jenkins.Jenkins.jenkins_request", side_effect=mock_request_500)
    def test_build_job_error(self, mock_requests: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(STUB_PARAMETERS)
        self.assertEqual(context.exception.cause, PluginException.causes[PluginException.Preset.UNKNOWN])
        self.assertEqual(context.exception.assistance, PluginException.assistances[PluginException.Preset.UNKNOWN])
        self.assertEqual(context.exception.data, "Response has been not implemented")
        mock_requests.assert_called()
