import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_crowdstrike_falcon_intelligence.actions.downloadArtifact import DownloadArtifact


@patch("requests.request", side_effect=Util.mock_request)
class TestDownloadArtifact(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DownloadArtifact())

    @parameterized.expand(
        [
            [
                "single_id",
                Util.read_file_to_dict("inputs/download_artifact.json.inp"),
                Util.read_file_to_dict("expected/download_artifact.json.exp"),
            ]
        ]
    )
    def test_download_artifact(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_id",
                Util.read_file_to_dict("inputs/download_artifact_invalid_id.json.inp"),
                PluginException.causes[PluginException.Preset.SERVER_ERROR],
                PluginException.assistances[PluginException.Preset.SERVER_ERROR],
            ]
        ]
    )
    def test_download_artifact_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
