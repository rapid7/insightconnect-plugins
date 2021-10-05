import insightconnect_plugin_runtime
from .schema import (
    GetIncidentAttachmentInput,
    GetIncidentAttachmentOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from icon_servicenow.util.request_helper import RequestHelper


class GetIncidentAttachment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_incident_attachment",
            description=Component.DESCRIPTION,
            input=GetIncidentAttachmentInput(),
            output=GetIncidentAttachmentOutput(),
        )

    def run(self, params={}):
        return {
            Output.ATTACHMENT_CONTENTS: RequestHelper.get_attachment(self.connection, params.get(Input.ATTACHMENT_ID))
        }
