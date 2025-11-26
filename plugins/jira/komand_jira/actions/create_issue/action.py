import insightconnect_plugin_runtime
from .schema import CreateIssueInput, CreateIssueOutput, Input, Output, Component

# Custom imports below
from komand_jira.util.util import look_up_project, normalize_issue, load_text_as_adf
from insightconnect_plugin_runtime.exceptions import PluginException


class CreateIssue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_issue",
            description=Component.DESCRIPTION,
            input=CreateIssueInput(),
            output=CreateIssueOutput(),
        )

    def check_issue_type_exists(self, issue_type: str) -> None:
        try:
            issue_types = (
                self.connection.client.issue_types()
                if not self.connection.is_cloud
                else self.connection.rest_client.get_all_issue_types()
            )
            issue_type_exists = False
            for retrieved_issue_type in issue_types:
                if not self.connection.is_cloud:
                    retrieved_issue_type = retrieved_issue_type.raw
                if retrieved_issue_type.get("name") == issue_type:
                    issue_type_exists = True
                    break
            if not issue_type_exists:
                raise PluginException
        except Exception as exception:
            raise PluginException(
                cause="Issue type not known or user doesn't have permissions.",
                assistance="Talk to your Jira administrator to add the type or delegate necessary permissions, "
                "or choose an available type.",
                data=exception,
            )

    def check_project_is_valid(self, project: str):
        valid_project = look_up_project(
            project, self.connection.client, self.connection.rest_client, is_cloud=self.connection.is_cloud
        )
        if not valid_project:
            raise PluginException(
                cause=f"Project {project} does not exist or user don't have permission to access the project.",
                assistance="Please provide a valid project ID/name or make sure project is accessible to user.",
            )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        project = params.get(Input.PROJECT, "")
        issue_type = params.get(Input.TYPE)
        summary = params.get(Input.SUMMARY, " ").replace("\n", " ")
        description = params.get(Input.DESCRIPTION, " ")
        attachment_filename = params.get(Input.ATTACHMENT_FILENAME, "")
        attachment_bytes = params.get(Input.ATTACHMENT_BYTES, "")
        fields = params.get(Input.FIELDS, {})
        # END INPUT BINDING - DO NOT REMOVE

        # Checks for valid project and issue type
        self.check_project_is_valid(project)
        self.check_issue_type_exists(issue_type)

        # Append required fields for issue creation
        fields["project"] = project if not self.connection.is_cloud else {"key": project}
        fields["summary"] = summary
        fields["description"] = description if not self.connection.is_cloud else load_text_as_adf(description)
        fields["issuetype"] = {"name": issue_type}

        # Map field names to IDs
        fields_function = (
            self.connection.client.fields
            if not self.connection.is_cloud
            else self.connection.rest_client.get_issue_fields
        )
        for client_field in fields_function():
            if client_field["name"] in fields:
                field_value = fields.pop(client_field["name"])
                fields[client_field["id"]] = {"value": field_value}

        # Create the issue
        if not self.connection.is_cloud:
            issue = self.connection.client.create_issue(fields=fields)
            issue_key = issue.key
        else:
            issue_key = self.connection.rest_client.create_issue(issue_fields=fields).get("key", "")
            issue = self.connection.rest_client.get_issue(issue_key)

        # Normalize the issue for output
        output = normalize_issue(issue, logger=self.logger, is_cloud=self.connection.is_cloud)

        # Handle issue attachment if provided
        if attachment_bytes and not attachment_filename:
            raise PluginException(
                cause="Attachment contents provided but no attachment filename.",
                assistance="Please provide attachment filename.",
            )
        elif attachment_filename and not attachment_bytes:
            raise PluginException(
                cause="Attachment filename provided but no attachment contents.",
                assistance="Please provide attachment contents.",
            )
        elif attachment_bytes and attachment_filename:
            self.connection.rest_client.add_attachment(
                issue_key,
                attachment_filename,
                attachment_bytes,
            )
        return {Output.ISSUE: output}
