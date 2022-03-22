import base64

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


class PutIncidentAttachment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="put_incident_attachment",
            description=Component.DESCRIPTION,
            input=PutIncidentAttachmentInput(),
            output=PutIncidentAttachmentOutput(),
        )

    def run(self, params={}):
        url = (
            f"{self.connection.attachment_url}/file?table_name=incident&table_sys_id={params.get(Input.SYSTEM_ID)}"
            f"&file_name={params.get(Input.ATTACHMENT_NAME)}"
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
            result = response["resource"].get("result")
        except KeyError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text) from e

        attachment_id = result.get("sys_id")
        return {Output.ATTACHMENT_ID: attachment_id}
