import os
import sys

sys.path.append(os.path.abspath("../"))

from base64 import b64encode
from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_servicenow.actions.put_incident_attachment import PutIncidentAttachment
from icon_servicenow.actions.put_incident_attachment.schema import PutIncidentAttachmentOutput
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from util import Util

ATTACHMENT_URL = "https://rapid7.service-now.com/api/now/attachment/file"


def attachment_input(system_id: str, attachment_name: str) -> Dict[str, Any]:
    return {
        "system_id": system_id,
        "attachment_name": attachment_name,
        "base64_content": b64encode(b"a report").decode("utf-8"),
        "mime_type": "text/plain",
        "other_mime_type": "",
    }


@patch("requests.post", side_effect=Util.mocked_requests)
class TestPutIncidentAttachment(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(PutIncidentAttachment())

    def test_put_incident_attachment(self, mock_post: MagicMock) -> None:
        actual = self.action.run(attachment_input("9de5069c5afe602b2ea0a04b66beb2c0", "report.txt"))
        validate(actual, PutIncidentAttachmentOutput.schema)
        self.assertEqual(actual, {"attachment_id": "b259f4062d9f78f9ffdd6efd05c492c7"})

    @parameterized.expand(
        [
            # A hash left as it is truncates the URL, so the file name would reach ServiceNow cut
            # short and everything after it would be dropped from the request.
            ["hash", "report #1.txt", "report%20%231.txt"],
            # An ampersand left as it is adds a parameter of its own to the URL.
            ["ampersand", "report&table_name=sys_user.txt", "report%26table_name%3Dsys_user.txt"],
            ["space", "monthly report.txt", "monthly%20report.txt"],
            ["plain_name", "report.txt", "report.txt"],
        ]
    )
    def test_put_incident_attachment_escapes_the_file_name(
        self, mock_post: MagicMock, test_name: str, attachment_name: str, expected: str
    ) -> None:
        self.action.run(attachment_input("9de5069c5afe602b2ea0a04b66beb2c0", attachment_name))
        self.assertEqual(
            mock_post.call_args_list[-1].kwargs.get("url"),
            f"{ATTACHMENT_URL}?table_name=incident&table_sys_id=9de5069c5afe602b2ea0a04b66beb2c0"
            f"&file_name={expected}",
        )

    def test_put_incident_attachment_raise_exception_on_an_invalid_system_id(self, mock_post: MagicMock) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(attachment_input("../../../table/sys_user", "report.txt"))
        self.assertEqual(error.exception.cause, "The system ID provided is not a valid ServiceNow record identifier.")
        mock_post.assert_not_called()
