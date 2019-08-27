import komand
from .schema import AssignIssueInput, AssignIssueOutput
# Custom imports below


class AssignIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='assign_issue',
            description='Assign Issue',
            input=AssignIssueInput(),
            output=AssignIssueOutput())

    def run(self, params={}):
        """ Run action"""
        id_ = params['id']
        issue = self.connection.client.issue(id=id_)

        if not issue:
            raise Exception('Error: No issue found with ID: ' + id_)

        result = self.connection.client.assign_issue(issue=issue, assignee=params['assignee'])
        return {'success': result}
