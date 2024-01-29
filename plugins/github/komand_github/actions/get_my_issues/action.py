import requests
import insightconnect_plugin_runtime

from komand_github.util.util import TIMEOUT, handle_http_exceptions
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
            results = requests.get(url=url, headers=self.connection.auth_header, timeout=TIMEOUT)

            handle_http_exceptions(results)
            return {Output.ISSUES: clean(results.json())}
        except Exception as error:
            if isinstance(error, PluginException):
                raise PluginException(cause=error.cause, assistance=error.assistance, data=error.data)
            else:
                raise PluginException(
                    cause="Error occoured when trying to get my issues.",
                    assistance="Please check that the provided inputs are correct and try again.",
                    data=error,
                )
