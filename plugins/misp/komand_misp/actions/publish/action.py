import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import PublishInput, PublishOutput, Input, Output, Component

# Custom imports below


class Publish(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="publish",
            description=Component.DESCRIPTION,
            input=PublishInput(),
            output=PublishOutput(),
        )

    def run(self, params={}):
        event = params.get(Input.EVENT)

        client = self.connection.client
        in_event = client.get_event(event)
        published = client.publish(in_event, True)
        try:
            published["id"]
        except KeyError:
            self.logger.error("Something went wrong see returned request")
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST)
        return {Output.PUBLISHED: published}
