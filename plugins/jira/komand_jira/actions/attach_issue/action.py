import insightconnect_plugin_runtime
from .schema import AttachIssueInput, AttachIssueOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class AttachIssue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="attach_issue",
            description=Component.DESCRIPTION,
            input=AttachIssueInput(),
            output=AttachIssueOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        issue_id = params.get(Input.ID, "")
        attachment_filename = params.get(Input.ATTACHMENT_FILENAME, "")
        attachment_bytes = params.get(Input.ATTACHMENT_BYTES, "")
        # END INPUT BINDING - DO NOT REMOVE

        # Retrieve issues from Jira, depending on whether it's Cloud or Server
        if not self.connection.is_cloud:
            issue = self.connection.client.issue(id=issue_id)
            issue_key = getattr(issue, "key", None)
        else:
            issue = self.connection.rest_client.get_issue(issue_id=issue_id)
            issue_key = issue.get("key")

        # Check if the issue exists before attempting to add an attachment
        if not issue:
            raise PluginException(
                cause=f"No issue found with ID: {issue_id}.",
                assistance="Please provide a valid issue ID.",
            )

        return {Output.ID: self.connection.rest_client.add_attachment(issue_key, attachment_filename, attachment_bytes)}
