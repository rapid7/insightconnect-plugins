import komand
from .schema import DeleteIncidentAttachmentInput, DeleteIncidentAttachmentOutput, Input, Output, Component
# Custom imports below


class DeleteIncidentAttachment(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_incident_attachment',
                description=Component.DESCRIPTION,
                input=DeleteIncidentAttachmentInput(),
                output=DeleteIncidentAttachmentOutput())

    def run(self, params={}):
        url = f'{self.connection.attachment_url}/{params.get(Input.ATTACHMENT_ID)}'
        method = "delete"

        response = self.connection.request.make_request(url, method)

        if response.get("status", 0) in range(200, 299):
            success = True
        else:
            success = False

        return {
            Output.SUCCESS: success
        }
