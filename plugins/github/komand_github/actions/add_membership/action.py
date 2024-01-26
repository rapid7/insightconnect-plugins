import requests
import insightconnect_plugin_runtime
import urllib.parse

from komand_github.util.util import TIMEOUT, handle_http_exceptions
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
            results = requests.put(url=url, headers=self.connection.auth_header, params={"role": role}, timeout=TIMEOUT)
            handle_http_exceptions(results)

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

        except Exception as error:
            if isinstance(error, PluginException):
                raise PluginException(cause=error.cause, assistance=error.assistance, data=error.data)
            else:
                raise PluginException(
                    cause="An error has occurred while adding a membership.",
                    assistance="Please check that the provided inputs are correct and try again.",
                    data=error,
                )
