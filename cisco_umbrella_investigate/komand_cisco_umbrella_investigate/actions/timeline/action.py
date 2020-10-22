import komand
from .schema import TimelineInput, TimelineOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class Timeline(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='timeline',
                description=Component.DESCRIPTION,
                input=TimelineInput(),
                output=TimelineOutput())

    def run(self, params={}):
        name = params.get(Input.NAME)
        try:
            output = self.connection.investigate.get_timeline(name)
        except Exception as e:
            raise PluginException(
                preset=PluginException.Preset.UNKNOWN,
                data=e
            )
        return {
            Output.TIMELINE: output
        }
