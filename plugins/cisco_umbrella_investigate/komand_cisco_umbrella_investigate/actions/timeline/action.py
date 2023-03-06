import insightconnect_plugin_runtime
from .schema import TimelineInput, TimelineOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class Timeline(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="timeline",
            description=Component.DESCRIPTION,
            input=TimelineInput(),
            output=TimelineOutput(),
        )

    def run(self, params={}):
        name = params.get(Input.NAME)
        try:
            output = self.connection.investigate.get_timeline(name)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        return {Output.TIMELINE: output}
