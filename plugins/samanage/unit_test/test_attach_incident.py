import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_samanage.connection.connection import Connection
from komand_samanage.actions.attach_incident import AttachIncident
from unit_test.util import Util, mock_request_200
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
expected_parameters = 'curl -H "X-Samanage-Authorization: Bearer Examplesecretkey" -F "file[attachable_type]=Incident" -F "file[attachable_id]=2134" -F "file[attachment]=@/var/folders/nz/ztdg17xn40b96w6l0yjydry40000gq/T/tmplwafpeig/Example attachment name" -H "Accept: application/vnd.samanage.v2.1+json" -H "Content-Type: multipart/form-data"  -X POST https://api.samanage.com/attachments.json'

class TestAttachIncident(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(AttachIncident())
    @patch("shutil.rmtree")
    @patch("insightconnect_plugin_runtime.helper.exec_command", return_value=test_attachment)
    def test_attach_incident(self, plugin_mock, rm_mock ):
        response = self.action.run(
            {"incident_id": 2134, "attachment_bytes": "ABCD", "attachment_name": "Example attachment name"}
        )
        plugin_mock.assert_called_with(expected_parameters)
        rm_mock.assert_called()
        expected = {"attachment": att}
        self.assertEqual(response, expected)
