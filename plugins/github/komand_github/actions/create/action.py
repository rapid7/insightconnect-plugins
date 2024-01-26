import insightconnect_plugin_runtime
import github

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_github.actions.create.schema import CreateInput, CreateOutput, Input, Output, Component


class Create(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create",
            description=Component.DESCRIPTION,
            input=CreateInput(),
            output=CreateOutput(),
        )

    def run(self, params={}):  # noqa: MC0001

        organization = params.get(Input.ORGANIZATION)
        repository = params.get(Input.REPOSITORY)
        title = params.get(Input.TITLE)
        body = params.get(Input.BODY)
        assignee = params.get(Input.ASSIGNEE)
        milestone = params.get(Input.MILESTONE)
        lables = params.get(Input.LABELS)

        if organization and repository:
            try:
                github_user = self.connection.github_user
                org = github_user.get_organization(organization)
                repo = org.get_repo(repository)
            except github.GithubException as err:
                if err.status == 403:
                    raise PluginException(
                        cause="Forbidden response returned from Github",
                        assistance="Account may need org permissions added",
                    )
                elif err.status == 404:
                    raise PluginException(
                        cause="Not Found response returned from Github",
                        assistance="The org or repo could not be found",
                    )
                else:
                    raise PluginException(
                        cause="Error occoured when trying to add label to get repo information",
                        assistance="Please check that the provided inputs are correct and try again.",
                        data=err,
                    )
        else:
            try:
                user = self.connection.user
                repo = user.get_repo(repository)
            except github.GithubException as err:
                if err.status == 403:
                    raise PluginException(
                        cause="Forbidden response returned from Github",
                        assistance="Account may need org permissions added",
                    )
                elif err.status == 404:
                    raise PluginException(
                        cause="Not Found response returned from Github",
                        assistance="The repo could not be found",
                    )
                else:
                    raise PluginException(
                        cause="Error occoured when trying to add label to get repo information",
                        assistance="Please check that the provided inputs are correct and try again.",
                        data=err,
                    )

        issue_params = {"title": title, "body": body}

        if assignee:
            issue_params.update({"assignee": assignee})
        if milestone:
            milestone = repo.get_milestone(milestone)
            issue_params.update({"milestone": milestone})
        if lables:
            labels_raw = lables.split(",")
            issue_params.update({"labels": labels_raw})

        try:
            issue = repo.create_issue(**issue_params)
            return {Output.URL: issue.html_url}
        except github.GithubException as err:
            raise PluginException(
                cause="Error occoured when trying to create issue",
                assistance="Please check that the provided inputs are correct and try again.",
                data=err,
            )
