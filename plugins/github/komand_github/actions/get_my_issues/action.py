import requests
import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_github.actions.get_my_issues.schema import GetMyIssuesInput, GetMyIssuesOutput, Input, Output, Component


class GetMyIssues(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_my_issues",
            description=Component.DESCRIPTION,
            input=GetMyIssuesInput(),
            output=GetMyIssuesOutput(),
        )

    def run(self):
        try:
            url = requests.compat.urljoin(self.connection.api_prefix, "/issues")
            results = requests.get(url=url, headers=self.connection.auth_header, timeout=60)

            if results.status_code == 200:
                return {"issues": clean(results.json())}

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
                    cause="Error occoured when trying to get my issues",
                    assistance="Please check that the provided inputs are correct and try again.",
                    data=error,
                )
