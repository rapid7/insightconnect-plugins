import sys
import os
from unittest import TestCase
from unittest.mock import patch
from icon_cortex_v2.actions.get_jobs import GetJobs
from icon_cortex_v2.actions.get_jobs.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.mock import Mock


sys.path.append(os.path.abspath("../"))


class TestGetJobs(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Mock.default_connector(GetJobs())
        cls.params = {
            Input.START: 0,
            Input.LIMIT: 10,
            Input.DATAFILTER: "",
            Input.DATATYPEFILTER: "",
            Input.ANALYZERFILTER: ""
        }

    @patch("requests.request", side_effect=Mock.mocked_request)
    def test_get_jobs(self, _mock_request):
        actual = self.action.run(self.params)
        expected = ""
        self.assertEqual(expected, actual)
