import requests
import insightconnect_plugin_runtime
import urllib.parse

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

            results = requests.get(url=url, params=search_params, headers=self.connection.auth_header, timeout=60)

            if results.status_code == 200:
                return {Output.RESULTS: clean(results.json())}

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
                    cause="Error occoured when trying to perfom a search",
                    assistance="Please check that the provided inputs are correct and try again.",
                    data=error,
                )
