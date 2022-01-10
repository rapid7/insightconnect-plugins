import insightconnect_plugin_runtime
from .schema import GetAttachmentsForAnIncidentInput, GetAttachmentsForAnIncidentOutput, Input, Output, Component

# Custom imports below
from icon_servicenow.util.request_helper import RequestHelper


class GetAttachmentsForAnIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_attachments_for_an_incident",
            description=Component.DESCRIPTION,
            input=GetAttachmentsForAnIncidentInput(),
            output=GetAttachmentsForAnIncidentOutput(),
        )

    def run(self, params={}):
        response = self.connection.request.make_request(
            f"{self.connection.attachment_url}?sysparm_query=table_sys_id={params.get(Input.INCIDENT_ID)}", "get"
        )
        attachment = response.get("resource").get("result")
        attachments = []
        for item in attachment:
            attachments.append(
                {
                    "file_name": item.get("file_name"),
                    "content": RequestHelper.get_attachment(self.connection, item.get("sys_id")),
                    "content_type": item.get("content_type"),
                }
            )

        return {Output.INCIDENT_ATTACHMENTS: attachments}
