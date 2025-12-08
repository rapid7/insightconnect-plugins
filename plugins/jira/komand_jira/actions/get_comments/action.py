import insightconnect_plugin_runtime
from .schema import GetCommentsInput, GetCommentsOutput, Input, Output, Component

# Custom imports below
from komand_jira.util.util import normalize_comment
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean


class GetComments(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_comments",
            description=Component.DESCRIPTION,
            input=GetCommentsInput(),
            output=GetCommentsOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        issue_id = params.get(Input.ID, "")
        # END INPUT BINDING - DO NOT REMOVE

        # Retrieve issues from Jira, depending on whether it's Cloud or Server
        if not self.connection.is_cloud:
            issue = self.connection.client.issue(id=issue_id)
        else:
            issue = self.connection.rest_client.get_issue(issue_id=issue_id)

        if not issue:
            raise PluginException(
                cause=f"No issue found with ID: {issue_id}.",
                assistance="Please provide a valid issue ID.",
            )

        # Retrieve comments based on instance type
        if not self.connection.is_cloud:
            comments = issue.fields.comment.comments or []
        else:
            # Get comments from the REST API response
            comments = issue.get("fields", {}).get("comment", {})

            # In some cases, comments may be directly a list
            # Otherwise, extract from the "comments" key
            if isinstance(comments, dict):
                comments = comments.get("comments", [])

        # Normalize comments and prepare output
        results = list(
            map(
                lambda comment: normalize_comment(comment, is_cloud=self.connection.is_cloud, logger=self.logger),
                comments,
            )
        )
        return {Output.COUNT: len(results), Output.COMMENTS: clean(results)}
