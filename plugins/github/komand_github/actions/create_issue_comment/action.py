import insightconnect_plugin_runtime
import github

from insightconnect_plugin_runtime.exceptions import PluginException
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

        if organization and repository:
            try:
                github_user = self.connection.github_user
                org = github_user.get_organization(organization)
                repo = org.get_repo(repository)
                issue = repo.get_issue(issue_number)
            except github.GithubException as err:
                if err.status == 403:
                    raise PluginException(
                        cause="Forbidden response returned from Github",
                        assistance="Account may need org permissions added",
                    )
                elif err.status == 404:
                    raise PluginException(
                        cause="Not Found response returned from Github",
                        assistance="The issue, org or repo could not be found",
                    )
                else:
                    raise PluginException(
                        cause="Error occoured when trying to add label to get issue information",
                        assistance="Please check that the provided inputs are correct and try again.",
                        data=err,
                    )
        else:
            try:
                user = self.connection.user
                repo = user.get_repo(repository)
                issue = repo.get_issue(issue_number)
            except github.GithubException as err:
                if err.status == 403:
                    raise PluginException(
                        cause="Forbidden response returned from Github",
                        assistance="Account may need org permissions added",
                    )
                elif err.status == 404:
                    raise PluginException(
                        cause="Not Found response returned from Github",
                        assistance="The issue or repo could not be found",
                    )
                else:
                    raise PluginException(
                        cause="Error occoured when trying to add label to get issue information",
                        assistance="Please check that the provided inputs are correct and try again.",
                        data=err,
                    )

        try:
            issue_params = {"body": body}
            issue = issue.create_comment(**issue_params)
            return {"url": issue.html_url}
        except github.GithubException as err:
            raise PluginException(
                cause="Error occoured when trying to add label to create a comment",
                assistance="Please check that the provided inputs are correct and try again.",
                data=err,
            )
