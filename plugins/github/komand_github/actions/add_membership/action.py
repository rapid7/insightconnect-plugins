import requests
import insightconnect_plugin_runtime
import urllib.parse


from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_github.actions.add_membership.schema import (
    AddMembershipInput,
    AddMembershipOutput,
    Input,
    Output,
    Component,
)


class AddMembership(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_membership",
            description=Component.DESCRIPTION,
            input=AddMembershipInput(),
            output=AddMembershipOutput(),
        )

    def run(self, params={}):

        organization = urllib.parse.quote(params.get(Input.ORGANIZATION))
        username = urllib.parse.quote(params.get(Input.USERNAME))
        role = params.get(Input.ROLE)

        url = requests.compat.urljoin(self.connection.api_prefix, f"/orgs/{organization}/memberships/{username}")

        try:
            results = requests.put(url=url, headers=self.connection.auth_header, params={"role": role}, timeout=60)

            if results.status_code == 200:
                data = results.json()
                data = clean(data)
                return {
                    Output.URL: data.get("url", ""),
                    Output.STATE: data.get("state", ""),
                    Output.ROLE: data.get("role", ""),
                    Output.USER: data.get("user", {}),
                    Output.ORGANIZATION: data.get("organization", {}),
                    Output.ORGANIZATION_URL: data.get("organization_url", ""),
                }

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
                    cause="An error has occurred while adding a membership",
                    assistance="Please check that the provided inputs are correct and try again.",
                    data=error,
                )
