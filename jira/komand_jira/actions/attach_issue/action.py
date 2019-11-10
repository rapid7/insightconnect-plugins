import komand
from .schema import AttachIssueInput, AttachIssueOutput

# Custom imports below
import base64
from io import BytesIO
from komand.exceptions import PluginException


class AttachIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='attach_issue',
            description='Add an attachment to an issue in Jira',
            input=AttachIssueInput(),
            output=AttachIssueOutput())

    def run(self, params={}):
        """Add attachment to issue"""
        id_ = params['id']
        issue = self.connection.client.issue(id=id_)

        if not issue:
            raise PluginException(cause=f'No issue found with ID: {id_}.',
                                  assistance='Please provide a valid issue ID.')

        filename = params.get('attachment_filename')
        file_bytes = params.get('attachment_bytes')

        try:
            data = base64.b64decode(file_bytes)
        except:
            raise PluginException(cause='Unable to decode attachment bytes.',
                                  assistance="Please provide a valid attachment bytes.")

        attachment = BytesIO()
        attachment.write(data)

        output = self.connection.client.add_attachment(
            issue=issue,
            attachment=attachment,
            filename=filename)

        self.logger.debug('Attach issue has returned: %s', output)

        return {'id': output.id}
