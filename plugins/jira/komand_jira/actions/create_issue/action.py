import insightconnect_plugin_runtime
from .schema import CreateIssueInput, CreateIssueOutput, Input, Output, Component

# Custom imports below
from komand_jira.util.util import look_up_project, normalize_issue
from insightconnect_plugin_runtime.exceptions import PluginException


class CreateIssue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_issue",
            description=Component.DESCRIPTION,
            input=CreateIssueInput(),
            output=CreateIssueOutput(),
        )

    def check_issue_type_exists(self, issue_type: str):
        try:
            issue_types = self.connection.client.issue_types()
            issue_type_exists = False
            for retrieved_issue_type in issue_types:
                if retrieved_issue_type.raw.get("name") == issue_type:
                    issue_type_exists = True
                    break
            if issue_type_exists is False:
                raise Exception
        except Exception as exception:
            raise PluginException(
                cause="Issue type not known or user doesn't have permissions.",
                assistance="Talk to your Jira administrator to add the type or delegate necessary permissions, "
                "or choose an available type.",
                data=exception,
            )

    def check_project_is_valid(self, project: str):
        valid_project = look_up_project(project, self.connection.client)
        if not valid_project:
            raise PluginException(
                cause=f"Project {project} does not exist or user don't have permission to access the project.",
                assistance="Please provide a valid project ID/name or make sure project is accessible to user.",
            )

    def run(self, params={}):
        """Run action"""
        project = params.get(Input.PROJECT)

        issue_type = params.get(Input.TYPE)
        summary = params.get(Input.SUMMARY, " ").replace("\n", " ")
        description = params.get(Input.DESCRIPTION, " ")
        fields = params.get(Input.FIELDS, {})

        self.check_project_is_valid(project)
        self.check_issue_type_exists(issue_type)

        self.logger.debug("Create issue with: %s", params)

        fields["project"] = project
        fields["summary"] = summary
        fields["description"] = description
        fields["issuetype"] = {"name": issue_type}

        for client_field in self.connection.client.fields():
            if client_field["name"] in fields:
                field_value = fields.pop(client_field["name"])
                fields[client_field["id"]] = {"value": field_value}

        issue = self.connection.client.create_issue(fields=fields)
        output = normalize_issue(issue, logger=self.logger)

        if params.get(Input.ATTACHMENT_BYTES) and not params.get(Input.ATTACHMENT_FILENAME):
            raise PluginException(
                cause="Attachment contents provided but no attachment filename.",
                assistance="Please provide attachment filename.",
            )

        if params.get(Input.ATTACHMENT_FILENAME) and not params.get(Input.ATTACHMENT_BYTES):
            raise PluginException(
                cause="Attachment filename provided but no attachment contents.",
                assistance="Please provide attachment contents.",
            )

        if params.get(Input.ATTACHMENT_BYTES) and params.get(Input.ATTACHMENT_FILENAME):
            self.connection.rest_client.add_attachment(
                issue.key,
                params.get(Input.ATTACHMENT_FILENAME),
                params.get(Input.ATTACHMENT_BYTES),
            )

        return {Output.ISSUE: output}
