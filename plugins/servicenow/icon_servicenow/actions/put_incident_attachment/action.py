import base64
from urllib.parse import quote

import insightconnect_plugin_runtime
from .schema import (
    PutIncidentAttachmentInput,
    PutIncidentAttachmentOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_servicenow.util.validators import validate_record_identifier


class PutIncidentAttachment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="put_incident_attachment",
            description=Component.DESCRIPTION,
            input=PutIncidentAttachmentInput(),
            output=PutIncidentAttachmentOutput(),
        )

    def run(self, params={}):
        system_id = validate_record_identifier(params.get(Input.SYSTEM_ID), "system ID")
        # The file name is chosen freely by the user, so it is escaped rather than validated: left as
        # it is, a name holding a hash truncates the URL and a name holding an ampersand adds a
        # parameter of its own to it.
        file_name = quote(params.get(Input.ATTACHMENT_NAME, ""), safe="")
        url = (
            f"{self.connection.attachment_url}/file?table_name=incident&table_sys_id={system_id}"
            f"&file_name={file_name}"
        )

        content_type = (
            params.get(Input.MIME_TYPE)
            if params.get(Input.OTHER_MIME_TYPE) == ""
            else params.get(Input.OTHER_MIME_TYPE)
        )

        response = self.connection.request.make_request(
            url, "post", data=base64.b64decode(params.get(Input.BASE64_CONTENT)), content_type=content_type
        )

        try:
            result = response.get("resource", {}).get("result")
        except AttributeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

        attachment_id = result.get("sys_id")
        return {Output.ATTACHMENT_ID: attachment_id}
