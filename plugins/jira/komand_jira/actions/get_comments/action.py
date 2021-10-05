import insightconnect_plugin_runtime
from .schema import GetCommentsInput, GetCommentsOutput, Input, Output, Component

# Custom imports below
from komand_jira.util.util import normalize_comment
from insightconnect_plugin_runtime.exceptions import PluginException


class GetComments(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_comments",
            description=Component.DESCRIPTION,
            input=GetCommentsInput(),
            output=GetCommentsOutput(),
        )

    def run(self, params={}):
        """Run action"""
        issue = self.connection.client.issue(id=params[Input.ID])

        if not issue:
            raise PluginException(
                cause=f"No issue found with ID: {params[Input.ID]}.",
                assistance="Please provide a valid issue ID.",
            )

        comments = issue.fields.comment.comments or []

        results = list(
            map(
                lambda comment: normalize_comment(comment, is_cloud=self.connection.is_cloud, logger=self.logger),
                comments,
            )
        )
        results = insightconnect_plugin_runtime.helper.clean(results)

        count = len(results)

        return {Output.COUNT: count, Output.COMMENTS: results}
