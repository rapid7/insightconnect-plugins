import komand 
from .schema import TransitionIssueInput, TransitionIssueOutput
# Custom imports below


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

        result = self.connection.client.transition_issue(
            issue=issue,
            transition=params['transition'],
            comment=params.get('comment')
        )

        self.logger.info('Result: %s', result)

        return {'success': True}

    def test(self):
        t = self.connection.test()
        if t:
            return {'success': True}
