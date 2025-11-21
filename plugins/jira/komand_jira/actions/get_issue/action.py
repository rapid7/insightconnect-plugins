import insightconnect_plugin_runtime
from .schema import GetIssueInput, GetIssueOutput, Input, Output, Component

# Custom imports below
from komand_jira.util.util import normalize_issue
from insightconnect_plugin_runtime.exceptions import PluginException


class GetIssue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_issue",
            description=Component.DESCRIPTION,
            input=GetIssueInput(),
            output=GetIssueOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        issue_id = params.pop(Input.ID, "")
        get_attachments = params.pop(Input.GET_ATTACHMENTS, False)
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

        # Normalize issue and prepare output
        output = normalize_issue(
            issue=issue,
            get_attachments=get_attachments,
            include_raw_fields=True,
            logger=self.logger,
            is_cloud=self.connection.is_cloud,
            rest_client=self.connection.rest_client,
        )
        return {Output.FOUND: True, Output.ISSUE: insightconnect_plugin_runtime.helper.clean(output)}
