import insightconnect_plugin_runtime
from .schema import UploadAttachmentInput, UploadAttachmentOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Attachments
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.util import get_logging_context
import base64
import mimetypes


class UploadAttachment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="upload_attachment",
            description=Component.DESCRIPTION,
            input=UploadAttachmentInput(),
            output=UploadAttachmentOutput(),
        )

    def run(self, params={}):
        filename = params.get(Input.FILENAME)
        file_content = base64.b64decode(params.get(Input.FILE_CONTENT))
        mime_type = mimetypes.guess_type(filename)[0]
        if not mime_type:
            mime_type = "text/plain"
        request = ResourceHelper(self.connection.session, self.logger)
        self.logger.info("Uploading an attachment...", **self.connection.cloud_log_values)
        response = request.upload_attachment(
            Attachments.attachments(self.connection.url), files={"filedata": (filename, file_content, mime_type)}
        )
        return {Output.ATTACHMENT: response, Output.SUCCESS: True}
