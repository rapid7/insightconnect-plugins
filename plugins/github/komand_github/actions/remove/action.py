import insightconnect_plugin_runtime
import github

from komand_github.util.util import handle_gihub_exceptions
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_github.actions.remove.schema import RemoveInput, RemoveOutput, Input, Output, Component


class Remove(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove", description=Component.DESCRIPTION, input=RemoveInput(), output=RemoveOutput()
        )

    def run(self, params={}):  # noqa: MC0001

        username = params.get(Input.USERNAME)
        organization = params.get(Input.ORGANIZATION)
        repository = params.get(Input.REPOSITORY)

        status = ""

        # user obj to remove
        github_user = self.connection.github_user
        user = self.connection.user
        remove_user = github_user.get_user(username)

        if self.connection.username == remove_user.name:
            raise PluginException(
                cause="Cannot remove your own username.",
                assistance="Please check that the provided inputs are correct and try again.",
            )

        try:
        # remove from repo in organization
            if organization and repository:
                org = github_user.get_organization(organization)
                repo = org.get_repo(repository)
                repo.remove_from_collaborators(remove_user)
                status = f"Successfully removed {remove_user.name} from the repo {repo.full_name} in {organization}"

            # remove from organization
            elif organization:
                org = github_user.get_organization(organization)
                org.remove_from_members(remove_user)
                status = f"Successfully removed {remove_user.name} from the Organization {organization}"

            # remove from repo
            else:
                repo = user.get_repo(repository)
                repo.remove_from_collaborators(remove_user)
                status = f"Successfully removed {remove_user.name} from the repo {repo.full_name}"
        
        except github.GithubException as err:
            handle_gihub_exceptions(err)
        

        return {Output.STATUS: status}
