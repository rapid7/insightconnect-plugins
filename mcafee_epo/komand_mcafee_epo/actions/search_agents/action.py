import insightconnect_plugin_runtime
from .schema import SearchAgentsInput, SearchAgentsOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class SearchAgents(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_agents',
                description=Component.DESCRIPTION,
                input=SearchAgentsInput(),
                output=SearchAgentsOutput())

    def run(self, params=None):
        if params is None:
            params = {}
        try:
            cleaned_response = []
            response = self.connection.client('system.find', params.get(Input.QUERY))
            self.logger.info("System information has been gathered")
            # Loop through response
            for prop in response:
                # Call clean_dict to clear null values
                cleaned_prop = insightconnect_plugin_runtime.helper.clean_dict(prop)
                # Added cleaned response to new list
                cleaned_response.append(cleaned_prop)
            # return the cleaned list
            return {
                Output.AGENTS: cleaned_response
            }
        except Exception as e:
            raise PluginException(
                cause="System information error.",
                assistance="Unable to query for system information",
                data=e
            )
