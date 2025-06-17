import insightconnect_plugin_runtime
from .schema import ListAttachmentsInput, ListAttachmentsOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Attachments
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper


class ListAttachments(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_attachments",
            description=Component.DESCRIPTION,
            input=ListAttachmentsInput(),
            output=ListAttachmentsOutput(),
        )

    def run(self, params={}):
        request = ResourceHelper(self.connection.headers, self.logger)
        self.logger.info(f"Listing the attachments for {params.get(Input.TARGET)}...")
        response = request.list_attachments(Attachments.attachments(self.connection.url), params)
        return {Output.ATTACHMENTS: response.get("data", []), Output.SUCCESS: True}
