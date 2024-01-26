import requests
import insightconnect_plugin_runtime
import urllib.parse

from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_github.actions.get_issues_by_repo.schema import (
    GetIssuesByRepoInput,
    GetIssuesByRepoOutput,
    Input,
    Output,
    Component,
)


class GetIssuesByRepo(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_issues_by_repo",
            description=Component.DESCRIPTION,
            input=GetIssuesByRepoInput(),
            output=GetIssuesByRepoOutput(),
        )

    def run(self, params={}):
        try:
            title = urllib.parse.quote(params.get(Input.TITLE))
            owner = urllib.parse.quote(params.get(Input.OWNER))

            url = requests.compat.urljoin(self.connection.api_prefix, f"/repos/{owner}/{title}/issues")

            results = requests.get(url=url, headers=self.connection.auth_header, timeout=60)

            if results.status_code == 200:
                return {Output.ISSUES: clean(results.json())}

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
                    cause="Error occoured when trying to get issues",
                    assistance="Please check that the provided inputs are correct and try again.",
                    data=error,
                )
