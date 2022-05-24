import insightconnect_plugin_runtime

from .schema import AdvancedHuntingInput, AdvancedHuntingOutput, Component, Input, Output


class AdvancedHunting(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="advanced_hunting",
            description=Component.DESCRIPTION,
            input=AdvancedHuntingInput(),
            output=AdvancedHuntingOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.QUERY)
        response = self.connection.client.advanced_hunting(query)
        return {Output.COLUMNS: response.get("Schema"), Output.ROWS: response.get("Results")}
