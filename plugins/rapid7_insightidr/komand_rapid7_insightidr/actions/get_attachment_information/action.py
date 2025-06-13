import insightconnect_plugin_runtime
from .schema import GetAttachmentInformationInput, GetAttachmentInformationOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Attachments
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.util import get_logging_context


class GetAttachmentInformation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_attachment_information",
            description=Component.DESCRIPTION,
            input=GetAttachmentInformationInput(),
            output=GetAttachmentInformationOutput(),
        )

    def run(self, params={}):
        attachment_rrn = params.get(Input.ATTACHMENT_RRN)
        request = ResourceHelper(self.connection.session, self.logger)
        self.logger.info(f"Getting the attachment information for {attachment_rrn}...", **self.connection.cloud_log_values)
        response = request.get_attachment_information(
            Attachments.get_attachment_information(self.connection.url, attachment_rrn)
        )
        return {Output.ATTACHMENT: response, Output.SUCCESS: True}
