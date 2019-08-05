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
        if params.get('organization') and params.get('repository'):
            g = self.connection.github_user
            issue = g.get_organization(params.get('organization')).get_repo(params.get('repository')).get_issue(int(params.get('issue_number')))
        else:
            g = self.connection.user
            issue = g.get_repo(params.get('repository')).get_issue(int(params.get('issue_number')))

        issue_params = params.get("label")
        issue = issue.add_to_labels(issue_params)
        return {}