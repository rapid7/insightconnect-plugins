import insightconnect_plugin_runtime
from .schema import DeleteCommentInput, DeleteCommentOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Comments
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper


class DeleteComment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_comment",
            description=Component.DESCRIPTION,
            input=DeleteCommentInput(),
            output=DeleteCommentOutput(),
        )

    def run(self, params={}):
        comment_rrn = params.get(Input.COMMENT_RRN)
        request = ResourceHelper(self.connection.headers, self.logger)
        self.logger.info(f"Deleting the {comment_rrn} comment...", **request.logging_context)
        request.delete_comment(Comments.delete_comment(self.connection.url, comment_rrn))
        return {Output.SUCCESS: True}
