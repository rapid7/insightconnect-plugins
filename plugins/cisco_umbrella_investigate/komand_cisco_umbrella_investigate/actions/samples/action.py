import insightconnect_plugin_runtime
from .schema import SamplesInput, SamplesOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class Samples(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="samples",
            description="Return all samples associated with the domain",
            input=SamplesInput(),
            output=SamplesOutput(),
        )

    def run(self, params={}):
        URL = params.get(Input.URL)
        limit = params.get(Input.LIMIT)
        offset = params.get(Input.OFFSET)
        sortby = params.get(Input.SORTBY)

        if not limit or limit == 0:
            limit = 10

        if not sortby or sortby == "":
            sortby = "score"

        if not offset:
            offset = 0

        try:
            samples = self.connection.investigate.samples(URL, limit=limit, offset=offset, sortby=sortby)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        return samples
