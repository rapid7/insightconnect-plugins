import insightconnect_plugin_runtime
from .schema import (
    MonitorIncidentsInput,
    MonitorIncidentsOutput,
    MonitorIncidentsState,
    Input,
    Output,
    Component,
    State,
)

# Custom imports below


class MonitorIncidents(insightconnect_plugin_runtime.Task):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_incidents",
            description=Component.DESCRIPTION,
            input=MonitorIncidentsInput(),
            output=MonitorIncidentsOutput(),
            state=MonitorIncidentsState(),
        )

    def run(self, params={}, state={}):
        # TODO: Implement run function
        return {}, {}
