import komand
from .schema import SearchIncidentAttachmentInput, SearchIncidentAttachmentOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class SearchIncidentAttachment(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_incident_attachment',
                description=Component.DESCRIPTION,
                input=SearchIncidentAttachmentInput(),
                output=SearchIncidentAttachmentOutput())

    def run(self, params={}):
        url = self.connection.attachment_url
        query = {"sysparm_query": "file_name=" + params.get(Input.NAME)}
        method = "get"

        response = self.connection.request.make_request(url, method, params=query)

        try:
            results = response["resource"].get("result")
        except KeyError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response.text) from e

        attachment_ids = [result.get("sys_id") for result in results]

        return {
            Output.ATTACHMENT_IDS: attachment_ids
        }
