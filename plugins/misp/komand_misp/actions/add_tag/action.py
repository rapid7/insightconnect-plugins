import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import AddTagInput, AddTagOutput, Input, Output, Component

# Custom imports below


class AddTag(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_tag", description=Component.DESCRIPTION, input=AddTagInput(), output=AddTagOutput()
        )

    def run(self, params={}):
        client = self.connection.client
        in_event = client.get_event(params.get(Input.EVENT))
        try:
            item = client.tag(in_event["Event"]["uuid"], tag=params.get(Input.EVENT))
            if "successfully" in item["name"]:
                return {Output.STATUS: True}
            else:
                self.logger.info(item)
                return {Output.STATUS: False}
        except Exception as error:
            self.logger.error(error)
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
