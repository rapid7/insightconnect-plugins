import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import RemoveTagInput, RemoveTagOutput, Input, Output, Component

# Custom imports below


class RemoveTag(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_tag",
            description=Component.DESCRIPTION,
            input=RemoveTagInput(),
            output=RemoveTagOutput(),
        )

    def run(self, params={}):
        client = self.connection.client
        in_event = client.get_event(params.get(Input.EVENT))

        if in_event.get("errors"):
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=in_event.get("errors"))

        try:
            item = client.untag(in_event["Event"]["uuid"], tag=params.get("tag"))
            if item.get("name") and "successfully" in item["name"]:
                return {"status": True}
            else:
                self.logger.info(item)
                return {Output.STATUS: False}
        except Exception as error:
            self.logger.error(error)
            raise PluginException(preset=PluginException.Preset.UNKNOWN)
