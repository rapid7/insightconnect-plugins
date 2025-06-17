import insightconnect_plugin_runtime
from .schema import ListCommentsInput, ListCommentsOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Comments
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper


class ListComments(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_comments",
            description=Component.DESCRIPTION,
            input=ListCommentsInput(),
            output=ListCommentsOutput(),
        )

    def run(self, params={}):
        request = ResourceHelper(self.connection.headers, self.logger)
        self.logger.info(f"Listing the comments for {params.get(Input.TARGET)}...")
        response = request.list_comments(Comments.comments(self.connection.url), params)
        return {Output.COMMENTS: response.get("data", []), Output.SUCCESS: True}
