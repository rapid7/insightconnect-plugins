import insightconnect_plugin_runtime
import github

from komand_github.util.util import handle_gihub_exceptions
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
        
        try:
            if organization and repository:
                github_user = self.connection.github_user
                org = github_user.get_organization(organization)
                repo = org.get_repo(repository)
            else:
                user = self.connection.user
                repo = user.get_repo(repository)

            issue_params = {"title": title, "body": body}

            if assignee:
                issue_params.update({"assignee": assignee})
            if milestone:
                milestone = repo.get_milestone(milestone)
                issue_params.update({"milestone": milestone})
            if lables:
                labels_raw = lables.split(",")
                issue_params.update({"labels": labels_raw})

        
            issue = repo.create_issue(**issue_params)
            return {Output.URL: issue.html_url}
        except github.GithubException as err:
            handle_gihub_exceptions(err)
