import insightconnect_plugin_runtime
from .schema import GetSiemEventsInput, GetSiemEventsOutput, Input, Output, Component
# Custom imports below


class GetSiemEvents(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_siem_events',
                description=Component.DESCRIPTION,
                input=GetSiemEventsInput(),
                output=GetSiemEventsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
