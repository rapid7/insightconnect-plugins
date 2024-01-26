import requests
import insightconnect_plugin_runtime
import urllib.parse

from komand_github.util.util import TIMEOUT, handle_http_exceptions
from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_github.actions.get_repo.schema import GetRepoInput, GetRepoOutput, Input, Output, Component


class GetRepo(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_repo",
            description=Component.DESCRIPTION,
            input=GetRepoInput(),
            output=GetRepoOutput(),
        )

    def run(self, params={}):
        try:
            title = urllib.parse.quote(params.get(Input.TITLE))
            owner = urllib.parse.quote(params.get(Input.OWNER))

            url = requests.compat.urljoin(self.connection.api_prefix, f"/repos/{owner}/{title}")

            results = requests.get(url=url, headers=self.connection.auth_header, timeout=TIMEOUT)

            handle_http_exceptions(results)
            return {Output.DATA: clean(results.json())}

        except Exception as error:
            if isinstance(error, PluginException):
                raise PluginException(cause=error.cause, assistance=error.assistance, data=error.data)
            else:
                raise PluginException(
                    cause="Error occoured when trying to get repo.",
                    assistance="Please check that the provided inputs are correct and try again.",
                    data=error,
                )
