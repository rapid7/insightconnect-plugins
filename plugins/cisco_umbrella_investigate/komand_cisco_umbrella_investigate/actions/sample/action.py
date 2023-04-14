import insightconnect_plugin_runtime
from .schema import SampleInput, SampleOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class Sample(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="sample",
            description="Return a file, or a file-like object, such as a process running in memory",
            input=SampleInput(),
            output=SampleOutput(),
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
            sample = self.connection.investigate.sample(hash_, limit=limit, offset=offset)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        return sample
