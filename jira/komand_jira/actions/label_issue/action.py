import komand
from .schema import LabelIssueInput, LabelIssueOutput, Input, Output, Component

# Custom imports below
from komand.exceptions import PluginException


class LabelIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='label_issue',
            description=Component.DESCRIPTION,
            input=LabelIssueInput(),
            output=LabelIssueOutput())

    def run(self, params={}):
        """Add label to issue"""

        issue = self.connection.client.issue(id=params[Input.ID])

        if not issue:
            raise PluginException(cause=f"No issue found with ID: {params[Input.ID]}.",
                                  assistance='Please provide a valid issue ID.')

        labels = params[Input.LABEL].split(',')

        for label in labels:
            if label not in issue.fields.labels:
                issue.fields.labels.append(label)

        self.logger.info('Adding labels to issue %s: %s', params[Input.ID], issue.fields.labels)

        issue.update(fields={'labels': issue.fields.labels})

        return {Output.SUCCESS: True}
