import insightconnect_plugin_runtime
from .schema import DownloadAttachmentInput, DownloadAttachmentOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Attachments
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.util import get_logging_context


class DownloadAttachment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="download_attachment",
            description=Component.DESCRIPTION,
            input=DownloadAttachmentInput(),
            output=DownloadAttachmentOutput(),
        )

    def run(self, params={}):
        attachment_rrn = params.get(Input.ATTACHMENT_RRN)
        request = ResourceHelper(self.connection.session, self.logger)
        self.logger.info(f"Downloading the {attachment_rrn} attachment...", **self.connection.log_values)
        content = request.download_attachment(Attachments.attachment(self.connection.url, attachment_rrn))
        return {Output.ATTACHMENT_CONTENT: content, Output.SUCCESS: True}
