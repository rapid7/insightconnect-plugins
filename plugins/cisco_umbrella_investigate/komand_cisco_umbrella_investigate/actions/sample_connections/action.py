import insightconnect_plugin_runtime
from .schema import SampleConnectionsInput, SampleConnectionsOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class SampleConnections(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="sample_connections",
            description="Information about network activity associated with this sample, such as connections to other domains or IPs",
            input=SampleConnectionsInput(),
            output=SampleConnectionsOutput(),
        )

    def run(self, params={}):
        hash_ = params.get(Input.HASH)
        limit = params.get(Input.LIMIT)
        offset = params.get(Input.OFFSET)

        if not limit or limit == 0:
            limit = 10

        if not offset:
            offset = 0

        try:
            sample_connections = self.connection.investigate.sample_connections(hash_, limit=limit, offset=offset)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        return sample_connections
