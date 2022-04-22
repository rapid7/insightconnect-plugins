import sys
import os
from unittest import TestCase
from unittest.mock import patch
from icon_cortex_v2.actions.delete_job import DeleteJob
from icon_cortex_v2.actions.delete_job.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.mock import Mock


sys.path.append(os.path.abspath("../"))


class TestDeleteJob(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Mock.default_connector(DeleteJob())
        cls.params = {
            Input.JOB_ID: "02pxZ35f7bX4Lnij"
        }

    @patch("requests.request", side_effect=Mock.mocked_request)
    def test_delete_job(self, _mock_request):
        actual = self.action.run(self.params)
        expected = {Output.STATUS: True}
        self.assertEqual(expected, actual)
