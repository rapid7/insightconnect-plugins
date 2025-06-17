import insightconnect_plugin_runtime
from .schema import CreateCommentInput, CreateCommentOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Comments, Attachments
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper


class CreateComment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_comment",
            description=Component.DESCRIPTION,
            input=CreateCommentInput(),
            output=CreateCommentOutput(),
        )

    def run(self, params={}):
        attachments = params.get(Input.ATTACHMENTS)
        request = ResourceHelper(self.connection.headers, self.logger)
        if attachments:
            for attachment in attachments:
                request.get_attachment_information(
                    Attachments.get_attachment_information(self.connection.url, attachment)
                )
        self.logger.info(f"Creating a comment for {params.get(Input.TARGET)}...")
        response = request.create_comment(Comments.comments(self.connection.url), params)
        return {Output.COMMENT: response, Output.SUCCESS: True}
