import komand
from .schema import LabelIssueInput, LabelIssueOutput

# Custom imports below
from komand.exceptions import PluginException


class LabelIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='label_issue',
            description='Label Issue',
            input=LabelIssueInput(),
            output=LabelIssueOutput())

    def run(self, params={}):
        """Add label to issue"""

        issue = self.connection.client.issue(id=params['id'])

        if not issue:
            raise PluginException(cause=f"No issue found with ID: {params['id']}.",
                                  assistance='Please provide a valid issue ID.')

        labels = params['label'].split(',')

        for label in labels:
            if label not in issue.fields.labels:
                issue.fields.labels.append(label)

        self.logger.info('Adding labels to issue %s: %s', params['id'], issue.fields.labels)

        issue.update(fields={'labels': issue.fields.labels})

        return {'success': True}
