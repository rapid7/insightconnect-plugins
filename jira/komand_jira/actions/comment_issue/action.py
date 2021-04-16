import insightconnect_plugin_runtime
from .schema import CommentIssueInput, CommentIssueOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class CommentIssue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="comment_issue",
            description=Component.DESCRIPTION,
            input=CommentIssueInput(),
            output=CommentIssueOutput(),
        )

    def run(self, params={}):
        """Run action"""
        id_ = params[Input.ID]
        issue = self.connection.client.issue(id=id_)

        if not issue:
            raise PluginException(
                cause=f"No issue found with ID: {id_}.",
                assistance="Please provide a valid issue ID.",
            )

        comment = self.connection.client.add_comment(issue=issue, body=params[Input.COMMENT])
        return {Output.COMMENT_ID: comment.id}
