import insightconnect_plugin_runtime
from .schema import CreateInlineAttachmentInput, CreateInlineAttachmentOutput, Input, Output, Component

# Custom imports below
import base64
import mimetypes


class CreateInlineAttachment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_inline_attachment",
            description=Component.DESCRIPTION,
            input=CreateInlineAttachmentInput(),
            output=CreateInlineAttachmentOutput(),
        )

    def run(self, params={}):
        provided_file = params.get(Input.FILE)
        filename = provided_file.get("filename")
        mime_type = mimetypes.guess_type(filename)[0]
        attachment = [("file", (filename, base64.b64decode(provided_file.get("content")), mime_type))]
        return {Output.URL: self.connection.api.create_inline_attachment(attachment).get("url")}
