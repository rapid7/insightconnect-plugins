import komand
from .schema import AddIssueLabelInput, AddIssueLabelOutput, Input, Output, Component
# Custom imports below


class AddIssueLabel(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_issue_label',
                description=Component.DESCRIPTION,
                input=AddIssueLabelInput(),
                output=AddIssueLabelOutput())

    def run(self, params={}):
        org = params.get(Input.ORGANIZATION)
        repo = params.get(Input.REPOSITORY)
        issue_number = params.get(Input.ISSUE_NUMBER)
        label = params.get(Input.LABEL)
        if org and repo:
            g = self.connection.github_user
            issue = g.get_organization(org).get_repo(repo).get_issue(issue_number)
        else:
            g = self.connection.user
            issue = g.get_repo(repo).get_issue(issue_number)

        try:
            issue = issue.add_to_labels(label)
            return {'success': True}
        except:
            return {'success': False}