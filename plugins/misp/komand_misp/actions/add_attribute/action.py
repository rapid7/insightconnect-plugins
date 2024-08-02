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
        item = client.add_attribute(
            event=in_event, attribute={"category": category, "type": type_value, "value": value, "comment": comment}
        )
        try:
            attribute = item["Attribute"]
        except KeyError:
            self.logger.error(f"Unable to add attribute {item}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=item)
        except Exception as error:
            self.logger.error(f"Error when adding attribute: {error}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        return {"attribute": attribute}
