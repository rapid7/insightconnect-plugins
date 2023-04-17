import sys
import os

sys.path.append(os.path.abspath("../"))
# Custom Imports

from unittest.mock import patch
from unittest import TestCase
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from unit_test.util import Util


class TestQuarantineFile(TestCase):
    @patch("requests.sessions.Session.post", side_effect=Util.mocked_requests_session)
    def test_connection_bad(self, mock_request):
        with self.assertRaises(ConnectionTestException) as context:
            action = Util.default_connector_bad()

        cause = "The service this plugin is designed for is currently unavailable."
        assist = f"Try again later. If the issue persists, please contact support."

        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(assist, context.exception.assistance)
