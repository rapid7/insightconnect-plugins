import insightconnect_plugin_runtime
from .schema import GetEventsByTypeInput, GetEventsByTypeOutput, Input, Output, Component
# Custom imports below


class GetEventsByType(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_events_by_type',
                description=Component.DESCRIPTION,
                input=GetEventsByTypeInput(),
                output=GetEventsByTypeOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
