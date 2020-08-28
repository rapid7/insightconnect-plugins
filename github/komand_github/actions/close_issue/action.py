import komand
from .schema import CloseIssueInput, CloseIssueOutput, Input, Output, Component
# Custom imports below


class CloseIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='close_issue',
                description=Component.DESCRIPTION,
                input=CloseIssueInput(),
                output=CloseIssueOutput())

    def run(self, params={}):
        org = params.get(Input.ORGANIZATION)
        repo = params.get(Input.REPOSITORY)
        issue_number = params.get(Input.ISSUE_NUMBER)
        if org and repo:
            g = self.connection.github_user
            issue = g.get_organization(org).get_repo(repo).get_issue(issue_number)
        else:
            g = self.connection.user
            issue = g.get_repo(repo).get_issue(issue_number)

        issue_params = {"state": "closed"}
        try:
            issue = issue.edit(**issue_params)
            return {'success': True}
        except:
            return {'success': False}