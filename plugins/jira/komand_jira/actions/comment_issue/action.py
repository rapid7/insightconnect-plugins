import insightconnect_plugin_runtime
from .schema import CommentIssueInput, CommentIssueOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_jira.util.util import load_text_as_adf


class CommentIssue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="comment_issue",
            description=Component.DESCRIPTION,
            input=CommentIssueInput(),
            output=CommentIssueOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        id_ = params.get(Input.ID)
        comment = params.get(Input.COMMENT, "")
        # END INPUT BINDING - DO NOT REMOVE

        # Check if issue exists
        if not self.connection.is_cloud:
            issue = self.connection.client.issue(id=id_)
        else:
            issue = self.connection.rest_client.get_issue(issue_id=id_)

        # If no issue is found, raise
        if not issue:
            raise PluginException(
                cause=f"No issue found with ID: {id_}.",
                assistance="Please provide a valid issue ID.",
            )

        if not self.connection.is_cloud:
            response = self.connection.client.add_comment(issue, comment)
        else:
            # Validate if comment can be parsed sa Atlassian Document Format (ADF)
            response = self.connection.rest_client.add_comment_to_issue(issue_id=id_, comment=comment)
        return {Output.COMMENT_ID: response.id if not self.connection.is_cloud else response.get("id", "")}
