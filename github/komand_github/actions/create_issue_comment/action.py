import komand
from .schema import CreateIssueCommentInput, CreateIssueCommentOutput, Input, Output, Component
# Custom imports below


class CreateIssueComment(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='create_issue_comment',
            description=Component.DESCRIPTION,
            input=CreateIssueCommentInput(),
            output=CreateIssueCommentOutput())

    def run(self, params={}):
        org = params.get(Input.ORGANIZATION)
        repo = params.get(Input.REPOSITORY)
        issue_number = params.get(Input.ISSUE_NUMBER)
        body = params.get(Input.BODY)
        if org and repo:
            g = self.connection.github_user
            issue = g.get_organization(org).get_repo(repo).get_issue(issue_number)
        else:
            g = self.connection.user
            issue = g.get_repo(repo).get_issue(issue_number)

        issue_params = {"body": body}
        issue = issue.create_comment(**issue_params)
        return {'url': issue.html_url}