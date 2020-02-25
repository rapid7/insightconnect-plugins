import komand
from .schema import CreateIssueInput, CreateIssueOutput, Input, Output, Component

# Custom imports below
from ...util import look_up_project, normalize_issue, add_attachment
from komand.exceptions import ConnectionTestException, PluginException


class CreateIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='create_issue',
            description=Component.DESCRIPTION,
            input=CreateIssueInput(),
            output=CreateIssueOutput())

    def run(self, params={}):
        """Run action"""
        project = params.get(Input.PROJECT)

        issue_type = params.get(Input.TYPE)
        summary = params.get(Input.SUMMARY, " ").replace("\n", " ")
        description = params.get(Input.DESCRIPTION, " ")
        fields = params.get(Input.FIELDS, {})

        valid_project = look_up_project(project, self.connection.client)
        if not valid_project:
            raise PluginException(
                cause=f"Project {project} does not exist or user don't have permission to access the project.",
                assistance='Please provide a valid project ID/name or make sure project is accessible to user.')

        self.logger.debug('Create issue with: %s', params)

        fields['project'] = project
        fields['summary'] = summary
        fields['description'] = description
        fields['issuetype'] = {
            'name': issue_type
        }

        # Check that the type is available in Jira before creating the ticket
        # This is not a perfect check though (see below)
        try:
            # This seems to work for some cases e.g. 'Blah' but not others 'Task' (Task is found below) depending on the Jira installation
            self.connection.client.issue_type_by_name(issue_type)
            # All types can be retrieved with scope via: self.connection.client.issue_types()
            # A future improvement may be able to validate the scope before continuing
            # However, this call doesn't return JSON :'( it returns this stupid thing:
            # [<JIRA IssueType: name='Bug', id='10004'>, <JIRA IssueType: name='Epic', scope={'type': 'PROJECT', 'project': {'id': '10008'} ]
        except KeyError:
            raise ConnectionTestException(cause="Issue type not known or user doesn't have permissions.",
                                          assistance="Talk to your Jira administrator to add the type or delegate necessary permissions, "
                                                     "or choose an available type.")

        for client_field in self.connection.client.fields():
            if client_field['name'] in fields:
                field_value = fields.pop(client_field['name'])
                fields[client_field['id']] = {'value': field_value}

        issue = self.connection.client.create_issue(fields=fields)
        output = normalize_issue(issue, logger=self.logger)

        if params.get(Input.ATTACHMENT_BYTES) and not params.get(Input.ATTACHMENT_FILENAME):
            raise PluginException(cause="Attachment contents provided but no attachment filename.",
                                  assistance="Please provide attachment filename.")

        if params.get(Input.ATTACHMENT_FILENAME) and not params.get(Input.ATTACHMENT_BYTES):
            raise PluginException(cause="Attachment filename provided but no attachment contents.",
                                  assistance="Please provide attachment contents.")

        if params.get(Input.ATTACHMENT_BYTES) and params.get(Input.ATTACHMENT_FILENAME):
            add_attachment(
                self.connection,
                self.logger,
                issue,
                params.get(Input.ATTACHMENT_FILENAME),
                params.get(Input.ATTACHMENT_BYTES)
            )

        return {Output.ISSUE: output}
