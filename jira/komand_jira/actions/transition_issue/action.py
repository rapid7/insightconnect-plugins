import komand 
from .schema import TransitionIssueInput, TransitionIssueOutput

# Custom imports below
from jira.exceptions import JIRAError
from komand.exceptions import PluginException

class TransitionIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='transition_issue',
            description='Transition Issue',
            input=TransitionIssueInput(),
            output=TransitionIssueOutput())

    def run(self, params={}):
        """Transition Issue"""

        issue = self.connection.client.issue(id=params['id'])

        if not issue:
            raise Exception('Error: No issue found with ID: ' + params['id'])

        try:
            result = self.connection.client.transition_issue(
                issue=issue,
                transition=params['transition'],
                comment=params.get('comment'),
                fields=params.get('fields')
            )
        except JIRAError as e:
            raise PluginException(cause=e.text if e.text else "Invalid input.", data=e)

        self.logger.info('Result: %s', result)

        return {'success': True}
