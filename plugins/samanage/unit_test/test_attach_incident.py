import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_samanage.connection.connection import Connection
from komand_samanage.actions.attach_incident import AttachIncident
from unit_test.util import Util, mock_request_200, mock_request_curl
from unittest.mock import patch, Mock
from parameterized import parameterized


att = {
    "id": 27211951,
    "content_type": "text/plain",
    "size": 12,
    "filename": "Hello.txt",
    "url": "https://example.com",
    "shared_attachment": False,
    "attachable_id": 31851783,
    "attachable_type": "Incident",
    "attachment_type": "attachment",
}
test_attachment = {"rcode": 0, "stdout": json.dumps(att)}


class TestAttachIncident(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(AttachIncident())

    @patch("insightconnect_plugin_runtime.helper.exec_command", return_value=test_attachment)
    @patch("shutil.rmtree")
    def test_attach_incident(self, plugin_mock, rm_mock):
        response = self.action.run(
            {"incident_id": 2134, "attachment_bytes": "ABCD", "attachment_name": "Example attachment name"}
        )
        plugin_mock.assert_called()
        rm_mock.assert_called()
        expected = {"attachment": att}
        self.assertEqual(response, expected)
