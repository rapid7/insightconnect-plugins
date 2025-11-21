import insightconnect_plugin_runtime
from .schema import LabelIssueInput, LabelIssueOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class LabelIssue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="label_issue",
            description=Component.DESCRIPTION,
            input=LabelIssueInput(),
            output=LabelIssueOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        issue_id = params.get(Input.ID, "")
        labels = params.get(Input.LABEL, "").split(",")
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

        # Add labels to the issue
        self.logger.info(f"Adding labels to issue {issue_id}: {labels}")
        if not self.connection.is_cloud:
            for label in labels:
                if label not in issue.fields.labels:
                    issue.fields.labels.append(label)
            issue.update(fields={"labels": issue.fields.labels})
        else:
            self.connection.rest_client.edit_issue(issue_id=issue_id, issue_fields={"labels": labels}, notify=False)
        return {Output.SUCCESS: True}
