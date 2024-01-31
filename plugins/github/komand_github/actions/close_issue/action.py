import insightconnect_plugin_runtime
import github

from komand_github.util.util import handle_gihub_exceptions
from komand_github.actions.close_issue.schema import CloseIssueInput, CloseIssueOutput, Input, Output, Component


class CloseIssue(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="close_issue",
            description=Component.DESCRIPTION,
            input=CloseIssueInput(),
            output=CloseIssueOutput(),
        )

    def run(self, params={}):
        organization = params.get(Input.ORGANIZATION)
        repository = params.get(Input.REPOSITORY)
        issue_number = params.get(Input.ISSUE_NUMBER)

        issue_params = {"state": "closed"}

        try:
            if organization and repository:
                github_user = self.connection.github_user
                org = github_user.get_organization(organization)
                repo = org.get_repo(repository)
            else:
                user = self.connection.user
                repo = user.get_repo(repository)

            issue = repo.get_issue(issue_number)
            issue.edit(**issue_params)
            return {Output.SUCCESS: True}

        except github.GithubException as err:
            handle_gihub_exceptions(err)
