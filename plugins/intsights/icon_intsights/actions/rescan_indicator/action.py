import insightconnect_plugin_runtime
from .schema import RescanIndicatorInput, RescanIndicatorOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import clean


class RescanIndicator(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="rescan_indicator",
            description=Component.DESCRIPTION,
            input=RescanIndicatorInput(),
            output=RescanIndicatorOutput(),
        )

    def run(self, params={}):
        response = self.connection.client.rescan_indicator(params.get(Input.INDICATOR_FILE_HASH))
        return clean({Output.TASK_ID: response.get("TaskId"), Output.STATUS: response.get("Status")})
