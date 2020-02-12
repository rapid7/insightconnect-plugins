import komand
from .schema import AttachIssueInput, AttachIssueOutput, Input, Output, Component
from ...util import add_attachment

# Custom imports below
from komand.exceptions import PluginException


class AttachIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='attach_issue',
            description=Component.DESCRIPTION,
            input=AttachIssueInput(),
            output=AttachIssueOutput())

    def run(self, params={}):
        """Add attachment to issue"""
        id_ = params[Input.ID]
        issue = self.connection.client.issue(id=id_)

        if not issue:
            raise PluginException(cause=f'No issue found with ID: {id_}.',
                                  assistance='Please provide a valid issue ID.')

        output = add_attachment(
            self.connection,
            self.logger,
            issue,
            params.get(Input.ATTACHMENT_FILENAME),
            params.get(Input.ATTACHMENT_BYTES)
        )

        return {Output.ID: output.id}
