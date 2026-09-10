import insightconnect_plugin_runtime
from .schema import (
    DeleteIncidentAttachmentInput,
    DeleteIncidentAttachmentOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from icon_servicenow.util.validators import validate_record_identifier


class DeleteIncidentAttachment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_incident_attachment",
            description=Component.DESCRIPTION,
            input=DeleteIncidentAttachmentInput(),
            output=DeleteIncidentAttachmentOutput(),
        )

    def run(self, params={}):
        attachment_id = validate_record_identifier(params.get(Input.ATTACHMENT_ID), "attachment ID")
        url = f"{self.connection.attachment_url}/{attachment_id}"
        method = "delete"

        response = self.connection.request.make_request(url, method)

        success = response.get("status", 0) in range(200, 299)

        return {Output.SUCCESS: success}
