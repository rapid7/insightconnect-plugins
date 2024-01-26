import requests
import insightconnect_plugin_runtime
import urllib.parse

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_github.actions.add_collaborator.schema import (
    AddCollaboratorInput,
    AddCollaboratorOutput,
    Input,
    Output,
    Component,
)


class AddCollaborator(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_collaborator",
            description=Component.DESCRIPTION,
            input=AddCollaboratorInput(),
            output=AddCollaboratorOutput(),
        )

    def run(self, params={}):
        organization = urllib.parse.quote(params.get(Input.ORGANIZATION))
        repository = urllib.parse.quote(params.get(Input.REPOSITORY))
        username = urllib.parse.quote(params.get(Input.USERNAME))
        permission = params.get(Input.PERMISSION)

        url = requests.compat.urljoin(
            self.connection.api_prefix, f"/repos/{organization}/{repository}/collaborators/{username}"
        )

        try:
            results = requests.put(
                url=url, headers=self.connection.auth_header, params={"permission": permission}, timeout=60
            )
            if results.status_code == 201:
                return {Output.RESULTS: results.json()}

            elif results.status_code == 204:
                raise PluginException(
                    cause=f"{username} is already a collaborator",
                    assistance="Please check that the provided inputs are correct and try again.",
                )

            elif results.status_code == 403:
                raise PluginException(
                    cause="Forbidden response returned from Github",
                    assistance="Account may need org permissions added",
                )

            else:
                raise PluginException(
                    cause=f"A status code of {results.status_code} was returned from Github",
                    assistance="Please check that the provided inputs are correct and try again.",
                )

        except Exception as error:
            if isinstance(error, PluginException):
                raise PluginException(cause=error.cause, assistance=error.assistance)
            else:
                raise PluginException(
                    cause="Error occoured when trying to add a collaborator",
                    assistance="Please check that the provided inputs are correct and try again.",
                    data=error,
                )
