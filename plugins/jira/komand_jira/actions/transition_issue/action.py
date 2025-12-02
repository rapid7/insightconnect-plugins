import insightconnect_plugin_runtime
from .schema import TransitionIssueInput, TransitionIssueOutput, Input, Output, Component

# Custom imports below
from jira.exceptions import JIRAError
from insightconnect_plugin_runtime.exceptions import PluginException


class TransitionIssue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="transition_issue",
            description=Component.DESCRIPTION,
            input=TransitionIssueInput(),
            output=TransitionIssueOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        issue_id = params.pop(Input.ID, "")
        transition = params.pop(Input.TRANSITION, "")
        comment = params.pop(Input.COMMENT, "")
        fields = params.pop(Input.FIELDS, {})
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

        try:
            if not self.connection.is_cloud:
                result = self.connection.client.transition_issue(
                    issue=issue,
                    transition=transition,
                    comment=comment,
                    fields=fields,
                )
            else:
                result = self.connection.rest_client.transition_issue(
                    issue_id=issue_id, transition_name=transition, comment=comment, fields=fields
                )
        except JIRAError as error:
            raise PluginException(cause=error.text if error.text else "Invalid input.", data=error)

        self.logger.info(f"Result: {result}")
        return {Output.SUCCESS: True}
