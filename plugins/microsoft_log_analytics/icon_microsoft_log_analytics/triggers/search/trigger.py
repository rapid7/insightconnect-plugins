import insightconnect_plugin_runtime
import time
from .schema import SearchInput, SearchOutput, Input, Component

# Custom imports below
from icon_microsoft_log_analytics.util.tools import return_non_empty_query_output


class Search(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search", description=Component.DESCRIPTION, input=SearchInput(), output=SearchOutput()
        )

    def run(self, params={}):
        interval = abs(params.get(Input.INTERVAL, 60))
        subscription_id = params.get(Input.SUBSCRIPTION_ID)
        resource_group_name = params.get(Input.RESOURCE_GROUP_NAME)
        workspace_name = params.get(Input.WORKSPACE_NAME)
        query = params.get(Input.QUERY)
        while True:
            self.logger.info(f"\nRunning query {query}...")
            response = return_non_empty_query_output(
                self.connection.client.get_log_data(subscription_id, resource_group_name, workspace_name, query)
            )
            if response.get("tables"):
                self.logger.info("Response received!")
                self.send(response)
            else:
                self.logger.info("No response has been received!")
            self.logger.info(f"Sleeping for {interval} seconds...")
            time.sleep(interval)
