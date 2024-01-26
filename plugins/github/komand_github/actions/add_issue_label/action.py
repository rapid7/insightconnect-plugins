import insightconnect_plugin_runtime
import github

from komand_github.util.util import handle_gihub_exceptions
from komand_github.actions.add_issue_label.schema import (
    AddIssueLabelInput,
    AddIssueLabelOutput,
    Input,
    Output,
    Component,
)


class AddIssueLabel(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_issue_label",
            description=Component.DESCRIPTION,
            input=AddIssueLabelInput(),
            output=AddIssueLabelOutput(),
        )

    def run(self, params={}):
        organization = params.get(Input.ORGANIZATION)
        repository = params.get(Input.REPOSITORY)
        issue_number = params.get(Input.ISSUE_NUMBER)
        label = params.get(Input.LABEL)

        try:
            if organization and repository:
                github_user = self.connection.github_user
                org = github_user.get_organization(organization)
                repo = org.get_repo(repository)
            else:
                user = self.connection.user
                repo = user.get_repo(repository)

            issue = repo.get_issue(issue_number)
            issue.add_to_labels(label)

            return {Output.SUCCESS: True}

        except github.GithubException as err:
            handle_gihub_exceptions(err)
