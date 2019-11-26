import komand
from .schema import PutIncidentAttachmentInput, PutIncidentAttachmentOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class PutIncidentAttachment(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='put_incident_attachment',
                description=Component.DESCRIPTION,
                input=PutIncidentAttachmentInput(),
                output=PutIncidentAttachmentOutput())

    def run(self, params={}):
        url = f'{self.connection.attachment_url}/file?table_name=incident&table_sys_id={params.get(Input.SYSTEM_ID)}' \
              f'&file_name={params.get(Input.ATTACHMENT_NAME)}'
        payload = params.get(Input.BASE64_CONTENT)
        content_type = params.get(Input.MIME_TYPE) if params.get(Input.OTHER_MIME_TYPE) == "" \
            else params.get(Input.OTHER_MIME_TYPE)
        method = "post"

        response = self.connection.request.make_request(url, method, payload=payload, content_type=content_type)

        try:
            result = response["resource"].get("result")
        except KeyError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response.text) from e

        attachment_id = result.get("sys_id")
        return {
            Output.ATTACHMENT_ID: attachment_id
        }
