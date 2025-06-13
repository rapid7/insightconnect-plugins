import insightconnect_plugin_runtime
from .schema import DeleteAttachmentInput, DeleteAttachmentOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Attachments
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.util import get_logging_context


class DeleteAttachment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_attachment",
            description=Component.DESCRIPTION,
            input=DeleteAttachmentInput(),
            output=DeleteAttachmentOutput(),
        )

    def run(self, params={}):
        attachment_rrn = params.get(Input.ATTACHMENT_RRN)
        request = ResourceHelper(self.connection.session, self.logger)
        self.logger.info(f"Deleting the {attachment_rrn} attachment...", **get_logging_context())
        request.delete_attachment(Attachments.attachment(self.connection.url, attachment_rrn))
        return {Output.SUCCESS: True}
