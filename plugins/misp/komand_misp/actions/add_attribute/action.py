import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import AddAttributeInput, AddAttributeOutput

# Custom imports below


class AddAttribute(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_attribute",
            description="Add an attribute to an event",
            input=AddAttributeInput(),
            output=AddAttributeOutput(),
        )

    def run(self, params={}):
        event = params.get("event")
        type_value = params.get("type_value")
        category = params.get("category")
        value = params.get("value")
        comment = params.get("comment")

        client = self.connection.client
        in_event = client.get_event(event)
        item = client.add_named_attribute(in_event, type_value, value, category, comment=comment)
        try:
            attribute = item[0]
        except IndexError:
            self.logger.error("Add attribute return invalid")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)
        try:
            attribute = attribute["Attribute"]
        except KeyError:
            self.logger.error("Improperly formatted attribute")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)
        return {"attribute": attribute}
