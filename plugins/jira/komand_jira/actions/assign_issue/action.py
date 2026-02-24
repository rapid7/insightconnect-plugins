import insightconnect_plugin_runtime
from .schema import AssignIssueInput, AssignIssueOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class AssignIssue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="assign_issue",
            description=Component.DESCRIPTION,
            input=AssignIssueInput(),
            output=AssignIssueOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        issue_id = params.get(Input.ID, "")
        assignee = params.get(Input.ASSIGNEE, "")
        # END INPUT BINDING - DO NOT REMOVE

        # Check if issue exists
        if not self.connection.is_cloud:
            issue = self.connection.client.issue(id=issue_id)
        else:
            issue = self.connection.rest_client.get_issue(issue_id=issue_id)

        # If no issue is found, raise
        if not issue:
            raise PluginException(
                cause=f"No issue found with ID: {issue_id}.",
                assistance="Please provide a valid issue ID.",
            )

        # Assign to the issue
        if not self.connection.is_cloud:
            result = self.connection.client.assign_issue(issue=issue, assignee=assignee)
        else:
            result = self.connection.rest_client.assign_issue(issue_id=issue_id, username=assignee)
        return {Output.SUCCESS: result}
