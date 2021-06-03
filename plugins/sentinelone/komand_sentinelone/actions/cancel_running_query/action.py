import insightconnect_plugin_runtime
from .schema import CancelRunningQueryInput, CancelRunningQueryOutput, Input, Output, Component

# Custom imports below


class CancelRunningQuery(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="cancel_running_query",
            description=Component.DESCRIPTION,
            input=CancelRunningQueryInput(),
            output=CancelRunningQueryOutput(),
        )

    def run(self, params={}):
        return {Output.RESPONSE: self.connection.cancel_running_query(params.get(Input.QUERY_ID))}
