import insightconnect_plugin_runtime
from .schema import EditIssueInput, EditIssueOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException

from ...util.util import load_text_as_adf


class EditIssue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="edit_issue",
            description=Component.DESCRIPTION,
            input=EditIssueInput(),
            output=EditIssueOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        issue_id = params.pop(Input.ID, "")
        notify = params.pop(Input.NOTIFY, True)
        # END INPUT BINDING - DO NOT REMOVE

        clean_params = {}
        for key, value in params.items():
            if value:
                clean_params[key] = value

        self.logger.info(f"Editing issue (ID: {issue_id}, notify: {notify}) and parameters: {clean_params}")
        try:
            if not self.connection.is_cloud:
                # https://github.com/pycontribs/jira/blob/master/jira/resources.py#L506
                issue = self.connection.client.issue(id=issue_id)
                issue.update(notify=notify, **clean_params)
            else:
                # If description provided as plain text, convert to ADF format
                if Input.DESCRIPTION in clean_params:
                    clean_params[Input.DESCRIPTION] = load_text_as_adf(clean_params[Input.DESCRIPTION])

                # If additional fields are provided, ęxtract from 'fields' input and merge with clean_params
                if Input.FIELDS in clean_params:
                    clean_params.update(clean_params.pop(Input.FIELDS, {}))

                # Send request to Jira API to edit the issue
                self.connection.rest_client.edit_issue(issue_id, issue_fields=clean_params, notify=notify)
        except Exception as error:
            raise PluginException(cause="An unknown error occurred.", data=error)
        return {Output.SUCCESS: True}
