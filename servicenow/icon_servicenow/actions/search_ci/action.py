import insightconnect_plugin_runtime
from .schema import SearchCiInput, SearchCiOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class SearchCi(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_ci',
                description=Component.DESCRIPTION,
                input=SearchCiInput(),
                output=SearchCiOutput())

    def run(self, params={}):
        url = f'{self.connection.table_url}{params.get(Input.TABLE)}'
        query = {"sysparm_query": params.get(Input.QUERY)}
        method = "get"

        response = self.connection.request.make_request(url, method, params=query)

        try:
            result = response["resource"].get("result")
        except KeyError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response.text) from e

        return {
            Output.SERVICENOW_CIS: result
        }
