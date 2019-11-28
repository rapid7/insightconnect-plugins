import komand
from .schema import GetIncidentAttachmentInput, GetIncidentAttachmentOutput, Input, Output, Component
# Custom imports below


class GetIncidentAttachment(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_incident_attachment',
                description=Component.DESCRIPTION,
                input=GetIncidentAttachmentInput(),
                output=GetIncidentAttachmentOutput())

    def run(self, params={}):
        url = f'{self.connection.attachment_url}/{params.get(Input.ATTACHMENT_ID)}/file'
        method = "get"

        response = self.connection.request.make_request(url, method)

        return {
            Output.ATTACHMENT_CONTENTS: response.get("resource")
        }
