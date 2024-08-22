import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import AddSightingInput, AddSightingOutput, Input, Output, Component

# Custom imports below


class AddSighting(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_sighting",
            description=Component.DESCRIPTION,
            input=AddSightingInput(),
            output=AddSightingOutput(),
        )

    def run(self, params={}):

        mappings = {"Sighting": 0, "False-positive": 1, "Expiration": 2}

        sighting = {
            "source": params.get(Input.SOURCE, ""),
            "type": mappings.get(params.get(Input.TYPE)),
            "date": params.get(Input.DATE, ""),
            "time": params.get(Input.TIME, ""),
        }

        client = self.connection.client
        try:
            item = client.add_sighting(sighting=sighting, attribute=int(params.get(Input.ATTRIBUTE)))
            if item.get("Sighting"):
                return {Output.SIGHTING: item.get("Sighting")}
            else:
                self.logger.error(item)
                raise PluginException(preset=PluginException.Preset.UNKNOWN)
        except Exception as error:
            self.logger.error(error)
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
