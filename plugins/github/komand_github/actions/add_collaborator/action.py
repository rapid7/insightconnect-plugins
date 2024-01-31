import requests
import insightconnect_plugin_runtime
import urllib.parse

from komand_github.util.util import TIMEOUT, handle_http_exceptions
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
                url=url, headers=self.connection.auth_header, params={"permission": permission}, timeout=TIMEOUT
            )

            handle_http_exceptions(results)

            if results.status_code == 204:
                raise PluginException(
                    cause=f"{username} is already a collaborator",
                    assistance="Please check that the provided inputs are correct and try again.",
                    data=results.text,
                )

            return {Output.RESULTS: results.json()}

        except Exception as error:
            if isinstance(error, PluginException):
                raise PluginException(cause=error.cause, assistance=error.assistance, data=error.data)
            else:
                raise PluginException(
                    cause="Error occoured when adding a collaborator.",
                    assistance="Please check that the provided inputs are correct and try again.",
                    data=error,
                )
