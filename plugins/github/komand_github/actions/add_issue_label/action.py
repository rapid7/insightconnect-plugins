import insightconnect_plugin_runtime
import github

from insightconnect_plugin_runtime.exceptions import PluginException
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
