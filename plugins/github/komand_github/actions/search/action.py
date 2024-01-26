import requests
import insightconnect_plugin_runtime
import urllib.parse

from komand_github.util.util import TIMEOUT, handle_http_exceptions
from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_github.actions.search.schema import SearchInput, SearchOutput, Input, Output, Component


class Search(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search",
            description=Component.DESCRIPTION,
            input=SearchInput(),
            output=SearchOutput(),
        )

    def run(self, params={}):

        try:
            search_type = urllib.parse.quote(params.get(Input.SEARCH_TYPE).lower())
            query = params.get(Input.QUERY)

            url = requests.compat.urljoin(self.connection.api_prefix, f"/search/{search_type}")
            search_params = {"q": query}

            results = requests.get(url=url, params=search_params, headers=self.connection.auth_header, timeout=TIMEOUT)

            handle_http_exceptions(results)
            return {Output.RESULTS: clean(results.json())}

        except Exception as error:
            if isinstance(error, PluginException):
                raise PluginException(cause=error.cause, assistance=error.assistance, data=error.data)
            else:
                raise PluginException(
                    cause="Error occoured when trying to perfom a search.",
                    assistance="Please check that the provided inputs are correct and try again.",
                    data=error,
                )
