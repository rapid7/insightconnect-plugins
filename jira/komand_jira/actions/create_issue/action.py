import komand
from .schema import CreateIssueInput, CreateIssueOutput
# Custom imports below
from ...util import *
import base64
from io import BytesIO
from komand.exceptions import ConnectionTestException


class CreateIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='create_issue',
            description='Create an issue in Jira',
            input=CreateIssueInput(),
            output=CreateIssueOutput())

    def run(self, params={}):
        """Run action"""

        project = params.get('project')

        if not project:
            project = self.connection.parameters.get('project')

        issueType = params.get('type')
        summary = params.get('summary', " ").replace("\n", " ")
        description = params.get("description", " ")
        fields = params.get('fields', {})

        self.logger.debug('Create issue with: %s', params)

        fields['project'] = project
        fields['summary'] = summary
        fields['description'] = description
        fields['issuetype'] = {
            'name': issueType
        }

        # Check that the type is available in Jira before creating the ticket
        # This is not a perfect check though (see below)
        try:
            # This seems to work for some cases e.g. 'Blah' but not others 'Task' (Task is found below) depending on the Jira installation
            types = self.connection.client.issue_type_by_name(issueType)
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

        # TODO: This code is a duplicate of what's in 'attach_issue' - they should share a common code
        if params.get('attachment_bytes') and not params.get('attachment_filename'):
            raise Exception("Error: Attachment contents provided but no attachment filename")

        if params.get('attachment_filename') and not params.get('attachment_bytes'):
            raise Exception("Error: Attachment filename provided but no attachment contents")

        if params.get('attachment_bytes') and params.get("attachment_filename"):
            filename = params['attachment_filename']
            file_bytes = params['attachment_bytes']

            try:
                data = base64.b64decode(file_bytes)
            except:
                raise Exception("Error: Unable to decode file input!")

            attachment = BytesIO()
            attachment.write(data)
            self.connection.client.add_attachment(issue=issue, attachment=attachment, filename=filename)

        return {"issue": output}
