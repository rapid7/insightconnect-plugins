import insightconnect_plugin_runtime
from .schema import QueryInput, QueryOutput, Input, Output, Component
# Custom imports below
from google.api_core.exceptions import GoogleAPIError
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime import helper


class Query(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='query',
                description=Component.DESCRIPTION,
                input=QueryInput(),
                output=QueryOutput())

    def run(self, params={}):
        new_results = []
        try:
            query_job = self.connection.client.query(params.get(Input.QUERY))
            results = query_job.result()
            for result in results:
                new_results.append(helper.clean_dict(result))
        except GoogleAPIError as e:
            self.logger.error(f"Google API error: Check query: {e}")
            raise PluginException(cause="Google API error",
                                  assistance="Check query",
                                  data=e)

        return {
            Output.RESULT: new_results
        }
