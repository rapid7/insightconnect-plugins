import insightconnect_plugin_runtime
from .schema import ClusterHealthInput, ClusterHealthOutput, Output, Component

# Custom imports below


class ClusterHealth(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="cluster_health",
            description=Component.DESCRIPTION,
            input=ClusterHealthInput(),
            output=ClusterHealthOutput(),
        )

    def run(self, params={}):
        return {
            Output.CLUSTER_HEALTH: insightconnect_plugin_runtime.helper.clean(self.connection.client.cluster_health())
        }
