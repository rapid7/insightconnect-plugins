import insightconnect_plugin_runtime
from .schema import EnrichIndicatorInput, EnrichIndicatorOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import clean


class EnrichIndicator(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="enrich_indicator",
            description=Component.DESCRIPTION,
            input=EnrichIndicatorInput(),
            output=EnrichIndicatorOutput(),
        )

    def run(self, params={}):
        ioc_value = params.get(Input.INDICATOR_VALUE)
        response = self.connection.client.enrich_indicator(ioc_value)
        return clean(
            {
                Output.ORIGINAL_VALUE: response.get("OriginalValue", ioc_value),
                Output.STATUS: response.get("Status", "Failed"),
                Output.DATA: response.get("Data", {}),
            }
        )
