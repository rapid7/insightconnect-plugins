import insightconnect_plugin_runtime
import github

from komand_github.util.util import handle_gihub_exceptions
from komand_github.actions.create_issue_comment.schema import (
    CreateIssueCommentInput,
    CreateIssueCommentOutput,
    Input,
    Output,
    Component,
)

# Custom imports below


class CreateIssueComment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_issue_comment",
            description=Component.DESCRIPTION,
            input=CreateIssueCommentInput(),
            output=CreateIssueCommentOutput(),
        )

    def run(self, params={}):  # noqa: MC0001
        organization = params.get(Input.ORGANIZATION)
        repository = params.get(Input.REPOSITORY)
        issue_number = params.get(Input.ISSUE_NUMBER)
        body = params.get(Input.BODY)

        try:
            if organization and repository:
                github_user = self.connection.github_user
                org = github_user.get_organization(organization)
                repo = org.get_repo(repository)
            else:
                user = self.connection.user
                repo = user.get_repo(repository)

            issue = repo.get_issue(issue_number)
            issue_params = {"body": body}
            issue = issue.create_comment(**issue_params)
            return {Output.URL: issue.html_url}
        except github.GithubException as err:
            handle_gihub_exceptions(err)
