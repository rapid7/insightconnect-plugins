import insightconnect_plugin_runtime
from .schema import (
    GetIncidentAttachmentInput,
    GetIncidentAttachmentOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException

import base64
import json


class GetIncidentAttachment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_incident_attachment",
            description=Component.DESCRIPTION,
            input=GetIncidentAttachmentInput(),
            output=GetIncidentAttachmentOutput(),
        )

    def run(self, params={}):
        url = f"{self.connection.attachment_url}/{params.get(Input.ATTACHMENT_ID)}/file"
        method = "get"

        response = self.connection.request.make_request(url, method)

        resource = response.get("resource")
        result = b""
        if resource is not None:
            if isinstance(resource, bytes):
                result = resource
            elif isinstance(resource, dict):
                try:
                    result = json.dumps(resource).encode("utf-8")
                except TypeError:
                    raise PluginException(PluginException.Preset.INVALID_JSON, data=resource)
            else:
                raise PluginException(PluginException.Preset.UNKNOWN, data=resource)

        return {Output.ATTACHMENT_CONTENTS: str(base64.b64encode(result), "utf-8")}
